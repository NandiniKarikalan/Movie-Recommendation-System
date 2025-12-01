# Movie-Recommendation-System
A Python-based interactive movie explorer that recommends similar titles or lists movies by their release year. Built with TF-IDF and cosine similarity. This content-based system allows users to search either by a specific movie name or filter results by year.

**🔧 Features**
- 🔎 Recommends similar movies based on title (using TF-IDF)
- 📅 Lists movies released in a given year (up to 50 max)
- 🛠 Robust preprocessing and error handling for messy data
- 📦 Lightweight and memory-efficient setup
- 🤖 Fully command-line based interaction (easy to upgrade to GUI or web later)

**🧠 How It Works**
1. Loads a movie dataset with IDs, titles, and release years.
2. Cleans the data and assigns headers (for headerless CSV).
3. Uses TF-IDF vectorization on titles to generate feature vectors.
4. Computes cosine similarity to find movies with similar title vectors.
5. Accepts user input to operate in either "title" mode or "year" mode.

**🚀 Set-Up**
1. Install dependencies:
    
    bash
    
    - pip install pandas scikit-learn # To install Python libraries
    - python main.py # To run the main file
2. Dataset:
    
    Kaggle: https://www.kaggle.com/datasets/ksavleen/movie-recommendation-dataset?select=movie_titles.csv
    

**🧰 Technologies Used**
- Programming Language: Python 3.x
- Data Processing: pandas
- Machine Learning: scikit-learn (TF-IDF + cosine similarity)
- CLI Interaction: input() + print() for command-line interactivity
- File Handling: CSV (Comma-Separated Values)
- Text Similarity: TF-IDF vectorization + cosine similarity
- Memory Management: Sampling with .head() to optimize performance
- Error Handling: Try-except blocks for safe user inputs and lookups
- Dataset Format: Headerless CSV with columns: id, release year, name
- Editor: Visual Studio Code

**🧪 Sample Output**
🎬 Welcome to the Movie Recommendation System!

➡️ Type 'movie title' to find similar movies

➡️ Type 'year of launch' to list movies by year

Your choice: movie title

🔎 Enter a movie title: Titanic

🎥 Recommendations for 'Titanic':

1. Titanic II
2. Poseidon
3. The Perfect Storm
4. Ghost Ship
5. The Abyss

**🧑‍💻 Author**
Created by Nandini Karikalan on 13.07.2025.
