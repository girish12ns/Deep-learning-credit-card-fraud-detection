import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s - %(message)s]')

project_name='card_fraud_detection'



list_files=[
    ".github/workflows/.gitkeep",
    "src/{}/component/__init__.py".format(project_name),
    "src/{}/utilis/__init__.py".format(project_name),
    "src/{}/utilis/commmon.py".format(project_name),
    "src/{}/config/__init__.py".format(project_name),
    "src/{}/config/configuration.py".format(project_name),
    "src/{}/Pipeline/__init__.py".format(project_name),
    "src/{}/entity/__init__.py".format(project_name),
    "src/{}/constants/__init__.py".format(project_name),
    "src/{}/__init__.py".format(project_name),
    "config/config.yaml",
    "dvc.yaml",
    "requirements.txt",
    "params.yaml",
    "setup.py",
    "research/trails.ipynb",
    "main.py",
    "templates/index.html",
    "templates/homepage.html"
]

for filename in list_files:
    filepath=Path(filename)
    
    fildir,file=os.path.split(filepath)

    if fildir!="":
        os.makedirs(fildir,exist_ok=True)

        logging.info("basic directory created")

    if (not os.path.exists(filepath)):
        
        with open(filepath,"w") as f:

            logging.info("files are created")
         

            pass


