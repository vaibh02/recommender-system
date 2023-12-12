import numpy as np
import pandas as pd
import streamlit as st
import pickle
import json
from streamlit_lottie import st_lottie as stl
import requests as r
def ll(url):
    R=r.get(url)
    if R.status_code != 200:
        return None
    return R.json()

ll1=ll("https://assets1.lottiefiles.com/packages/lf20_ybiszbil.json")
st.set_page_config("Book Recommendation",layout="wide")


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
        st.dataframe(df.iloc[:,1:-1])
        a,b,c,d,e=st.columns(5)
        m=[a,b,c,d,e]
        # st.success("Here is what we choose for you!!!")
        for i in range(len(m)):
            with m[i]:
                st.image(df.iloc[i,-1])
                st.write(df.iloc[i,1])
                st.write(df.iloc[i,3])
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
            row=df.loc[df['title']==i]
            n=pd.concat([n,row],ignore_index=True)
        n.drop_duplicates(['title'],inplace=True)
        return n
    except:
        st.write("Please Enter Book name!!")

df=pd.read_csv('books.csv')
left,right=st.columns(2)
with left:
    with st.container():

        st.write("# Books Recommendation System  📔📗📘📙")

        st.write("""

                 ## Here we have a recommender system

                 Let's Caught what kind of things this small project consist
                 Let us Start Now!!

                 """)

        prompt=st.text_input("Enter the book name",placeholder='eg. Homeport, Summer Pleasures ')
        # st.write("----")
        


        # def get(promt):
        #     index=np.where(pt.index==promt)
        #     d,s=model.kneighbors(pt.iloc[index[0][0],:].values.reshape(1,-1),n_neighbors=6)
        #     n=pd.DataFrame(columns=df.columns)
        #     m=[]
        #     for i in range(1,len(s[0])):
        #         # print(pt.index[s[0][i]])
        #         m.append(pt.index[s[0][i]])    
        #     for i in m:
        #         row=df.loc[df['title']==i]
        #         n=pd.concat([n,row],ignore_index=True)
        #     n.drop_duplicates(['title'],inplace=True)
        #     return n

        # def get(promt):
        #     try:    
        #         index=np.where(pt.index==promt)
        #         d,s=model.kneighbors(pt.iloc[index[0][0],:].values.reshape(1,-1),n_neighbors=6)
        #         n=pd.DataFrame(columns=df.columns)
        #         m=[]
        #         for i in range(1,len(s[0])):
        #             # print(pt.index[s[0][i]])
        #             m.append(pt.index[s[0][i]])    
        #         for i in m:
        #             row=df.loc[df['title']==i]
        #             n=pd.concat([n,row],ignore_index=True)
        #         n.drop_duplicates(['title'],inplace=True)
        #         return n
        #     except:
        #         st.write("Please Enter Book name!!")
        new=get(prompt)
        st.write("----")

        # def func(new):
        #     st.dataframe(new)
        #     a,b,c,d,e=st.columns(5,gap='small')
        #     with a:  
        #         st.image(new.iloc[0,-1])
        #         st.write(new.iloc[0,1])
        #         st.write(new.iloc[0,3])
        #     with b:
        #         st.image(new.iloc[1,-1])
        #         st.write(new.iloc[1,1])
        #         st.write(new.iloc[1,3])
        #     with c:
        #         st.image(new.iloc[2,-1])
        #         st.write(new.iloc[2,1])
        #         st.write(new.iloc[2,3])
        #     with d:
        #         st.image(new.iloc[3,-1])
        #         st.write(new.iloc[3,1])
        #         st.write(new.iloc[3,3])
        #     with e:
        #         st.image(new.iloc[4,-1])
        #         st.write(new.iloc[4,1])
        #         st.write(new.iloc[4,3])

        # def fun(df):
        #     try:
        #         a,b,c,d,e=st.columns(5,gap='small')
        #         m=[a,b,c,d,e]
        #         # st.success("Here is what we choose for you!!!")
        #         for i in range(len(m)):
        #             with m[i]:
        #                 st.image(df.iloc[i,-1])
        #                 st.write(df.iloc[i,1])
        #                 st.write(df.iloc[i,3])
        #     except:
        #         st.error("Suggesions Not Found!!")


        fun(new)




with right:
    ll2=ll("https://assets8.lottiefiles.com/packages/lf20_Q895iE.json")
    stl(ll2,height=250)

import streamlit as st

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
background-image: url("a.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

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
<div class="footer">Made by Vipul Malyan</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)
