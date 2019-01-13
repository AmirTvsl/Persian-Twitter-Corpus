from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time


#consumer key, consumer secret, access token, access secret.
ckey="Pugtk5W3En0xAxV12jzdvSOv0"
csecret="QmKediAatKO79mXg1LH2CBBuNgh2GiFTcgPtJMs1bVRgnnxYyi"
atoken="943564393996083201-rvxRPPecOqYgSMI8jor0xNx5sIORBCn"
asecret="6Cgrx9ltxfb3rU2PH5sMVId3VBCgsKABp5KAa4CtYbODK"

#---------------------------------------------------------------
class listener(StreamListener):

    def on_data(self, data):
        try:
            #print(data)

            tweet = data.split(',"text":"')[1].split('","source')[0]
            print (tweet)
            saveThis = str(tweet)
            
            saveFile = open('twitDB.csv','a')
            saveFile.write(saveThis)
            saveFile.write('\n')
            saveFile.close()
            return True
        except BaseException as e:
            print ('failed ondata,',str(e))
            time.sleep(5)
            
    def on_error(self, status):
        print (status)
#-----------------------------------------------------------------
auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["ايران"],languages=['fa'])
		
