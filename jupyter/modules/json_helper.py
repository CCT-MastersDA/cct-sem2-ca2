"""
json_helper.py

This file contains the definition of the JSON class,
which was implemented to handle JSON files in this project.

This class was implemented as a module to avoid code duplicate and for easier reference.
"""
# importing modules
import json
import logging

# use a logger to help debugging
logger = logging.getLogger('json_helper_logger')

# set logger level
logger.setLevel(logging.ERROR)

class JsonHelper:
    '''
    This class handles JSON data types.
    
    Attributes:
        json_data  (dict): Dictionary to be manipulated as JSON.
    '''
    json_data = {}
    
    def __init__(self, json_data):
        '''
        The constructor for JsonHelper class.

        Parameters:
            json_data (dict): Dictionary to be manipulated as JSON.
        '''
        self.json_data = json_data

    def to_file(self, outfile):
        '''
        Auxiliary method to save the json into a file.

        Parameters:
            outfile (str): Full file path.
        '''
        if len(outfile) == 0:
            logger.warning('Output filename is empty!')
            return

        with open(outfile, 'w', encoding='utf-8') as f:
            json.dump(self.json_data, f, ensure_ascii=False, indent=4)

    def to_string(self):
        '''
        Auxiliary method to return the string version of the json data.
        '''
        return json.dumps(self.json_data, indent=4, sort_keys=True, ensure_ascii=False)