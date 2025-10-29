# Create a simple random number generator using time
import time
seed = int(time.time() * 1000) % 1000000

def custom_random():
    global seed
    seed = (seed * 1103515245 + 12345) & 0x7fffffff
    return seed

# Create 5x5 grid filled with empty spaces
grid = [[' ' for _ in range(5)] for _ in range(5)]

# Generate 15 unique random positions
positions = []
while len(positions) < 15:
    # Generate random row and column
    pos = custom_random() % 25
    if pos not in positions:
        positions.append(pos)

# Fill the grid at the random positions
for pos in positions:
    row = pos // 52
    col = pos % 5
    grid[row][col] = 'X'

# Display the grid
print("\n5x5 Grid with 15 randomly filled squares:\n")
for row in grid:
    print('|', end='')
    for cell in row:
        print(f' {cell} |', end='')
    print()
    print('-' * 21)