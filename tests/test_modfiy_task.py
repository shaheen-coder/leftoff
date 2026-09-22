'''
                              PYTEST ( MODIFY )
                    this test case for lefoff modify func   
'''
# py 
import json
from pathlib import Path
# leftoff 
from leftoff.core.cli import CLI
from leftoff.core.parser import LeftOffParser
from leftoff.core.dtypes import TodoJson
def test_mod_task(root_dir : Path):

    # core
    engine = LeftOffParser(root_dir / "tests/data")
    cli = CLI(engine)

    cli.mod_task(
        'feat',
        "3,FIXING"
    )

    file : Path = root_dir / "tests/data" /  "leftoff.json"

    assert file.exists(), "[MOD TEST] Json File not Found"

    # mod a id 3 status from todo to FIXING

    with file.open(mode='r') as json_file:
        data : TodoJson  = json.load(json_file)

    tasks = data['mode']['feat']

    task = next((x for x in tasks if x['id'] == 3), None)

    assert task, "[MOD TEST] status modfication failed"

    assert task['status'] == "FIXING" , "[MOD TEST] Status is not modfied"
