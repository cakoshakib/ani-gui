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
        self.offset = max(self.selected - 22, 0)

    def render(self) -> Panel:
        table = Table.grid(padding=(1, 1), expand=True)
        table.add_column("title", justify="left", ratio=1)
        for i in range(self.offset, len(self.rows)):
            row = self.rows[i]
            if i == self.selected:
                table.add_row(Align(row, vertical="middle"), style="green")
            else:
                table.add_row(Align(row, vertical="middle"), style="white")
        return table 
