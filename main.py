from fastapi import FastAPI
from pymongo import MongoClient

client = MongoClient("mongodb+srv://teo_deville:2IJW0bXiZexSSL75@cluster0-csv2v.mongodb.net/test")

db = client.get_database('MyFirstMongoDB')

records = db.MyFirstMongoCollection
i= records.count_documents({})
print (i)

app = FastAPI()

@app.get("/my-first-api")
def hello(name = None):

    if name is None:
        text = 'Hoy!'

    else:
        text = 'Hoy ' + name + '!' + i

    return text
