import json
import random
from collections import OrderedDict

DICTIONARY_FILENAME = "./dictionary.json"

with open(DICTIONARY_FILENAME) as json_file:
  dictionary = json.load(json_file)

def find_random_expression(level):
  total_entries = len(dictionary)
  return dictionary[random.randint(0, total_entries - 1)]["expression"]

def definition(expression, keyword):
  matching_definitions = list(filter(lambda entry: expression in entry["expression"], dictionary))
  if keyword:
    matching_definitions = list(filter(lambda entry: keyword_matches(entry, keyword), matching_definitions))
  return matching_definitions

def keyword_matches(entry, keyword):
  return (
    keyword in entry["context"] or 
    keyword in entry["meaning"] or 
    keyword in entry["example"] or 
    keyword in entry["extra"] or 
    keyword in entry["keywords"]
  ) 

def update_score(expr, value):
  matching_index = [dictionary.index(entry) for entry in dictionary if entry["expression"] == expr][0]
  dictionary[matching_index]["score"] = dictionary[matching_index]["score"] + value
  save_dictionary(dictionary)

def print_dictionary_entries(entries):
  print('\n')
  for e in entries:
    print ('  Expression:  %s  ' %(e["expression"].capitalize()))
    print ('  Context:  %s  ' %(e["context"]))
    print ('  Meaning:  %s  ' %(e["meaning"]))
    print ('  Example:  %s  ' %(e["example"]))
    print('\n')

def save_dictionary(dictionary):
  ordered_dict = list(map(lambda entry: OrderedDict(
    [
      ("expression", entry["expression"]),
      ("context", entry["context"]),
      ("meaning", entry["meaning"]),
      ("example", entry["example"]),
      ("extra", entry["extra"]),
      ("keywords", entry["keywords"]),
      ("score", entry["score"]),
    ]
  ), dictionary))
  with open(DICTIONARY_FILENAME, 'w') as file:
    json.dump(ordered_dict, file, indent=4)

## Al final de test, VOLVER A ESCRIBIR el JSON en el archivo
