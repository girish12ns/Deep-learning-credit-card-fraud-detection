import logging
import os
import sys

loging_str='[%(asctime)s: %(levelname)s: %(module)s: %(message)s]'

logs='LOGS'
file_path=os.path.join(logs,'current_logs.log')

os.makedirs(logs,exist_ok=True)


logging.basicConfig(
    level=logging.INFO,
    format=loging_str,

     handlers=[
        logging.FileHandler(file_path),
        logging.StreamHandler(sys.stdout)]
)

logger=logging.getLogger("card_detection")