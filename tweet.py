from twython import Twython
from pymongo import MongoClient
import json
import pprint

# client = MongoClient()
# db = client.twitterdb
# xs={"name":"mahika","afe":"19"}
# db.eg.insert(xs)
# print "majika"
# for a in db.eg.find():
# 	print a

app_key = 'frEaJdpWcYQRcaYSvtmCg1uyI'
app_secret = 'xtSQzEW1jQSF74bjoHk94bP8FEUZy7TiTdkcHdv2VqcPVaUIJc'
oauth_token = "712657229174812673-ufHCP8sJr8jvj8bFgSbjXLpC8fweIZV" # from step 2
oauth_token_secret = 'gPbcmF2dc9t3xlvA4qmxpycppIanIJ5eBj27gkUzdlx78' # from step 2

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)
user_input = raw_input("Enter ids separated by commas: ")

input_list = user_input.split(',')
for i in input_list:
	trends = twitter.search(q=i,result_type="mixed",count=100)
	for hashtag in trends:
		pprint.pprint(trends[hashtag])
		print("\n\n\n\n\n")
	# 	print ""
	# 	for x in t:
	# 		print x
	# print(trends[0]['trends'])
	# f = open('out.txt', 'w')

	# for item in trends:
	#     for data_item in item['trends']:
	#     	if(data_item['tweet_volume'] is None):
	#     		data_item['tweet_volume'] = ""
	#     	if(data_item['url'] is None):
	#     		data_item['url'] = ""
	#     	try:
	#     		f.write(data_item['name'] + "  " + str(data_item['tweet_volume']) +  "\n")
	#     	except UnicodeEncodeError:
	#     		f.write(data_item['name'].encode('utf-8') + "\n")
	# f.close()


