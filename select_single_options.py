#set up django environment
import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sanskrit_annotator.settings")
django.setup()


#script
from annotator.models import Sentence,Word,WordOption
from django.db.models import Count

solved = Word.objects.all().annotate(opts = Count('wordoption')).filter(opts=1)

for word in solved:
	wo = WordOption.objects.get(word_id=word.id)
	wo.isSelected = True
	wo.save()
	