import streamlit as st
import pandas as pd
import requests
import snowflake.connector

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")


fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "kiwi")

#New Section to display fruityvice api response
st.header('Fruityvice Fruit Advice!')
fruit_choice = st.text_input('What fruit would you like information about?', 'Kiwi')
st.write('The user entered', fruit_choice)
requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

# take the json version of the response and normalize it
fruityvice_normalized = pd.json_normalize(fruityvice_response.json())
#output it the screen as a table
st.dataframe(fruityvice_normalized)

st.dataframe(my_fruit_list)
st.header("Header")
#df = pd.DataFrame({
#  'first column': [1, 2, 3, 4],
#  'second column': [10, 20, 30, 40]
#})
#df

st.header('Breakfast Menu')
st.text('Omega 3 & Blueberry Oatmeal')
st.text('Kale, Spinach & Rocket Smoothie')
st.text('Hard-Boiled Free-Range Egg')


pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")

my_fruit_list.set_index("Fruit")

# Let's put a pick list here so they can pick the fruit they want to include
fruitsSelect = st.multiselect(
    "Pick some fruits:",
    #options=list(my_fruit_list.index),
    options=list(my_fruit_list["Fruit"]),
    default=["Avocado","Strawberries"])


#names = pd.DataFrame({'labels':["Green","Yellow","Red","Blue"]})
#nameSelect = st.multiselect(
#    "What are your favorite colors",
#    options=list(names['labels']), # convert to list
#    default=["Yellow"]
#)
fruit_to_show = my_fruit_list.loc[fruitsSelect]
#display the table on the page
print('Print:', fruit_to_show)
st.dataframe(fruitsSelect)

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
st.text("Hello from Snowflake:")
st.text(my_data_row)


