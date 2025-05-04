from transformers import pipeline

# Load the pipelines once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def summarize_text(text):
    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        return summary
    except Exception as e:
        raise RuntimeError(f"Summarization failed: {e}")

def analyze_sentiment(text):
    try:
        sentiment = sentiment_analyzer(text)[0]
        return f"{sentiment['label']} ({sentiment['score']:.2f})"
    except Exception as e:
        raise RuntimeError(f"Sentiment analysis failed: {e}")
