from rich.style import StyleType
from rich.console import RenderableType
from rich.panel import Panel
from textual.widget import Widget


class Header(Widget):
    def __init__(
        self,
        label: RenderableType,
        name: str | None = None,
    ):
        super().__init__(name=name)
        self.name = name or str(label)
        self.label = label

    def render(self) -> Panel:
        return Panel(self.label)
