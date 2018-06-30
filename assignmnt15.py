            #ASSIGNMENT-15 (REGULAR EXPRESSIONS)

# Q.1- Extract the user id, domain name and suffix from the following email addresses. 
# emails = "zuck26@facebook.com" "page33@google.com"
# "jeff42@amazon.com"
# desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]
#SOLUTION
import re
emails = "zuck26@facebook.com  page33@google.com  jeff42@amazon.com"
p=(r"(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})")
R=re.findall(p,emails,flags=re.IGNORECASE)
print(R)


# Q.2- Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
# text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, 
# To make the bitter butter better." 
#solution:
import re
s="Betty bought a bit of butter, But the butter was so bitter,So she bought some better butter,To make the bitter butter better." 
p=re.compile(r"[b]\w+")
result=p.findall(s)
print(result)



# Q.3- Split the following irregular sentence into words 
# sentence = "A, very very; irregular_sentence"
# desired_output = "A very very irregular sentence"
#solution:
import re
s = "A, very very; irregular_sentence"
a=re.sub(r"[^\w]"," ",s)
p=re.sub("_"," ",a)
print(p)




 # Q.1- Clean up the following tweet so that it contains only the user’s message. 
 # That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs. 
# tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats''' 
# desired_output = 'Good advice What I would do differently if I was learning to code today'
#solution:
import re
tweet ='''Good advice! RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt'''

def clean_tweet(tweet):
    tweet=re.sub('http\S+\s*',' ',tweet) 
    tweet=re.sub('RT|cc',' ',tweet)
    tweet=re.sub('#\S+',' ',tweet)
    tweet=re.sub('@\S+',' ',tweet)
    tweet=re.sub('[%s]'% re.escape("""!"#$%&'( )*+,-./:;<=>?@[\]^_ `{|}~"""),' ',tweet)
    #tweet=re.sub('\s+',' ',tweet)
    return tweet
print(clean_tweet (tweet))

