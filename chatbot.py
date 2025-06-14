import random
import nltk
import spacy
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

nlp = spacy.load("en_core_web_sm")

faq = {
    "what is your name": "I am a ChatBot powered by NLP.",
    "how are you": "I'm doing well, thank you!",
    "what can you do": "i am chatbot designed to answer about NLP",
    "what is NLP": "NLP is a field of AI that gives machines the ability to read, understand, and respond to human languages.",
    "bye": "Bye! Have a great day.",
    "hello": "Hi there! How can I assist you today?",
    "thank you": "your welcome! anything else i may help u with"
}

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))

def preprocess(text):
    text = text.lower().translate(str.maketrans('', '', string.punctuation))
    tokens = nltk.word_tokenize(text)
    filtered = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    return filtered

def get_response(user_input):
    user_doc = nlp(user_input)
    max_similarity = 0
    best_match = None
    for question in faq:
        question_doc = nlp(question)
        similarity = user_doc.similarity(question_doc)
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = question
    if max_similarity < 0.6:  # Threshold
        return "I'm sorry, I don't understand that yet."
    return faq[best_match]

def chat():
    print("ChatBot: Hello! I am your ChatBot")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("ChatBot: Bye! Have a great day")
            break
        response = get_response(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    chat()

