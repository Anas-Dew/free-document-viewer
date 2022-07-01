import pandas as pd
import matplotlib.pyplot as plt

def import_data(filepath):
    if '.csv' in filepath:
        data = pd.read_csv(filepath, on_bad_lines=False) 
        #changed pd.read to pd.read_csv because pandas doesnt have any attrebute 'read'
        # and there was an error of tokenizing while reading csv files so i added this error_bad_lines = false
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
