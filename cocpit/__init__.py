"""
COCPIT package:

Classification of Cloud Particle Imagery and Thermodynamics

modules:
-------

preprocess_sheets_with_text:
    - Extracts single images from the muliple images per frame or sheet
    - Saves single images to a directory for later creation of the database

pic: 'particle image classification'
    - Holds the main Image class for image manipulation using opencv 
    and calculates particle geometrical attributes 

build_ML_model:
    - Loads the prebuilt pytorch models
    see: https://pytorch.org/docs/stable/torchvision/models.html
    - Sets up the pytorch dataloaders based on cross fold validation or not
    - Takes into account all hyperparameters from __main__.py
    - Includes gpu support    

run_ML_model:
    -classifies good ice images through a convolutional neural network that
    was presaved or built in build_ML_model
    -transforms, makes predictions, and appends classification to dataframe 
    
train_ML_model:
    - Houses the execution of training the model for all epochs and batches 
    - Iterates through training and validation phases for specified CNN
    - Called in run_ML model
    - Writes accuracy and loss logs for each dataset (training and validation)
    - Returns classification report 

data_loaders:
    - Retrives data loaders from Pytorch for training and validation data
    - Appends path 
    - Called in run_ML_model
    
calculate_metrics:
    - outputs batch and epoch accuracy and losses to .csv's
    
classification_metrics:
    - calculation and plotting functions for reporting performance metrics from sklearn
    - precision, recall, f1, etc
    
plot:
    - plotting scripts for publication
    
"""

import cocpit.pic
import cocpit.process_png_sheets_with_text
import cocpit.data_loaders
import cocpit.build_ML_model
import cocpit.check_classifications
import cocpit.run_ML_model
import cocpit.train_ML_model
import cocpit.classification_metrics

# from os.path import dirname, basename, isfile, join
# import glob
# modules = glob.glob(join(dirname(__file__), "*.py"))
# __all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]
# from cocpit import *