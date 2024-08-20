from flask import Flask,request,jsonify,render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

appplication = Flask(__name__)
app=appplication

#import ridge regressor and standrad scaler
ridge_model=pickle.load(open('ridge.pk1','rb'))
standrad_scaler=pickle.load(open('scaler.pk1','rb'))


@app.route("/result_data")#'/home',methods= ['GET','POST'])
def index():
    #print("FUNCTION CALLED")
    return render_template('index.html')

@app.route('/predict_data',methods=['GET','POST'])
def predict_datapoints():
    if request.method=='POST':
        Temprature=float(request.form.get('Temprature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        
        
        new_data_scaled=standrad_scaler.transform([[Temprature,RH,Ws,Rain,FFMC,DMC,ISI,Classes,Region]])
        result=ridge_model.predict(new_data_scaled)
        
        
            
        # pass
        print("IF CONDITION0--------------------------------------------",request.form)
        #a= 10
        return render_template('index.html',results=result)
    else:
        print("ELSE CONDITIONS------------------------------------------")
        return render_template('home.html')
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')