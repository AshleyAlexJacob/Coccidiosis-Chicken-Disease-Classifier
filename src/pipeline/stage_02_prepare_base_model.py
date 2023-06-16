from src.components.prepare_base_model import PrepareBaseModel
from src.config.configuration import ConfigurationManager
from src.logging import logger

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config= prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
        obj = PrepareBaseModelPipeline()
        obj.main()
        logger.info(f">>>>>> Stage {STAGE_NAME} Completed ✅ <<<<<<")
    except Exception as e:
        logger.exception(e)
        