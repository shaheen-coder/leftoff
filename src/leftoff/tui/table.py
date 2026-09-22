'''
                           Table Compoent ( TUI )
                    this is general Table Compoent for both issue ans feature 
'''
from textual.widgets import DataTable
from rich.text import Text

from leftoff.core.dtypes import Table

class GTable(DataTable):
    ''' Genral Tabel Format  '''

    
    STATUS_STYLES = {
        "TODO": "bold green",
        "FIXED": "bold yellow",
        "FIXING": "bold magenta",
    }
    
    def __init__(self, table_data : list[Table], **kwargs) -> None :

        super().__init__(**kwargs)

        self.table_data : list[Table] = table_data


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
            self.add_row(
                str(item["id"]),
                item["task"],
                Text(f"[{item['status']}]", style=style),
                Text(item["due"], style="yellow"),
                key=str(item["id"]),
            )
        self.move_cursor(row=0)
