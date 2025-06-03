'''
parser.py

this module handles the parsing of the excel files and the application of the ml based university standardization on a specific column
'''

#TODO: implement parser logic

def excel_parser(attribute_name: str, excel_path: str):

'''
design thoughts:
-takes in the file via file path
-looks at the user typed in attribute
-isolate that attribute's column from the dataFrame
-for statement that calls model.py
            -Keep a data structure that remembers previously used university names so that it is more efficient
            -Collect: matched standardized name + confidence score
# - Append new columns to the original DataFrame
# - Return the modified DataFrame or export to Excel

'''
