import streamlit as st
import dataSample as dS
import pymongo

uri = "mongodb+srv://cmmurgav:8N8gtofsst8aJ2qN@cluser-exercise-log.qi8xd3g.mongodb.net/?retryWrites=true&w=majority&appName=cluser-exercise-log"



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