from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import cv2
import numpy as np

# Initialize the Flask application
app = Flask(__name__)

# Load the trained model
model = load_model('model4.h5')

@app.route('/')
def hello_world():
    return 'Hello, World!'

# Endpoint to classify image
@app.route('/classify', methods=['POST'])
def classify_image():
    img = request.files.get('image').read()
    img = cv2.imdecode(np.frombuffer(img, np.uint8), -1)
    img = cv2.resize(img, (250, 250))
    img = img / 255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)
    class_label = np.argmax(prediction)
    
    return jsonify({'class_label': class_label})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)


