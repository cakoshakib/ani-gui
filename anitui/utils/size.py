from rich.console import Console

console = Console()

def entry_height(entry, table_width):
    padding = 2
    line = (len(entry) // table_width) + 1
    return line + padding

def table_size():
    console = Console()
    table_width = console.width - (console.width // 3)
    table_height = console.height - 2
    return table_height, table_width

def validate_selected(entries, selected):
    """ Returns True if selected is within table view """
    table_height, table_width = table_size()
    # Calculate how many lines each "entry" takes
    total_height = 0
    for i in range(len(entries)):
        total_height += entry_height(entries[i], table_height)
        if total_height > table_height:
            return i
        if i == selected:
            return selected
    return selected







    
