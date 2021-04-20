from itertools import cycle
kolvo = 20
inp = [10, 15]
print([f'{i, j}' for i, j in enumerate(cycle(inp)) if i < int(kolvo)])