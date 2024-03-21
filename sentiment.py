from textblob import TextBlob
def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    
    # Classify sentiment
    if sentiment_polarity > 0:
        return "Positive"
    elif sentiment_polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example text
text = input("enter text:")

# Analyze sentiment
sentiment = analyze_sentiment(text)
print("Sentiment Analysis Result:", sentiment)
