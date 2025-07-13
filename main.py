import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ✅ Load CSV with manual headers
column_names = ['id', 'release year', 'name']
df = pd.read_csv('movie_titles.csv', encoding='latin1', on_bad_lines='skip', low_memory=False, header=None, names=column_names)

# ✅ Clean column headers (just in case)
df.columns = df.columns.str.strip()

# ✅ Clean data
df = df.dropna(subset=['name'])
df = df.drop_duplicates(subset='name')
df = df.reset_index(drop=True)

# 💡 Optional: Limit dataset size to avoid memory errors
df = df.head(5000)

# ✅ TF-IDF on movie titles
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['name'])

# ✅ Recommend similar movies
def recommend_by_title(title):
    try:
        idx = df[df['name'].str.lower() == title.lower()].index[0]
    except IndexError:
        return ["❌ Movie not found. Please check spelling or try another title."]

    tfidf_vector = tfidf.transform([df['name'].iloc[idx]])
    sim_scores = cosine_similarity(tfidf_vector, tfidf_matrix).flatten()
    top_indices = sim_scores.argsort()[-6:-1][::-1]
    return df['name'].iloc[top_indices].tolist()

# ✅ List movies by year (limit to 50)
def list_by_year(year):
    try:
        year = int(year)
    except ValueError:
        return ["⚠️ Invalid year. Please enter a number."]

    matches = df[df['release year'] == year]['name'].dropna().unique().tolist()
    return matches[:50] if matches else [f"❌ No movies found from {year}."]

# 🧠 Main user interaction
print("\n🎬 Welcome to the Movie Recommendation System!")
choice = input("What would you like to explore?\n➡️ Type 'movie title' to find similar movies\n➡️ Type 'year of launch' to list movies by year\nYour choice: ").strip().lower()

if choice == 'movie title':
    user_title = input("🔎 Enter a movie title: ").strip()
    recommendations = recommend_by_title(user_title)
    print(f"\n🎥 Recommendations for '{user_title}':")
    for i, title in enumerate(recommendations, 1):
        print(f"{i}. {title}")

elif choice == 'year of launch':
    user_year = input("📅 Enter the year: ").strip()
    movies = list_by_year(user_year)
    print(f"\n📽️ Movies released in {user_year} (up to 50):")
    for i, title in enumerate(movies, 1):
        print(f"{i}. {title}")

else:
    print("❌ Invalid input. Please type either 'movie title' or 'year of launch'.")