import logging


class Loggen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="../Logs/automation.Logs", filemode='w',
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%d/%m%Y %I:%M:%S: %p")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
