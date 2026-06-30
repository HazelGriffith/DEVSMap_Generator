import json
import os
from abc import ABC, abstractmethod

class DEVSMap_Generator(ABC):
    
    '''
    Initializes every DEVSMap Generator with the empty DEVSMap dictionary and the given model's name
    '''
    def __init__(self, model_name: str):
        
        self.model_devsmap_dict = {model_name: {"s": {}, "x": {}, "y": {}, "delta_int": {}, "delta_ext": {}, "delta_con": {}, "lambda": {}, "ta": {}, "include_sets": [], "parameters": {}}}
        
        self.model_name = model_name
            
    '''
    Parse state variables and store them in "s" dictionary
    '''
    @abstractmethod
    def getStateVariables(self):
        pass
    
    '''
    Parse input ports and store them in "x" dictionary
    '''
    @abstractmethod
    def getInputPorts(self):
        pass
    
    '''
    Parse output ports and store them in "y" dictionary
    '''
    @abstractmethod
    def getOutputPorts(self):
        pass
    
    '''
    Parse internal transition function and store as "delta_int" dictionary
    '''
    @abstractmethod
    def getInternalTransition(self):
        pass
    
    '''
    Parse external transition function and store as "delta_ext" dictionary
    '''
    @abstractmethod
    def getExternalTransition(self):
        pass
    
    '''
    Parse confluence transition function and store as "delta_con" dictionary
    '''
    @abstractmethod
    def getConfluenceTransition(self):
        pass
    
    '''
    Parse output function and store as "lambda" dictionary
    '''
    @abstractmethod
    def getOutput(self):
        pass
    
    '''
    Parse time advance function and store as "ta" dictionary
    '''
    @abstractmethod
    def getTimeAdvance(self):
        pass
    
    '''
    load your model data however is necessary
    '''
    @abstractmethod
    def loadFile(self):
        pass
    
    '''
    Saves the model devsmap dictionary as a json file.
    If one already exists it is deleted and replaced
    @param save_folder_path is a string path to the destination folder
    @param file_name is a string name of the file being saved without an extension
    '''
    def saveDEVSMap(self, save_folder_path: str, file_name: str):
        try:
            with open(f"{save_folder_path}{file_name}.json", 'x') as devsmapfile:
                json.dump(self.model_devsmap_dict, devsmapfile)
                
        except Exception as e:
            os.remove(f"{save_folder_path}{file_name}.json")
            self.saveDEVSMap(save_folder_path, file_name)

    '''
    Controls the execution flow of parsing data, storing it in the right format, and then saving as a DEVSMap JSON file
    '''
    def convertToDEVSMap(self, save_folder_path:str, file_name:str):
        # Parse values and store them in devsmap dictionary
        self.getStateVariables()
        self.getInputPorts()
        self.getOutputPorts()
        self.getInternalTransition()
        self.getExternalTransition()
        self.getConfluenceTransition()
        self.getOutput()
        self.getTimeAdvance()
        
        # save completed devsmap dictionary as a JSON file 
        self.saveDEVSMap(save_folder_path, file_name)
        
        
        
        
        