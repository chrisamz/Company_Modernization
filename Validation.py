pip install pandas scikit-learn

import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    # Example test data and true labels
    data = {
        'company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
        'true_labels': [0, 1, 0, 1, 0],
        'predicted_labels': [0, 1, 0, 0, 0]
    }
    df = pd.DataFrame(data)
    return df

def validate_model(true_labels, predicted_labels):
    accuracy = accuracy_score(true_labels, predicted_labels)
    precision = precision_score(true_labels, predicted_labels)
    recall = recall_score(true_labels, predicted_labels)
    f1 = f1_score(true_labels, predicted_labels)
    
    print(f"Accuracy: {accuracy:.2f}")
    print(f"Precision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")
    print(f"F1 Score: {f1:.2f}")

    return accuracy, precision, recall, f1

def plot_confusion_matrix(true_labels, predicted_labels):
    cm = confusion_matrix(true_labels, predicted_labels)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
    plt.xlabel('Predicted')
    plt.ylabel('True')
    plt.title('Confusion Matrix')
    plt.show()

if __name__ == "__main__":
    df = load_data()
    true_labels = df['true_labels']
    predicted_labels = df['predicted_labels']
    
    accuracy, precision, recall, f1 = validate_model(true_labels, predicted_labels)
    plot_confusion_matrix(true_labels, predicted_labels)
