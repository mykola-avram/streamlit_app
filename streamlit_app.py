import streamlit as st
import pandas as pd

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
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




