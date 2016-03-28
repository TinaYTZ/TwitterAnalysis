# TwitterAnalysis
Please run: data_processing.py firist
Raw data sholud be named as twitterstream.json
Also put it with python file together
Run: python data_processing.py | head -10  
Get the sum of real Tweets
Real_tweet.json and With_hashtags.json generated automatically
First time, run python data_processing.py | sort | uniq -c | sort -n -r -o popularhashtag.txt
Get the the popularhashtags.txt
Real_tweet.json and With_hashtags.json generate automatically
Run:  python afinn.py
Assume afinn.py , With_hashtags.json, popularhashtag.txt and AFINN-111.txt in the same folder


