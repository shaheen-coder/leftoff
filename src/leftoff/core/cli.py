'''
                        CLI
        this cli class handel leftoff json parser with cli arguments data.
    
'''
# engine
from leftoff.core.parser import LeftOffParser
from leftoff.core.input_val import clean_args
# typing 
from typing import Literal
# py date and time lin 
from datetime import datetime,timedelta
import sys 

class CLI:

    def __init__(self, parser_engine : LeftOffParser) -> None:

        self.engine =  parser_engine
               
    def add_task(self, mode : Literal['feat', 'issue'] , add_input_text : str) -> None :
        vals : list = clean_args(add_input_text)
        if vals == [] :
            print(f"Enter valid Input\nExample : 'task name,num of days' ( 'fix that,3')")
            sys.exit(1)
        today = datetime.now().date()
        mode_id : int = self.engine.get_feat_id if mode == 'feat' else self.engine.get_issue_id
        self.engine.add_task(mode,[{
                            "id" : mode_id + 1,
                            "task" : vals[0],
                            "status" : "TODO",
                            "due" : (today + timedelta(days=int(vals[1]))).strftime("%d-%m-%Y")
                        }])
        self.engine.json_writer()

    def mod_task(self, mode : Literal['feat','issue'], mod_input_text : str ) -> int:

        vals : list = clean_args(mod_input_text)
        if vals == [] :
            print(f"Enter valid Input\nExample : 'task name,num of days' ( 'fix that,3')")
            sys.exit(1)
        self.engine.mod_status(mode,
                            task_id=int(vals[0]),
                            status=vals[1]
                        )
        self.engine.json_writer()
        return int(vals[0])

    def rm_task(self, mode : Literal['feat', 'issue'], task_id : int ) -> None:

        self.engine.rm_task(mode,task_id=task_id)

        self.engine.json_writer()
        
