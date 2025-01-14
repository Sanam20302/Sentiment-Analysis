import streamlit as st
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from io import StringIO

# Function to analyze sentiment using VADER
def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(text)
    if scores['compound'] >= 0.05:
        return 'positive'
    elif scores['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# Streamlit app
def main():
    st.title("Sentiment Analysis with VADER")

    uploaded_file = st.file_uploader("Upload a CSV file", type=['csv'])
    
    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        
        # Check if the CSV file contains the necessary column
        if 'text' not in data.columns:
            st.error('CSV file must contain a "text" column')
        else:
            # Analyze sentiment for each text
            data['sentiment'] = data['text'].apply(analyze_sentiment_vader)
            
            # Display the resulting dataframe
            st.write(data)
            
            # Convert dataframe to CSV
            output = StringIO()
            data.to_csv(output, index=False)
            processed_data = output.getvalue()
            
            # Provide download link for the new CSV file
            st.download_button(
                label='Download CSV with Sentiments',
                data=processed_data,
                file_name='text_with_sentiments.csv',
                mime='text/csv'
            )

if __name__ == '__main__':
    # Download VADER for the first run
    import nltk
    nltk.download('vader_lexicon')
    main()
