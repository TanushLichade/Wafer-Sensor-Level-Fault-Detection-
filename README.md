# Wafer-Level Sensor Fault Detection using Machine Learning

## 📌 Project Overview
This project focuses on **automated sensor fault detection at the wafer probe stage** in semiconductor manufacturing.  
Traditional threshold-based methods fail to capture subtle or latent sensor-level faults, leading to yield loss and higher costs.  
We propose a **machine learning–based framework** to improve the accuracy and reliability of wafer-level testing.

---

## ⚙️ Workflow
1. **Data Preprocessing**  
   - Normalization and noise handling  
   - Dimensionality reduction (optional)  

2. **Class Imbalance Handling**  
   - Applied **SMOTETomek** to balance faulty vs. good sensor dies  

3. **Model Training**  
   - Supervised ML models explored:  
     - Support Vector Machine (SVM)  
     - Random Forest  
     - Gradient Boosting (XGBoost)  
   - Hyperparameter tuning with GridSearchCV  

4. **Evaluation**  
   - Metrics: Accuracy, Precision, Recall, F1-score, Confusion Matrix  
   - Best-performing model selected for deployment  

5. **Deployment**  
   - Built an **end-to-end ML pipeline**  
   - Developed a **Flask web interface** for real-time wafer data input and prediction  
   - Containerized using **Docker**  
   - Integrated with **MongoDB** for data storage  

---

## 🚀 Features
- Automated wafer probe fault classification  
- Class imbalance handling with SMOTETomek  
- Multiple ML models with hyperparameter tuning  
- End-to-end pipeline for training and prediction  
- Web-based interface for real-time usability  
- Deployable using Docker + MongoDB  

---

## 📊 Tech Stack
- **Python**, **Scikit-learn**, **Imbalanced-learn**  
- **Flask**, **Docker**, **MongoDB**  
- **Pandas**, **NumPy**, **Matplotlib/Seaborn**  

---

## 📈 Results
- Significant improvement in **fault detection accuracy** compared to rule-based thresholds  
- Final model achieved high **F1-score** with balanced precision and recall  

---

## 📌 Future Work
- Integration with real wafer probe equipment  
- Extension to deep learning models if time-series data becomes available  
- Industrial-scale deployment in semiconductor fabs  

---

