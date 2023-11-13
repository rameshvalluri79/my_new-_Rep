import streamlit
streamlit.title('Oh ! My God Its My New First streamlit Message')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and BluBerry Oatmeal')
streamlit.text('🥗 Kale & Spinach Rocket meal')
streamlit.text('🐔 Hard Boiled Egg')
streamlit.text('🥑🍞 Brandy Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Kiwifruit','Pineapple'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
# Display the table on the page.
streamlit.dataframe(fruits_to_show)
