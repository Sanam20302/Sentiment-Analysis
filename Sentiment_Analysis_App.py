pip.install textblob
import streamlit as st
import pandas as pd
from textblob import TextBlob
from io import StringIO

# Function to analyze sentiment
def analyze_sentiment(quote):
    analysis = TextBlob(quote)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'

# Streamlit app
def main():
    st.title('Sentiment Analysis of Quotes')
    
    uploaded_file = st.file_uploader('Upload a CSV file', type=['csv'])
    
    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
        
        # Check if the CSV file contains the necessary column
        if 'quote' not in data.columns:
            st.error('CSV file must contain a "quote" column')
        else:
            # Analyze sentiment for each quote
            data['sentiment'] = data['quote'].apply(analyze_sentiment)
            
            # Display the resulting dataframe
            st.write(data)
            
            # Convert dataframe to CSV
            output = StringIO()
            data.to_csv(output, index=False)
            processed_data = output.getvalue()
            
            # Provide download link for the new CSV file
            st.download_button(label='Download CSV with Sentiments',
                               data=processed_data,
                               file_name='quotes_with_sentiments.csv',
                               mime='text/csv')

if __name__ == '__main__':
    main()
