import json
import pandas as pd
from pprint import pprint
from cleantext import clean
from unidecode import unidecode
from utils.utils import save_data


def custom_clean(text: str)-> str:
    output = clean(
        text,
        no_emoji=True,
        lower=True, 
        no_punct=True,
        replace_with_punct=""
        )
    return output



def prep_taxonomie(skills:list)->list:
    

    text = unidecode(skills)
    text = (
        text
        .lower()
        .replace("(programming language)", "")
        .replace("(python package)", "")
        .replace("(r package)", "")
        .replace("(.net library)", "")
        .replace("(neural network library)", "")
        .replace("(c++ library)", "")
        .replace("(software library)", "")
        .replace("(java library)", "")
        .replace("(biochemical algorithms library)", "")
        .replace("(c standard library)", "")
        .replace("(js library)", "")
        .replace("(machine learning library)", "") 
        .replace("imaging libraries", "")
        .replace("(version control system)","") 
        .strip()
    )

    
    return text 


with open('./scrap/output/remotar.json', 'r',encoding='utf-8') as file:
    remotar_jobs = json.load(file)
final_jobs = []

for item in remotar_jobs:
    item_prep = {
        "title": item['title'] ,
        "description": item['description'],
        "source": 'remotar'
    }
    final_jobs.append(item_prep)

with open('./scrap/output/catho_jobs.jl','r', encoding = 'utf-8') as file:
    catho_jobs = pd.read_json(file,lines =True)
    catho_jobs = catho_jobs.to_dict(orient='records')



for item in catho_jobs:
    item_prep = {
        "title": item['title'] ,
        "description": item['description'],
        "source": 'catho'
    }
    final_jobs.append(item_prep)



with open('./experiment/data/jobs.json','w') as file:
    json.dump(final_jobs,file,indent=4)

# tax
tax_hard_skill = pd.read_csv('./taxonomies/output/hard-skills-taxonomy.csv')
tax_soft_skill = pd.read_csv('./taxonomies/output/soft-skills-taxonomy.csv')


tax_output = {}
tax_output['soft-skill'] = list(set(tax_soft_skill['soft skills'].tolist()))
tax_output['hard-skill'] = list(set(tax_hard_skill['name'].tolist()))

for tax in tax_output.keys():
    print(tax)
    tax_output[tax] = [prep_taxonomie(skill) for skill in  tax_output[tax]]

save_data(object = tax_output, filename='data/taxonomies.json')