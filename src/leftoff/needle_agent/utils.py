from pathlib import Path
from platformdirs import user_data_dir
from leftoff.needle_agent.dtypes import DataJson
from leftoff import __version__

import json

def create_leftoff_dir() -> Path:
    '''
      Return path of global json store
 
    '''
    data_dir = Path(user_data_dir("leftoff"))
    data_dir.mkdir(parents=True,exist_ok=True)
    # create a global json
    data_json_path = data_dir / "leftoff.json"

    return data_json_path


def create_leftoff_base_json(file_path : Path ) -> None :
    '''
    this create a base leftoff json file in shared app dir
    '''
    data : DataJson = {
        "version" : float(__version__),
        "projects" : []
    }

    json.dump(data,file_path.open())
    

    

    
