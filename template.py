import os
from pathlib import Path # for path issues
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

PROJECT_NAME = "coccidiosis_classifier"

LIST_FILES = [
    ".github/workflows/.gitkeep",
    "Dockerfile",
    "docker-compose.yml",
    "server.py",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/utils/__init__.py",
    "src/config/__init__.py",
    "src/config/configuration.py",
    "src/pipeline/__init__.py",
    "src/entity/__init__.py",
    "src/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/experiments/trials.ipynb",
    "init_setup.sh",
    "templates/index.html",
    "src//models/__init__.py",
    "src/controllers/__init__.py",
    "src/routes.py",
    "src/logging.py",
    ".env",
    "artifacts/test.json"
]

for file_path in LIST_FILES:
    file_path = Path(file_path)
    file_dir, file_name = os.path.split(file_path)

    # first make dir
    if file_dir!="":
        os.makedirs(file_dir, exist_ok= True)
        logging.info(f"Creating Directory: {file_dir} for file: {file_name}")
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Creating an empty file: {file_path}")
    else:
        logging.info(f"File already exists {file_path}")
        