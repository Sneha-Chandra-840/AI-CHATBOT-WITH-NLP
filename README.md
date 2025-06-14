# AI-CHATBOT-WITH-NLP

"COMPANY" : CODTECH IT SOLUTIONS

"NAME" : SNEHA CHANDRA

"INTERN ID" : CT1MTDF345

"DOMAIN" : PYTHON PROGRAMING

"DURATION" : 4 WEEKS

"MENTOR" : NEELA SANTOSH KUMAR

"PROJECT DISCRIPTION" : Project Overview : This project focuses on building a simple yet intelligent chatbot that uses Natural Language Processing (NLP) techniques to understand and respond to user queries. The chatbot has been implemented using two major Python libraries in the NLP domain: NLTK (Natural Language Toolkit) and spaCy. The goal of this project is to simulate human-like conversation by understanding the context of a user's input and generating relevant responses using natural language understanding techniques.
The chatbot works by maintaining a FAQ-based corpus, which contains a set of predefined questions and their respective answers. When the user inputs a query, the chatbot processes the input text using NLP steps such as tokenization, stopword removal, lemmatization, and semantic similarity comparison. The response is then selected based on the closest matching question in the predefined corpus.


Key Technologies and Tools Used:
Python – The core programming language used to build the chatbot.
NLTK (Natural Language Toolkit) – Used for tokenization, lemmatization, and removing stopwords.
spaCy – Used for computing sentence-level similarity using its Doc.similarity() method.
Text Corpus – A dictionary that holds common questions and their answers.
Command-Line Interface (CLI) – The chatbot interacts with the user through a console interface.


How it Works:
1. Text Preprocessing (NLTK):
The chatbot first processes user input using the preprocess() function. It:
Converts the input to lowercase
Removes punctuation
Tokenizes the text using nltk.word_tokenize()
Filters out stopwords like “is”, “the”, “in”
Lemmatizes each word using WordNetLemmatizer
This helps normalize the user input, making it easier to match with the FAQ corpus.

2. Similarity Matching (spaCy):
To determine which question in the FAQ corpus best matches the user's input, spaCy is used to:
Convert both the user input and each FAQ question into spaCy Doc objects
Calculate similarity scores using Doc.similarity()
Select the FAQ entry with the highest similarity score above a defined threshold (e.g., 0.6)
This allows the chatbot to respond even when the user doesn't ask the question exactly as written in the FAQ.

3. Interactive Chat Loop:
The chatbot runs an infinite loop using a simple CLI interface. It greets the user and allows them to enter queries. If the user types "exit", "quit", or "bye", the chatbot ends the session. Otherwise, it responds with the best-matching answer or a fallback message like:
“I'm sorry, I don't understand that yet.”


Conclusion:
This project demonstrates how natural language processing can be effectively used to simulate human conversation. Using NLTK and spaCy, we created a chatbot that understands and responds to user input with reasonable accuracy. It showcases the importance of linguistic preprocessing and vector-based similarity measures in building conversational AI. This project serves as a foundational step toward more advanced and intelligent chatbot systems.
