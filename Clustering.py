pip install pandas scikit-learn

import pandas as pd
from sklearn.cluster import KMeans, DBSCAN
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    # Example data
    data = {
        'company': ['Company A', 'Company B', 'Company C', 'Company D', 'Company E'],
        'vectorized_features': [
            [0.1, 0.2, 0.3, 0.4],
            [0.2, 0.1, 0.4, 0.3],
            [0.3, 0.3, 0.1, 0.1],
            [0.4, 0.2, 0.2, 0.2],
            [0.3, 0.4, 0.3, 0.5]
        ]
    }
    df = pd.DataFrame(data)
    return df

def preprocess_data(df):
    X = df['vectorized_features'].tolist()
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

def kmeans_clustering(X, n_clusters=2):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans_labels = kmeans.fit_predict(X)
    return kmeans_labels

def dbscan_clustering(X, eps=0.5, min_samples=2):
    dbscan = DBSCAN(eps=eps, min_samples=min_samples)
    dbscan_labels = dbscan.fit_predict(X)
    return dbscan_labels

def plot_clusters(X, labels, title):
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette='Set1')
    plt.title(title)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.show()

if __name__ == "__main__":
    df = load_data()
    X_scaled = preprocess_data(df)
    
    # K-means Clustering
    kmeans_labels = kmeans_clustering(X_scaled, n_clusters=2)
    print("K-means Clustering Labels:", kmeans_labels)
    plot_clusters(X_scaled, kmeans_labels, title="K-means Clustering")
    
    # DBSCAN Clustering
    dbscan_labels = dbscan_clustering(X_scaled, eps=0.5, min_samples=2)
    print("DBSCAN Clustering Labels:", dbscan_labels)
    plot_clusters(X_scaled, dbscan_labels, title="DBSCAN Clustering")
