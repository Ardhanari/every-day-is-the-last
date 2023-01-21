import datetime
import pymongo
import urllib
import dns
import env

TODAY = datetime.date.today()
print(TODAY)

# connect to mongoDB
# Replace the uri string with your MongoDB deployment's connection string.
client = pymongo.MongoClient("mongodb+srv://" + env.USERNAME +':' + env.PASSWORD + '@firstcluster.jvp2j.mongodb.net/every-day-is-the-last?retryWrites=true&w=majority")', serverSelectionTimeoutMS=5000)
try:
    yay = client.server_info()
    print(yay)
except Exception as e:
    print("Unable to connect to the server.")
    print(e)

db = client['every-day-is-the-last']
poems = db.poems
print(poems.find_one())