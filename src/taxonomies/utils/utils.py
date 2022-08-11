
import json
from cleantext import clean
from unidecode import unidecode

def save_data(object, filename:str):
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




def load_data(filename:str)->dict:
    """_summary_

    Args:
        filename (str): _description_

    Returns:
        dict: _description_
    """

    with open(filename, 'r', encoding="utf-8") as outfile:
        data = json.load(outfile)

    return data

def prep_taxonomie(skills:list)->list:
    """_summary_

    Args:
        skills (list): _description_

    Returns:
        list: _description_
    """
    output = []
    for item in skills:
        text = unidecode(item)
        text = text.lower().strip()
        output.append(text)
        
    return output 



def custom_clean(text: str)-> str:
    output = clean(
        text,
        no_emoji=True,
        lower=True, 
        no_punct=True,
        replace_with_punct="",
        lang = 'pt'
        )
    return output