import os
from math import ceil
import subprocess

from rich.markdown import Markdown
from rich.console import Console, ConsoleOptions, RenderResult, RenderableType
from rich.panel import Panel
from rich.style import StyleType
from rich.align import Align
from rich.table import Table
from rich.console import Console

from textual import events
from textual.app import App, DockLayout
from textual.widgets import Header, Footer, Placeholder, ScrollView, Button, ButtonPressed
from textual.reactive import Reactive
from textual.widget import Widget

from table import TableWidget
from utils.config import get_config

console = Console()
config = get_config()

class FileRenderable:
    def __init__(self, label: RenderableType, style: StyleType = "") -> None:
        self.label = label
        self.style = style

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        width = options.max_width
        height = options.max_height or 1

        yield Align.center(
            self.label, vertical="middle", style=self.style, width=width, height=height
        )
    
class File(Widget):
    def __init__(
        self,
        label: RenderableType,
        name: str | None = None,
        style: StyleType = "white on dark_blue",
    ):
        super().__init__(name=name)
        self.name = name or str(label)
        self.button_style = style

        self.label = label

    label: Reactive[RenderableType] = Reactive("")

    def render(self) -> Panel:
        return FileRenderable(self.label, style=self.button_style)

    async def on_click(self, event: events.Click) -> None:
        event.prevent_default().stop()
        await self.emit(ButtonPressed(self))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False

class MyApp(App):
    filetypes = ['.mp4', '.mkv']
    dir = config['anime_dir']
    script_path = config['script_path']
    selected = 0
    btns_list = []
    open_dir = []

    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")
        await self.bind("u", "back()", "Go back")

    async def on_mount(self, event: events.Mount) -> None:
        """Create and dock the widgets."""
        await self.view.dock(Footer(), edge="bottom")
        await self.load_buttons()

    async def action_back(self):
        parent_dir = os.path.abspath(os.path.join(self.dir, os.pardir))
        await self.change_dir(parent_dir)

    async def load_buttons(self) -> None:
        self.btns_list = []
        self.open_dir = os.listdir(self.dir)
        for i in range(len(self.open_dir)):
            file = self.open_dir[i]
            s = "white on grey0" if i != self.selected else "white"
            self.btns_list.append(File(label=file, style=s))
        await self.clear_buttons()
        self.btns = (btn for btn in self.btns_list)
        await self.view.dock(TableWidget(rows=self.open_dir, style="white", selected=self.selected), edge="top")

    async def clear_buttons(self) -> None:
        self.view.layout.docks.clear()
        self.view.widgets.clear()
        await self.view.dock(Footer(), edge="bottom")

    async def change_dir(self, new_dir) -> None:
        self.selected = 0
        self.dir = new_dir
        await self.load_buttons()

    def open_anime(self, file) -> None:
        os.startfile(file)
        os.startfile(self.script_path)

    async def handle_click(self, file) -> None:
        child = f'{self.dir}/{file}'
        if any(ext in file for ext in self.filetypes):
            self.open_anime(child)
            return
        await self.change_dir(child)

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        await self.handle_click(message.sender.name)

    async def increment(self):
        if self.selected + 1 < len(self.btns_list):
            self.selected += 1
        await self.load_buttons()

    async def decrement(self):
        if self.selected - 1 >= 0:
            self.selected -= 1
        await self.load_buttons()

    async def on_key(self, event) -> None:
        if event.key == "down":
            await self.increment()
        elif event.key == "up":
            await self.decrement()
        elif event.key == "enter":
            await self.handle_click(self.open_dir[self.selected])


MyApp.run(title="Anime TUI", log="textual.log")
