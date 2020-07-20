from minesweeper import *

ai = MinesweeperAI()

ai.add_knowledge((0, 0), 0)
for x in ai.knowledge:
    print(x)
print(ai.make_safe_move())
