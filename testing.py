from champion import *

c = Champions()
byStat = c.sortByStat(stat="hp")
[print(c.name, c.stats['hp']) for c in byStat]