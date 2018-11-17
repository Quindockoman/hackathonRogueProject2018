import tcod
import math

class Tile:
    blocked = False
    charToken = ""
    #a tile of the map and its properties
    def __init__(self, blocked):
        self.blocked = blocked

class Room:
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    spdPenalty = 1

    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

class Map:
    maxHeight = 0
    maxWidth = 0
    numRooms = 0
    map = []

    def __init__(self, maxHeight, maxWidth, numRooms):
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        self.numRooms = numRooms


    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        for x in range(room.x1 + 1, room.x2):
            for y in range(room.y1 + 1, room.y2):
                self.map[x][y].blocked = False
                self.map[x][y].charToken = "."

    def create_h_tunnel(self, x1, x2, y):
        # horizontal tunnel. min() and max() are used in case x1>x2
        for x in range(min(x1, x2), max(x1, x2) + 1):
            self.map[x][y].blocked = False

    def create_v_tunnel(self, y1, y2, x):
        # vertical tunnel
        for y in range(min(y1, y2), max(y1, y2) + 1):
            self.map[x][y].blocked = False

    def create_hdoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "|"

    def create_vdoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "-"

    def make_map(self):
        # fill map with "blocked" tiles
        self.map = [
            [Tile(True) for y in range(self.maxHeight)]
            for x in range(self.maxWidth)
         ]

        xStart = 0
        xEnd = 4
        yStart = 0
        yEnd = 4
        for i in range(1, self.numRooms+1):
            print(xStart, xEnd, yStart, yEnd)
            newRoom = Room(xStart, xEnd, yStart, yEnd)
            self.create_room(newRoom)
            xStart += 4
            xEnd += 4
            if(i > 0 and i % math.sqrt(self.numRooms) == 0):
                yStart += 4
                yEnd += 4
                xStart = 0
                xEnd = 4
            else:
                self.create_hdoor(xEnd-4, int(yEnd - 2))
                if(i > math.sqrt(self.numRooms)):
                    self.create_vdoor(xEnd-2, int(yEnd - 4))
        # create two rooms
        # room1 = Room(0, 4, 0, 4)
        # room2 = Room(4, 6, 0, 2)
        # self.create_room(room1)
        # self.create_room(room2)
        #
        # # connect them with a tunnel
        # self.create_h_tunnel(6, 6, 1)
