import yaml
import os
import time
import json
import logging
import base64




def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info("yaml file: {path_to_yaml} loaded successfully")
    return content
def create_directory(dirs: list):
    for dir_path in dirs:
        os.makedirs(dir_path,exist_ok = True)
        logging.info(f"directory is created at {dir_path}")
    return

def get_timestamp(name):
    timestamp= time.asctime().replace(" ","_").replace(":","_")
    unique_name = f"{name}_at_{timestamp}"
    return unique_name


def decodeImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())    
       
