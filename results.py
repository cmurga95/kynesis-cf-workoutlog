import streamlit as st
import dataSample as dS
# import pymongo
import utility as util

utilities = util



# def app():
utilities.init_connection()
items = utilities.get_data("open2024", "open2024")
st.title("OPEN2024 KYNESIS RESULTS")
# date = st.date_input("Enter the date")

# st.write(items.get('Nombre') == 'Laura' )

def get_unique_values(items, field):
    return sorted(set(item[field] for item in items))


if len(items) > 0:
    table_data = [{k: v for k, v in item.items() if k != '_id' and k!= 'Fecha'} for item in items]
    items = table_data

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
    st.table(items)

else:
    st.write("No data found, contact your administrator.")

