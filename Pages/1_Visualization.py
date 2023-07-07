#Importing the Packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import altair as alt
import streamlit as st
import numpy as np
import seaborn as sns
from wordcloud import WordCloud


@st.cache
def load_data():
    df = pd.read_csv('Dataset.csv', index_col='Year')
    return df

st.sidebar.title("*Analysis of Movie Dataset*")
st.sidebar.image('https://wpvip.edutopia.org/wp-content/uploads/2022/10/wolpert-gawron-using-film-analytical-skills-01.png?w=2880&quality=85?im=Resize=(1400,720),aspect=fill;Crop,size=(1400,720),gravity=Center')
user_menu= st.sidebar.radio(
    'click on a Dashboard to view',
     ('Show Movie Dataset', 'Release Year Vs Number of Movies', 'Release Year Vs Budget of Movies','Runtime Vs Release year','Top 25 Director who has directed maximum movies', 'Top 25 Actors who has acted in maximum movies', 'Top 25 Writer who has written maximum movies', 'Percentage and Number of Movies in each genre','Word Cloud of Countries which produced movies','Correlation between Budget and Gross')
)


df = load_data()

data=df.groupby('Year').count()['Name']
print(data)


if user_menu=='Show Movie Dataset':
    st.title(" Summary of the dataset ")
    st.table(df)


if user_menu=='Release Year Vs Number of Movies':

    data=df.groupby('Year').count()['Id']
    print(data.tail())
        
    st.title("*Number of movies releasing each Year*")
    df.groupby('Year').count()['Id'].plot(xticks = np.arange(1980,2025,5))

 
    sns.set(rc={'figure.figsize':(10,5)})
    plt.title("Year Vs Number Of Movies",fontsize = 14)
    plt.xlabel('Year',fontsize = 13)
    plt.ylabel('Number Of Movies',fontsize = 13)
    #set the style sheet
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Release Year Vs Budget of Movies':

    df.groupby('Year')['Budget'].mean().plot()

    st.title("*Budget of movies releasing each year*")
    plt.title("Year Vs Budget",fontsize = 14)
    plt.xlabel('Year',fontsize = 13)
    plt.ylabel('Budget',fontsize = 13)

  
    sns.set(rc={'figure.figsize':(10,5)})
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Runtime Vs Release year':
    
    df.groupby('Year').mean()['Runtime'].plot(xticks = np.arange(1980,2022,5))

    st.title("*Movies Runtime for each year of release*")
    sns.set(rc={'figure.figsize':(10,5)})

   
    plt.title("Runtime Vs Year",fontsize = 14)

   
    plt.xlabel('Year',fontsize = 13)
    plt.ylabel('Runtime',fontsize = 13)
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()


def count_genre(x):
    
    data_plot = df[x].str.cat(sep = '|')
    data = pd.Series(data_plot.split('|'))
    #conts each of the genre and return.
    info = data.value_counts(ascending=False)
    return info

if user_menu=='Top 25 Director who has directed maximum movies':
 
    count_actor_flims = count_genre('Director')
    count_actor_flims.iloc[:25].plot.bar(figsize=(13,6),colormap= 'tab20c',fontsize=12)
    st.title("*Number of movies made by director*")
    plt.title("Most Frequent Director",fontsize=15)
    plt.xticks(rotation = 70)
    plt.xlabel('Director',fontsize=13)
    plt.ylabel("Number Of Movies",fontsize= 13)
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Top 25 Actors who has acted in maximum movies':
    
    
    count_actor_flims = count_genre('Star')
    count_actor_flims.iloc[:20].plot.bar(figsize=(13,6),colormap= 'tab20c',fontsize=12)

    st.title("*Number of movies acted by each star*")
    plt.title("Most Frequent Star",fontsize=15)
    plt.xticks(rotation = 70)
    plt.xlabel('Star',fontsize=13)
    plt.ylabel("Number Of Movies",fontsize= 13)
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Top 25 Writer who has written maximum movies':

    count_actor_flims = count_genre('Writer')
    count_actor_flims.iloc[:25].plot.bar(figsize=(13,6),colormap= 'tab20c',fontsize=12)

    st.title("*Number of movies written by each writer*")
    plt.title("Most Frequent Writer",fontsize=15)
    plt.xticks(rotation = 70)
    plt.xlabel('Writer',fontsize=13)
    plt.ylabel("Number Of Movies",fontsize= 13)
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Percentage and Number of Movies in each genre':

    total_genre_movies = count_genre('Genre')
    
    total_genre_movies.plot(kind= 'barh',figsize = (13,6),fontsize=12,colormap='tab20c')
    st.title("*Percentage of Movies in each genre*")
    i = 0
    genre_count = []
    for Genre in total_genre_movies.index:
        genre_count.append([Genre, total_genre_movies[i]])
        i = i+1
        
    plt.rc('font', weight='bold')
    f, ax = plt.subplots(figsize=(5, 5))
    genre_count.sort(key = lambda x:x[1], reverse = True)
    labels, sizes = zip(*genre_count)
    labels_selected = [n if v > sum(sizes) * 0.01 else '' for n, v in genre_count]
    ax.pie(sizes, labels=labels_selected,
        autopct = lambda x:'{:2.0f}%'.format(x) if x > 1 else '',
        shadow=False, startangle=0)
    ax.axis('equal')
    plt.tight_layout()

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()
    
    def count_genre(x):
    #concatenate all the rows of the genrs.
        data_plot = df[x].str.cat(sep = '|')
        data = pd.Series(data_plot.split('|'))
    #conts each of the genre and return.
        info = data.value_counts(ascending=False)
        return info

    #call the function for counting the movies of each genre.
    total_genre_movies = count_genre('Genre')
    #plot a 'barh' plot using plot function for 'genre vs number of movies'.
    total_genre_movies.plot(kind= 'barh',figsize = (13,6),fontsize=12,colormap='tab20c')

    #setup the title and the labels of the plot.
    plt.title("Genre With Highest Release",fontsize=15)
    plt.xlabel('Number Of Movies',fontsize=13)
    plt.ylabel("Genres",fontsize= 13)
    sns.set_style("whitegrid")

    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()

if user_menu=='Word Cloud of Countries which produced movies':
    
    st.title("*Word Cloud of Countries which produced movies*")
    
    st.markdown('<p class="big-font"> Countries </p>', unsafe_allow_html=True)
    wc = WordCloud(max_font_size=130, min_font_size=25, colormap='tab20', background_color='white', 
                           prefer_horizontal=.95, width=1500, height=500, random_state=0)
    counts = df['Country'].value_counts()
    cloud = wc.generate_from_frequencies(counts)
    plt.figure(figsize=(18,15))
    plt.imshow(cloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()
    
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()
    
if user_menu=='Correlation between Budget and Gross':
    
    st.title("*Correlation between Budget and Gross*")
    ax = sns.regplot(x=df['Budget'], y=df['Gross'],color='c')

    
    ax.set_title("Budget Vs Gross",fontsize=13)
    ax.set_xlabel("Budget",fontsize=12)
    ax.set_ylabel("Gross",fontsize=12)
    #set the figure size
    sns.set(rc={'figure.figsize':(6,4)})
    sns.set_style("whitegrid")

   
    df['Gross'] = df['Gross'].replace(0,np.NAN)
    df['Budget'] = df['Budget'].replace(0,np.NAN)

   
    data_corr = df.corr()
    print("Correlation Between Revenue And Budget : ",data_corr.loc['Budget','Gross'])
    
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.pyplot()
    
  
  

    
    

    

























