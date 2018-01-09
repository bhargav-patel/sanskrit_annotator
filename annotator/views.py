from django.http import HttpResponse
from django.shortcuts import render,redirect

from .forms import SearchForm
from .models import Sentence,Word,WordOption
# Create your views here.
def index(request):

	words = None

	if request.method == 'POST':
		form = SearchForm(request.POST)
		if form.is_valid():
			request.session['search_form_sent_id'] = form.cleaned_data["sent_id"]
			request.session['search_form_word'] = form.cleaned_data["word"]
			request.session['search_form_POS'] = form.cleaned_data["POS"]
			request.session['search_form_dep'] = form.cleaned_data["dep"]
			request.session['search_form_lemma'] = form.cleaned_data["lemma"]
			request.session['search_form_morph'] = form.cleaned_data["morph"]
			request.session['search_form_color_class'] = form.cleaned_data["color_class"]
			request.session['search_form_level'] = form.cleaned_data["level"]
	else:
		form = SearchForm(initial={
									'sent_id' : request.session.get('search_form_sent_id',''),
									'word' : request.session.get('search_form_word',''),
									'POS' : request.session.get('search_form_POS',''),
									'dep' : request.session.get('search_form_dep',''),
									'lemma' : request.session.get('search_form_lemma',''),
									'morph' : request.session.get('search_form_morph',''),
									'color_class' : request.session.get('search_form_color_class',''),
									'level' : request.session.get('search_form_level','') 					,
								})


	sent_id = request.session.get('search_form_sent_id',None)
	word = request.session.get('search_form_word','')
	POS = request.session.get('search_form_POS','')
	dep = request.session.get('search_form_dep','')
	lemma = request.session.get('search_form_lemma','')
	morph = request.session.get('search_form_morph','')
	color_class = request.session.get('search_form_color_class','')
	level = request.session.get('search_form_level',None) 

	words = Word.objects.filter(wordoption__isEliminated=False,wordoption__isSelected=False).distinct()

	if sent_id is not None:
		words = words.filter(sent_id=sent_id)

	if word!="":
		words = words.filter(text__icontains=word)

	if POS!="":
		words = words.filter(POS=POS)

	if dep!="":
		words = words.filter(dep__icontains=dep)

	if lemma!="":
		words = words.filter(wordoption__lemma__icontains=lemma).distinct()

	if morph!="":
		words = words.filter(wordoption__morph__icontains=morph).distinct()

	if color_class!="":
		words = words.filter(wordoption__color_class__icontains=color_class).distinct()

	if level is not None:
		words = words.filter(wordoption__level=level).distinct()

	# currunt_word = 	130

	currunt_word = request.session.get('currunt_word',None)
	print(currunt_word)
	if not currunt_word:
		currunt_word = words.first().id

	word_current = Word.objects.get(id=currunt_word)
	word_childs = Word.objects.filter(sent_id=word_current.sent_id,head=word_current.wordID)
	word_parent = None
	if word_current.head!=0:
		word_parent = Word.objects.get(sent_id=word_current.sent_id,wordID=word_current.head)

	numDone = Word.objects.filter(wordoption__isSelected=True).distinct().count()
	numTotal = Word.objects.count()

	context = {"form":form, "words":words,'word_current':word_current,'word_childs':word_childs,'word_parent':word_parent,'numDone':numDone,'numTotal':numTotal}
	return render(request, 'index.html', context)

def change_word(request,word_id):
	request.session['currunt_word'] = word_id
	return redirect('index')

def select_wordoption(request,wordoption_id):
	wo = WordOption.objects.get(id=wordoption_id)
	wo.isSelected = True
	wo.save()

	siblings = WordOption.objects.filter(word_id=wo.word_id)
	for s in siblings:
		if s!=wo:
			s.isEliminated = True
			s.save()
	return redirect('index')

def eliminate_wordoption(request,wordoption_id):
	wo = WordOption.objects.get(id=wordoption_id)
	wo.isEliminated = True
	wo.save()
	return redirect('index')

def reset_session(request):
	for key in list(request.session.keys()):
		del request.session[key]
	return redirect('index')

def undo_selections(request,word_id):
	opts = WordOption.objects.filter(word_id=word_id)
	if opts.count()>1:
		for o in opts:
			o.isEliminated = False
			o.isSelected = False
			o.save()
	return redirect('index')