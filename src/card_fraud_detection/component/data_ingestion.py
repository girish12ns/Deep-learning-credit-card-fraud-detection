import pandas as pd
from sklearn.model_selection import train_test_split


class Dataingestion:
    def __init__(self,config):
        self.config = config

    def get_data(self):

        df=pd.read_csv(self.config.source_dir)

        train_df,test_df= train_test_split(df,test_size=0.2,random_state=42)

        train_df.to_csv(self.config.train_dir,header=True,index=False)

        test_df.to_csv(self.config.test_dir,header=True,index=False)

        return (self.config.train_dir,
                self.config.test_dir)