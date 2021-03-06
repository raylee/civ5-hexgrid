import operator

def megahex_count(radius):
    """
    counts from zero, so megahex radius 1 -> 6
    Computes the maximum number on a given level

    Computation based on the sequence of Hex (or centered hexagonal) numbers: 3*n*(n+1)+1
    """

    return 3*radius*(radius+1)

def print_map(hexmap, radius):
    for y in range(-radius, radius+1):
        print "{",
        for x in range(-radius, radius+1):
            if y in hexmap and x in hexmap[y]:
                print ("%3d," % (hexmap[y][x])),
            else:
                print " -1,",
        print "},"

def mark(hexmap, hex, id):
    hexmap[ hex[1] ][ hex[0] ] = id

def move(hex, direction):
    return tuple(map(operator.add, hex, direction))

def hex_spiral(size):
    # six tuples which encode moving the six different cardinal directions on a hex grid,
    # rendered on a matrix. Specific to Civ5's crazy numbering scheme, do not reuse in other
    # projects. generated by starting from hex #1 and writing down the deltas necessary for
    # the sample 5x5 below. (dx, dy).

    #              1-> 2    2-> 3    3-> 4   4-> 5    5-> 6   6-> 7
    hex_delta = [ (-1,+1), (-1,0), (0,-1), (+1,-1), (+1,0), (0,+1) ]

    # // this is the 5 ring layout
    #  -5  -4  -3  -2  -1   0   1   2   3   4   5  -- in the Y direction
    # {-1, -1, -1, -1, -1, 81, 82, 83, 84, 85, 86,}, // -5 hex-space x
    # {-1, -1, -1, -1, 80, 53, 54, 55, 56, 57, 87,}, // -4 hex-space x
    # {-1, -1, -1, 79, 52, 31, 32, 33, 34, 58, 88,}, // -3 hex-space x
    # {-1, -1, 78, 51, 30, 15, 16, 17, 35, 59, 89,}, // -2 hex-space x
    # {-1, 77, 50, 29, 14,  5,  6, 18, 36, 60, 90,}, // -1 hex-space x
    # {76, 49, 28, 13,  4,  0,  1,  7, 19, 37, 61,}, //  0 hex-space x
    # {75, 48, 27, 12,  3,  2,  8, 20, 38, 62, -1,}, //  1 hex-space x
    # {74, 47, 26, 11, 10,  9, 21, 39, 63, -1, -1,}, //  2 hex-space x
    # {73, 46, 25, 24, 23, 22, 40, 64, -1, -1, -1,}, //  3 hex-space x
    # {72, 45, 44, 43, 42, 41, 65, -1, -1, -1, -1,}, //  4 hex-space x
    # {71, 70, 69, 68, 67, 66, -1, -1, -1, -1, -1,}, //  5 hex-space x

    if size < 0:
        return

    hex = (0,0)
    yield hex

    r = 1
    while r <= size:
        hex = (r, 0)
        for direction in hex_delta:
            for edge_length in range(r):
                yield hex
                hex = move(hex, direction)
        r += 1


if __name__=='__main__':

    # init a hexmap. simulate negative indexed arrays with a dict
    hexmap = {}
    radius = 15
    for i in range(-radius*2, radius*2 + 1):
        hexmap[i] = {}

    id = 0
    for hex in hex_spiral(15):
        mark(hexmap, hex, id)
        id += 1


    print_map(hexmap, 15)









