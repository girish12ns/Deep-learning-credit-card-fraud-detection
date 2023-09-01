from flask import Flask,render_template,request
from flask import Flask, request, render_template
from src.card_fraud_detection.Pipeline.predictionPipeline import Prediction,Custom_data
import numpy as np

app = Flask(__name__)

@app.route('/')
def welcome():
     return render_template('index.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        data = Custom_data(
            transaction_dollar_amount=float(request.form['transaction_dollar_amount']),
            Long=float(request.form['Long']),
            Lat=float(request.form['Lat']),
            city=request.form['city'],
            state=request.form['state'],
            credit_card_limit=int(request.form['credit_card_limit'])
        )
        
        df = data.get_data_frame()
        print(df)

        prediction = Prediction()
        result = prediction.predict_data(df)
        print(result)
        
        final_result = np.where(result[0] > 0.5, 1, 0)
        
        return render_template('index.html', result=final_result)

if __name__=='__main__':
      app.run(host='0.0.0.0',port=8080)
