# 🩺 Skin Cancer Detection Using Deep Learning

<p align="center">
  <img src="images/banner.png" width="900">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue">
  <img src="https://img.shields.io/badge/TensorFlow-DeepLearning-orange">
  <img src="https://img.shields.io/badge/Flask-WebApp-green">
  <img src="https://img.shields.io/badge/ComputerVision-MedicalAI-red">
</p>

---

# 📌 Project Overview

Skin cancer is one of the most common forms of cancer worldwide. Early detection significantly increases treatment success rates and improves patient survival.

This project develops a Deep Learning-based system capable of classifying skin lesion images and supporting early skin cancer screening. The solution combines Computer Vision techniques, Convolutional Neural Networks (CNN), and a Flask-based web application for real-time prediction.

The project demonstrates a complete Machine Learning pipeline, including:

* Data Collection
* Data Preprocessing
* Exploratory Data Analysis (EDA)
* Deep Learning Model Training
* Model Evaluation
* Web Application Deployment

---

# ⭐ Key Highlights

* Developed an end-to-end Deep Learning pipeline for medical image classification.
* Applied Convolutional Neural Networks (CNN) for skin lesion analysis.
* Performed image preprocessing and augmentation techniques.
* Evaluated model performance using multiple classification metrics.
* Built and deployed a Flask web application for real-time prediction.
* Applied Artificial Intelligence to a real-world healthcare problem.

---

# 🎯 Problem Statement

Traditional skin cancer diagnosis relies heavily on dermatologists' experience and manual examination. This process can be time-consuming and may not always be accessible in remote areas.

The objective of this project is to build an automated image classification system capable of identifying potential skin cancer cases from dermoscopic images, supporting healthcare professionals in early-stage screening.

---

# 📊 Dataset

This project utilizes the HAM10000 dataset from the International Skin Imaging Collaboration (ISIC).

Dataset Characteristics:

* More than 10,000 dermoscopic images
* Medical image dataset
* Expert-labeled skin lesion categories
* Widely used benchmark dataset in skin cancer research

Disease Categories:

| Label | Disease              |
| ----- | -------------------- |
| akiec | Actinic Keratoses    |
| bcc   | Basal Cell Carcinoma |
| bkl   | Benign Keratosis     |
| df    | Dermatofibroma       |
| mel   | Melanoma             |
| nv    | Melanocytic Nevi     |
| vasc  | Vascular Lesions     |

---

# 🧠 Deep Learning Architecture

The project uses a Convolutional Neural Network (CNN) for image classification.

Architecture Flow:

Input Image
↓
Image Preprocessing
↓
Convolution Layer
↓
ReLU Activation
↓
Max Pooling
↓
Convolution Layer
↓
Max Pooling
↓
Flatten
↓
Dense Layer
↓
Dropout
↓
Softmax Classification

---

# 🔄 Machine Learning Pipeline

1. Data Collection
2. Data Cleaning
3. Image Resizing
4. Normalization
5. Data Augmentation
6. CNN Training
7. Model Evaluation
8. Flask Deployment
9. User Prediction Interface

---

# 📈 Model Performance

| Metric | Value |
|----------|----------|
| Test Accuracy | 74.30% |
| Validation Accuracy | 73.26% |
| Test Loss | 0.6797 |
| Validation Loss | 0.7088 |

### Performance Analysis

- Achieved **74.30% classification accuracy** on the test dataset.
- Validation accuracy reached **73.26%**, indicating stable model generalization.
- The difference between training and validation performance is relatively small, suggesting limited overfitting.
- Data augmentation and dropout layers contributed to improved robustness.
- The model demonstrated strong performance on majority classes while maintaining acceptable performance across minority classes.

### Confusion Matrix Insights

- Highest prediction accuracy was achieved for the dominant lesion categories.
- Misclassifications mainly occurred among visually similar skin lesion types.
- Dataset imbalance remains a key challenge affecting minority-class performance.
- Future improvements may include Transfer Learning (EfficientNet, ResNet50), class weighting, and ensemble methods.

---

## Training Results

### Accuracy & Loss Curves

![Training Curve](images/training_curve.png)

