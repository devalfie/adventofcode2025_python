##rolls of paper == @
## The forklists can only access a roll of paper if 
# there are less than 4 rolls of paper in eight adjacent positions

with open('day4.txt','r') as file:
    puzzle = file.read().splitlines()

rolls = {complex(x,y) for y, row in enumerate(puzzle) for x, char in enumerate(row) if char == '@'}

neighbours = {r: {r+complex(x,y) for x in (-1,0,1) for y in (-1,0,1) if x or y} for r in rolls}

# initial (single-pass) accessible rolls: those with fewer than 4 adjacent rolls
initial_accessible = sum(1 for r in rolls if len(neighbours[r] & rolls) < 4)

removal_counts = []
while removals := {r for r in rolls if len(neighbours[r] & rolls) < 4}:
    removal_counts.append(len(removals))
    rolls -= removals

print(initial_accessible)
print(removal_counts[2], sum(removal_counts))