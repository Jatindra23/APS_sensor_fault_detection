from sensor.exception import SensorException
import sys
from sensor.logger import logging


def test_exception():
    try: 
        logging.info("test case has started")
        a = 1/2
    except Exception as e:
        logging.exception(f"An error Occured {e}")
        raise SensorException(e,sys)
        


if __name__ == "__main__":
    try:
        test_exception()

    except Exception as e:
        print(e)