from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import re


MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
config = AutoConfig.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def preprocess(text):
    # Remove HTML tags
    html_pattern = re.compile('<.*?>')
    text = html_pattern.sub(r'', text)

    # Remove URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text = url_pattern.sub(r'', text)

    return text


def sentiment_analysis(text):
    
    text = preprocess(text)

    encoded_input = tokenizer(text, return_tensors='pt')

    output = model(**encoded_input)

    #sentiment score
    scores = output[0][0].detach().numpy()
    ranking = scores.argsort()

    #sentiment
    sentiment = config.id2label[ranking[::-1][0]]
    
    return sentiment

