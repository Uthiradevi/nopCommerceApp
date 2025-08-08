
import logging
import os

class LogGen:

    @staticmethod
    def loggen():
        log_folder = os.path.join(os.path.dirname(__file__), '../Logs')
        os.makedirs(log_folder, exist_ok=True)
        log_file = os.path.join(log_folder, 'customLogger.log')
        logger = logging.getLogger("customLogger")
        logger.setLevel(logging.INFO)
        if not logger.handlers:
            file_handler = logging.FileHandler(log_file)
            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        return logger



