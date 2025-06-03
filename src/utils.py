#text cleaning helper methods
'''
utils.py

holds all the helper methods
to start off some include:
1. tokenization
    -remove all non-alphabetical characters
    -lowercase everything

2. TALK TO MATT ABOUT BEST DATA STRUCTURE FOR THIS
    large csv of canonical university names but how do we efficient store into a data structure

    '''

    def cleaned_input(raw_uni_name: str) -> str:
        lowered = raw_uni_name.lowercase()
