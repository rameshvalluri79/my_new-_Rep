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
streamlit.header('Fruityvice Fruit Advice!')
# Allow the end user to add a fruit to the list
def insert_row_snowflake (new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('from streamlit')") 
         return "Thanks for adding + new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?') 
if streamlit.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets ["snowflake"]) 
   back_from_function = insert_row_snowflake(add_my_fruit)
   streamlit.text(back_from_function)

streamlit.header("The fruit load list contains:") 
#Snowflake-related functions
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

# Add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe (my_data_rows)
streamlit.stop()
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like to add ?','Jackfruit')
streamlit.write('Thanks for adding ', fruit_choice)
my_cur.execute("insert into fruit_load_list values('From Streamlit')")

