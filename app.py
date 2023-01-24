import streamlit as st
import joblib
import pandas as pd

train=pd.read_csv('train.csv')
state_df=pd.read_csv('state_value.csv')

with open('clf2','rb') as f:
    rf=joblib.load(f)

st.title('Churn Predictor')
st.header('It predicts wheteher the customer will churn or not based on the imput data')

state=st.selectbox('select the state',train['state'].unique())
Intl_pln=st.selectbox('Any international',['Yes','No'])
voice_plan=st.selectbox('Any voice plan',['Yes','No'])

if Intl_pln=='Yes':
    Intl_pln_val=1
else:
    Intl_pln_val=0 

if voice_plan=='Yes':
    voice_plan_val=1
else:
    voice_plan_val=0 


no_email=st.number_input('Enter number of emails recieved per day by customer')
no_csc=st.number_input('Enter number of Customer service call recieved by customer')
no_email=no_email
no_csc=int(no_csc)
total_minutes=no_csc*2.5
total_charge=total_minutes*0.5
mail_wise_rank=0
if no_email==0:
    mail_wise_rank=2
elif no_email%2==0:
    mail_wise_rank=1
else:
    mail_wise_rank=0
csc_wise_rank=0
if no_csc in [0,1,2,3,4]:
    csc_wise_rank=1
else:
    csc_wise_rank=0

state_value=state_df[state_df['state']==state]['value']
x=[Intl_pln_val,voice_plan_val,total_minutes,total_charge,state_value,mail_wise_rank,csc_wise_rank]
y=rf.predict(x)
if st.button('Predict'):
    if y==0:
        st.write('Custumer will not churn')
    else:
        st.write('Custumer will churn')
