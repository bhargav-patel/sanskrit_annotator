#set up django environment
import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sanskrit_annotator.settings")
django.setup()


#parameters
data_dir = "data"

#script
from annotator.models import Sentence,Word,WordOption
import pandas as pd
from tqdm import tqdm

sentences = os.listdir(data_dir)

for i in tqdm(range(len(sentences))):
	sent_id = sentences[i]

	sent = Sentence(id=int(sent_id))
	sent.save()

	with open(data_dir+"/"+sent_id+"/dependency.txt") as depFile:
		#header : wordorder,word,POS,dep,head
		depFile.readline()
		for line in depFile:
			try:
				sl = line.strip().split(",")
				if sl[4]=='':
					sl[4] = '0'
				word = Word(wordID = int(float(sl[0].split('.')[0].strip("*"))),
							sent = sent,
							text = sl[1],
							POS = sl[2],
							dep = sl[3],
							head = int(float(sl[4].split('.')[0].strip("*")))
						)
				word.save()
			except Exception as e:
				print(e)
				print("Word not inserted : ",sent_id,"/",sl[1])

	df = pd.read_csv(data_dir+"/"+sent_id+"/dataframe_towork.csv")

	for i in range(df.shape[0]):
		row = df.iloc[i]
		try:
			word = Word.objects.get(sent=sent,wordID=row["wordorder"])
		except:
			word = None

		try:
			word_option = WordOption(word = word,
									level = row["level"],
									color_class = row["color_class"],
									position = row["position"],
									chunk_no = row["chunk_no"],
									lemma = row["lemma"],
									pre_verb = row["pre_verb"],
									morph = row["morph"],
									colspan = row["colspan"],
									wordlength = row["wordlenth"],
									aux_info = row["aux_inf"],
									sandhi_indexs = row["sandhi_indexs"],
									sandhi_words = row["sandhi_words"],
									)
			word_option.save()
		except Exception as e:
			print("WordOption not inserted : ",sent_id,"/",word)
			print(e)