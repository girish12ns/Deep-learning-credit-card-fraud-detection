import os
import pandas as pd
from pathlib import  Path
from src.card_fraud_detection.utilis.commmon import load_model


class Prediction:
    def __init__(self):
        pass

    def predict_data(self,features):
        model_path=Path('artifacts\model_trainer\model.pkl')
        processor_path=Path('artifacts\data_transformations\preprocessor.pkl')
        model=load_model(model_path)
        preprocessor=load_model(processor_path)
        scaled_data=preprocessor.transform(features)
        result=model.predict(scaled_data)
        return result






class Custom_data:
    def __init__(self,transaction_dollar_amount,Long,Lat,city,state,credit_card_limit):
        self.transaction_dollar_amount=transaction_dollar_amount
        self.Long=Long
        self.Lat=Lat
        self.city=city
        self.state=state
        self.credit_card_limit=credit_card_limit,
        

    def get_data_frame(self):
        custom_data={
            'transaction_dollar_amount':self.transaction_dollar_amount,
            'Long':self.Long,
            'Lat':self.Lat,
            'city':self.city,
            'state':self.state,
            'credit_card_limit':self.credit_card_limit
        }
        df=pd.DataFrame(custom_data)
        return df