from typing import TypedDict
from pathlib import Path 

class Projects(TypedDict):

    name : str
    version : float
    description : str 
    path : Path

 
class DataJson(TypedDict):
    version : float

    projects : list[Projects]

    
