import os
import sys
import json

## Please run data_processing.py firist
## Assume this file , With_hashtags.json and AFINN-111.txt in the same folder


#open afinn111 txt
afinn = dict(map(lambda (k,v): (k,int(v)), [ line.split('\t') for line in open("AFINN-111.txt") ]))
rate=0
hashtags=[]
pos=0
neg=0
with open ("With_hashtags.json",'r')as f:
	hashtags = json.load(f)
f.close()		
try:
	with open("popularhashtag.txt", 'r') as f:
		a=[]
		pos_score=0
		neg_score=0

		for i in range (0,len(hashtags)-1):
			line=f.readline()
			a=line.split()
			num =float(a[0])
			rate=0
			for j in range ( 1, len(hashtags)):
				tweet = hashtags[j]
				if tweet['entities']['hashtags'][0]['text']==a[1]:
					score=sum(map(lambda word: afinn.get(word, 0), tweet['text'].lower().split()))
					rate+=score
			print int(num),a[1],"average Pos/Neg:",float(rate/num)
			if i<=10 :
				if float(rate/num) > pos:
					pos_text=a[1]
				if float(rate/num) < neg:
					neg_text=a[1]
except IndexError: pass
f.close()
print "In popular hashtags,"
print "most postive hashtag:", "\n",pos_text
print "most negtive hashtag:", "\n",neg_text
