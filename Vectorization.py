pip install pandas sklearn gensim

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
import numpy as np

def vectorize_tfidf(text_data):
    """Convert textual data into numerical vectors using TF-IDF."""
    vectorizer = TfidfVectorizer(max_features=500)  # You can adjust the number of features
    tfidf_matrix = vectorizer.fit_transform(text_data)
    return tfidf_matrix

def vectorize_word2vec(text_data):
    """Convert textual data into numerical vectors using Word2Vec embeddings."""
    tokenized_data = [sentence.split() for sentence in text_data]
    model = Word2Vec(sentences=tokenized_data, vector_size=100, window=5, min_count=1, workers=4)  # Adjust parameters as needed
    word_vectors = model.wv

    # Calculate sentence vectors by averaging word vectors
    sentence_vectors = []
    for tokens in tokenized_data:
        vector = np.mean([word_vectors[token] for token in tokens if token in word_vectors], axis=0)
        sentence_vectors.append(vector)
    
    return np.array(sentence_vectors)

def main():
    # Example data
    data = {
        'company': ['Company A', 'Company B'],
        'description': [
            'Company A is a leading provider of technology solutions.',
            'Company B specializes in manufacturing and industrial services.'
        ]
    }
    df = pd.DataFrame(data)
    
    # TF-IDF Vectorization
    tfidf_vectors = vectorize_tfidf(df['description'])
    print("TF-IDF Vectors:")
    print(tfidf_vectors.toarray())
    
    # Word2Vec Vectorization
    word2vec_vectors = vectorize_word2vec(df['description'])
    print("Word2Vec Vectors:")
    print(word2vec_vectors)
    
if __name__ == "__main__":
    main()
