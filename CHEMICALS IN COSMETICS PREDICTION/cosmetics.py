# -*- coding: utf-8 -*-
"""cosmetics.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bXe-upfdWR9GqsomeYg-B86xzoteDzbq
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    knn_classifier = KNeighborsClassifier(n_neighbors=3)
    knn_classifier.fit(X_train, y_train)
    y_pred = knn_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)
    y_pred = rf_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    xgb_classifier = XGBClassifier()
    xgb_classifier.fit(X_train, y_train)
    y_pred = xgb_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    nb_classifier = GaussianNB()
    nb_classifier.fit(X_train, y_train)
    y_pred = nb_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)
    dt_classifier = DecisionTreeClassifier()
    dt_classifier.fit(X_train, y_train)
    y_pred = dt_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy:.4f}')

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from tensorflow.keras import layers

file_path = 'chemicals-in-cosmetics--.csv'
cosmetics_data = pd.read_csv(file_path)

cosmetics_data = cosmetics_data.drop(['CDPHId', 'CSFId', 'CSF', 'CompanyId', 'ChemicalId'], axis=1)
cosmetics_data = cosmetics_data.fillna(0)

categorical_columns = ['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber', 'ChemicalName']
cosmetics_data[categorical_columns] = cosmetics_data[categorical_columns].astype(str)

le = LabelEncoder()
for column in categorical_columns:
    cosmetics_data[column] = le.fit_transform(cosmetics_data[column])

X = cosmetics_data[['ProductName', 'CompanyName', 'BrandName', 'PrimaryCategory', 'CasNumber']]
y = cosmetics_data['ChemicalCount']

# Standardize features
scaler = StandardScaler()
X_standardized = scaler.fit_transform(X)

accuracies = []
for i in range(10):
    X_train, X_test, y_train, y_test = train_test_split(X_standardized, y, test_size=0.2, random_state=i)

    # Build the ANN model
    model = keras.Sequential([
        layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
        layers.Dense(32, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)

    # Make predictions on the test set
    y_pred = (model.predict(X_test) > 0.5).astype(int).reshape(-1)

    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)
    print(f'Accuracy {i + 1}: {accuracy:.4f}')

mean_accuracy = sum(accuracies) / len(accuracies)
print(f'Mean Accuracy: {mean_accuracy:.4f}')