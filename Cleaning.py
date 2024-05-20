pip install pandas scikit-learn

import pandas as pd
from sklearn.preprocessing import StandardScaler

def remove_duplicates(df):
    """Remove duplicate rows from the DataFrame."""
    return df.drop_duplicates()

def handle_missing_values(df, strategy='mean'):
    """Handle missing values in the DataFrame."""
    if strategy == 'mean':
        return df.fillna(df.mean())
    elif strategy == 'median':
        return df.fillna(df.median())
    elif strategy == 'mode':
        return df.fillna(df.mode().iloc[0])
    elif strategy == 'drop':
        return df.dropna()
    else:
        raise ValueError("Strategy not recognized. Use 'mean', 'median', 'mode', or 'drop'.")

def normalize_data(df):
    """Normalize numerical features in the DataFrame."""
    scaler = StandardScaler()
    numerical_features = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_features] = scaler.fit_transform(df[numerical_features])
    return df

def clean_data(df, missing_value_strategy='mean'):
    """Clean the DataFrame by removing duplicates, handling missing values, and normalizing data."""
    df = remove_duplicates(df)
    df = handle_missing_values(df, strategy=missing_value_strategy)
    df = normalize_data(df)
    return df

if __name__ == "__main__":
    # Example usage:
    # Load a sample dataset
    data = {
        'A': [1, 2, 2, 4, None],
        'B': [5, None, 7, 8, 9],
        'C': [10, 11, 11, 13, 14],
        'D': [15, 16, 17, 17, 19]
    }
    df = pd.DataFrame(data)

    print("Original DataFrame:")
    print(df)

    cleaned_df = clean_data(df, missing_value_strategy='mean')
    print("\nCleaned DataFrame:")
    print(cleaned_df)
