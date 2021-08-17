from rich.tree import Tree
from rich import print

my_tree = Tree("Car data")
engine = my_tree.add('engine')
engine.add('[red]Turbo')
engine.add('[blue]Compressor')
engine.add('[green]Cooler')
my_tree.add('door1')
my_tree.add('door2')
my_tree.add('trunk')
my_tree.add('hook')

print(my_tree)