🎬 Movie Recommender System (Hollywood + Indian Cinema)
by Harsh Prasad

A content-based Movie Recommender System built using Machine Learning that suggests similar movies across Hollywood and Indian cinema (Bollywood + regional industries). The system is deployed using Streamlit Cloud and dynamically fetches movie posters using the TMDB API.

🚀 Live Demo

🔗 https://movie-recommender-full.streamlit.app/

📌 Features
🎯 Recommends Top 5 similar movies based on user selection
🌍 Supports Hollywood + Bollywood + South Indian movies
🖼️ Dynamically fetches and displays movie posters (TMDB API)
⚡ Fast and interactive UI using Streamlit
☁️ Cloud deployed and accessible globally
📊 Handles 20,000+ movies dataset across multiple industries
🧠 How It Works

The system uses content-based filtering:

Movie metadata (genre, keywords, cast, etc.) is processed
Feature engineering is applied to convert data into vectors
Cosine similarity is computed between movie vectors
Based on selected movie, top similar movies are recommended
Posters are fetched in real-time using TMDB API
📊 Dataset

📁 Source:
🔗 https://www.kaggle.com/datasets/ishanluhani/indian-and-american-movies-1970-2023

Key Details:
🎬 20,000+ movies from American and Indian cinema
🇺🇸 Covers Hollywood movies (except 2017)
🇮🇳 Covers Hindi cinema (except 2017)
🎥 Includes Telugu, Tamil, Kannada, Marathi movies (2018–2023)
📦 Contains 14 features (with some NULL values handled during preprocessing)
🛠️ Tech Stack
Python
Pandas
Scikit-learn
Streamlit
TMDB API
Pickle
📂 Project Structure
Movie_Recommender/
│
├── main.py                # Streamlit application
├── movie_list.pkl         # Processed movie metadata
├── similarity.pkl         # Precomputed similarity matrix (external storage)
├── requirements.txt       # Dependencies
⚙️ Installation & Setup
1. Clone the repository
git clone https://github.com/HARSH2815/Movie_Recommendar_Hollywood.git
cd Movie_Recommendar_Hollywood
2. Install dependencies
pip install -r requirements.txt
3. Run the application
streamlit run main.py
☁️ Deployment
Deployed using Streamlit Community Cloud
Code hosted on GitHub
Dependencies managed via requirements.txt
Large similarity matrix (~180MB) is fetched dynamically from external storage (Google Drive)
⚠️ Notes
similarity.pkl is not included in the repository due to large size
File is downloaded at runtime for smooth deployment
NULL values in dataset are handled during preprocessing
📈 Future Improvements
⭐ Add movie ratings, overview, and reviews
🔀 Implement hybrid recommendation system (content + collaborative)
⚡ Optimize performance using caching techniques
👤 Add user personalization and login system
🌐 Multi-language filtering support
👨‍💻 Author

Harsh Prasad
🔗 https://github.com/HARSH2815

⭐ Acknowledgements
TMDB API for movie data and posters
Kaggle dataset contributors
Streamlit for easy deployment
📌 License

This project is open-source and intended for educational purposes.
