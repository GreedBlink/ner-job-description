import json
from unidecode import unidecode


def load_data(filename:str)->dict:
    """_summary_

    Args:
        filename (str): _description_

    Returns:
        _type_: _description_
    """

    with open(filename, 'r', encoding="utf-8") as outfile:
        data = json.load(outfile)

    return data



def save_data(object, filename:str)->None:
    """_summary_

    Args:
        object (_type_): _description_
        filename (str): _description_

    Returns:
        _type_: _description_
    """

    with open(filename,'w') as outfile:
        json.dump(object,outfile,indent=4)
    
    return None



