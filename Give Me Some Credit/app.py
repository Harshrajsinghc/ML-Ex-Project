import streamlit as st
import pandas as pd 
import numpy as np 
import pickle


pickle_in = open("model2.pkl","rb")
model2 = pickle.load(pickle_in)

def variables(RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30to59DaysPastDueNotWorse,DebtRatio,MonthlyIncome,NumberOfOpenCreditLinesAndLoans,NumberOfTimes90DaysLate,NumberRealEstateLoansOrLines,NumberOfTime60to89DaysPastDueNotWorse,NumberOfDependents ):
    inputs = [RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30to59DaysPastDueNotWorse,DebtRatio,MonthlyIncome,NumberOfOpenCreditLinesAndLoans,NumberOfTimes90DaysLate,NumberRealEstateLoansOrLines,NumberOfTime60to89DaysPastDueNotWorse,NumberOfDependents]
    inputs = [float(x) if x != '' else 0.0 for x in inputs]
    prediction = model2.predict_proba([inputs])
    return prediction



def main():
    st.title("Financial distress")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center">Stream Financial Distress </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    RevolvingUtilizationOfUnsecuredLines = st.text_input("Revolving Utilization Of Unsecured Lines")
    age = st.text_input("Age")
    NumberOfTime30to59DaysPastDueNotWorse= st.text_input("Number Of Time 30 to 59 Days Past Due Not Worse")
    DebtRatio = st.text_input("Debit Ratio")
    MonthlyIncome = st.text_input("Monthly Income")
    NumberOfOpenCreditLinesAndLoans = st.text_input("Number Of Open Credit Lines And Loans")
    NumberOfTimes90DaysLate = st.text_input("Number Of Times 90 Days Late")
    NumberRealEstateLoansOrLines = st.text_input("Number Real Estate Loans")
    NumberOfTime60to89DaysPastDueNotWorse = st.text_input("Number Of Time 60 to 89 Days Past Due Not Worse")
    NumberOfDependents = st.text_input("Number Of Dependents")
    result = ""
    if st.button("Predict"):
        result = variables(RevolvingUtilizationOfUnsecuredLines,age,NumberOfTime30to59DaysPastDueNotWorse,DebtRatio,MonthlyIncome,NumberOfOpenCreditLinesAndLoans,NumberOfTimes90DaysLate,NumberRealEstateLoansOrLines,NumberOfTime60to89DaysPastDueNotWorse,NumberOfDependents )
        st.success('The probability is {} '.format(result))

if __name__ =='__main__':
    main()