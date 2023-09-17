import pickle
import sklearn
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__, static_folder='static')

@app.route('/index1')
def home():
    return render_template('index1.html')

@app.route('/details') # rendering the html template
def index() :
    return render_template('details.html')

@app.route('/result', methods=['GET','POST'])
def submit() :
    # loading model which we saved
    gender= float(request.form['gender'])
    educationlevel= float(request.form['educationlevel'])
    institution= float(request.form['institution'])
    it= float(request.form['it'])
    financial= float(request.form['financial'])
    internet= float(request.form['internet'])
    network = float(request.form['network'])
    device= float(request.form['device'])
    

    prediction =model.predict(pd.DataFrame([[gender,educationlevel,institution,it,financial,internet,network,device]], columns= ['gender', 'educationlevel', 'institution', 'it', 'financial', 'internet','network','device']))
    
    print(prediction)
    if (prediction == 0):
        return render_template("output.html",result ="Adaptivity Level is High")
    elif (prediction == 1):
        return render_template("output.html",result ="Adaptivity Level is medium") 
    else:
        return render_template("output.html",result = "Adaptivity Level is Low")
    
    
    return render_template('Crop_predict.html', prediction_text ="{}".format(prediction))



if __name__ == '__main__':
    app.run()
