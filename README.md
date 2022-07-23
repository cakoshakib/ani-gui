# ani-tui

TUI written in Python using [Textual](https://github.com/Textualize/textual) to navigate local Anime files. 

## Showcase

![GIF of AniTUI](./fluff/anitui-showcase.gif)

## Getting Started

### Prerequisites

- Python 3.9+

### Install

To use ani-tui simply install the Python package:

**Unix**
```bash
pip3 install anitui
```

**Windows**
```powershell
py -m pip install anitui
```

The TUI can then be run by simply typing `anitui` in the shell.

## Connecting with [VLC-Ani-Discord](https://github.com/cakoshakib/vlc-ani-discord)

ani-tui is capable of launching the vlc-ani-discord script along with your chosen media to display Discord Rich Presence and automatically update your Anilist episode progress. Note that this is only applicable if you are using VLC as your media player. The setup for this is a bit convoluted at the moment so it is automatically turned off. However, if you would like to use this feature here's how to do it! :)

1. Find out where ani-tui was installed
    ```bash
    pip show anitui
    ```
   Here you should see something of the form:
    ```bash
    Location: {PATH}
    ```

2. Go to the directory
    ```bash
    cd {PATH}/script
    ```

3. Here you will find a `README.md` with instructions on setting up `vlc-ani-discord`. Complete the setup and then move on to Step 4

4. Modify the ani-tui config file `~/.config/anitui/config.json` in your chosen editor. Simply change `"script": false` to `"script": true`. 

Then you're done! I will be improving this process to be more straightforward in the future. 

## Notes

Still in development, expect bugs! :)

## License
MIT

