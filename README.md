 News Headline Category Classifier

This project is a Machine Learning-based web application that classifies news headlines into predefined categories (e.g., Legal, Climate, Sustainability) using Natural Language Processing (NLP) techniques. It was developed as a final Big Data course project to demonstrate data mining, model building, and deployment on real-world unstructured data.

Why This Project?

In today's digital age, news is generated at an overwhelming speed. Categorizing news content manually is inefficient and error-prone — especially across massive platforms like Reuters or The Guardian. This project tackles that issue using Big Data and Machine Learning to automatically classify headlines based on their textual content.

Unlike most academic projects that focus on reviews, products, or finance, this one:
- Uses **real, recent news data** from Reuters
- Tackles a **socially relevant domain** (legal, climate, corruption, etc.)
- Deals with **unstructured text**, reflecting real-world data mining challenges

This makes it both a technically rich and ethically meaningful application of Big Data principles.



How It Works

1. Data Collection: News headlines were scraped from Reuters, each labeled with a `News_Type`.
2. Preprocessing: Headlines were cleaned (lowercased, stripped of noise), then vectorized using TF-IDF.
3. Modeling: A Multinomial Naive Bayes classifier was trained to learn patterns between headline text and their categories.
4. Deployment: The final model was deployed as an interactive web app using Streamlit.



Tech Stack

- Python 3
- Scikit-learn – TF-IDF, Naive Bayes, Evaluation
- Pandas, NumPy – Data processing
- Streamlit – App deployment
- Joblib– Model serialization

Key Features
Clean, modern web interface

Realtime prediction based on user input

Trained on real headlines with meaningful classes

Lightweight and fast with a small model footprint