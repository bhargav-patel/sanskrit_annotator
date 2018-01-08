from django import forms

class SearchForm(forms.Form):
	word = forms.CharField(max_length=100,required=False)
	sent_id = forms.IntegerField(required=False)
	POS = forms.CharField(max_length=100,required=False)
	dep = forms.CharField(max_length=100,required=False)
	lemma = forms.CharField(max_length=100,required=False)
	morph = forms.CharField(max_length=100,required=False)
	color_class = forms.CharField(max_length=100,required=False)
	level = forms.IntegerField(required=False)