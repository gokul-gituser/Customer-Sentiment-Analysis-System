# Customer Sentiment Analysis
## Objective
To develop a web application that employs a sentiment analysis model to classify customer feedback on products as positive, neutral, or negative
## Project Description
The home page of the website allows customers to create an account and then login. After successful login, customers can access a form to provide feedback on various products available on the website.
The form contains fields to enter the customer's name, product name and a feedback field to enter the their opinion on that particular product.  Since customers are required to log in, their name is automatically pre-filled in the form.
They only have to enter the product name and its feedback. The product name field has auto-complete functionality. When the customer starts to type in a product name, products from the database that has similar names are displayed as sugestions in a dropdown list.
When the customer clicks on one of the available suggestions from the dropdown, the selected item gets
filled in the product name field. After entering the feedback, the customer can click the submit button. On button click, sentiment analysis is performed in the feedback text and
it is shown to the customer if their feedback was positive, neutral or negative.
## Key Features
### Frontend:
- User Authentication
  - Registration Form: Allows new customers to create an account by providing their name, email, and password.
  - Login Form: Enables existing customers to log in, to access the feedback submission functionality.

- Feedback Submission Form:

  - Input fields for customer name, product name and feedback text.
  - Product field has autocomplete functionality 
  - Submit button to analyze and display the sentiment of the feedback.
 
###  Backend:

- Sentiment Analysis:
  - A pre-trained sentiment analysis model processes the feedback text and classifies it into positive, neutral, or negative sentiments.
  - APIs handle product name autocomplete, feedback submissions and data persistence.
 
### Data Handling
- Store customers in Customer table
  
  - id : Unique identifier for each customer.
  - name :The customer's name.
  - email : The customer's email address.
  - password : The customer's password for authentication.
- Store products in Product table
  
  - id :  unique identifier for each product.
  - name: The name of the product.
  - category: The category to which the product belongs
  - rating : Rating of the product
- Store customer feedback for products along with sentiment
  
  - id : Unique identifier for each feedback entry 
  - customer : Foreign Key. References the Customer table, linking feedback to the customer
  - product : Foreign Key. References the Product table, linking feedback to the product
  - feeedback_text : The feedback provided by the customer.
  - sentiment : Result of sentiment analysis on feedback text

## Technologies Used
- Django: High-level Python web framework that includes all essential components like ORM (Object-Relational Mapping), URL routing, authentication, and an admin interface out of the box. This eliminates the need for integrating multiple tools manually
  Django REST Framework (DRF) provides tools to develop APIs with built-in serialization, authentication, and validation features. Django provides built-in protection against common web vulnerabilities like SQL injection, cross-site scripting, and
  cross-site request forgery (CSRF), making it a secure choice.
- SQLite : Chosen for its simplicity and ease of setup, making it an excellent choice for development and prototyping phases. Django supports SQLite as the default database engine, ensuring seamless integration and eliminating additional configuration.
- Frontend : The frontend leverages HTML and CSS ,with Bootstrap used for minor design enhancements and JavaScript implemented to add interactive features, such as input field autocomplete.
- Pre-trained Sentiment Analysis Model: cardiffnlp/twitter-roberta-base-sentiment-latest was used for sentiment analysis. This is a RoBERTa-base model trained on 124 million tweets and finetuned for sentiment classification into positive, neutral and negative.
  As a Hugging Face model, it integrates seamlessly into Python-based projects using the transformers library.The model's training on Twitter data allows it to handle informal and user-generated content, like feedback data submitted by customer.

## Installation and Setup
- Clone the project repository from GitHub:
- Navigate to the project directory
- Create a virtual environment
  ```
  python -m venv env
  
  ```
- Activate the virtual environment
  - Windows
  ```
  env\Scripts\activate
  
  ```
  - macOS/Linux:
  ```
    source env/bin/activate

  ```
- Install Required Dependencies
  ```
  pip install -r requirements.txt

  ```
- Set Up the Database
  ```
  python manage.py makemigrations
  python manage.py migrate

  ```
- Start the Development Server
  ```
  python manage.py runserver
  
  ```
  The application will be accessible at http://127.0.0.1:8000.

## Usage Instructions
- Create Account

  - Click on the Sign Up button
  - Fill out the form with name and email id
  - Choose a password
  - Confirm the password
  - Click on Sign Up button
    
After creating an account Log In form will be shown

- Login
  - Enter the name and password
  - Click on Log In button

Logged in customer is redirected to their dashboard containing a form for feedback submission

- Feedback Submission and Sentiment Display
  - Customer's name will appear on the name field automatically
  - Enter the name of the product in the field provided
  - Enter your feedback of the product
  - Click on Submit button
  - After a couple of seconds the sentiment of the customer's feedback will be displayed on screen
- Log Out
  - Customer can log out by clicking the Log Out button provided
  - A message is displayed on screen to indicate a successful log out.


