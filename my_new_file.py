import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title('Oh ! My God Its My New First streamlit Message')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and BluBerry Oatmeal')
streamlit.text('🥗 Kale & Spinach Rocket meal')
streamlit.text('🐔 Hard Boiled Egg')
streamlit.text('🥑🍞 Brandy Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Kiwifruit','Pineapple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#create the repeatable code block (called a function) 
def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
    
streamlit.header('Fruityvice Fruit Advice!')
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about?') 
    if not fruit_choice:
        streamlit.error("Please select a fruit to get information.")
    else:
        back_from_function = get_fruityvice_data(fruit_choice) 
        streamlit.dataframe(back_from_function)
