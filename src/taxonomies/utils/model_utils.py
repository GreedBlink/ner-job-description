from spacy.pipeline import EntityRuler
from spacy.lang.pt import Portuguese


def make_traing_data(tax:list, type:str)->list:
    """_summary_

    Args:
        tax (list): _description_
        type (str): _description_

    Returns:
        list: _description_
    """
    
    patterns = []
    for item in tax:
        pattern = {
            "label": type,
            "pattern": item
        }
        patterns.append(pattern)
    return patterns


def test_model(model, text):
    doc = model(text)
    results = []
    for ent in doc.ents:
        if len(ent.text) > 1:
            results.append(ent.text)
    return results

def generate_rules(patterns:list, model_name:str):

    #nlp = spacy.load('pt_core_news_sm')
    nlp = Portuguese()
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(patterns)
    nlp.to_disk(model_name)