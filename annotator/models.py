from django.db import models

# Create your models here.

# dependenct.txt : wordorder,word,POS,dep,head
# datafram_towork.csv : id,level,color_class,position,chunk_no,word,lemma,pre_verb,morph,colspan,wordlenth,aux_inf,word_slp1,sandhi_indexs,sandhi_words,word_wx,wordorder

class Sentence(models.Model):
	def __str__(self):
		return str(self.id) +"/ "+ " ".join([ str(word.text) for word in self.word_set.all() ])

	def numWords(self):
		return str(self.word_set.count())
	numWords.admin_order_field = 'numWords'
	numWords.short_description = 'Number of words in the sentence.'

class Word(models.Model):
	sent = models.ForeignKey(Sentence, on_delete=models.CASCADE)

	wordID = models.IntegerField(default=0)
	text = models.CharField(max_length=100)
	POS = models.CharField(max_length=100)
	dep = models.CharField(max_length=100)
	head = models.IntegerField(default=0)

	def __str__(self):
		return str(self.sent.id) + "/ "+ str(self.id) + "/ "+self.text

	class Meta:
		unique_together = (("sent", "wordID"),)

class WordOption(models.Model):
	word = models.ForeignKey(Word, on_delete=models.CASCADE,null=True)

	level = models.IntegerField(default=0)
	color_class = models.CharField(max_length=100)
	position = models.IntegerField(default=0)
	chunk_no = models.IntegerField(default=0)
	lemma = models.CharField(max_length=100)
	pre_verb = models.CharField(max_length=100)
	morph = models.CharField(max_length=100)
	colspan = models.IntegerField(default=0)
	wordlength = models.IntegerField(default=0)
	aux_info = models.CharField(max_length=100)
	sandhi_indexs = models.CharField(max_length=100)
	sandhi_words = models.CharField(max_length=100)
	isEliminated = models.BooleanField(default=False)
	isSelected = models.BooleanField(default=False)

	def __str__(self):
		return str(self.word) + "( "+ self.lemma+", "+self.morph+" )"

	class Meta:
		unique_together = (("word","level","color_class","position","chunk_no","lemma","pre_verb","morph","colspan","wordlength","aux_info","sandhi_indexs","sandhi_words"),)