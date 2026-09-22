import json
from pathlib import Path
from leftoff.core.cli import CLI
from leftoff.core.parser import LeftOffParser
from leftoff.core.dtypes import TodoJson

def test_rm_task(root_dir : Path) :

    # core engine
    engine = LeftOffParser(root_dir / "tests/data")
    cli = CLI(engine)

    cli.rm_task(
        'feat',
        3
    )

    file : Path = root_dir / "tests/data" / "leftoff.json"

    assert file.exists(), "[RM TEST] Json File not Found"

    with file.open(mode='r') as json_file:
        data : TodoJson  = json.load(json_file)

    tasks = data['mode']['feat']

    task = next((x for x in tasks if x['id'] == 3), None)

    assert task is not None, "[RM TEST] Task is not removed"
     