## API Documentation
All API endpoints are prefixed with /api/
- Product Name Autocomplete
  - Endpoint:
    - GET `/api/product-name-autocomplete/`
  - This endpoint returns a list of products whose names contain the query string provided by the user. It is used for the product name autocomplete
  - The ProductSerializer is used to serialize the data. The serializer returns the id and name fields of the Product model.
    ```
    class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']  
    ```
  - JavaScript Integration
      - The input field triggers an API request to /api/product-name-autocomplete/ as the customer types.
      - A dropdown list is populated with products whose names match the query.
      - When a product is selected from the dropdown, the input field is updated with the product name.
        
- Submit Feedback
  - Endpoint:
    - POST `/api/submit-feedback/`
  - This endpoint allows customers to submit feedback on a product. The feedback text undergoes sentiment analysis and the sentiment result is stored along with the feedback in the database.
    The sentiment result is also returned in the response.
  - FeedbackSerializer is used to validate and serialize the data for feedback submission
    ```
    class FeedbackSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), write_only=True)
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True)

    class Meta:
        model = Feedback
        fields = ['customer', 'product', 'feedback_text', 'sentiment']
        read_only_fields = ['sentiment']

    
    def create(self, validated_data):
        validated_data['customer'] = validated_data.pop('customer')
        return super().create(validated_data)


    ```
  - The request body contains the customer, product, and feedback data from the frontend. After performing sentiment analysis on feedback text, sentiment is sent back in the response body.
  - JavaScript Integration
    - When the form is submitted, the data from the form (customer, product, and feedback text) is sent to the /api/submit-feedback/ endpoint.
    - The sentiment result from the response body is displayed in the frontend

## Sentiment Analysis
Sentiment analysis is the process of analyzing digital text to determine if the emotional tone of the message is positive, negative, or neutral. In this project, sentiment analysis is applied to customer's feedback 
on different products that are available on the website
- `cardiffnlp/twitter-roberta-base-sentiment-latest` was used for sentiment analysis. This is a RoBERTa-base model trained on 124 million tweets and finetuned for sentiment classification into positive, neutral and negative.
  As a Hugging Face model, it integrates seamlessly into Python-based projects using the transformers library. The model's training on Twitter data allows it to handle informal and user-generated content, like feedback data submitted by customer.
- The sentiment analysis is performed through the following steps:
  - The text is cleaned by removing HTML tags and URLs to prevent irrelevant content from influencing sentiment classification
  - The cleaned text is tokenized into a format that can be fed into the model. Tokenization breaks down the text into tokens like words or subwords, which is essential for understanding and processing natural language.
  - The preprocessed and tokenized text is passed through the sentiment analysis model. The model outputs sentiment scores, indicating how likely the feedback is to belong to each sentiment category.
  - The model outputs sentiment scores for each sentiment class. These scores are sorted, and the class with the highest score is selected as the sentiment of the feedback.
  ```
  
  from transformers import AutoModelForSequenceClassification
  from transformers import AutoTokenizer, AutoConfig
  import numpy as np
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
  ```

- `AutoTokenizer` provides an easy way to load the tokenizer for a specific model. By calling `from_pretrained(MODEL_NAME)`, we can load the tokenizer that was trained along with the model.
- `AutoConfig` class is used to load the configuration of the model. `from_pretrained(MODEL_NAME)`, loads the configuration associated with the pre-trained model.
- `AutoModelForSequenceClassification` class is used for models designed for sequence classification including sentiment analysis. By calling `from_pretrained(MODEL_NAME)`, we load the pre-trained weights and model architecture.
- After preprocessing, cleaned text is tokenized using the tokenizer object. The tokenizer() method converts the text into subword tokens and returns them as tensor data in a format suitable for the model
  ```
  encoded_input = tokenizer(text, return_tensors='pt')
  ```

- The tokenized input is passed to the model using the model() method. The model generates a prediction in the form of sentiment scores. The `**encoded_input` syntax unpacks the tokenized input and passes it to the model.
  ```
  output = model(**encoded_input)
  ```

- The model's output is a tensor containing sentiment scores. The scores are extracted using `output[0][0]` to get the first element from the output tensor. Then, it is detached from the computation graph and converted it into a NumPy array using `.detach().numpy()` for easier manipulation.
  ```
  scores = output[0][0].detach().numpy()
  ```

- `argsort()` method is used on the sentiment scores to sort them in ascending order. This will give the indices of the scores, from the lowest to the highest. The index corresponding to the highest score will represent the most likely sentiment
  ```
  ranking = scores.argsort()
  ```

- To prioritize the highest sentiment score, reverse the order of the sorted indices `(ranking[::-1])`. The first element after reversing will be the index of the sentiment with the highest score. Then map this index to its corresponding sentiment label using `config.id2label[ranking[::-1][0]]`
  ```
  sentiment = config.id2label[ranking[::-1][0]]
  ```
  
- Finally, the sentiment label corresponding to the highest score is returned as the result of the sentiment analysis

- Model Output
  - The model classifies feedback into one of the following categories:
    - positive
    - negative
    - neutral
      
- This sentiment result is returned as part of the API response. It is displayed in the frontend and stored alongside the feedback in the database

## Future Improvements
- Implement a trending Products Dashboard or Sentiments Dashboard
