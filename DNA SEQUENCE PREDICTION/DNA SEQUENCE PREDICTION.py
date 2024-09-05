# -*- coding: utf-8 -*-
""".ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GfRiqTz11j7RLXZZ1C-PaAqV2QPYwnx3
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score

def read_dna_sequence(file_path, label):
    with open(file_path, 'r') as file:
        sequences = file.readlines()
    df = pd.DataFrame({'sequence': sequences, 'label': label})
    return df

def train_and_evaluate_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    gb_classifier = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb_classifier.fit(X_train, y_train)
    predictions = gb_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Load data
human_df = read_dna_sequence('human.txt', 'human')
chimpanzee_df = read_dna_sequence('chimpanzee.txt', 'chimpanzee')
dog_df = read_dna_sequence('dog.txt', 'dog')
all_data = pd.concat([human_df, chimpanzee_df, dog_df], ignore_index=True)
all_data['sequence_length'] = all_data['sequence'].apply(len)

# Extract features and labels
X = all_data[['sequence_length']]
y = all_data['label']

# Print 10 accuracies
for i in range(10):
    accuracy = train_and_evaluate_model(X, y)
    print(f" {accuracy * 100 : .2f}")

import pandas as pdDD
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def read_dna_sequence(file_path, label):
    with open(file_path, 'r') as file:
        sequences = file.readlines()
    df = pd.DataFrame({'sequence': sequences, 'label': label})
    return df

def train_and_evaluate_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    xgb_classifier = XGBClassifier(n_estimators=100, random_state=42)
    xgb_classifier.fit(X_train, y_train)
    predictions = xgb_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Load data
human_df = read_dna_sequence('human.txt', 'human')
chimpanzee_df = read_dna_sequence('chimpanzee.txt', 'chimpanzee')
dog_df = read_dna_sequence('dog.txt', 'dog')
all_data = pd.concat([human_df, chimpanzee_df, dog_df], ignore_index=True)

# Use LabelEncoder to convert string labels to integers
label_encoder = LabelEncoder()
all_data['label'] = label_encoder.fit_transform(all_data['label'])

all_data['sequence_length'] = all_data['sequence'].apply(len)

# Extract features and labels
X = all_data[['sequence_length']]
y = all_data['label']

# Print 10 accuracies
for i in range(10):
    accuracy = train_and_evaluate_model(X, y)
    print(f"Accuracy {i + 1}: {accuracy * 100 : .2f}")

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

def read_dna_sequence(file_path, label):
    with open(file_path, 'r') as file:
        sequences = file.readlines()
    df = pd.DataFrame({'sequence': sequences, 'label': label})
    return df

def train_and_evaluate_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )
    mlp_classifier = MLPClassifier(hidden_layer_sizes=(100,), max_iter=1000, random_state=42)
    mlp_classifier.fit(X_train, y_train)
    predictions = mlp_classifier.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy

# Load data
human_df = read_dna_sequence('human.txt', 'human')
chimpanzee_df = read_dna_sequence('chimpanzee.txt', 'chimpanzee')
dog_df = read_dna_sequence('dog.txt', 'dog')
all_data = pd.concat([human_df, chimpanzee_df, dog_df], ignore_index=True)

# Use LabelEncoder to convert string labels to integers
label_encoder = LabelEncoder()
all_data['label'] = label_encoder.fit_transform(all_data['label'])

all_data['sequence_length'] = all_data['sequence'].apply(len)

# Extract features and labels
X = all_data[['sequence_length']]
y = all_data['label']

# Print 10 accuracies
for i in range(10):
    accuracy = train_and_evaluate_model(X, y)
    print(f"Accuracy {i + 1}: {accuracy * 100 : .2f}")

!pip install biopython

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder
import numpy as np

# Function to pad or truncate sequences
def pad_or_truncate_sequence(sequence, max_length):
    if len(sequence) < max_length:
        return sequence + 'N' * (max_length - len(sequence))
    else:
        return sequence[:max_length]

# Read the data
human_data = pd.read_csv('human.txt', delimiter='\t')
chimpanzee_data = pd.read_csv('chimpanzee.txt', delimiter='\t')
dog_data = pd.read_csv('dog.txt', delimiter='\t')

# Combine the data
all_data = pd.concat([human_data, chimpanzee_data, dog_data], ignore_index=True)

# Set a maximum sequence length (adjust as needed)
max_sequence_length = 500

# One-hot encode DNA sequences
encoder = OneHotEncoder(sparse=False, dtype=int)
X_encoded = np.array(encoder.fit_transform(all_data['sequence'].apply(lambda x: list(pad_or_truncate_sequence(x, max_sequence_length))).tolist()))

# Separate features (X) and labels (y)
X = X_encoded
y = all_data['class']

# Perform 10 runs and print accuracies
for i in range(10):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=i)

    # Train a Random Forest classifier
    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=i)
    rf_classifier.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = rf_classifier.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f' {accuracy * 100:.2f}')

def print_head(file_path, num_lines=5):
    with open(file_path, 'r') as file:
        lines = [next(file) for _ in range(num_lines)]
    print(f"--- Head of {file_path} ---")
    print("".join(lines))

# Print the head of each file
print_head('human.txt')
print_head('chimpanzee.txt')
print_head('dog.txt')