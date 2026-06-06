import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Load dataset (since you put dataset.csv next to manage.py)
movies = pd.read_csv("dataset.csv")

# ✅ Create 'tags' column by combining genre + overview
movies['tags'] = movies['genre'].fillna('') + " " + movies['overview'].fillna('')

# ✅ Keep only required columns
new = movies[['id', 'title', 'tags']]

# ✅ Vectorize tags
cv = CountVectorizer(max_features=10000, stop_words='english')
vec = cv.fit_transform(new['tags'].values.astype('U')).toarray()

# ✅ Cosine similarity matrix
sim = cosine_similarity(vec)

# ✅ Recommendation function
def recommend(movie_title):
    try:
        index = new[new['title'] == movie_title].index[0]
    except IndexError:
        return ["Movie not found in dataset"]

    distances = sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])
    results = []
    for i in distances[0:10]:
        results.append(new.iloc[i[0]].title)
    return results

def search_movies(query):
    # Case-insensitive substring match
    matches = new[new['title'].str.contains(query, case=False, na=False)]
    return matches['title'].tolist()

