import dns.resolver
dns.resolver.default_resolver=dns.resolver.Resolver(configure=False)
dns.resolver.default_resolver.nameservers=['8.8.8.8']

import streamlit as st
import dataSample as dS
# import pymongo
import utility as util
import pandas as pd

utilities = util



# def app():
utilities.init_connection()
items = utilities.get_data("open2024", "open2024")
st.title("OPEN2024 KYNESIS RESULTS")
table_data = [{k: v for k, v in item.items() if k != '_id' and k!= 'Fecha'} for item in items]
items = table_data

def get_unique_values(items, field):
    return sorted(set(item[field] for item in items))

horarios = ('6:00:00 AM', '7:00:00 AM', '8:00:00 AM', '9:00:00 AM', '4:00:00 PM', '5:00:00 PM', '6:00:00 PM', '7:00:00 AM', '8:00:00 AM', 'Open gym')

st.title('Add new records')
horario_input = st.selectbox('Horario', horarios)
name_input = st.text_input('Nombre')
categoria_input = st.text_input('Categoria o peso')
resultado_input = st.text_input('Resultado')
create_button = st.button('Create new record')


feats = ("Horario", "Nombre", "Categoria (o peso)", "Resultado (reps)")
vals = [horario_input, name_input, categoria_input, resultado_input]

if create_button:
    if len(name_input) and len(categoria_input) > 0 and len(horario_input) > 0 and len(resultado_input) > 0:
        document = dict(zip(feats, vals))
        utilities.insert_document(document, 'open2024', 'open2024')

st.title('Current records')

if len(items) > 0:

    # Dropdowns for filtering
    filter_options = ['None', 'Horario', 'Categoria (o peso)']
    filter_choice = st.selectbox('Filter by:', filter_options)

    if filter_choice != 'None':
        if filter_choice == 'Categoria (o peso)':
            filter_value = st.selectbox(f'Select value for {filter_choice}:', set(item[filter_choice] for item in items))
            items = [item for item in items if item.get(filter_choice) == filter_value]
        else:
            filter_value = st.selectbox(f'Select value for {filter_choice}:', get_unique_values(items, filter_choice))
            items = [item for item in items if item.get(filter_choice) == filter_value]


    # Apply filtering
    if filter_choice != 'None':
        items = [item for item in table_data if item.get(filter_choice) == filter_value]
    
    # Apply sorting
    items.sort(key=lambda x: x.get('Resultado (reps)', ''), reverse = True)

    # Apply projection to exclude _id column
    df = pd.DataFrame(items)
    edited_df = st.data_editor(df)
    edit_button = st.button('Save changes')

    if edit_button:
        utilities.update_mongodb(edited_df, 'open2024', 'open2024')

else:
    st.write("No data found, contact your administrator.")

