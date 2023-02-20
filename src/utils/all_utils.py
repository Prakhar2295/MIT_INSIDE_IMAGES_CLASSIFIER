import yaml
import os
import time
import json
import logging


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

import re
import base64

import numpy as np

from PIL import Image
from io import BytesIO


def base64_to_pil(img_base64):
    """
    Convert base64 image data to PIL image
    """
    image_data = re.sub('^data:image/.+;base64,', '', img_base64)
    pil_image = Image.open(BytesIO(base64.b64decode(image_data)))
    return pil_image


def np_to_base64(img_np):
    """
    Convert numpy image (RGB) to base64 string
    """
    img = Image.fromarray(img_np.astype('uint8'), 'RGB')
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return u"data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode("ascii")    
       
