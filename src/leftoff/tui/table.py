'''
                           Table Compoent ( TUI )
                    this is general Table Compoent for both issue ans feature 
'''
# textual and rich
from textual.widgets import DataTable
from rich.text import Text
# leftoff 
from leftoff.core.dtypes import Table
# py
from datetime import datetime
from datetime import date as Date

class GTable(DataTable):
    ''' Genral Tabel Format  '''

    
    STATUS_STYLES = {
        "TODO": "bold green",
        "FIXED": "bold yellow",
        "FIXING": "bold magenta",
        "DONE" : "bold cyan",
    }
    
    def __init__(self, table_data : list[Table], **kwargs) -> None :

        super().__init__(**kwargs)

        self.table_data : list[Table] = table_data

    def deadline_cell(self, due : Date ) -> Text :
        days = ( due - Date.today()).days
        if days < 0 : return Text(f'{due.day}-{due.month}',style="bold white on red")
        if days == 0 : return Text(f'{due.day}-{due.month}',style="bold white on red")
        return Text(f"{due.day}-{due.month}",style="yellow")        

    def on_mount(self) -> None :

        self.cursor_type = "row"
        self.zebra_stripes = False
        
        # adding cols of table 
        self.add_column("ID",width=4)
        self.add_column("TASK",width=30)
        self.add_column("STATUS",width=10)
        self.add_column("DUE",width=12)

        # adding rows of  table
        for item in self.table_data:
            style = self.STATUS_STYLES.get(item["status"],"White")
            due_date = datetime.strptime(item['due'],"%d-%m-%Y").date()
            self.add_row(
                str(item["id"]),
                item["task"],
                Text(f"[{item['status']}]", style=style),
                self.deadline_cell(due_date),
                key=str(item["id"]),
            )
        self.move_cursor(row=0)
