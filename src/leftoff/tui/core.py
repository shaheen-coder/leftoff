'''
                                   TUI CORE
             this is core tui class for showing tui compoents
'''
# textual
from textual.widgets import Header
from textual.containers import Vertical,Horizontal
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container
# leftoff 
from leftoff.core.dtypes import Table,StatsType
from leftoff.tui.table import GTable

class TuiApp(App):
    CSS_PATH = "tcss/core_tui.tcss"
    
    TITLE = "Todo CLI"

    def __init__(self,title : str | None,
                    version : float | None,
                    mode : str | None,
                    feat_tabel : list[Table],
                    issue_tabel : list[Table],
                    stats : StatsType
              ) -> None:

        super().__init__()
        
        if title : self.title = f"{title} | {version}V"
        if mode : self.HEADER_MODE = mode

        self.tabel_data_feat : list[Table] = feat_tabel
        self.tabel_data_issue : list[Table] = issue_tabel
        self.stats_data : StatsType = stats


    def compose(self) -> ComposeResult:
        # Header
        yield Header(show_clock=False)

        with Vertical(id="main") :            
            # --- STATS --
            with Container(id="stats-box"):
                
                yield Static("─ STATISTICS ─", id="stats-title")
                with Horizontal(id="stats-row"):
                    yield Static(f"Active: [{self.stats_data.get('active')}]", classes="stat stat-green")
                    yield Static(f"Features: [{self.stats_data.get('feat_count')}]", classes="stat stat-blue")
                    yield Static(f"Issues: [{self.stats_data.get('issue_count')}]", classes="stat stat-red")
                    yield Static(f"Completed: [{self.stats_data.get('compl')}]", classes="stat stat-yellow")

            # --- Tabel ----
            with Container(id="tasks-box"):
                yield Static("─ ACTIVE PROJECT TASKS ─", id="tasks-title")
                with Horizontal(id="tables"):
                    with Vertical(id="features-panel"):
                        yield Static("[ FEATURES / WORKS ]", classes="panel-title")
                        yield GTable(id="features-table",table_data=self.tabel_data_feat)
                    with Vertical(id="issues-panel"):
                        yield Static("[ ISSUES / FIXES ]", classes="panel-title")
                        yield GTable(id="issues-table",table_data=self.tabel_data_issue)
        

    def on_mount(self) -> None:
        self.query_one("#features-table", GTable).focus()

