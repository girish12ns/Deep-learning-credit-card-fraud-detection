from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,Activation
import tensorflow as tf
import pandas as pd
from src.card_fraud_detection.utilis.commmon import save_model
 




class Model_trainer:
    def __init__(self,config):
        self.config=config

    def get_data_trainer(self):
        x_train=pd.read_csv(self.config.train_dr)


        model=Sequential()
        model.add(Dense(64,activation='relu',input_dim=x_train.shape[1]))
        model.add(Dense(64,activation='relu'))
        model.add(Dense(1,activation='sigmoid'))

        model.compile(optimizer='adam',loss=tf.keras.losses.BinaryCrossentropy(),metrics=tf.keras.metrics.Recall(
        thresholds=None, top_k=None, class_id=None, name=None, dtype=None))
        return model

    def model_trainer_initiated(self,x_train,y_train,x_test,y_test):
        model=self.get_data_trainer()
        histroy=model.fit(x_train,y_train,batch_size=120,epochs=30)

        save_model(filepath=self.config.model_dir,obj=model)
        return histroy