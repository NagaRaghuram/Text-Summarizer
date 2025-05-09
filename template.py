import os
from pathlib import Path 
import logging #Because I want to log all the information

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name = "Text Summarizer"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  #Components,utils, logging, config, pipeline, entity, constants==Folder
    f"src/{project_name}/utils/__init__.py",       #after the folder names known to be files in src
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)   #if you already have folder, it won't create it again. If its not there, it will print.
        logging.info(f"Created directory: {filedir} for the file {filename}")  #log the information to a file.

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): #if file size is 0 then we create the file
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filepath} already exists.")