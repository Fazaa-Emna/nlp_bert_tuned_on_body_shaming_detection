import pickle
from sklearn.feature_extraction.text import TfidfVectorizer


class BinaryBodyShaming():
    def __init__(self):
        # Load the TF-IDF vectorizer
        with open("root/workspace/models/vectorizer_SVM.pkl", 'rb') as vec_file:
            self.vectorizer = pickle.load(vec_file)

        # Load the SVM model
        with open("root/workspace/models/model_SVM.pkl", 'rb') as model_file:
            self.model = pickle.load(model_file)

        self.labels = ["pas d'insulte", "insulte du corps"]
        self.output = ["not body shaming", 'body shaming']

    
    def predict(self, text):
        # Use the fitted vectorizer to convert text to numerical features
        text_features = self.vectorizer.transform([text])
        print("Number of features:", text_features.shape[1])
        # Get the decision function values (confidence scores) from the SVM model
        decision_values = self.model.decision_function(text_features)

        # Make predictions with the SVM model
        prediction = self.model.predict(text_features)

        # Extract label and confidence score from predictions
        label = self.labels[prediction[0]]
        confidence_score = abs(decision_values[0])  # Using the decision function values as confidence scores

        return label, confidence_score
