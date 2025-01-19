# Sentiment Analysis with TextBlob and Streamlit

This project demonstrates a simple sentiment analysis tool built using **TextBlob** and **Streamlit**.

In this application, 
- There are three options available.
- One, Checking polarity of single text.
- Two, cleaning the text(ie. Removing numbers and special characters).
- Three, it is asked to upload a csv file containing a column named "text".
- This column should contain different texts for sentiment analysis.
- Textblob will work on this data.
- Then outputs a new dataframe with 2 additional columns named "sentiment" and "score".
- This additional column contains the sentiment(Positive, Negative, Neutral) and polarity score(-1 to 1) of the respective text.
- User can download this new csv file by clicking the download button.

Built with Streamlit, the app features an interactive and user-friendly interface, making it easy to explore sentiment analysis in real time.
Copy the code to your system and use the command 'streamlit run Sentiment_Analysis_App.py'for trying out.
