import json 
from pathlib import Path
from leftoff.core.dtypes import TodoJson

def create_json(root_dir : Path) -> None :
    
    TITLE : str = "ShaProj"
    VERSION : float = 1.0

    data : TodoJson = {
        "title" : TITLE,
        "version" : VERSION,
        "mode" : {
            "feat" : [],
            "issue" : []
        }
    }
    file : Path = root_dir / "tests/data" / "temp_leftoff.json"
    json.dump(data,file.open(mode='w'))


def test_inital_leftoff_json(root_dir : Path):

    create_json(root_dir)
    file : Path = (root_dir / "tests/data" / "temp_leftoff.json")
    
    assert file.exists(), "[INIT TEST] The Core Json file creation error"

    with file.open(mode='r') as json_file :
        data : TodoJson = json.load(json_file)

        assert data['title'] == "ShaProj", "[INIT TEST] json title mismatch"
        assert data['version'] == 1.0, "[INIT TEST] json version missmatch"
        assert data['mode'] == {"feat" : [], "issue" : []}, "[INIT TEST] json mode structure error"
        assert data['mode']['feat'] == [] or data['mode']['issue'] == []  , "[INIT TEST] json modes inner structure error"


    file.unlink()
