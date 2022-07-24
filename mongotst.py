import pymongo

'''client = pymongo.MongoClient("mongodb+srv://pradeepbhs:Bhs243608@cluster0.f7ntnlr.mongodb.net/?retryWrites=true&w=majority")
db = client.test'''

client = pymongo.MongoClient("mongodb+srv://pradeep:ineuron@cluster0.kjwt7om.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d1 = {"name":"pradeep",
      "email":"bhs@gmail.com",
      "surname": "bandaru"}
db1 = client['mongotst']
coll = db1['test']
coll.insert_one(d1)
print("abc")