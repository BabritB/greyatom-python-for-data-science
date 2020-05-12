# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
bank=pd.DataFrame(bank_data)
#print(bank.info())
categorical_var=bank.select_dtypes(include='object')
#print(categorical_var.shape)
numerical_var=bank.select_dtypes(include='number')
#print(numerical_var.shape)
bank.drop('Loan_ID',axis=1,inplace=True)
banks=bank.copy()
#print(banks.isnull().columns)
for col in banks.isnull().columns:
    #print(type(banks[col].mode()[0]))
    banks[col].fillna(banks[col].mode()[0],inplace=True)
# bank_mode=banks.mode()
# print(type(bank_mode))
# banks.fillna(bank_mode.values,inplace=True)
print(banks.isnull().sum().values.sum())
avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc='mean')
print(avg_loan_amount['LoanAmount'][1])

loan_approved_se=banks[banks['Self_Employed']=='Yes']+banks[banks['Loan_Status']=='Y']

loan_approved_nse=banks[banks['Self_Employed']=='No']+banks[banks['Loan_Status']=='Y']

print(loan_approved_se.shape[0])
print(banks.shape[0])
print(loan_approved_nse.shape[0])

percentage_se=((loan_approved_se.shape[0]/banks.shape[0])*100)
percentage_nse=((loan_approved_nse.shape[0]/banks.shape[0])*100)

loan_term=banks['Loan_Amount_Term'].apply(lambda x:x//12)
#print(type(loan_term))
tenure=[i for i in loan_term if i>=25.0]
#print(len(tenure))

big_loan_term=len(tenure)
#print(big_loan_term['Loan_Amount_Term'])

loan_groupby=banks.groupby('Loan_Status')[['ApplicantIncome', 'Credit_History']]
print(loan_groupby.head())
#loan_groupby=loan_groupby[:,['ApplicantIncome', 'Credit_History']]
mean_values=loan_groupby.mean()

print(mean_values.iloc[1,0])




