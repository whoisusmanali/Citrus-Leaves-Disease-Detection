# Citrus Leaves Disease Detection

This project aims to classify various diseases affecting citrus leaves using **Convolutional Neural Networks (CNN)** and **transfer learning techniques**. A web application has also been developed using the **Flask framework**, with an intuitive front-end built using HTML, CSS, and JavaScript.  

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Workflow](#workflow)  
4. [Data Collection](#data-collection)  
5. [Data Preprocessing](#data-preprocessing)  
6. [Model Building](#model-building)  
7. [Testing and Evaluation](#testing-and-evaluation)  
8. [Web Application](#web-application)  
9. [Installation](#installation)  
10. [Usage](#usage)  
11. [Future Work](#future-work)  
12. [Contributing](#contributing)  
13. [License](#license)  

---

## Overview

Citrus crops are vulnerable to various diseases that affect yield and quality. This project focuses on identifying these diseases from images of citrus leaves using deep learning techniques.  
The classification is achieved using a CNN model trained on a labeled dataset of citrus leaf images, and the predictions are served through a Flask-based web application.

---

## Features

- **Disease Classification**: Predicts diseases from images of citrus leaves.
- **Transfer Learning**: Utilizes pre-trained models for better accuracy.
- **Interactive Web App**: Upload an image and get predictions instantly.
- **Real-Time Testing**: Enables users to test the model using their own data.

---

## Workflow

1. Collect and preprocess data.  
2. Train a CNN model with transfer learning.  
3. Test and evaluate the model's performance.  
4. Develop a Flask-based web application.  
5. Deploy the application for user interaction.

---

## Data Collection

The dataset used for training and testing was sourced from **publicly available repositories** containing labeled images of citrus leaves. The dataset includes categories like:
- Healthy leaves.
- Leaves affected by citrus canker.
- Leaves with greasy spot.
- Other diseases.

Key points about the dataset:
- **Number of images**: ~10,000.  
- **Classes**: 4 (Healthy, Canker, Greasy Spot, Others).  

---

## Data Preprocessing

The preprocessing pipeline includes:
1. **Image Resizing**: All images were resized to a fixed dimension (e.g., 128x128 pixels).
2. **Normalization**: Pixel values were scaled to the range [0, 1].
3. **Data Augmentation**: Techniques such as rotation, flipping, and zooming were applied to increase dataset diversity.
4. **Train-Test Split**: The dataset was split into training (80%) and testing (20%) subsets.

---

## Model Building

The classification model was built using **Convolutional Neural Networks (CNN)**.  
- **Base Model**: Transfer learning with pre-trained models like ResNet50 and VGG16.  
- **Architecture**:  
  - Custom layers were added for feature extraction and classification.  
  - The output layer uses a softmax activation function to classify images into disease categories.  
- **Optimization**:  
  - Loss Function: Categorical Cross-Entropy.  
  - Optimizer: Adam.  
  - Learning Rate Scheduler for dynamic adjustments during training.

---

## Testing and Evaluation

The trained model was evaluated using:
- **Accuracy**: Achieved an accuracy of ~94% on the test set.  
- **Precision, Recall, and F1-Score**: Metrics were calculated for each class to ensure robust performance.  
- **Confusion Matrix**: Analyzed to identify misclassifications.  
- **ROC Curve**: Examined for evaluating model performance across thresholds.

---

## Web Application

The Flask-based web application allows users to upload citrus leaf images and receive predictions.  

### Features:
- **User-Friendly Interface**: Designed with HTML, CSS, and JavaScript.  
- **Real-Time Predictions**: Upload an image to get instant results.  
- **Model Information**: Displays confidence scores for each class.  

---

## Installation

Follow these steps to set up and run the project locally:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/whoisusmanali/Citrus-Leaves-Disease-Detection.git
   cd Citrus-Leaves-Disease-Detection
   ```

2. Install required dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Start the Flask application:  
   ```bash
   python app.py
   ```

4. Open your browser and visit:  
   ```
   http://127.0.0.1:5000
   ```

---

## Usage

1. Upload an image of a citrus leaf via the web application.  
2. The model processes the image and predicts the disease.  
3. View results including the class and confidence score.

---

## Future Work

- **Dataset Expansion**: Incorporate more disease categories and diverse data.  
- **Mobile Integration**: Develop a mobile application for easy field usage.  
- **Deployment**: Deploy the app on a cloud platform for global accessibility.  