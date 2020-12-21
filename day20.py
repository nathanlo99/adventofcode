
import sys
from collections import defaultdict

def get_right(tile):
    return "".join(line[-1] for line in tile)

def get_bottom(tile):
    return tile[-1]

def get_left(tile):
    return "".join(line[0] for line in tile)

def get_top(tile):
    return tile[0]

def get_edges(tile):
    result = []
    result.append(tile[0]) # Top, going right
    result.append("".join(line[-1] for line in tile)) # Right, going down
    result.append(tile[-1][::-1]) # Bottom, going left
    result.append("".join(line[0] for line in tile[::-1])) # Left, going up
    result.append(tile[0][::-1]) # Top, going left
    result.append("".join(line[-1] for line in tile[::-1])) # Right, going up
    result.append(tile[-1]) # Bottom, going right
    result.append("".join(line[0] for line in tile)) # Left, going down
    return result

# Rotates a square tile clockwise by 90 degrees
def rotate(tile):
    width, height = len(tile[0]), len(tile)
    assert(width == height)
    result = [list(x) for x in tile]
    for y in range(height):
        for x in range(width):
            result[y][x] = tile[height - 1 - x][y]
    return list(map(lambda x: "".join(x), result))

# Flips a tile along the x-axis
def flip_vertical(tile):
    width, height = len(tile[0]), len(tile)
    assert(width == height)
    result = [list(x) for x in tile]
    for y in range(height):
        for x in range(width):
            result[y][x] = tile[y][width - 1 - x]
    return list(map(lambda x: "".join(x), result))

# Flips a tile along the x-axis
def flip_horizontal(tile):
    width, height = len(tile[0]), len(tile)
    assert(width == height)
    result = [list(x) for x in tile]
    for y in range(height):
        for x in range(width):
            result[y][x] = tile[height - 1 - y][x]
    return list(map(lambda x: "".join(x), result))

tiles = dict()
graph = defaultdict(list)
edge_to_tile = defaultdict(list)

while True:
    id_line = input().strip()
    if id_line == "DONE":
        break
    id = int(id_line.split()[1][:-1])
    tile = []
    while True:
        next_line = input().strip()
        if next_line == "":
            break
        tile.append(next_line)
    edges = get_edges(tile)
    for edge_idx, edge in enumerate(edges):
        for neighbour_idx, neighbour_tile in edge_to_tile[edge]:
            graph[id].append((edge_idx, neighbour_tile))
            graph[neighbour_tile].append((neighbour_idx, id))
        edge_to_tile[edge].append((edge_idx, id))
    tiles[id] = (tile, edges)

border_edges = list()
seen = defaultdict(int)
for edge, possibilities in edge_to_tile.items():
    if len(possibilities) == 1:
        idx, tile = possibilities[0]
        border_edges.append((edge, idx, tile))
        seen[tile] += 1

corners = list()
ans = 1
for thing, freq in seen.items():
    if freq == 4:
        ans *= thing
        corners.append(thing)
print(ans)
print(corners)

dimension = int(len(tiles) ** 0.5)
one_corner_tile, one_corner_edges = tiles[corners[0]]
tile_dimension = len(one_corner_tile)
total_dimension = dimension * (tile_dimension - 2)
print(one_corner_tile, one_corner_edges)
print(dimension, tile_dimension)

result = [[None for _ in range(total_dimension)] for __ in range(total_dimension)]
tile_layout = [[None for _ in range(dimension)] for __ in range(dimension)]

def stamp(result, tile, tx, ty):
    start_x, start_y = tx * (tile_dimension - 2), ty * (tile_dimension - 2)
    width, height = len(tile[0]), len(tile)
    result_width, result_height = len(result[0]), len(result)
    for row in range(tile_dimension - 2):
        for col in range(tile_dimension - 2):
            result[start_y + row][start_x + col] = tile[col + 1][row + 1]
    return result

