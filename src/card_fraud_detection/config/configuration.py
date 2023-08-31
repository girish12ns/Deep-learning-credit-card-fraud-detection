from src.card_fraud_detection.utilis.commmon import create_directories
from src.card_fraud_detection.utilis.commmon import read_yaml
from src.card_fraud_detection.constants import config_file_path,params_file_path
from src.card_fraud_detection.entity import DataingestionConfig,DataTransformationConfig,Model_trainerConfig


class Confuguration:
    def __init__(self,confi_path=config_file_path,params_path=params_file_path):
        self.config=read_yaml(confi_path)
        self.params=read_yaml(params_path)

        create_directories([self.config.Artifacts])

    def get_data_ingestion_config(self)->DataingestionConfig:
        data_ingestion=self.config.Data_ingestion
        

        create_directories([data_ingestion.root_dir])
      
        data_ingestion=DataingestionConfig(
            root_dir=data_ingestion.root_dir,
            source_dir=data_ingestion.source_dir,
            train_dir=data_ingestion.train_dir,
            test_dir =data_ingestion.test_dir
        )
        return data_ingestion
    def data_transformation_config(self)->DataTransformationConfig:
        transformation=self.config.data_transformation
        ingestion=self.config.Data_ingestion

        create_directories([transformation.root_dir])

        data_transformation=DataTransformationConfig(
            root_dir=transformation.root_dir,
            processor_dir=transformation.processor_dir,
            train_dir=ingestion.train_dir,
            test_dir=ingestion.test_dir

        )
        return data_transformation
    
    def get_model_trainer_config(self)->Model_trainerConfig:
        trainer=self.config.Model_trainer
        ingestion =self.config.Data_ingestion

        create_directories([trainer.root_dir])

        trainer=Model_trainerConfig(
            root_dir=trainer.root_dir,
            model_dir=trainer.model_dir,
            train_dir=ingestion.train_dir,
            test_dir=ingestion.test_dir
        )
        return trainer
    
    def get_model_trainer_config(self)->Model_trainerConfig:
        trainer=self.config.Model_trainer
        ingestion =self.config.Data_ingestion
        transformation=self.config.data_transformation

        create_directories([trainer.root_dir])

        trainer=Model_trainerConfig(
            root_dir=trainer.root_dir,
            model_dir=trainer.model_dir,
            train_dir=ingestion.train_dir,
            test_dir=ingestion.test_dir,
            processor_dir= transformation.processor_dir
        )
        return trainer

    

