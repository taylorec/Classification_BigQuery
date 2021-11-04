# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:25:51 2021

@author: evan
"""

import streamlit as st
import joblib

st.title('Tip Predictor')
st.write("This app predicts if a customer will give a tip. This data comes from the chicago_taxi_trips.taxi_trips Google Big Query database.")
 
loaded_GB = joblib.load('GBmodel.joblib')

trip_seconds = st.number_input('Trip duration in seconds', min_value=1)
trip_miles = st.number_input('Trip distance in miles', min_value=0.1)
pickup_comm = st.number_input('Community area of pick up', min_value=1)
dropoff_comm = st.number_input('Community area of drop off', min_value=1)
fare = st.number_input('Cost of fare', min_value=0.01)
tolls = st.number_input('Cost of tolls', min_value=0.00)
extras = st.number_input('Cost of extras', min_value=0.00)
payment_type = st.selectbox('Payment type', ['Credit Card', 'Cash', 'Mobile', 'Prcard', 'No Charge', 'Other'])
month = st.selectbox('Month of trip', ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                                        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
day = st.selectbox('Day of trip', ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
hour = st.selectbox('Closest hour of trip start', ['12am', '1am', '2am', '3am',
                                                    '4am', '5am', '6am', '7am',
                                                    '8am', '9am', '10am', '11am',
                                                    '12pm', '1pm', '2pm', '3pm',
                                                    '4pm', '5pm', '6pm', '7pm',
                                                    '8pm', '9pm', '10pm', '11pm'])


if payment_type == 'Credit Card':
    payment_type = 0
elif payment_type == 'Cash':
    payment_type = 1
elif payment_type == 'Mobile':
    payment_type == 2
elif payment_type == 'Prcard':
    payment_type = 3
elif payment_type == 'No Charge':
    payment_type = 4
elif payment_type == 'Other':
    payment_type = 5
    
if hour == '12am':
    hour = 0
elif hour == '1am':
    hour = 1
elif hour == '2am':
    hour = 2
elif hour == '3am':
    hour = 3
elif hour == '4am':
    hour = 4
elif hour == '5am':
    hour = 5
elif hour == '6am':
    hour = 6
elif hour == '7am':
    hour = 7    
elif hour == '8am':
    hour = 8
elif hour == '9am':
    hour = 9
elif hour == '10am':
    hour = 10
elif hour == '11am':
    hour = 11
elif hour == '12pm':
    hour = 12
elif hour == '1pm':
    hour = 13
elif hour == '2pm':
    hour = 14
elif hour == '3pm':
    hour = 15
elif hour == '4pm':
    hour = 16
elif hour == '5pm':
    hour = 17
elif hour == '6pm':
    hour = 18
elif hour == '7pm':
    hour = 19
elif hour == '8pm':
    hour = 20
elif hour == '9pm':
    hour = 21
elif hour == '10pm':
    hour = 22
elif hour == '11pm':
    hour = 23

if month == 'Jan':
    month = 0
if month == 'Feb':
    month = 1
if month == 'Mar':
    month = 2
if month == 'Apr':
    month = 3
if month == 'May':
    month = 4
if month == 'Jun':
    month = 5
if month == 'Jul':
    month = 6
if month == 'Aug':
    month = 7
if month == 'Sep':
    month = 8
if month == 'Oct':
    month = 9
if month == 'Nov':
    month = 10
if month == 'Dec':
    month = 11

if day == 'Mon':
    day = 0
if day == 'Tue':
    day = 1
if day == 'Wed':
    day = 2
if day == 'Thu':
    day = 3
if day == 'Fri':
    day = 4
if day == 'Sat':
    day = 5
if day == 'Sun':
    day = 6

prediction = loaded_GB.predict([[trip_seconds, trip_miles, pickup_comm, dropoff_comm,
                                 fare, tolls, extras, payment_type, month, day, hour]])
if prediction == 0:
    prediction = 'No, this model predicts the customer will not tip.'
else: 
    prediction = 'Yes, this model predicts the customer will tip'
st.write('Is this customer predicted to give a tip? {}'.format(prediction))


