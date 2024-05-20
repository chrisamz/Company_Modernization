pip install pandas scikit-learn tensorflow

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

def load_data():
    # Example data
    data = {
        'company': ['Company A', 'Company B', 'Company C', 'Company D'],
        'vectorized_features': [
            [0.1, 0.2, 0.3, 0.4],
            [0.2, 0.1, 0.4, 0.3],
            [0.3, 0.3, 0.1, 0.1],
            [0.4, 0.2, 0.2, 0.2]
        ],
        'label': [0, 1, 0, 1]  # 0: slow to adapt, 1: quick to adapt
    }
    df = pd.DataFrame(data)
    return df

def preprocess_data(df):
    X = df['vectorized_features'].tolist()
    y = df['label'].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_random_forest(X_train, y_train):
    rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)
    return rf_model

def train_svm(X_train, y_train):
    svm_model = SVC(kernel='linear', probability=True, random_state=42)
    svm_model.fit(X_train, y_train)
    return svm_model

def train_neural_network(X_train, y_train):
    model = Sequential()
    model.add(Dense(64, input_dim=len(X_train[0]), activation='relu'))
    model.add(Dense(32, activation='relu'))
    model.add(Dense(2, activation='softmax'))  # Assuming binary classification
    
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    
    y_train_cat = to_categorical(y_train)
    model.fit(X_train, y_train_cat, epochs=50, batch_size=5, verbose=1)
    
    return model

def evaluate_model(model, X_test, y_test, is_neural_net=False):
    if is_neural_net:
        y_test_cat = to_categorical(y_test)
        loss, accuracy = model.evaluate(X_test, y_test_cat, verbose=0)
        print(f"Neural Network Accuracy: {accuracy}")
    else:
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        print(f"Model Accuracy: {accuracy}")
        print("Classification Report:")
        print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    df = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(df)
    
    # Train Random Forest
    rf_model = train_random_forest(X_train, y_train)
    print("Random Forest Model:")
    evaluate_model(rf_model, X_test, y_test)
    
    # Train SVM
    svm_model = train_svm(X_train, y_train)
    print("SVM Model:")
    evaluate_model(svm_model, X_test, y_test)
    
    # Train Neural Network
    nn_model = train_neural_network(X_train, y_train)
    print("Neural Network Model:")
    evaluate_model(nn_model, X_test, y_test, is_neural_net=True)
