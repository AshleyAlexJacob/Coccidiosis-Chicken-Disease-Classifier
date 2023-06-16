"""
        Main Entry Point of the Project
        For testing the pipeline
"""

from src.logging import logger
from src.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage_02_prepare_base_model import PrepareBaseModelPipeline
from src.pipeline.stage_03_model_training import ModelTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed ✅ <<<<<<")
except Exception as e:
        logger.exception(e)

# =======================================================================

STAGE_NAME = "Prepare Base Model Stage"
try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed ✅ <<<<<<")
except Exception as e:
        logger.exception(e)
    

# =======================================================================

STAGE_NAME = "Model Training Stage"
try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed ✅ <<<<<<")
except Exception as e:
        logger.exception(e)
