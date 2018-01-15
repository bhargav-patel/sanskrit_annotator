from django import forms

class SearchForm(forms.Form):
	word = forms.CharField(max_length=100,required=False,help_text="Partial or Full word case insensitive")
	sent_id = forms.IntegerField(required=False,help_text="sentence id")
	POS = forms.CharField(max_length=100,required=False,help_text="POS tag of word")
	dep = forms.CharField(max_length=100,required=False,help_text="dependecy tag of relation between word and its parent")
	lemma = forms.CharField(max_length=100,required=False,help_text="Words with options having this lemma")
	morph = forms.CharField(max_length=100,required=False,help_text="Words with options having this morph")
	color_class = forms.CharField(max_length=100,required=False,help_text="Words with options having this color_class")
	# level = forms.IntegerField(required=False,help_text="Words with options having this level")
	show_unresolved_words_only = forms.BooleanField(required=False,initial=True,help_text="Unselect this to see all words.")