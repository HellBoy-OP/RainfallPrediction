# Rainfall Prediction System
> Using Machine Learning (Python)

This project showcases the integration of machine learning with modern web technologies to address real-world challenges effectively.

# Technologies Used:
- Frontend:
  > JavaScipt, HTML, Tailwind CSS

- Backend & ML Model:
  > Python (Flask, numpy, skikit-learn, matplotlib)

## Objective
> The primary aim of this project is to accurately predict rainfall using historical data spanning from 1901 to 2015. By leveraging this extensive dataset, the model can provide valuable insights and predictions for rainfall patterns, which can be crucial for agricultural planning, water resource management, and disaster preparedness.

## Key Features
- Utilizes a comprehensive dataset for accurate predictions
- Interactive and user-friendly frontend interface
- Robust and efficient backend processing

## Dataset:
> Monthly rainfall data of Indian State and UT from year 1901 to 2015.

## Models:
- [ ] Linear Regression Model
- [ ] Lasso Model
- [ ] Ridge Model
- [ ] SVM Model
- [x] Random Forest Model

  > We will be using Random Forest Model for this project.

## Create Model:
- Install requirements from `requirements.txt`

      pip3 install -r requirements.txt

- Create the model

      python3 src.py

## Deploy Flask App:
- Before deploying make sure that `model.onnx` is present in root directory.
- Now deploy the flask app.
 
      python3 main.py

<!---
- ## Team:
    - Anand Dubey
    - Suman Das
    - Sanjib Hansda
    - Soudipta Modal
    - Satyam Shaw
--->

