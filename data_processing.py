import json
import os
import sys

##Raw data sholud be named as twitterstream.json
##Also put it with python file together
##First time, run python data_processing.py | sort | uniq -c | sort -n -r -o popularhashtag.txt
##Get the the popularhashtags.txt
##Real_tweet.json and With_hashtags.json generate automatically

tweets = []
newcreate=[]
hashtags=[]

#open and read json file
with open ("twitterstream.json",'r') as f:
	try:
		while True:
			line= f.readline()
			tweets.append(json.loads(line))
	except ValueError: pass
f.close()

#length of all records
print "All records:",len(tweets)

#filter
for  i in range (1,len(tweets)):
    	tweet = tweets[i]
    	keys=tweet.keys()
    	for i in range ( 1 ,len(keys)):
		if keys[i]=="text":
			newcreate.append(tweet)
fout= open ("Real_tweet.json", 'w')
json.dump(newcreate,fout)
fout.close()
#length of real tweets
print "Real tweets:",len(newcreate)

#hashtag
for  i in range (1,len(newcreate)):
	tweet = newcreate[i]
	try:
		hasharray = tweet['entities']['hashtags']
		try:
			hashtext = hasharray[0]['text']
			try:	
				hashtags.append(tweet)		
				print(hashtext)
			except ValueError: pass
  		except IndexError: pass
	except KeyError: pass
print "With hashtags:", len(hashtags)
fout= open ("With_hashtags.json", 'w')
json.dump(hashtags,fout)
fout.close()

