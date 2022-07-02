import pandas as pd
import matplotlib.pyplot as plt

def import_data(filepath):
    """
    This function takes in a filepath and returns a dataframe
    
    :param filepath: The path to the file you want to import
    :return: A dataframe
    """
    if '.csv' in filepath:
        data = pd.read_csv(filepath, on_bad_lines='skip',encoding = "ISO-8859-1") 
    elif '.xlsx' in filepath:
        data = pd.read_excel(filepath)
    else:
        print('Invalid File Format! Only .csv and .xlsx files are Accepted!')
    return data

def descriptive(data):
    return data.describe()

# Main Function
def Analysis(filepath):
    data = import_data(filepath=filepath)
    return data

if __name__ == "__main__" :

    pass
