'''
                       Input Validator
                           for cli agrument  
'''
def clean_args(input_text : str ) -> list :

    return [x.strip() for x in input_text.split(",")]
