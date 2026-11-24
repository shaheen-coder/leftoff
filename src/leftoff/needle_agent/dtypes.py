from typing import TypedDict
from pathlib import Path 

class Projects(TypedDict):

    name : str
    version : str
    description : str 
    path : Path

 
class DataJson(TypedDict):
    version : str

    projects : list[Projects]

    
