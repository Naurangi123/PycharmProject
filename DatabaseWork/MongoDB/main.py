import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Commercial"] # Database name

mycoll=mydb["customers"] # Collection name

mydict = { "name": "Naurangi lal", "address": "Duahi Ghzaibad","profile":"Student" }

x = mycoll.insert_one(mydict)
print(x.inserted_id)


# To check database is existed or not
dbs=myclient.list_database_names()
print(dbs)
if "Commercial" in dbs:
    print("dbs is exsists")
# To check Collection existed or not
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")

