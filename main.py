from src.card_fraud_detection.Pipeline.data_ingestion_pipeline import data_ingestionPipeline
from src.card_fraud_detection.Pipeline.data_transformation import DataTransformationPipeline
from src.card_fraud_detection.Pipeline.data_trainer import Model_trainerPipeline
from src.card_fraud_detection import logger

try:
    ingestion=data_ingestionPipeline()
    ingestion.main()

    logger.info("Data_ingestion has been  completed")


except Exception as e:
    raise e

try:
    ingestion=DataTransformationPipeline()
    ingestion.main()

    logger.info("Data_transformation has been  completed")


except Exception as e:
    raise e


try:
    trainer=Model_trainerPipeline()
    ingestion.main()

    logger.info("Model_training completed has been  completed")


except Exception as e:
    raise e



