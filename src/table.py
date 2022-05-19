from rich.align import Align
from rich.panel import Panel
from rich.style import StyleType
from rich.table import Table
from textual.widget import Widget

class TableWidget(Widget):
    def __init__(
        self,
        *,
        tall: bool = True,
        style: StyleType = "white on dark_green",
        clock: bool = True,
        rows: [str],
        selected: int
    ) -> None:
        super().__init__()
        self.tall = tall
        self.style = style
        self.clock = clock
        self.rows = rows
        self.selected = selected

    def render(self) -> Panel:
        table = Table.grid(padding=(0, 1), expand=True)
        table.add_column("title", justify="center", ratio=1)
        for i in range(len(self.rows)):
            row = self.rows[i]
            if i == self.selected:
                table.add_row(Align.center(row, vertical="middle"), style="green")
            else:
                table.add_row(Align.center(row, vertical="middle"))
        return table 
