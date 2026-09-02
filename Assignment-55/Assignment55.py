# Customer loan approval using voring classification 
###############################################
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import VotingClassifier


border  = "-"*30
print(border)
print("Building voting classifier")
print(border)

def load_dataset():
# Task 1 : Load the dataset 
    print("Step 1 : Load the dataset")
    df = pd.read_csv("Customer_Loan_Approval.csv") 
    print("Dataset Loaded successfully ")
    print(df.head())
    print(border)
    return df

def checkmissing(df):
# Task 2 : check misisng values  
    print(border)
    print("Step 2 : Check Missing values")
    print(border)
    print("Total missing values : ")
    print(border)
    print(df.isnull().sum())
    print(border)
    return df

def input_output(df):
# Task 3 : Seperate independent and dependent variables

    print(border)
    print("step 3 : Seperate independent and dependent variables")
    print(border) 

    X = df[["Age","Income","CreditScore","ExistingLoan","EmploymentExperience","LoanAmount"]]

    Y = df["LoanApproved"]

    print("Input/Independent variables : ")
    print(X.head())

    print("Output/dependent variables : ")
    print(Y.head())
    return X,Y

def splitting(X,Y):
# Task 4 : Split th dataset 
    print(border)
    print("step 4 : Split the dataset ")
    print(border) 

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size =0.2,random_state = 42)
    print("Training data : ",X_train.shape)
    print("Testing data : ",X_test.shape)
    scalar = StandardScaler()
    X_train_scaled = scalar.fit_transform(X_train)
    X_test_scaled = scalar.transform(X_test)
    return X_train_scaled, X_test_scaled, Y_train, Y_test

def logistic(X_test,X_train,Y_test,Y_train):
# Task 5 : Train logistic regression 
    scalar = StandardScaler()
    X_train = scalar.fit_transform(X_train)
    X_test = scalar.fit_transform(X_test)


    print(border)
    print("step 5 : Train logistic regression ")
    model_log= LogisticRegression(max_iter=1000)
    model_log= model_log.fit(X_train,Y_train)
    Y_pred= model_log.predict(X_test)
    print("Accuracy of logistic regression is : ",accuracy_score(Y_test,Y_pred)*100)
    return model_log

def decisiontree(X_test,X_train,Y_test,Y_train):
# Task 6 : Train decision Tree 
    print(border)
    print("step 6 : Train DecisionTree classfier  ")
    model_det= DecisionTreeClassifier()
    model_det= model_det.fit(X_train,Y_train)
    Y_pred= model_det.predict(X_test)
    print("Accuracy of decision tree classifier is : ",accuracy_score(Y_test,Y_pred)* 100)
    return model_det

def KNN(X_test,X_train,Y_test,Y_train):
# Task 7 : Train Knn classifier
    print(border)
    print("step 7 : Train knn classifier")
    model_knn = KNeighborsClassifier(n_neighbors=5)
    model_knn = model_knn.fit(X_train, Y_train)
    Y_pred= model_knn.predict(X_test)
    print("Accuracy of knn classifier is : ", accuracy_score(Y_test, Y_pred) * 100)
    return model_knn

def hardvoting_classifier(X_test,X_train,Y_test,Y_train,m_log,m_det,m_knn):
# Task 9 : Create a Had voting classifier 
    print(border)
    print("step 9 : Create a Hard voting classifier")
    model = VotingClassifier(estimators=[('logistic',m_log),('decision_tree',m_det),('knn',m_knn)],voting = 'hard')
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    print("Accuracy Hard voting classifier is : ",accuracy_score(Y_test,Y_pred)*100)
    

def softvoting_classifier(X_test,X_train,Y_test,Y_train,m_log,m_det,m_knn):

# Task 10 : Create a soft voting classifier 
    print(border)
    print("step 10 : Create a soft voting classifier ")
    model = VotingClassifier(estimators=[('logistic',m_log),('decision_tree',m_det),('knn',m_knn)],voting = 'hard')
    model = model.fit(X_train,Y_train)
    Y_pred = model.predict(X_test)
    print("Accuracy soft voting classifier is : ",accuracy_score(Y_test,Y_pred)*100)
    

def main():
    print("")
    df = load_dataset()
    checkmissing(df)
    X, Y = input_output(df)
    X_train, X_test, Y_train, Y_test = splitting(X, Y)
    
    # 2. FIXED: Changed variable names so they do NOT match function names
    model_log = logistic(X_train, X_test, Y_train, Y_test)
    model_det = decisiontree(X_train, X_test, Y_train, Y_test)
    model_knn = KNN(X_train, X_test, Y_train, Y_test)
    
    # 3. Pass distinct model objects into ensemble classifiers
    hardvoting_classifier(X_train, X_test, Y_train, Y_test, model_log, model_det, model_knn)
    softvoting_classifier(X_train, X_test, Y_train, Y_test, model_log, model_det, model_knn)
    
    print(border)
    print("End of the code")
    print(border)
    

if __name__ == "__main__":
    main()


'''
OUTPUT: 

========================================
       FINAL ACCURACY COMPARISON       
========================================
   Model Name                 Accuracy (%)
Logistic Regression             72.5%
Decision Tree                   90.00%
K-Nearest Neighbors (KNN)       82.5%
Soft Voting Classifier          87.5%
Hard Voting Classifier          87.5%
========================================

'''