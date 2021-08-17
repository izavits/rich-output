# Using tqdm you can easily produce beautiful progress bars, but let's try rich.

from rich.progress import track
from time import sleep


def process_data():
    sleep(0.1)


for _ in track(range(100), description='[green]Processing data'):
    process_data()
