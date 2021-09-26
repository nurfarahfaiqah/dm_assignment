# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 16:35:01 2021

@author: User
"""

import streamlit as st 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


from PIL import Image 
Image.open('mmu_logo.png').convert('RGB').save('mmu_logo.png')
im = Image.open("mmu_logo.png")
st.image(im, width=300)

st.header("TDS3301: DATA MINING")

st.header("Title: Data Mining in E-Commerce")


st.subheader("Prepared by:")
st.subheader("1181101517  AINA AFRINA BINTI MOHD NASIR")
st.subheader("1181101238  NURFARAH FAIQAH BINTI DAUD")
st.subheader("1181101272  NUR WAHAFIZAH BINTI AHMADI ")



st.markdown("## Question 3")

st.markdown("### (i) Discuss the exploratory data analysis steps you have conducted including detection of outliers and missing values?")

st.markdown("** Check for missing values**")
cases_malaysia = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_malaysia.csv')
cases_state = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/cases_state.csv')
clusters = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/clusters.csv')
tests_malaysia = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/tests_malaysia.csv')
test_state = pd.read_csv('https://raw.githubusercontent.com/MoH-Malaysia/covid19-public/main/epidemic/tests_malaysia.csv')

cases_malaysia
cleaned_cases_malaysia = cases_malaysia.fillna(0)
cleaned_cases_malaysia

st.markdown("There are four datasets all together:")
st.markdown("* cases_malaysia")
st.markdown("* cases_state")
st.markdown("* clusters")
st.markdown("* test_malaysia")
st.markdown("Out of the four datasets, only cases_malaysia dataset has missing values. We solve this problem by filling the null values with 0.")

st.markdown("** Exploratory Data Analysis**")


fig1, ax = plt.subplots(figsize=(15, 5))
sns.boxplot(data = cleaned_cases_malaysia, orient = 'h', ax = ax)
fig1
st.markdown("Figure 1 : Boxplot for cases_malaysia")


fig2, ax = plt.subplots(figsize=(15, 5))
sns.boxplot(data = cases_state, orient = 'h', ax = ax)
fig2
st.markdown("Figure 2 : Boxplot for cases_state")


fig3, ax = plt.subplots(figsize=(20, 5))
sns.boxplot(data = clusters, orient = 'h', ax = ax)
fig3
st.markdown("Figure 3 : Boxplot for clusters")


fig4, ax = plt.subplots(figsize=(15, 5))
sns.boxplot(data = tests_malaysia, orient = 'h', ax = ax)
fig4
st.markdown("Figure 4 : Boxplot for test_malaysia")

st.markdown("### 3(ii) What are the states that exhibit strong correlation with (i) Pahang, and (ii) Johor?")


fig5, ax = plt.subplots(figsize=(15, 5))
cs_pivot = cases_state.pivot(columns='state')
cleaned_cs_pivot = cs_pivot.fillna(0)
state_cases_import = cleaned_cs_pivot['cases_import']
state_cases_import = state_cases_import.fillna(0)
state_cases_import = state_cases_import.iloc[:,:].corr().round(1)
sns.heatmap(state_cases_import.corr(), cmap='cividis')
fig5
st.markdown("Figure 5 : Correlation for cases_import")

fig6, ax = plt.subplots(figsize=(15, 5))
state_cases_new = cleaned_cs_pivot['cases_new']
state_cases_new = state_cases_new.fillna(0)
state_cases_new = state_cases_new.iloc[:,:].corr().round(1)
sns.heatmap(state_cases_new.corr(), cmap='cividis')
fig6
st.markdown("Figure 6 : Correlation for cases_new")

fig7, ax = plt.subplots(figsize=(15, 5))
state_cases_recovered = cleaned_cs_pivot['cases_recovered']
state_cases_recovered = state_cases_recovered.fillna(0)
state_cases_recovered = state_cases_recovered.iloc[:,:].corr().round(1)
sns.heatmap(state_cases_recovered.corr(), cmap='cividis')
fig7
st.markdown("Figure 7 : Correlation for cases_recovered")
