import tcod

class Tile:
    blocked = 0
    #a tile of the map and its properties
    def __init__():
        self.blocked = 0

class Room:
    width = 0
    height = 0
    topLeftX = 0
    topLeftY = 0

    def __init__(w, h, x, y):
        this.width = w
        this.height = h
        this.topLeftX = x
        this.topLeftY = y

class Map:
    maxHeight = 0
    maxWidth = 0
    def __init__(maxHeight, maxWidth, numRooms):
        this.maxHeight = maxHeight
        this.maxWidth = maxWidth


    def create_room(room):
        global map
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                map[x][y].blocked = False


    def create_h_tunnel(x1, x2, y):
        global map
        # horizontal tunnel. min() and max() are used in case x1>x2
        for x in range(min(x1, x2), max(x1, x2) + 1):
            map[x][y].blocked = False


    def create_v_tunnel(y1, y2, x):
        global map
        # vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            map[x][y].blocked = False


    def make_map():
        global map

        # fill map with "blocked" tiles
        map = [
            [Tile(True) for y in range(MAP_HEIGHT)]
            for x in range(MAP_WIDTH)
        ]

        # create two rooms
        room1 = Rect(20, 15, 10, 15)
        room2 = Rect(50, 15, 10, 15)
        create_room(room1)
        create_room(room2)

        # connect them with a tunnel
        create_h_tunnel(25, 55, 23)
