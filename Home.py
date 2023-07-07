from PIL import Image
import streamlit as st

img=Image.open("icon.png")
st.set_page_config(
    page_title="Visualisation for a Movie Dataset",
    page_icon=img,
)

st.title("*Movie Dataset Analysis Recommendation*")

st.header("*Project Goal*")

st.markdown("The main Goal of this project is to create visualizations on Movie Dataset using Streamlit. Dataset has attributes such as Movie name, Rating, Genre, Released Year, Score, Details of Actors, Directors, Writers, Gross and Budget of the movie etc., which helps to analyze the patterns such as the Profit for the production companies, which genre movies are released more in each year, Top 25 actors who acted in most number of movies in a year etc..")

st.header("*Submitted by*")
st.markdown("Jaswanth Yadla")
st.markdown("Veda Samhitha Dyawanapally")
st.markdown("Penuel Odiaka")
st.markdown("Jakob Stallard")
