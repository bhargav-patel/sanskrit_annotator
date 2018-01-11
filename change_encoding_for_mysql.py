#set up django environment
import os
import django
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sanskrit_annotator.settings")
django.setup()

#script
from django.db import connection
cursor = connection.cursor()
cursor.execute('SHOW TABLES')
results=[]
for row in cursor.fetchall(): results.append(row)
for row in results: cursor.execute('ALTER TABLE %s CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;' % (row[0]))