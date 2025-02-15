from pymongo import MongoClient
import pprint
import re

# client  = MongoClient('localhost', 27017)
client = MongoClient('mongodb://localhost:27017/')

# Get reference to 'chinook' database
db = client ["chinook"]

# Get reference to 'customers' collection
customers_collection = db["customers"]

doc1 = customers_collection.find_one()
print(doc1)

# print all documents
for all_doc in customers_collection.find():
    print(all_doc)

# retrun only the LastName and FirstName
for rec in customers_collection.find({}, {"_id": 0, "LastName": 1, "FirstName": 1}):
    print(rec)

# Print all customers with LastName that starts with "G"

rgx = re.compile('^G.*?$', re.IGNORECASE) #compile the regex
cursor  = customers_collection.find({"LastName": rgx})  
num_docs = 0
for document in cursor: 
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of document found: " + str(num_docs))
client.close()