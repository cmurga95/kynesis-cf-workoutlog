import streamlit as st
import dataSample as dS
import pymongo

username = st.secrets['username']
password = st.secrets['password']

# uri = f"mongodb+srv://cmmurgav:8N8gtofsst8aJ2qN@cluser-exercise-log.qi8xd3g.mongodb.net/"

uri = f"mongodb+srv://{username}:{password}@cluser-exercise-log.qi8xd3g.mongodb.net/"


# client = pymongo.MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)



@st.cache_resource
def init_connection():
    client = pymongo.MongoClient(uri)
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)

    return client


client = init_connection()
# db = client("myOwn")
# collection = db("sample_collection")

@st.cache_data(ttl=600)

def get_data(database, collection):
    db = client[database]
    collection = db[collection]
    items = list(collection.find())  # make hashable for st.cache_data
    return items

def client_data(database, collection):
    client = pymongo.MongoClient(uri)
    db = client[database]
    collection = db[collection]
    return client, db, collection

def update_mongodb(data, database, collection):
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)
    db = client[database]
    collection = db[ collection]

    # Convert DataFrame to list of dictionaries
    data_dict = data.to_dict(orient='records')

    # Update MongoDB collection with new data
    collection.delete_many({})  # Clear existing data
    collection.insert_many(data_dict)  # Insert new data

def insert_document(data, database, collection):
    # Connect to MongoDB
    client = pymongo.MongoClient(uri)
    db = client[database]
    collection = db[ collection]
    collection.insert_one(data)
