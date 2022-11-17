import pymongo

client = pymongo.MongoClient("mongodb+srv://harshinde:Harsh123@sky.nildvoj.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

#client = pymongo.MongoClient("mongodb+srv://harshinde:Harsh@123@sky.nildvoj.mongodb.net/?retryWrites=true&w=majority")

d = {
    "name":"Harsh",
    "email":"Harsh@ineuron.ai",
    "surname":"Shinde"
}
db1 = client['mongotest']
collection = db1['test']
collection.insert_one(d )

