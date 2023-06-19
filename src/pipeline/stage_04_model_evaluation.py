from src.config.configuration import ConfigurationManager
from src.components.model_evaluation import ModelEvaluation
from src.logging import logger




STAGE_NAME = "Model Evaluation stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        val_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(val_config)
        evaluation.evaluate_model()
        evaluation.save_scores()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed  ✅ <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
            