
from leftoff.core.dtypes import StatsType,Table

class Stats:

    def __init__(self, table_data : list[Table]) -> None :

        self.table_data : list[Table] = table_data


    def get_count(self) -> int : return len(self.table_data)

    def get_active_count(self) -> tuple[int , int]:

        ac_count : int = 0
        comp_count : int = 0
        
        for task in self.table_data:
            status : str = task.get('status')
            if  status == 'TODO' or status == 'FIXING' : ac_count += 1
            elif status == 'FIXED' : comp_count += 1 

        return (ac_count,comp_count) 
    

            
