import datetime
import pymongo
import urllib
import dns
import env

TODAY = datetime.date.today()
print(TODAY)

def connect_to_db():
    # connect to mongoDB
    # Replace the uri string with your MongoDB deployment's connection string.
    client = pymongo.MongoClient("mongodb+srv://" + env.USERNAME +':' + env.PASSWORD + '@firstcluster.jvp2j.mongodb.net/every-day-is-the-last?retryWrites=true&w=majority")', serverSelectionTimeoutMS=5000)
    try:
        yay = client.server_info()
        print(yay)
        return client
    except Exception as e:
        print("Unable to connect to the server.")
        print(e)
        return None


def find_last_poem():
    client = connect_to_db()
    db = client['every-day-is-the-last']
    poems = db.poems
    # print(poems.find_one())
    poem = poems.find_one()

    return poem