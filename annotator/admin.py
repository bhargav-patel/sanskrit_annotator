from django.contrib import admin

# Register your models here.
from .models import Sentence,Word,WordOption

class SentenceAdmin(admin.ModelAdmin):
    list_display = ('id','__str__','numWords',)
    search_fields = ['id']

class WordAdmin(admin.ModelAdmin):
    list_display = ('id','sent_id','wordID','text','POS','dep','head')
    search_fields = ['text','POS','dep']
    list_filter = ['POS','dep']

class WordOptionAdmin(admin.ModelAdmin):
    list_display = ("id","word","lemma","morph","level","color_class","isEliminated","isSelected","position","chunk_no","pre_verb","colspan","wordlength","aux_info","sandhi_indexs","sandhi_words")
    search_fields = ['word__text',"color_class","lemma","pre_verb","morph","aux_info","sandhi_words"]
    list_filter = ["color_class","morph","level"]


admin.site.register(Sentence,SentenceAdmin)
admin.site.register(Word,WordAdmin)
admin.site.register(WordOption,WordOptionAdmin)

	