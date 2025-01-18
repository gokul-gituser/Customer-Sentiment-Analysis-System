from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax
import re

# model chosen for the task.  
# RoBERTa-base "cardiffnlp/twitter-roberta-base-sentiment-latest" model trained on ~124M tweets. 
# finetuned for sentiment analysis
MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

#tokenizer, model configuration and model for sentiment analysis
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME) 
config = AutoConfig.from_pretrained(MODEL_NAME)        
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

# Function to preprocess text by removing HTML tags and URLs
def preprocess(text):
    # Remove HTML tags
    html_pattern = re.compile('<.*?>')
    text = html_pattern.sub(r'', text)

    # Remove URLs
    url_pattern = re.compile(r'https?://\S+|www\.\S+')
    text = url_pattern.sub(r'', text)

    return text


#function to perform sentiment analysis
def sentiment_analysis(text):
    #preprocess the feedback text
    text = preprocess(text)
    #Tokenize into input format that the model can understand
    encoded_input = tokenizer(text, return_tensors='pt')
    #sentiment scores obtained for the feedback
    output = model(**encoded_input)

    #sentiment score converted into numpy array
    scores = output[0][0].detach().numpy()

    #indices of scores are sorted in ascending order by argsort() method
    # the last index now corresponds to the sentiment with highest score
    ranking = scores.argsort()
    #the order is reversed,making the index of the sentiment with highest score come first
    #ranking[::-1] reverses the array. ranking[::-1][0] selects the first element
    #config.id2label maps the score to the required sentiment
    # sentiment label corresponding to the highest score is returned
    sentiment = config.id2label[ranking[::-1][0]]
    
    return sentiment

