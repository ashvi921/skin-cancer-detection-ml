# 🧠 Skin Cancer Detection System Using Machine Learning

An end-to-end AI-powered system for early detection of skin cancer using Convolutional Neural Networks (CNN), integrated with image preprocessing, lesion segmentation, and a web-based interface for real-time predictions.

---

## 📌 Problem Statement

Skin cancer is one of the most common forms of cancer worldwide. Early detection is critical for effective treatment and survival. Manual diagnosis can be time-consuming and subjective. This project aims to automate skin lesion classification using machine learning techniques to assist in early diagnosis.

---

## 🚀 Key Features

* 📤 Upload dermoscopic skin images via web interface
* 🧹 Image preprocessing using OpenCV and NumPy
* 🔍 Lesion segmentation using GLCM (Gray-Level Co-occurrence Matrix)
* 🧠 CNN-based classification (Benign vs Malignant)
* ⚡ Real-time prediction through backend API
* 🌐 Full-stack integration (Frontend + Backend)

---

## 🏗️ System Architecture

```
Input Image → Preprocessing → Segmentation → CNN Model → Prediction Output
```

---

## 🧪 Tech Stack

### 🔹 Machine Learning

* Python
* TensorFlow / Keras
* OpenCV
* NumPy

### 🔹 Backend

* Flask / FastAPI

### 🔹 Frontend

* HTML / CSS / JavaScript *(or React if implemented)*

---

## 📂 Project Structure

```
skin-cancer-detection-ml/
│
├── src/                # Core ML logic (preprocessing, model, prediction)
├── notebooks/          # Training & experimentation
├── web/                # Frontend interface
├── app.py              # Backend server
├── requirements.txt    # Dependencies
└── README.md
```

---

## 🧠 Model Details

* Model Type: Convolutional Neural Network (CNN)
* Input: Skin lesion images
* Output: Binary classification (Benign / Malignant)
* Training Framework: TensorFlow/Keras
* Feature Extraction: GLCM-based texture analysis

---

## 📊 Results

* Achieved strong classification performance on test data
* Model generalizes well across different lesion types

> *(Add your actual accuracy here for credibility — e.g., 87% accuracy)*

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/ashvi921/skin-cancer-detection-ml.git
cd skin-cancer-detection-ml
pip install -r requirements.txt
python app.py
```

---

## 📁 Dataset

This project uses publicly available datasets such as:

* ISIC (International Skin Imaging Collaboration)

> ⚠️ Dataset is not included in the repository due to size constraints.

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**.
It is **not a substitute for professional medical diagnosis**.

---

## 🌟 Future Improvements

* 🔬 Use Transfer Learning (ResNet, EfficientNet)
* 📱 Mobile app integration
* ☁️ Cloud deployment (AWS / GCP)
* 📊 Model explainability using Grad-CAM

---

## 👨‍💻 Author

**Ashvita**

* GitHub: https://github.com/ashvi921

---

## ⭐ If you found this useful

Give it a ⭐ on GitHub and feel free to contribute!
