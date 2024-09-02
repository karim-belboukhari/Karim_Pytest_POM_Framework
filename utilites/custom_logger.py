import logging
import os

class LoggingGenerator:

    @staticmethod
    def log_gen():
        log_dir = os.path.join(os.path.dirname(__file__), '..', 'Logs')
        log_file = os.path.join(log_dir, 'automation.log')

        # Ensuring the Logs directory exists
        os.makedirs(log_dir, exist_ok=True)

        # here i Configure logger
        logging.basicConfig(
            filename=log_file,
            format='%(asctime)s: %(levelname)s: %(message)s',
            datefmt='%m/%d/%Y %I:%M:%S %p',
            level=logging.INFO
        )

        logger = logging.getLogger()
        return logger
