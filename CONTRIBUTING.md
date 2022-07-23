# ani-tui

Thank you for looking to contribute! Here's how to get started:

## Setup

### Prerequisites

Ensure you have the following installed prior to installation

- Python 3.9+
- [Poetry](https://python-poetry.org/)
- Git (of course!)
- Node/NPM (if you want to modify `anitui/script`)

### Development Installation

1. Fork the repository and clone down your branch
    ```bash
    git clone https://github.com/{your username}/ani-tui
    ```

2. Install the Python packages
    ```bash
    poetry install
    ```

3. Verify the TUI runs
    ```bash
    poetry run anitui
    ```

## Making Changes

If you would like to make a change, please first create an [issue](https://github.com/cakoshakib/ani-tui/issues) describing the change or issue you are trying to solve!

Once you have made your changes, ensure you push it to your branch and create a PR. Upon review, I will then merge your changes if they look good :).

Please follow [PEP8](https://peps.python.org/pep-0008/) standard in your code. A simple way to clean up your code is running
```bash
poetry run black .
```

