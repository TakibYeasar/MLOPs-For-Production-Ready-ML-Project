# from src.logger import logging
# from src.exception import USvisaException
# import sys

# logging.info("Welcome to our custom log...")

# try:
#     a=2/0
# except Exception as e:
#     raise USvisaException(e, sys)

from src.pipeline.training_pipeline import TrainPipeline

obj = TrainPipeline()
obj.run_pipeline()