for row in range(dimension):
    for col in range(dimension):
        if (row, col) == (0, 0):
            target1, target2 = set(one_corner_edges[idx] for idx, tile in graph[corners[0]] if idx < 4)
            for i in range(4):
                if get_right(one_corner_tile) == target1 and get_bottom(one_corner_tile)[::-1] == target2:
                    break
                if get_right(one_corner_tile) == target2 and get_bottom(one_corner_tile)[::-1] == target1:
                    break
                one_corner_tile = flip_vertical(one_corner_tile)
                if get_right(one_corner_tile) == target1 and get_bottom(one_corner_tile)[::-1] == target2:
                    break
                if get_right(one_corner_tile) == target2 and get_bottom(one_corner_tile)[::-1] == target1:
                    break
                one_corner_tile = flip_vertical(one_corner_tile)
                one_corner_tile = rotate(one_corner_tile)
            else:
                assert(False)

            tile_layout[row][col] = (corners[0], one_corner_tile)
            result = stamp(result, one_corner_tile, 0, 0)
        elif col == 0:
            # Grab from the top
            above_id, above_tile = tile_layout[row - 1][col]
            above_border = get_bottom(above_tile)
            neighbouring_tiles = [x[1] for x in edge_to_tile[above_border]]
            assert len(neighbouring_tiles) == 2
            this_id = neighbouring_tiles[0] ^ neighbouring_tiles[1] ^ above_id
            this_tile = tiles[this_id][0]
            for _ in range(4):
                if get_top(this_tile) == above_border:
                    break
                if get_top(this_tile) == above_border[::-1]:
                    this_tile = flip_vertical(this_tile)
                    break
                this_tile = rotate(this_tile)
            tile_layout[row][col] = (this_id, this_tile)
            result = stamp(result, this_tile, row, col)
        else:
            # Match the left
            left = tile_layout[row][col - 1]
            left_id, left_tile = tile_layout[row][col - 1]
            left_border = get_right(left_tile)
            neighbouring_tiles = [x[1] for x in edge_to_tile[left_border]]
            this_id = neighbouring_tiles[0] ^ neighbouring_tiles[1] ^ left_id
            this_tile = tiles[this_id][0]
            for _ in range(4):
                if get_left(this_tile) == left_border:
                    break
                if get_left(this_tile) == left_border[::-1]:
                    this_tile = flip_horizontal(this_tile)
                    break
                this_tile = rotate(this_tile)
            tile_layout[row][col] = (this_id, this_tile)
            result = stamp(result, this_tile, row, col)

def is_dark(image, row, col):
    width, height = len(image[0]), len(image)
    return 0 <= row < height and 0 <= col < width and image[row][col] != "."

def count_sea_monsters(image):
    sea_monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   ",
    ]
    width, height = len(sea_monster[0]), len(sea_monster)
    offsets = []
    for row, line in enumerate(sea_monster):
        for col, chr in enumerate(line):
            if chr == "#":
                offsets.append((row - 1, col))
    assert((0, 0) in offsets)
    found = False
    image_copy = [[x for x in thing] for thing in image]
    for row, line in enumerate(image):
        for col, chr in enumerate(line):
            if chr != ".":
                for offset_y, offset_x in offsets:
                    if not is_dark(image, row + offset_y, col + offset_x):
                        break
                else:
                    for offset_y, offset_x in offsets:
                        image_copy[row + offset_y][col + offset_x] = "O"
                    found = True
    not_sea_monster = sum(line.count("#") for line in image_copy)
    return found, not_sea_monster

for thing in tile_layout:
    for id, tile in thing:
        print(id, end=" ")
    print()

image = ["".join(thing) for thing in result]
image = rotate(rotate(rotate(flip_vertical(image))))


print("\n".join(image))
for i in range(4):
    print(count_sea_monsters(image))
    image = rotate(image)
image = flip_vertical(image)
for i in range(4):
    print(count_sea_monsters(image))
    image = rotate(image)
