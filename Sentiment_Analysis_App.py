import pandas as pd
import streamlit as st
from textblob import TextBlob
import cleantext

st.header("Sentiment Analysis")

with st.expander("Analyse Text"):
    text = st.text_input("Enter the text here")
    if text:
        data = TextBlob(text)
        st.write("Polarity : ",round(data.sentiment.polarity,2))
        st.write("Subjectivity : ",round(data.sentiment.subjectivity,2))
    
    text2 = st.text_input("Clean text")
    if text2:
        st.write(cleantext.clean(text2,clean_all=False,extra_spaces=True,stopwords=True,lowercase=True,numbers=True,punct=True))
with st.expander("Analyse CSV"):
    upl_file = st.file_uploader("Upload File")

    def pol_score(text):
        blob2 = TextBlob(text)
        return blob2.polarity
    def sentiment(score):
        if score <= -0.5:
            return "Negative"
        elif score >= 0.5:
            return "Positive"
        else:
            return "Neutral"
    def clean_txt(text):
        cleaned_txt = cleantext.clean(str(text),clean_all=False,extra_spaces=True,stopwords=True,lowercase=True,numbers=True,punct=True)
        return cleaned_txt
    
    if upl_file:
        df = pd.read_csv(upl_file)

        df['score'] = df['text'].apply(pol_score)
        df['sentiment'] = df['score'].apply(sentiment)
        st.write(df.head())

    @st.cache_data
    def convert_df(df):
        return df.to_csv().encode('utf-8')
    
    final_csv = convert_df(df)
    st.download_button(
        label = "Download CSV",
        data = final_csv,
        file_name = 'after_senti_anaysis.csv',
        mime = 'text/csv'
        )

