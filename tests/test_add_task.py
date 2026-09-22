import json
from pathlib import Path
from leftoff.core.cli import CLI
from leftoff.core.parser import LeftOffParser
from leftoff.core.dtypes import TodoJson,Table

def test_add_task(root_dir : Path) :
    # core 
    engine = LeftOffParser(root_dir / "tests/data")
    cli_parser = CLI(engine)

    cli_parser.add_task(mode='feat',add_input_text="deploy,1")

    file : Path = root_dir / "tests/data" / 'leftoff.json'

    assert file.exists(), "[ADD TEST] Json File not Found Error"

    with file.open(mode='r') as json_file:

        data : TodoJson = json.load(json_file)

    data_feat_tables : list[Table] = data['mode']['feat']

    # we already have 3 task and we added 4 the one
    task = next((x for x in data_feat_tables if x['id'] == 4),None)

    assert task, "[ADD TEST] Task is not added"

    # remove newly add task
    tasks = data['mode']['feat']
    data_feat_tables = [
        task for task in tasks if task['id'] != 4
    ]

    # re-set task ids
    for i,task in enumerate(data['mode']['feat'],start=1) : task['id'] = i

    with file.open(mode="w") as json_file : json.dump(data,json_file)
