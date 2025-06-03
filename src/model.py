#ml matching logic
'''
model.py

this module is focused on the computation of the parser attribute field. uses ml based model to determine what university
the text field is and cleans the original text entry with the standardized university name
'''

#TODO: implement model logic

def match_uni_name(raw_uni_name: str, model, canonical_names: list[str], canonical_embedding) -> tuple[str, float]:

'''
design thoughts
-function call in parser.py
-takes in the specific text-field as free text
-preprocesses the name
-analyzes this field through the model
-compars input against a list of standardize university names
Returns:
    -best matching standardized name (string)
    -confidence score (float)
'''
