'''
                            MAIN
            Main cli runner file manage cli and tui 
    
'''
# engine
from leftoff.core.dtypes import StatsType # stats type dict 
from leftoff.core.parser import LeftOffParser  # main todo engine 
from leftoff.core.stats import Stats # statics of task 
from leftoff.core.cli import CLI # cli manger 
# tui 
from leftoff.tui.core import TuiApp # core tui app 
# py libs
from pathlib import Path # py path lib
import argparse as cli # cli argument parser
# json
import json
# sys
import sys

def create_base_json(root_dir : Path) -> None :
    '''
         creates inital `leftoff.json` with title and version get from user
    '''

    title : str = input("Enter the Title : ")
    version : float = float(input("Enter your current version : "))
    data : dict = {
                "title" : title,
                "version": version,
                "mode" : {
                    'feat'  : [],
                    'issue' : [] 
                }
            }

    file : Path = root_dir / "leftoff.json"
    json.dump(data,file.open(mode='w'))

# tui
def show_tui(l_engine):
    if l_engine.data['mode']['feat'] == [] and  l_engine.data['mode']['issue'] == []  :
        print("There is no task to show")
        return 
    feat_stats = Stats(l_engine.get_feat_table())
    issue_stats = Stats(l_engine.get_issue_table())
    stats = StatsType(
                      feat_count=feat_stats.get_count(),
                      issue_count=issue_stats.get_count(),
                      active=(feat_stats.get_active_count()[0] + issue_stats.get_active_count()[0]),
                      compl=(feat_stats.get_active_count()[1] + issue_stats.get_active_count()[1])
                  ) 
    app = TuiApp(
                  title=l_engine.get_title(),
                  version=l_engine.get_version(),
                  mode=None,
                  feat_tabel=l_engine.get_feat_table(),
                  issue_tabel=l_engine.get_issue_table(),
                  stats=stats
              )
    app.run()

def main() -> None :

    
    root_dir : Path = Path(".")
    # if  leftover.json isnt in root everything falls apart
    if not (root_dir / "leftoff.json").exists() :
        create_base_json(root_dir)
        print("\nGood Luck with project !!")
        return

    parser = cli.ArgumentParser(description="Todo cli also support tui")
    parser.add_argument("--tui", action="store_true",help="show tui")
    parser.add_argument("--mode",type=str,help="feature mode")
    parser.add_argument("--add",type=str,help="add to task")
    parser.add_argument("--mod",type=str,help="Change the task status")
    parser.add_argument("--rm",type=int,help="Remove task")
    args = parser.parse_args()

    if len(sys.argv) == 1 :
        print("To Know how to use it ? use ( --help )")
        return 
    
    engine = LeftOffParser(root_dir)
    cli_parser = CLI(engine)

    if args.tui: show_tui(engine)

    # cli 
    
    if args.mode == 'feat':
        if args.add is not None :
            cli_parser.add_task('feat',args.add)
            print("New task is added on Feature !!")

        if args.mod is not None :
            mod_id = cli_parser.mod_task('feat',args.mod)
            print(f"Task {mod_id} status is modifed")

        if args.rm is not None :
            cli_parser.rm_task('feat',task_id=args.rm)
            print(f"Task {args.rm} is removed")

    if args.mode == 'issue':
        if args.add is not None :
            cli_parser.add_task('issue',args.add)
            print("New task is added on issue !!")

        if args.mod is not None :

            mod_id = cli_parser.mod_task('issue',args.mod)
            print(f"Task {mod_id} status is modifed")

        if args.rm is not None :
            cli_parser.rm_task('issue',task_id=args.rm)
            print(f"Task {args.rm} is removed")


if __name__ == "__main__":

    main()
