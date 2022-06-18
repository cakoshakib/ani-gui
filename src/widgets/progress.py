from rich import box
from rich.align import Align
import requests
import json

from rich.console import RenderableType
from rich.panel import Panel
from rich.pretty import Pretty

from textual.geometry import Offset
from textual.widget import Reactive, Widget
from rich.table import Table

class Progress(Widget):

    style: Reactive[str] = Reactive("")
    height: Reactive[int | None] = Reactive(None)

    def __init__(self, *, name: str | None = None, height: int | None = None, username: str | None = None) -> None:
        super().__init__(name=name)
        self.height = height
        self.username = username

    def get_data(self, query, variables):
        url = 'https://graphql.anilist.co'
        response = requests.post(url, json={"query": query, "variables": variables})
        return response.json()


    def query_watch_list(self):
        query = """
        query ($page: Int, $perPage: Int, $userName: String) {
          Page (page: $page, perPage: $perPage) {
            mediaList (userName: $userName, status: CURRENT, type: ANIME) {
              mediaId
              media {
                title {
                  english
                }
              }
              progress
            }
          }
        }
        """
        variables = {
            'page': 1,
            'perPage': 20,
            'userName': self.username,
        }
        res = self.get_data(query, variables)
        return res['data']['Page']['mediaList']

    def construct_watch_list(self):
        data = self.query_watch_list()
        table = Table.grid(padding=(1, 2), expand=True)
        table.style = self.style
        table.add_column("Title")
        table.add_column("Episode", justify="right", ratio=1)
        for anime in data:
            title = anime['media']['title']['english']
            episode = anime['progress']
            table.add_row(str(title), str(episode))
        return table

    def render(self) -> RenderableType:
        table = self.construct_watch_list()

        return Panel(
            table,
            title='Watch List',
            border_style="green",
            style=self.style,
            height=self.height,
        )
