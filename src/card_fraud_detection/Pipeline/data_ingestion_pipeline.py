from src.card_fraud_detection.config.configuration import Confuguration
from src.card_fraud_detection.component.data_ingestion import Dataingestion
from src.card_fraud_detection import logger


class data_ingestionPipeline:
    def __init__(self):
        pass


    def main(self):
        data_ingestion_config=Confuguration()

        config=data_ingestion_config.get_data_ingestion_config()
    
        data_ingestion=Dataingestion(config)

        train_set,test_set=data_ingestion.get_data()




