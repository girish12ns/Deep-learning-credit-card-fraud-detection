from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
import pandas as pd
from src.card_fraud_detection.utilis.commmon import save_model


class DataTransformation:
    def __init__(self,config):
        self.config = config

    def get_the_data_transformation(self):

        cat_features =['city','state']
        numerical_features= ['transaction_dollar_amount','Long','Lat','credit_card_limit']

        num_pip=Pipeline(steps=[
            ('impueter',SimpleImputer(strategy='mean')),
            ('scaler',StandardScaler())])
        cat_pip=Pipeline(steps=[
            ('impueter',SimpleImputer(strategy='most_frequent')),
            ('coder',OneHotEncoder())
            ])
        preprocessor=ColumnTransformer([
            ('num_pip',num_pip,numerical_features),
            ('cat_pip',cat_pip,cat_features)])
        
        return preprocessor
    
    def data_transformation_initiated(self,):

     

        train_df=pd.read_csv(self.config.train_dir)

        test_df=pd.read_csv(self.config.test_dir)

        train_df.dropna()  #dropping the null values

        test_df.dropna() #dropping the null values

        train_df.drop(['zipcode','date','credit_card'],axis=1,inplace=True)

        test_df.drop(['zipcode','date','credit_card'],axis=1,inplace=True)

        target_feature=['Is_fraud']

        x_train,y_train,x_test,y_test = (train_df.iloc[:,:-1],train_df[target_feature],test_df.iloc[:,:-1],test_df[target_feature])

        preprocessor= self.get_the_data_transformation()

        x_train=preprocessor.fit_transform(x_train)

        x_test= preprocessor.transform(x_test)



        x_train=x_train.toarray() #convert to array from sparse matrix

        x_test= x_test.toarray() #convert to array from sparse matrix

        
        save_model(filepath=self.config.processor_dir,obj=preprocessor)

        return(x_train,y_train,x_test,y_test)


