import logging  

def test_logging_demo():
    logger = logging.getLogger(__name__)


    filehandler = logging.FileHandler('logfile.log')

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    
    filehandler.setFormatter(formatter)

    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)

    logger.info("info about the case")

    logger.debug(" a debug statement is executed")

    logger.warning("something is in waring mode")

    logger.error("A major error has occured")

test_logging_demo()