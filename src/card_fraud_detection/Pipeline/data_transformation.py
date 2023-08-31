from src.card_fraud_detection.config.configuration import Confuguration
from src.card_fraud_detection.component.data_ingestion import Dataingestion
from src.card_fraud_detection import logger
from src.card_fraud_detection.component.data_transformation import DataTransformation



class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            data_transformation=Confuguration()

            config=data_transformation.data_transformation_config()

            data_transformation=DataTransformation(config)

            x_train,y_train,x_test,y_test=data_transformation.data_transformation_initiated()
            
        except Exception as e:
            raise e