import os
import subprocess
import json

from rich.markdown import Markdown
from rich.panel import Panel

from textual import events
from textual.app import App, DockLayout
from textual.widgets import Header, Footer, Placeholder, ScrollView, Button, ButtonPressed
from textual.reactive import Reactive
from textual.widget import Widget

with open('config.json', 'r') as configfile:
    config = json.loads(configfile.read())
    
class File(Widget):
    mouse_over = Reactive(False)

    def render(self) -> Panel:
        return Panel("Hello [b]World[/b]", style=("on red" if self.mouse_over else ""))

    def on_enter(self) -> None:
        self.mouse_over = True

    def on_leave(self) -> None:
        self.mouse_over = False


class MyApp(App):
    filetypes = ['.mp4', '.mkv']
    dir = config['anime_dir']
    script_path = config['script_path']

    async def on_load(self, event: events.Load) -> None:
        """Bind keys with the app loads (but before entering application mode)"""
        await self.bind("q", "quit", "Quit")
        await self.bind("escape", "quit", "Quit")
        await self.bind("u", "back()", "Go back")

    async def action_back(self):
        parent_dir = os.path.abspath(os.path.join(self.dir, os.pardir))
        await self.change_dir(parent_dir)

    async def on_mount(self, event: events.Mount) -> None:
        """Create and dock the widgets."""

        # Header / footer / dock
        await self.view.dock(Footer(), edge="bottom")

        self.btns = (Button(label=file, style="white on grey0") for file in os.listdir(self.dir))
        await self.view.dock(*self.btns, edge="top")

    async def clear_buttons(self) -> None:
        self.view.layout.docks.clear()
        self.view.widgets.clear()
        await self.view.dock(Footer(), edge="bottom")

    async def change_dir(self, new_dir) -> None:
        self.dir = new_dir
        await self.clear_buttons()
        self.btns = (Button(label=file, style="white on grey0") for file in os.listdir(self.dir))
        await self.view.dock(*self.btns, edge="top")

    def open_anime(self, file) -> None:
        os.startfile(file)
        os.startfile(self.script_path)

    async def handle_button_pressed(self, message: ButtonPressed) -> None:
        child = f'{self.dir}/{message.sender.name}'
        if any(ext in message.sender.name for ext in self.filetypes):
            self.open_anime(child)
            return
        await self.change_dir(child)

    async def on_key(self, event) -> None:
        pass


MyApp.run(title="Anime TUI", log="textual.log")
