# Body Shaming Text Classifier

This repository contains a text classifier for identifying body shaming and non-body shaming content in the French language. The classifier is built using the BERT (Bidirectional Encoder Representations from Transformers) model and achieves an accuracy of approximately **95%.**

## Dataset

The dataset used for training and evaluation of the classifier consists of a collection of text samples labeled as either body shaming or non-body shaming.

## Model Architecture

The text classifier is built using the BERT (Bidirectional Encoder Representations from Transformers) model, which is a state-of-the-art deep learning architecture for natural language processing tasks. BERT is based on the transformer architecture and has achieved remarkable performance across various NLP domains.

The BERT model used in this project has been pre-trained on a large corpus of text data and fine-tuned for the specific task of body shaming classification.

## Usage

To use the body shaming text classifier, follow these steps:

1. Install Docker on your machine.
2. Clone this repository to your local machine.
3. Navigate to the deploiement folder in the cloned repository.
4. Run the following command to start the classifier service using Docker Compose:
- docker-compose up

This command will build the Docker image and start the FastAPI server hosting the body shaming text classifier.

Once the server is up and running, you can access the classifier API at http://localhost:8999.

To classify text, send a POST request to the /docs endpoint with the text as the request body. The API expects a JSON payload in the following format:
```json
{
  "text": "Your text goes here."
}
```
The API will respond with a JSON object containing the classification result:
```json
{
  "model": "body shaming fr",
  "class":"body shaming",
  "proba": 0.92
}
```
The class field indicates whether the text is classified as body shaming or not, and the proba field represents the probability or confidence score associated with the classification.

You can send multiple requests to the API for classifying different texts.

Note: Ensure that Docker is running and no other service is already using port 8999 on your machine.

Refer to the provided example scripts or notebook for a detailed implementation guide.

## Performance and Evaluation

The body shaming text classifier achieves an accuracy of approximately **90%** on the evaluation dataset. 
This accuracy metric indicates the proportion of correctly classified samples in the evaluation set. It is important to note that the accuracy may vary depending on the quality and diversity of the data used for training and evaluation.

To ensure the reliability and generalizability of the classifier, it is recommended to perform regular evaluations on new datasets to monitor its performance and make necessary improvements.

