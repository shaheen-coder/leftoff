'''
                                  Main Agent class  
'''

from pathlib import Path

from leftoff.needle_agent.utils import create_leftoff_dir


class Agent:

    def __init__(self) ->  None:
        
        self.leftoff_json : Path = create_leftoff_dir()
         
    
