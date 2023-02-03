# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:41:34 2023

@author: Namitha
"""

from deta import Deta
import streamlit as st
DETA_KEY=st.secrets["DETE_KEY"]
# Initialize with a project key
deta = Deta(DETA_KEY)
# This is how to create/connect a database
db = deta.Base("Calorie_data")

def insert_data(age,gender,height,weight,duration,heart_rate,temparature,result):
    return db.put({"age": age, "gender": gender,"Height":height,"Weight":weight,"Duration":duration,
        "Heart_rate":heart_rate,"Temparature":temparature,"Result":result})

