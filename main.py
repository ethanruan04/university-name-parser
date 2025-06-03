'''
main.py

this is the start to the university name standardization tool. 
1. accepts the inputted excel file via file path
2. accepts the users wanted target column
3. accepts a confidence score threshold to allow for user customization of correctness
'''
#TODO: main method

def main():
    '''
    -parse user arguments
    -loads ML model and canonical name list
    -computes embeddings
    -applies matching and filtering based on threshold
    -saves cleaned results to output excel file

    '''