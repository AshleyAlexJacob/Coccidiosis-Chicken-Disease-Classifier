from src.components.prepare_callback import PrepareCallbacks
from src.components.model_trainer import ModelTrainer
from src.config.configuration import ConfigurationManager
from src.logging import logger

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callback_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callback_list = prepare_callbacks.get_tb_ckpt_callbacks()
        # Model Training Section
        training_config = config.get_model_training_config()
        training = ModelTrainer(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train(
                callback_list=callback_list
            )



if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed ✅ <<<<<<")
    except Exception as e:
        logger.exception(e)
        