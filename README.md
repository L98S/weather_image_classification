# weather_image_classification
Hello and welcome to a new data science project, one that I'm excited to work on because it involves images! Yes, my friend, we are diving into image classification, specifically focusing on weather images.

The field of computer vision is rapidly expanding and finds applications in a variety of fields, from medicine to the military. Today, we're going to apply it to weather and classify images of different types of weather. In this project, we aim to achieve the following objectives:

1. Conduct an exploratory data analysis (EDA) to understand the dataset.
2. Develop and evaluate a multi-class classification model to identify the weather condition in each image.
3. Develop an API to serve the model, making it accessible for real-world applications.
---
![201109651_tgazweather_t800](https://github.com/L98S/weather_image_classification/assets/110102931/7f3f785d-e2f1-4967-8f39-2a8f3a501d9f)

---
# Running the Project:
In this repository, you'll find:
1. A 'requirements.txt' file that includes all the libraries needed for this project.
2. A 'weather_image_classification.ipynb' file that offers a step-by-step approach for the project.
3. An API file that includes:
   * "Dockerfile.txt" contains the instructions to build a Docker image for the API
   * "app.py" containing the Flask API and model inference code
   * Please note that due to file size constraints, the best-performing model couldn't be uploaded directly into the API folder. To use the API as intended, you'll need to first generate this model by running the notebook weather_image_classification.ipynb. This will download the best model, allowing you to fully utilize the API's capabilities


**For the best experience, please open the project in Google Colab to view all the visualizations and navigate easily through the steps. A link to the Colab notebook is provided at the top of the weather_image_classification.ipynb file.**



# About The Project:
The project follows a systematic approach to data analysis, preprocessing, model training, and evaluation. Here is an overview of the key steps involved:

1. Introduction
3. Load The Data
4. Splitting the dataset into train and test sets
5. Exploratory Data Analysis
  * 4.1-Sample Images Visualization
  * 4.2-Image Size Distribution
  * 4.3-Color Distribution
5. Data Preprocessing
  * 5.1-Image Resizing
  * 5.2-Image Scaling
  * 5.3-Label Encoding
6. Modeling and Evaluation
  * 6.1-Simple CNN Model
  * 6.2-DenseNet
  * 6.3-Final model
7. Conclusion

