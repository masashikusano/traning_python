#!/usr/bin/env python
#-*- coding:utf-8 -*-
from requests_oauthlib import OAuth1Session
import json
### Constants
oath_key_dict = {
    "consumer_key" : "wZQ7lwaKpatg9k8FE6XsbzUUV",
    "consumer_secret" : "coy2bwrQJoT8kG1o7Vtu13M3R0p27g3yQAZP72Ivt4En7g2PAX",
    "access_token" : "759761046-MpkQlNnSlyFu8kaQAcH6JoOHBdhLITBum0KEwT3i",
    "access_token_secret" : "CmdRijuG6o5X6HuERLD2YkPduRIOzRcBC4ybe8ZU8ZCwj"
    }
### Functions
def main():
    tweets = tweet_search("hadoop",oath_key_dict)
    for tweet in tweets["statuses"]:
        tweet_id = tweet[u'id_str']
        text = tweet[u'text']
        created_at = tweet[u'created_at']
        user_id = tweet[u'user'][u'id_str']
        user_description = tweet[u'user'][u'description']
        screen_name = tweet[u'user'][u'screen_name']
        user_name = tweet[u'user'][u'name']
        print "tweet_id:",tweet_id
        print "text:",text
        print "created_at:",created_at
        print "user_id:",user_id
        print "user_desc:",user_description
        print "screen_name:",screen_name
        print "user_name:",user_name
        f = open('test.txt',"a")
        f.write((u"tweet_id:" + tweet_id + u"\n").encode("utf-8"))
        f.write((u"text:" + text + u"\n").encode("utf-8"))
        f.write((u"created_at:" + created_at + u"\n").encode("utf-8"))
        f.write((u"user_id:" + user_id + u"\n").encode("utf-8"))
        f.write((u"user_desc:" + user_description + u"\n").encode("utf-8"))
        f.write((u"screen_name:" + screen_name + u"\n").encode("utf-8"))
        f.write((u"user_name:" + user_name + u"\n\n").encode("utf-8"))
        f.close()
    return

def create_oath_session(oath_key_dict):
    oath = OAuth1Session(
    oath_key_dict["consumer_key"],
    oath_key_dict["consumer_secret"],
    oath_key_dict["access_token"],
    oath_key_dict["access_token_secret"]
    )
    return oath

def tweet_search(search_word,oath_key_dict):
    url = "https://api.twitter.com/1.1/search/tweets.json?"
    params = {
        "q" : unicode(search_word),
        "lang" : "ja",
        "result_type": "recent",
        "count" : "15"
        }
    oath = create_oath_session(oath_key_dict)
    responce = oath.get(url,params = params)
    if responce.status_code != 200:
        print "Error code: %d" %(responce.status_code)
        return None
    tweets = json.loads(responce.text)
    return tweets

### Execute
if __name__ == "__main__":
    main()
