# Q.1- What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).
 # solution: An access token is an object that describes the security context of a process or thread. 
 # The information in a token includes the identity and privileges of the user account associated with the process or thread 
 # The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.
 # The information in a token includes the identity and privileges of the user account associated with the process or thread.
 # The security identifier (SID) for the user's account. SIDs for the groups of which the user is a member.
consumer_key='7lj1hR51VyMIfIZWuG7*****'
consumer_secret='lxFPkCQY9L2XtFVIZ9GKp8V4yeyHPf34lhjklfzWSqXEIpeJV'
access_token='1011129229440794624-GJL97j80DP6VJ2fAcfSZWNnBcmngd3'
access_secret='wn5d8sC6DD5Nxsfs0LSiAc0WnhqofEgdbherGVJ39UIi' 



# Q.2- Get the IP address of some common sites like Google, Facebook by using DNS lookup.
  #solution:
# C:\Users\dell\Desktop>nslookup google.com
# Server:  UnKnown
# Address:  fe80::5e99:60ff:fe0d:42ab

# Non-authoritative answer:
# Name:    google.com
# Addresses:  2404:6800:4002:807::200e
          # 172.217.161.14


# C:\Users\dell\Desktop>nslookup youtube.com
# Server:  UnKnown
# Address:  fe80::5e99:60ff:fe0d:42ab

# Non-authoritative answer:
# Name:    youtube.com
# Addresses:  2404:6800:4002:807::200e
          # 172.217.161.14


# C:\Users\dell\Desktop>nslookup whatsapp.com
# Server:  UnKnown
# Address:  fe80::5e99:60ff:fe0d:42ab

# Non-authoritative answer:
# Name:    whatsapp.com
# Addresses:  64:ff9b::a92c:5266
          # 64:ff9b::b8ad:9327
          # 64:ff9b::c09b:d4ca
          # 64:ff9b::b8ad:9326
          # 64:ff9b::a92c:54b2
          # 64:ff9b::c09b:d4cb
          # 192.155.212.203
          # 169.44.82.102
          # 184.173.147.39
          # 192.155.212.202
          # 184.173.147.38
          # 169.44.84.178



 # Q.3- Using Tweepy library try to extract tweets from Twitter.
import tweepy 

consumer_key='7lj1hR51VyMIfIZWuG78akjhg'
consumer_secret='lxFPkCQY9L2XtFVIZ9GKp8V4yeyHPf34lHLTeKyjkjhWSqXEIpeJV'

access_token='1011129229440794624-GJL97j80DP6VJ2fAcfSZWNvhjhghjcTdhWk'
access_secret='wn5d8sC6DD5Nhjjus0LSiAc0WnhqofEgc3sk46GVJ39UIi'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)
api=tweepy.API(auth)

tweets=api.search('#veereydiwedding',lang='en',count='5',tweet_mode="extended")

for tweet in tweets:
    print(".......")
    print(tweet.full_text)
    print(".........")
 
 # Q.4- What is a difference between library and API . Figure it out with examples.
 # solution:
# 1. A library is a collection of classes / methods you can use via referencing a compiled file.
# So your application is going to "include" those items and you'll need to take care of updates, deployment, etc.
import os
print(os.name)



# 2. An API (application programming interface)is just an interface, 
# so you can interact with other external applications without a direct relationship.
# For example: if you are dealing with dates, you will need to import the Java API for dates.
#API Java date Util
 
 

 