### Confusion Matrix

![Confusion Matrix](images/confusion_matrix.png)

The CNN model achieved a test accuracy of **74.30%** on a seven-class skin lesion classification task using the HAM10000 dataset. The results demonstrate the feasibility of applying Deep Learning techniques to support early skin cancer screening and medical image analysis.

---

# 🌐 Web Application

A Flask-based web application was developed to allow users to upload skin lesion images and obtain predictions instantly.

Features:

✅ Upload image

✅ Automatic preprocessing

✅ Deep Learning prediction

✅ Probability estimation

✅ User-friendly interface

---

# 📸 Application Demo

## Home Page

<p align="center">
  <img width="1366" height="768" alt="114df189dc5b54050d4a1" src="https://github.com/user-attachments/assets/9a372109-7278-40cc-9e33-66550c25c297" />
  <img width="1366" height="768" alt="8c71a1c88c1a04445d0b3" src="https://github.com/user-attachments/assets/1bf7de24-acf2-4965-b4db-22f805f91b7a" />
  <img width="1366" height="768" alt="765f1b9c364ebe10e75f2" src="https://github.com/user-attachments/assets/59f64bd7-99b4-4473-83e2-77b689c0720a" />
</p>

## Prediction Page


<p align="center">
  <img width="1366" height="768" alt="42f855437891f0cfa9804" src="https://github.com/user-attachments/assets/3de3f1e6-5e59-4aa6-a86d-f3992dc0be6a" />
</p>

## Prediction Result

<p align="center">
  <img width="1366" height="768" alt="376ad9c4f4167c4825075" src="https://github.com/user-attachments/assets/5e240ae7-1cd4-4b1b-b2fc-ca0c42df3d97" />
  <img width="1366" height="768" alt="41ce996ab4b83ce665a96" src="https://github.com/user-attachments/assets/8faad9f2-cce6-4430-9673-0ebc2c8ed5ac" />
</p>

---

# 💻 Technologies Used

## Programming Language

* Python

## Data Science

* NumPy
* Pandas
* Matplotlib
* Scikit-Learn

## Deep Learning

* TensorFlow
* Keras

## Computer Vision

* OpenCV

## Web Development

* Flask
* HTML
* CSS
* Bootstrap

## Development Tools

* Jupyter Notebook
* Git
* GitHub

---

# 📂 Project Structure

```text
SkinCancerDetection/
│
├── DASKIN.ipynb
├── test_model.ipynb
├── model.h5
│
├── web/
│   ├── app.py
│   ├── model.h5
│   │
│   ├── templates/
│   │   ├── home.html
│   │   └── predict.html
│   │
│   └── static/
│       └── uploads/
│
├── images/
│   ├── training_curve.png
│   ├── confusion_matrix.png
│   ├── homepage.png
│   ├── predict_page.png
│   └── result.png
│
└── README.md
```

---

# 🔬 Future Improvements

* Apply Transfer Learning (EfficientNet, ResNet50, DenseNet).
* Improve dataset balancing.
* Add Explainable AI (Grad-CAM).
* Deploy to Cloud (AWS, Azure, GCP).
* Develop Mobile Application.
* Integrate Doctor Recommendation System.

---

# 🌍 Real-world Impact

This project demonstrates how Artificial Intelligence can support healthcare by:

* Assisting dermatologists during screening.
* Improving accessibility to medical services.
* Reducing diagnosis time.
* Increasing awareness of early skin cancer detection.
* Supporting healthcare systems in resource-limited environments.

---

# 🛠 Skills Demonstrated

* Machine Learning
* Deep Learning
* Computer Vision
* Medical Image Analysis
* CNN Architecture Design
* Data Preprocessing
* Model Evaluation
* Flask Deployment
* Git Version Control
* End-to-End AI Development

---

# 👨‍💻 Author

**Tran Nguyen Thanh Nam**

**Tran Nguyen Anh Tuan**

Data Science Student

Interests:

* Artificial Intelligence
* Machine Learning
* Deep Learning
* Computer Vision
* Healthcare AI

GitHub:
https://github.com/tntnammm

---

⭐ If you find this project useful, please consider giving it a star.
