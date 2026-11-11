import json
from leftoff.needle_agent.utils import (
    create_leftoff_dir,
    create_leftoff_base_json
)
from leftoff.needle_agent.dtypes import Projects

class AgentCLI:

    def __init__(self):

        self.json_path = create_leftoff_dir()

        if not self.json_path.exists() : create_leftoff_base_json(self.json_path)


    def add_project(self, data : Projects) -> None :

        json_file = json.load(self.json_path.open())

        json_file['projects'].append(data)

    def chat(self) -> None :

        pass
