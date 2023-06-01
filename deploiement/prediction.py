from tensorflow.python.ops.numpy_ops import np_config
np_config.enable_numpy_behavior()
import joblib


class BinaryBodyShaming():
    def __init__(self):
        classifier = joblib.load(f"root/workspace/models/model.pkl")
        self.trained_model = classifier
        self.labels= ['insulte du corps', "pas d'insulte"]
        self.output=['body shaming','not body shaming']
        return

    def predict(self, text):
        res = self.trained_model(text,self.labels)
        label, proba = res['labels'][0],res['scores'][0]
        if label == self.labels[0]:
            label = self.output[0]
        else:
            label = self.output[1]
        return label, proba
        