# (i) to run this file firstly go the env environment by : 
#     conda activate env 

# (ii) streamlit run app.py




import streamlit as st
import requests
import pickle

movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances= similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]

    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        # st.text(movie_id)
        recommended_movies.append(movies.iloc[i[0]].title)
        # st.text(recommended_movies)

        # fetching poster from Api
        recommended_movies_poster.append(fetch_poster(movie_id))
        # st.text(recommended_movies_poster)

    return recommended_movies,recommended_movies_poster

def fetch_poster(movie_id):
    # st.text(movie_id)
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=7c631c8fe1fb0c42468977a68130a88a&&language=en-US'.format(movie_id))
    # st.text(response)
    data=response.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
    
    


st.title('Movie Recommender System')
selected_movie_name = st.selectbox('Hey ! select a movie bro : ',(movies['title']  ))

st.write('You selected:', selected_movie_name)

if st.button('Recommend'):
    names,poster=recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])

    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
