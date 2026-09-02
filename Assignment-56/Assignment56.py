import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import BaggingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, f1_score ,recall_score
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, VotingClassifier

border = "-" * 35
print(border)

def load_data():
    print("Load the dataset")
    df = pd.read_csv("Fraudulent_Transaction_Detection.csv") 
    print("First few records in dataset : ")
    print(df.head(6))
    return df

def preprocessing(df):
    x = df.drop("Fraud", axis=1)
    y = df["Fraud"]

    print("X shape", x.shape)
    print("Y shape", y.shape)

    # Split dataset for training and testing
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=42)

    # Scale the features
    scalar = StandardScaler()
    x_train = scalar.fit_transform(x_train)
    x_test = scalar.transform(x_test) # Use transform here
    
    return x_train, x_test, y_train, y_test

def decisiontree(x_train, x_test, y_train, y_test):
    print(border)
    print("Task 1 - build decisionTree classifier ")
    base_model = DecisionTreeClassifier(random_state=42)
    base_model.fit(x_train, y_train)
    y_pred = base_model.predict(x_test)
    
    print("Accuracy is : ", accuracy_score(y_test, y_pred) * 100)
    print("precision score  : ", precision_score(y_test, y_pred, zero_division=0)*100)
    print("F1 score  : ", f1_score(y_test, y_pred, zero_division=0)*100)
    print("Recall score     : ", recall_score(y_test, y_pred, zero_division=0)*100)
    print("confusion matrix :")
    print(confusion_matrix(y_test, y_pred))
    return base_model

def bagging(x_train, x_test, y_train, y_test, base_model):
    print(border)
    print("Task 2 - build BaggingTree classifier ")
    model_bag = BaggingClassifier(estimator=base_model, n_estimators=10, random_state=42)
    model_bag.fit(x_train, y_train)
    y_pred = model_bag.predict(x_test)

    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    print("confusion matrix :")
    print(confusion_matrix(y_test, y_pred))
    print("precision score  : ", precision_score(y_test, y_pred, zero_division=0)*100)
    print("F1 score  : ", f1_score(y_test, y_pred, zero_division=0)*100)
    print("Recall score     : ", recall_score(y_test, y_pred, zero_division=0)*100)
    return model_bag

def randmforest(x_train, x_test, y_train, y_test):
    print(border)
    print("Task 3 - Build Randomforest classifier ")
    model_randomForst = RandomForestClassifier(n_estimators=10, random_state=42)
    model_randomForst.fit(x_train, y_train)
    y_pred = model_randomForst.predict(x_test)

    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    print("precision score  : ", precision_score(y_test, y_pred, zero_division=0)*100)
    print("F1 score  : ", f1_score(y_test, y_pred, zero_division=0)*100)
    print("Recall score     : ", recall_score(y_test, y_pred, zero_division=0)*100)
    print("confusion matrix :")
    print(confusion_matrix(y_test, y_pred))
    return model_randomForst

def boosting(x_train, x_test, y_train, y_test):
    print(border)
    print("Task 4 - build AdaBoost classifier ")
    model_boost = AdaBoostClassifier(n_estimators=50, learning_rate=0.1, random_state=42)
    model_boost.fit(x_train, y_train)
    y_pred = model_boost.predict(x_test) # Fixed prediction model

    print("Accuracy : ", accuracy_score(y_test, y_pred) * 100)
    print("precision score  : ", precision_score(y_test, y_pred, zero_division=0)*100)
    print("F1 score  : ", f1_score(y_test, y_pred, zero_division=0)*100)
    print("Recall score     : ", recall_score(y_test, y_pred, zero_division=0)*100)
    print("confusion matrix :")
    print(confusion_matrix(y_test, y_pred))
    return model_boost

def votingclassifier(x_train, x_test, y_train, y_test, b_model, bag_model, r_model, boost_model):
    print(border)
    print("Task 5 - build Voting classifier ")
    model_v = VotingClassifier(
        estimators=[('decision_tree', b_model), ('bagging', bag_model), ('random_forest', r_model), ('Boosting', boost_model)], 
        
    )
    model_v.fit(x_train, y_train)
    y_pred = model_v.predict(x_test)
    print("Accuracy voting classifier is : ", accuracy_score(y_test, y_pred) * 100)
    print("precision score  : ", precision_score(y_test, y_pred, zero_division=0)*100)
    print("F1 score  : ", f1_score(y_test, y_pred, zero_division=0)*100)
    print("Recall score     : ", recall_score(y_test, y_pred, zero_division=0)*100)
    print("confusion matrix :")
    print(confusion_matrix(y_test, y_pred))

def main():
    df = load_data()
    x_train, x_test, y_train, y_test = preprocessing(df) # Fixed unpacking
    
    # Passing models sequentially through returns
    b_model = decisiontree(x_train, x_test, y_train, y_test)
    bag_model = bagging(x_train, x_test, y_train, y_test, b_model)
    r_model = randmforest(x_train, x_test, y_train, y_test)
    boost_model = boosting(x_train, x_test, y_train, y_test)
    
    votingclassifier(x_train, x_test, y_train, y_test, b_model, bag_model, r_model, boost_model)

if __name__ == "__main__":
    main()


''' 
OUTPUT: 

===========================================================================
                    FINAL ACCURACY COMPARISON       
===========================================================================
   Model Name                 Accuracy(%)     precision   Recall       F1
---------------------------------------------------------------------------
 
Decision Tree                   97.80           100        91.30      95.45

Bagging Tree classifier         93.40           100        73.91      85.0

RandomForest classifier         95.45           100        91.30      95.45

AdaBoost Classifier             97.80           100        91.30      95.45

Hard Voting Classifier          95.60           100        82.60      90.47
-----------------------------------------------------------------------------

'''