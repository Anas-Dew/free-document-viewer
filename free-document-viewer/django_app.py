import pandas as pd

def import_data(filepath):

    # Checking if the file is a csv or xlsx or xls file. If it is, it will read the file. If not, it will
    # return an error message.
    if '.csv' in filepath:
        data = pd.read_csv(filepath, on_bad_lines='skip',encoding = "ISO-8859-1") 
    elif '.xlsx' in filepath:
        data = pd.read_excel(filepath)
    elif '.xls' in filepath:
        return "<h3>Currently file not supported. Come back soon...</h3>"
    else:
        pass
        # return "<h3>File not supported.</h3>"
    return data


# Main Function
def Analysis(filepath):
    data = import_data(filepath=filepath)
    return data

if __name__ == "__main__" :

    pass
