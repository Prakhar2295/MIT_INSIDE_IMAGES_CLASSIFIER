import argparse
import os
import logging
import io
from tqdm import tqdm
from sklearn.metrics import confusion_matrix,classification_report,mean_absolute_error,mean_squared_error,r2_score
from src.utils.data_management import train_valid_generator
from src.utils.all_utils import create_directory, read_yaml
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing import image
import pandas as pd
import json



logging_str = "[%(asctime)s: %(levelname)s: %(module)s]: %(message)s"
log_dir= "logs"
os.makedirs(log_dir,exist_ok = True)
logging.basicConfig(filename=os.path.join(log_dir,"running_logs.log"),
level=logging.INFO, format = logging_str,filemode= "a")

def evaluate_model(config_path,params_path):
    config = read_yaml(config_path)
    params = read_yaml(params_path)

    artifacts = config["artifacts"]

    artifacts_dir = config["artifacts"]["ARTIFACTS_DIR"]

    data_dir = config["artifacts"]["DATA_DIR"]
    trained_model_dir = config["artifacts"]["TRAINED_MODEL_DIR"]

    data_fir_path = os.path.join(artifacts_dir, data_dir)
    trained_model_dir_path = os.path.join(artifacts_dir,trained_model_dir)

    trained_model_filename = config["artifacts"]["TRAINED_MODEL_FILENAME"]

    trained_model_file_path = os.path.join(artifacts_dir,trained_model_dir,trained_model_filename)


    model =load_model(trained_model_file_path)

    train_generator,valid_generator = train_valid_generator(
        data_dir= artifacts["DATA_DIR"],
        IMAGE_SIZE=tuple(params["IMAGE_SIZE"][:-1]),
        BATCH_SIZE=params["BATCH_SIZE"],
        do_data_augmentation=params["AUGMENTATION"]
    )

    test_image = image.load_img('data/airport_inside/airport_inside_0001.jpg', target_size = (224,224))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = model.predict(test_image)
    train_generator.class_indices
    if  result[0][0] ==1:
        prediction = "airport_inside"
        print(prediction)
    elif result[0][1] == 1:
        prediction = "artstudio"
        print(prediction)
            
    elif result[0][2] == 1:
        prediction = "auditorium"
        print(prediction)
    else:
         print('Negative number')
       

    



    
               
    
    

        


   
    

if __name__ == "__main__":
    args = argparse.ArgumentParser()

    args.add_argument("--config","-c",default ="config/config.yaml")
    args.add_argument("--params","-p",default ="params.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(">>> Stage 05 started")
        evaluate_model(config_path = parsed_args.config, params_path= parsed_args.params)
        logging.info(">>> stage 05 completed! training is done >>>>>\n")
    except Exception as e:
        logging.exception(e)
        raise e




