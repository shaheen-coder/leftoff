'''
                              DType
        these are typing classes for json data structure  
'''

from typing import TypedDict,Literal


class Table(TypedDict):

    id : int
    task : str
    status : Literal["TODO","FIXING","FIXED"] 
    due : str #  deadline date as str  


class TodoJson(TypedDict):
    title : str
    version : float
    mode : dict[Literal["feat","issue"],list[Table]] 
    
'''
{
    "title" : "shatokens",
    "version" : 0.1,
    "mode" : {
        "feat" : [
            {
                "id" : 1,
                "task" : "add mult file reading",
                "status" : false,
                "due" : "12-08-2026" 
            },
            {...}
        ],
        "issue" : [
            {
                "id" : 1,
                "task" : "fix the padding on encode function",
                "status" : false,
                "due" : "21-08-2026" 
            }
        ]
    }
        
    
}    
''' 

class  StatsType(TypedDict):

    feat_count : int

    issue_count : int

    active : int

    compl : int # complete task 
