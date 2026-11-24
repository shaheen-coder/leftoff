import json
from leftoff.needle_agent.utils import (
    create_leftoff_dir,
    create_leftoff_base_json
)
from leftoff.needle_agent.dtypes import Projects
from leftoff.needle_agent.agent_fn import get_all_tools
from needle import Needle

class AgentCLI:

    def __init__(self):

        self.json_path = create_leftoff_dir()

        if not self.json_path.exists() : create_leftoff_base_json(self.json_path)


    def add_project(self, data : Projects) -> None :

        json_file = json.load(self.json_path.open())

        json_file['projects'].append(data)

    def chat(self) -> None :
        needle_agent = Needle(
            tools=get_all_tools()
        )

        print("Chat with Leftoff AI ( type q or quit to exit)")
        while True : # chat loop 

            prompt = input("you : ")
            if prompt in ["q", "quit"] : break
            response = needle_agent.run(prompt)
            print(f"AI : {response.get('results','')}")
            # print("-"*50)
            # print(response)
            # print("-"*50)
            needle_agent.reset()
