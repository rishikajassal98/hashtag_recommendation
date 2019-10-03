# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:23:42 2018

@author: Rishika
"""
import csv
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = "ZzAnVAGAhYFlPeMNqV49MhOzP"
consumer_secret ="86usOlYQnpN6XoUaLosW73gewXXz9hYd2Fe0gJBa36kJOypQKT" 
access_token ="1005133638244036608-eKLh5A2QIwQiq1wiTPKySIOITYd0wA"
access_secret ="h6HrCMS3VhIP0xumLNq2JUTiwAfOQNQWr5cVCrpB7e1pF"
def get_hashtags(text, order=False):
    tags = [item.strip("#.,-\"\'&*^!") for item in text.split() if (item.startswith("#") and len(item) < 256)]
    return sorted(tags) if order else tags

def getNew(text, order=False):
    for item in text.split():
        if (item.startswith("#") and len(item) < 256):
            tags=str(item.strip("#.,-\'&*^!"))
    return tags

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
    def __init__(self):
        super().__init__()
        self.counter = 0
        self.limit = 978
 
    def on_status(self, status):
        
        csvFile = open('TwoThousand.csv', 'a', encoding="utf-8")
        csvWriter = csv.writer(csvFile)
        z=[]
        z=get_hashtags(status.text, True)
        if(len(z) == 1):
            print(self.counter+1)
            print (status.created_at, status.text)
            getNew(status.text, True)
            csvWriter.writerow([status.created_at, status.text.encode('utf-8'), getNew(status.text, True)])
            csvFile.close()
            self.counter +=1
        if self.counter < self.limit:
            return True
        else:
            stream.disconnect()

 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening


l = StdOutListener()
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
stream = Stream(auth, l)

stream.filter(languages=['en'], track=['friday', 'saturday', 'sunday', 
              'weekend', 'party', 'morning', 'night', 'funny', 
              'happy', 'love', 'bliss', 'photography', 'funday', 
              'dance', 'music', 'art', 'festive', 'rock', 'best', 'friend'])