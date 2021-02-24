from flask import Flask, request
import json
from flask import jsonify
from constants import l1
import pickle


app = Flask(__name__)


# @app.route('/predict/<test>')
# def default(test):
#     return "Testing Flask App" + test


@app.route('/predict', methods=['GET'])
def main():
    # symptoms = []
    # symptoms.append(request.args.get('s1', None))
    # symptoms.append(request.args.get('s2',))
    # symptoms.append(request.args.get('s3'))
    # symptoms.append(request.args.get('s4'))
    # symptoms.append(request.args.get('s5'))

    print(request.args.get('s1'))

    # print(symptoms)

    # l2 = []
    # for x in range(0, len(l1)):
    #     l2.append(0)

    # for k in range(0, len(l1)):
    #     for z in symptoms:
    #         if(z == l1[k]):
    #             l2[k] = 1

    # infile = open('finalized_model.pickle', 'rb')
    # model = pickle.load(infile)
    # infile.close()

    # return jsonify(model.predict([l2]))


if __name__ == '__main__':
    app.run(debug=True)
