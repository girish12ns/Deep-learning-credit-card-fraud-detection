from src.card_fraud_detection.config.configuration import Confuguration
from src.card_fraud_detection.component.data_ingestion import Dataingestion
from src.card_fraud_detection import logger
from src.card_fraud_detection.component.data_transformation import DataTransformation
from src.card_fraud_detection.component.Model_trainer import Model_trainer



class Model_trainerPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            trainer_config=Confuguration()
            config=trainer_config.get_model_trainer_config()

            data_trans=DataTransformation(config=config)
            x_train,y_train,x_test,y_test=data_trans.data_transformation_initiated()



            model_trainer=Model_trainer(config=config)

            histroy=model_trainer.model_trainer_initiated(x_train=x_train,x_test=x_test,y_train=y_train,y_test=y_test)

        except Exception as e:
            raise e