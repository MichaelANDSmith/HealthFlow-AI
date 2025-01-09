from transformers import pipeline

def analyze_text(text):
    """
    Analyzes the user's text input using NLP techniques.
    :param text: The text input from the user
    :return: Analysis result (e.g., sentiment, intent)
    """
    nlp_pipeline = pipeline("sentiment-analysis")
    result = nlp_pipeline(text)
    return result
