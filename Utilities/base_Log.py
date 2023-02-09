import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig ( filename="Logs/testing_logs.log" ,
                              format='%(asctime)s: %(levelname)s: %(message)s' , datefmt='%m/%d/%Y %I:%M:%S %p' )
        logger = logging.getLogger ()
        logger.setLevel ( logging.INFO )
        return logger

    # formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s')
    # file_handler = logging.FileHandler("login_page.log")
    # # file_handler.setLevel(logging.INFO)
    # file_handler.setFormatter(formatter)
    # stream_handler = logging.StreamHandler()
    # stream_handler.setFormatter(formatter)
    # logger.addHandler(file_handler)
    # logger.addHandler(stream_handler)

