import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle
import jinja2
from flask_cors import CORS,cross_origin


app=Flask(__name__)
cors=CORS(app)
model=pickle.load(open("trained_model.sav",'rb'))
data=pd.read_excel("Book4.xlsx")


@app.route('/')
def index():
    region = sorted(data['region'].unique())
    age = sorted(data['age'].unique())
    sex = sorted(data['sex'].unique(), reverse=True)
    size = data['size'].unique()
    return render_template('a.html',region=region,sex=sex,age=age,size=size)

@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
        region = request.form.get('region')

        sex = request.form.get('sex')
        age= (request.form.get('age'))
        size = request.form.get('size')


        prediction = model.predict(pd.DataFrame(columns=['region', 'sex', 'age', 'size'],
                                                data=np.array(
                                                    [region, sex, age, size, ]).reshape(1, 4)))

        # prediction = model.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
        #                                          columns=['name', 'company', 'year','kms_driven', 'fuel_type']))
        return str(np.round(prediction[0]))

if __name__ == "__main__":
        app.run(debug=True)

# @app.route('/predict', methods=['POST'])
# def predict():
#     int_features = [int(x) for x in request.form.values()]
#     final_features = [np.array(int_features)]
#     prediction = model.predict(final_features)
#     output = round(prediction[0], 2)
#     return render_template('index.html', prediction_text='Employee Salary should be $ {}'.format(output))
#
# if __name__ == "__main__":























