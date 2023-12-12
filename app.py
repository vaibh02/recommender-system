import numpy as np
import pandas as pd
import streamlit as st
import pickle
import json
from streamlit_lottie import st_lottie as stl
import requests as r
import sklearn
# import base64

def ll(url):
    R=r.get(url)
    if R.status_code != 200:
        return None
    return R.json()

ll1=ll("https://assets1.lottiefiles.com/packages/lf20_ybiszbil.json")
st.set_page_config("recommender system",layout="wide",page_icon="📚")
def hide_streamlit_elements():
    # Hide Streamlit "Powered by Streamlit" footer
    st.markdown(
        """
        <style>
            .viewerBadge_container__1QSob {
                display: none !important;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Hide top-right corner information
    st.markdown(
        """
        <style>
            .toolbarContainer {
                visibility: hidden;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

sidebar=st.sidebar
with sidebar:
    # st.header("System")
    st.subheader("""
                    System
                 This recommender suggests you the books based on popularity of books.              
                  """)
    stl(ll1,height=300,key='book')
    
model=pickle.load(open('model.pkl','rb'))

pt=pickle.load(open("pt.pkl",'rb'))

def fun(df):
    try:
        a,b,c,d,e=st.columns(5,gap='small')
        # st.success("Here is what we choose for you!!!")

        with a:
            st.image(df.iloc[0,-1])
            st.write(df.iloc[0,1])
            st.write(df.iloc[0,3])
        with b:
            st.image(df.iloc[1,-1])
            st.write(df.iloc[1,1])
            st.write(df.iloc[1,3])
        with c:
            st.image(df.iloc[2,-1])
            st.write(df.iloc[2,1])
            st.write(df.iloc[2,3])
        with d:
            st.image(df.iloc[3,-1])
            st.write(df.iloc[3,1])
            st.write(df.iloc[3,3])
        with e:
            st.image(df.iloc[4,-1])
            st.write(df.iloc[4,1])
            st.write(df.iloc[4,3])

        st.dataframe(df.iloc[:,1:-1])
    except:
        st.error("Suggesions Not Found!!")

def get(promt):
    try:    
        index=np.where(pt.index==promt)
        d,s=model.kneighbors(pt.iloc[index[0][0],:].values.reshape(1,-1),n_neighbors=6)
        n=pd.DataFrame(columns=df.columns)
        m=[]
        for i in range(1,len(s[0])):
            # print(pt.index[s[0][i]])
            m.append(pt.index[s[0][i]])    
        for i in m:
            row=df.loc[df['Title']==i]
            n=pd.concat([n,row],ignore_index=True)
        n.drop_duplicates(['Title'],inplace=True)
        return n
    except:
        st.write("Please Enter Book name!!")

df=pd.read_csv('books.csv')
left,right=st.columns(2)
    # with st.container():

st.write("# Books Recommendation System  📔📗📘📙")

st.write("""

                 ## Here we have a recommender system

                 Let's Caught what kind of things this small project consist
                 Let us Start Now!!

                 """)

# prompt=st.text_input("Enter the book name",placeholder='eg. Homeport, Summer Pleasures ')
prompt=st.selectbox("Enter the book name",df["Title"].unique())

        # st.write("----")
        


        
new=get(prompt)
st.write("----")

        

fun(new)

# with right:
#     ll2=ll("https://assets8.lottiefiles.com/packages/lf20_Q895iE.json")
#     stl(ll2,height=250)
    
hide_streamlit_elements()

import streamlit as st

background_image = './a.jpg'
    # Add some custom styles to set the background image
st.markdown(
    f"""
        <style>
            body {{
                background-image: url('{background_image}');
                background-size: cover;
            }}
        </style>
        """,
    unsafe_allow_html=True
)
hide_st_style = '''
<style> footer {visibility: hidden;} 
</style>
'''
st.markdown(hide_st_style, unsafe_allow_html=True)

footer_html = """
<style>
.footer {
    position: fixed;
    bottom: 0;
    width: 100%;
    color: white; /* Text color */
    padding: 10px;
    text-align: center; /* Center the text */
    font-size: 18px; /* Adjust the font size */
}
</style>
<div class="footer"></div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
