import json
import difflib
from difflib import SequenceMatcher, get_close_matches

class Diccionario:
    '''Busca palabras y revisa coincidencias en el archivo data.json'''
    def __init__(self):
        self.data = json.load(open("json/data.json"))

    def dict(self,key):
        flag = True
        key = key.lower()
        if key in self.data:

            return (self.data[key],flag)
        if key.title() in self.data:

            return (self.data[key.title()],flag)
        if key.upper() in self.data:

            return (self.data[key.upper()],flag)
        elif len(get_close_matches(key,self.data.keys())) > 0:
            flag = False
            message = ("Quisiste decir %s?" % get_close_matches(key,self.data.keys())[0])
            return (message,flag,get_close_matches(key,self.data.keys())[0])

        else:
            return ("Ingrese una palabra valida",flag)
