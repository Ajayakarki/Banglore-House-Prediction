import pickle
import json 
import numpy as np 

## Declearing the global variable
__locations = None
__data_columns = None
__model = None

def load_saved_artefacts():
    print("Loading artefacts")


    global __data_columns
    global __locations
    with open("./artefacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns'] ## Here ['data_columns'] is a key in columns.json file
        __locations = __data_columns[3:] ## After 3rd columns

    global __model
    if __model is None:
        with open("./artefacts/house_prediction_model.pickle", 'rb') as f:
            __model = pickle.load(f)

        print("Loading Complete")

    
def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns


def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower()) ## Since the __data columns is list so to find index we use .index function
    except:
        loc_index = -1
### We use try except because if element is not found then it throws an exception so to handle...

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2) ## round method set to 2 so that the number after the . is 2


if __name__ == '__main__':
    load_saved_artefacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))




