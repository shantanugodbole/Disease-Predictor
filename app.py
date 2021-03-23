from flask import Flask, request
import json
from flask import jsonify
from constants import l1
import pickle


app = Flask(__name__)

key = {0: 'Fungal infection', 1: 'Allergy', 2: 'GERD', 3: 'Chronic cholestasis', 4: 'Drug Reaction',
       5: 'Peptic ulcer diseae', 6: 'AIDS', 7: 'Diabetes ', 8: 'Gastroenteritis', 9: 'Bronchial Asthma', 10: 'Hypertension ',
       11: 'Migraine', 12: 'Cervical spondylosis',
       13: 'Paralysis (brain hemorrhage)', 14: 'Jaundice', 15: 'Malaria', 16: 'Chicken pox', 17: 'Dengue', 18: 'Typhoid', 19: 'hepatitis A',
       20: 'Hepatitis B', 21: 'Hepatitis C', 22: 'Hepatitis D', 23: 'Hepatitis E', 24: 'Alcoholic hepatitis', 25: 'Tuberculosis',
       26: 'Common Cold', 27: 'Pneumonia', 28: 'Dimorphic hemmorhoids(Piles)', 29: 'Heart attack', 30: 'Varicose veins', 31: 'Hypothyroidism',
       32: 'Hyperthyroidism', 33: 'Hypoglycemia', 34: 'Osteoarthristis', 35: 'Arthritis',
       36: '(Vertigo) Paroymsal  Positional Vertigo', 37: 'Acne', 38: 'Urinary tract infection', 39: 'Psoriasis',
       40: 'Impetigo'}


@app.route('/test/<test>')
def default(test):
    return "Testing Flask App" + test


@app.route('/predict/<s1>/<s2>/<s3>/<s4>/<s5>')
def predict(s1, s2, s3, s4, s5):
    symptoms = []
    symptoms.append(s1)
    symptoms.append(s2)
    symptoms.append(s3)
    symptoms.append(s4)
    symptoms.append(s5)
    # return s1
    l2 = []
    for x in range(0, len(l1)):
        l2.append(0)

    for k in range(0, len(l1)):
        for z in symptoms:
            if(z == l1[k]):
                l2[k] = 1

    infile = open('finalized_model.pickle', 'rb')
    model = pickle.load(infile)
    predicted = tuple(model.predict([l2]).tolist())
    # print(predicted)

    output = json.dumps(predicted[0])
    output = int(output)
    if output == 12 or output == 34 or output == 35:
        return "Orthopedist"
    elif output == 11 or output == 13 or output == 36:
        return "Neurologist"
    elif output == 5 or output == 8 or output == 28 or output == 38:
        return "General Surgery"
    elif output == 0 or output == 40 or output == 37 or output == 39:
        return "Dermatologist"
    elif output == 9 or output == 25 or output == 27 or output == 29:
        return "Pulmonologist"
    else:
        return "Physician"
    infile.close()


if __name__ == '__main__':
    app.run(debug=True)
