# -*- coding: utf-8 -*-
"""silver.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pU8yfyWJwPFLxXQUp_8KHf_vEC1eaikS
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

data = pd.read_csv('LBMA-SILVER.csv', parse_dates=['Date'], dayfirst=True)
threshold = data['USD'].mean()
data['Price_Category'] = np.where(data['USD'] > threshold, 'High', 'Low')
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

X = data[['Day', 'Month', 'Year']]
y = data['Price_Category']

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    svm_model = SVC(kernel='linear')
    svm_model.fit(X_train, y_train)
    y_pred = svm_model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy {i+1}: {accuracy:.4f}')

# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('LBMA-SILVER.csv', parse_dates=['Date'], dayfirst=True)

# Calculate the mean of the silver prices
threshold = data['USD'].mean()

# Create a new column 'Price_Category' based on the threshold
data['Price_Category'] = np.where(data['USD'] > threshold, 'High', 'Low')

# Feature engineering: Extracting day, month, and year from the 'Date' column
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

# Split the data into features (X) and target variable (y)
X = data[['Day', 'Month', 'Year']]
y = data['Price_Category']

# Repeat the process 10 times and print accuracies for KNN
for i in range(20):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)

    # Initialize the KNN model (you can adjust the number of neighbors, here set to 5)
    knn_model = KNeighborsClassifier(n_neighbors=5)

    # Train the model
    knn_model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = knn_model.predict(X_test)

    # Evaluate the model and print accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy {i+1}: {accuracy:.4f}')

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv('LBMA-SILVER.csv', parse_dates=['Date'], dayfirst=True)
threshold = data['USD'].mean()
data['Price_Category'] = np.where(data['USD'] > threshold, 1, 0)
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

X = data[['Day', 'Month', 'Year']]
y = data['Price_Category']

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = Sequential()
    model.add(Dense(units=64, activation='relu', input_dim=X_train.shape[1]))
    model.add(Dense(units=1, activation='sigmoid'))

    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train_scaled, y_train, epochs=10, batch_size=32, verbose=0)

    y_pred_prob = model.predict(X_test_scaled)
    y_pred = [1 if prob > 0.5 else 0 for prob in y_pred_prob]

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy {i+1}: {accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv('LBMA-SILVER.csv', parse_dates=['Date'], dayfirst=True)
threshold = data['USD'].mean()
data['Price_Category'] = (data['USD'] > threshold).astype(int)
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

X = data[['Day', 'Month', 'Year']]
y = data['Price_Category']

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)

    y_pred_prob = linear_model.predict(X_test)
    threshold = 0.5
    y_pred = (y_pred_prob > threshold).astype(int)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy {i+1}: {accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

data = pd.read_csv('LBMA-SILVER.csv', parse_dates=['Date'], dayfirst=True)
threshold = data['USD'].mean()
data['Price_Category'] = (data['USD'] > threshold).astype(int)
data['Day'] = data['Date'].dt.day
data['Month'] = data['Date'].dt.month
data['Year'] = data['Date'].dt.year

X = data[['Day', 'Month', 'Year']]
y = data['Price_Category']

for i in range(20):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    decision_tree_model = DecisionTreeClassifier(random_state=42)
    decision_tree_model.fit(X_train, y_train)

    y_pred = decision_tree_model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy {i+1}: {accuracy:.4f}')