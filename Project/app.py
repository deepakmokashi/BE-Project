from flask import Flask, render_template, request
from mylib.preprocessing import predict_career
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('career_prediction.pickle', 'rb'))

app = Flask(__name__)


@app.route('/')
def man():
    return render_template('dashboard.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/profile')
def profilepage():
    return render_template('Profile.html')

@app.route('/contact')
def Contactpage():
    return render_template('contactus.html')

@app.route('/explore')
def explore():
    return render_template('explore.html')

@app.route('/predict', methods=['POST','GET'])
def home():
    career_choice = ""
    data1 = int(request.form.get('problemsolvingskills'))
    data2 = int(request.form.get('analyticalskills'))
    data3 = int(request.form.get('Logicalskills'))
    data4 = int(request.form.get('responsbility'))
    data5 = int(request.form.get('mathscore'))
    data6 = int(request.form.get('nata'))
    data7 = int(request.form.get('biology'))
    data8 = int(request.form.get('reasoningskills'))
    data9 = int(request.form.get('Negotiation Skills'))
    data10 = int(request.form.get('lang'))
    data11 = int(request.form.get('expansive'))
    data12 = int(request.form.get('Assurity'))
    data13 = int(request.form.get('niftskills'))
    data14 = int(request.form.get('typography'))
    data15 = int(request.form.get('critical'))
    data16 = int(request.form.get('neet'))
    data17 = int(request.form.get('expriemental'))
    data18 = int(request.form.get('communication'))
    data19 = int(request.form.get('pcm'))
    data20 = int(request.form.get('coding'))
    data21 = int(request.form.get('sciscore'))
    data22 = int(request.form.get('diagnostic'))
    data23 = int(request.form.get('literature'))

    data24 = (request.form.get('mentalc'))
    data25 = (request.form.get('prescription'))
    data26 = (request.form.get('careanimal'))
    data27 = (request.form.get('likeanimal'))
    data28 = (request.form.get('others'))
    data29 = (request.form.get('verbalcom'))
    data30 = (request.form.get('teamwork'))
    data31 = (request.form.get('preference'))
    data32 = (request.form.get('conlearning'))
    data33 = (request.form.get('patience'))
    data34 = (request.form.get('memoryskills'))
    data35 = (request.form.get('budget'))
    data36 = (request.form.get('research'))
    data37 = (request.form.get('workinteam'))
    data38 = (request.form.get('selflearning'))

    arr = [[data1,data2,data3,data4,data5,data6,data7,data8,
    data9,data10,data11,data12,data13,data14,data15,data16,
    data17,data18,data19,data20,data21,data22,data23,data24,
    data25,data26,data27,data28,data29,data30,data31,data32,
    data33,data34,data35,data36,data37,data38]]

    df = predict_career(arr)
    op_array = model.predict(df)
    op_array = op_array.tolist()
    temp = op_array[0]
    choice = temp.index(1.0)
    dist = {1:'Architecure', 2: 'BCS/BCA',
            3:'BSC', 4:'BVSc',5:'Engineering', 
            6:'Interior Design',7:'Medical', 
            8:'Pharmacy'}
    career_choice = dist[choice+1] 
    print(career_choice)
    return render_template('after.html', data=career_choice)


if __name__ == "__main__":
    app.run(debug=True)