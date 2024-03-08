# import streamlit as st
# import pandas as pd
# from pymongo import MongoClient
# import results, registerResults


# import dataSample as dS

# #connecting to mongoDB

# uri = "mongodb+srv://cmmurgav:8N8gtofsst8aJ2qN@cluser-exercise-log.qi8xd3g.mongodb.net/?retryWrites=true&w=majority&appName=cluser-exercise-log"

# client = MongoClient(uri)

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# st.title('Welcome')

# PAGES = {
#     "Create WOD": results,
#     "registerResults": registerResults
# }

# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Title", list(PAGES.keys()))
# page = PAGES[selection]
# page.app()
