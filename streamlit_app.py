import streamlit

streamlit.title("Hello welcome to JenJen's new healthy diner, wow")

streamlit.header("Breakfast Menu")

streamlit.text("🥣 Omega 3 & Blueberry Oatmeal")
streamlit.text("🥗 kale, Spinach, Apple & Rocket Smoothie")
streamlit.text("🐔 🐔 Hard Boiled Free Range VEGAN Egg")
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
