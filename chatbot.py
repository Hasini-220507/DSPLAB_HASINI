from sklearn.feature_extraction.text import TfidfVectorizer;
from sklearn.linear_model import LogisticRegression;

questions=[
    "hello","hi","hey",
    "how are you","how r u","how do you do",
    "what is your name","who are you",
    "help me","can you help","i need help",
    "good morning","gm",
    "bye","goodbye","tinnava","em doing"
]

labels=[
    "greeting","greeting","greeting",
    "status", "status", "status",
    "name", "name",
    "help", "help", "help",
    "morning", "morning",
    "bye", "bye","food","work"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

model = LogisticRegression(
    max_iter=1000,
    class_weight="balanced"
)
model.fit(X, labels)

responses = {
    "greeting": "Hello! How can I help you?",
    "status": "I'm doing great 😊",
    "name": "I am an ML-based Python chatbot.",
    "help": "Sure! Tell me how I can help you.",
    "morning": "Good morning! Have a great day ☀️",
    "bye": "Goodbye! Have a nice day 👋",
    "food":"haa tinna maa nuvvu",
    "work":"ntg iam free tell me"
}

print("ML Chatbot: Hello! Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("ML Chatbot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_input])

    if user_vector.nnz == 0:
        print("ML Chatbot: I can't understand.")
        continue

    intent = model.predict(user_vector)[0]
    print("ML Chatbot:",responses.get(intent,"i can't understand."))
