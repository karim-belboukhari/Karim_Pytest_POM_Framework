import logging

class Logenerator:
    
    def log_gen():
        logging.basicConfig(filename=".\\karim.belboukhari\\Project51\\Logs\\automation.log",
        format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger