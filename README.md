# Disease Predictor

![](https://img.shields.io/badge/-Flask-blue?style=for-the-badge&logo=flask) ![](https://img.shields.io/badge/-Heroku-purple?style=for-the-badge&logo=heroku)

## What is Disease Predictor?
Disease Predictor is a helper module created to support [Smart Health Assistant](https://github.com/sanb26/Health-Assistant-App) which predicts a probable disease based on the symptoms given by a patient. 
The predictor takes in 5 symptoms to predict the ailment and also classifies the disease by corresponding specialization.

## Using Disease Predictor

To use the classifier, pass 5 symptoms as parameters to the hosted application as follows

 ```https://disease-detector.herokuapp.com/symptom1/symptom2/symptom3/symptom4/symptom5```

The output will be returned in the form of Doctor Specialization in order to maintain privacy of the patient.

## Integration 
The module is integrated with the Flutter app, using a simple ```http.get()``` call. The information is stored into the Firebase Firestore Database for future reference by the concerned doctor.

## Dataset

The dataset used for training can be found [here](https://www.kaggle.com/itachi9604/disease-symptom-description-dataset?select=dataset.csv)
