import streamlit
import snowflake.connector

streamlit.header("Zenas Amazing Atheleisure Catalog")


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])

def return_colours():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select COLOR_OR_STYLE from catalog_for_website")
        return my_cur.fetchall()

colours = return_colours()
streamlit.text(type(colours))

#fruits_selected = streamlit.multiselect("Pick a sweatsuit colour or style:", list(my_fruit_list.index),["Avocado","Strawberries"])

