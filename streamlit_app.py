import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("Hello welcome to JenJen's new healthy diner, wowee")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 kale, Spinach, Apple & Rocket Smoothie")
streamlit.text("🐔 🐔 Hard Boiled Free Range VEGAN Egg")
streamlit.text("🥑🍞 Avocado Toast")

#import pandas
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

# Display the table on the page.
streamlit.dataframe(fruits_to_show)

#new section to display fruityvice api response
streamlit.header("Fruityvice Fruit Advice!")
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

#import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" +fruit_choice)

# normal the json response
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it as a table
streamlit.dataframe(fruityvice_normalized)

#dont run anything past here whilst we troubleshoot
streamlit.stop()

#import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)

#allow end user to add a fruit to the list
add_my_fruit = streamlit.text_input('What fruit would you like to add to the list?','Kiwi')
streamlit.write('Thanks for adding ', add_my_fruit)

#this will not work correctly yet
my_cur.execute("insert into fruit_load_list values ('from streamlit')");
