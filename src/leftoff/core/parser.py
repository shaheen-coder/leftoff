from typing import Literal
from pathlib import Path

import json

from leftoff.core.dtypes import TodoJson,Table,StatsType
from leftoff.core.type_val import validate_todo,InvalidTodo

class  LeftOffParser:

    def __init__(self, root_dir : Path ) -> None :

        self.root_dir : Path =  root_dir

        self.todo_file : Path = root_dir / "leftoff.json"

        if not self.todo_file.exists :
            raise FileNotFoundError("todo file is not found")

        self.data : TodoJson  = self.json_reader()
        if not validate_todo(self.data):
            raise InvalidTodo("Invalid todo.json format")
        
    def json_reader(self) -> TodoJson :
        
        data = json.load(self.todo_file.open(mode='r'))

        return data

    def json_writer(self) -> None:
        json.dump(self.data,self.todo_file.open(mode="w"))

    # reader
    
    def get_title(self) -> str : return self.data.get('title')

    def get_version(self) -> float : return self.data.get("version")

    def get_feat_table(self) -> list[Table] : return self.data['mode']['feat']

    def  get_issue_table(self) -> list[Table] : return self.data['mode']['issue']

    # utils
    @property
    def get_feat_id(self) -> int : return self.get_feat_table()[-1].get('id') if self.get_feat_table() != []  else  0
    @property
    def get_issue_id(self) -> int : return self.get_issue_table()[-1].get('id') if self.get_issue_table() != [] else 0

    # writer

    def add_task(self,mode : Literal['feat', 'issue'], task : list[Table]) -> None :

        self.data['mode'][mode].extend(task)

    def mod_status(self, mode : Literal['feat', 'issue'], task_id : int, status : Literal['FIXING', 'FIXED'] ) -> None :

        tasks = self.data['mode'][mode]

        task = next((x for x in tasks if x['id'] == task_id),None)

        if task is not None : task['status'] = status

    def rm_task(self, mode : Literal['feat', 'issue'], task_id: int ) -> None :

        tasks = self.data['mode'][mode]

        if tasks is None:
            print("There is No task to delete")
            return
        
        # re-build the tasks without detele one     
        self.data['mode'][mode] = [
            task for task in tasks if task['id'] != task_id
        ]

        # re-set task ids
        for i,task in enumerate(self.data['mode'][mode],start=1) : task['id'] = i
        
