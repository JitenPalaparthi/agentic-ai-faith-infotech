"""12 — Simple text features and TF-IDF."""
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

df = pd.read_csv("data/customers.csv")

df["review_char_count"] = df["review_text"].str.len()
df["review_word_count"] = df["review_text"].str.split().str.len()

print("Simple features:")
print(df[["review_text", "review_char_count", "review_word_count"]])

tfidf = TfidfVectorizer(max_features=10)
X = tfidf.fit_transform(df["review_text"])

print("\nTF-IDF feature names:")
print(tfidf.get_feature_names_out())
print("\nTF-IDF shape:", X.shape)
print(X.toarray())
