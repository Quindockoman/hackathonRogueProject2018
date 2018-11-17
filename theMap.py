import tcod
import math

roomNameList = ["library", "study", "crypt", "foyer", "kitchen", "dining hall", "master bedroom", "garden", "closet"]

class Tile:
    blocked = False
    charToken = ""
    #a tile of the map and its properties
    def __init__(self, blocked):
        self.blocked = blocked

class Room:
    connectedUp = False
    connectedDown = False
    connectedLeft = False
    connectedRight = False
    roomDiscovered = False
    roomName = ""
    playerList = []
    itemList = []
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    spdPenalty = 1

    def __init__(self, x1, x2, y1, y2, nameOfRoom):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.roomName = nameOfRoom
        self.playerList = []
        self.itemList = []
        self.roomDiscovered = False
        self.connectedUp = False
        self.connectedDown = False
        self.connectedLeft = False
        self.connectedRight = False

class Map:
    maxHeight = 0
    maxWidth = 0
    numRooms = 0
    map = []
    roomList = []

    def __init__(self, maxHeight, maxWidth, numRooms):
        self.maxHeight = maxHeight
        self.maxWidth = maxWidth
        self.numRooms = numRooms

    def movePlayer(self, playerToMove, direction):
        moveAdjuster = math.sqrt(self.numRooms)
        # find the room the player is in
        playerRoomIndex = -1
        for i in range(0, len(self.roomList)):
            for i2 in range(0, len(self.roomList[i].playerList)):
                # print(self.roomList[i].playerList[i2].name)
                # print(playerToMove.name)    ``
                if(playerToMove.name == self.roomList[i].playerList[i2].name):
                    playerRoomIndex = i
                    print("matched " + playerToMove.name + " to " + self.roomList[i].playerList[i2].name + " in room " + str(i))
        print("direction",direction)
        print("room connections","up: ",self.roomList[playerRoomIndex].connectedUp,"down: ",self.roomList[playerRoomIndex].connectedDown,"left: " ,self.roomList[playerRoomIndex].connectedLeft,"right: ",self.roomList[playerRoomIndex].connectedRight)
        newRoomIndex = -1
        if(direction == 0):
            print("moving player " + playerToMove.name + " up to room index " + str(playerRoomIndex - 3) + " from room index " + str(playerRoomIndex))
            print(self.roomList[playerRoomIndex].connectedUp)
            if(self.roomList[playerRoomIndex].connectedUp == True):
                self.remove_player(playerToMove, playerRoomIndex)
                self.insert_player(playerToMove, playerRoomIndex - 3)
                newRoomIndex = playerRoomIndex - 3
            else:
                print("invalid move")
        elif(direction == 1):
            print("moving player " + playerToMove.name + " right to room index " + str(playerRoomIndex + 1) + " from room index " + str(playerRoomIndex))
            print(self.roomList[playerRoomIndex].connectedRight)
            if(self.roomList[playerRoomIndex].connectedRight == True):
                self.remove_player(playerToMove,playerRoomIndex)
                self.insert_player(playerToMove, playerRoomIndex + 1)
                newRoomIndex = playerRoomIndex + 1
            else:
                print("invalid move")
        elif(direction == 2):
            print("moving player " + playerToMove.name + " down to room index " + str(playerRoomIndex + 3) + " from room index " + str(playerRoomIndex))
            print(self.roomList[playerRoomIndex].connectedDown)
            if(self.roomList[playerRoomIndex].connectedDown == True):
                self.remove_player(playerToMove, playerRoomIndex)
                self.insert_player(playerToMove, playerRoomIndex + 3)
                newRoomIndex = playerRoomIndex + 3
            else:
                print("invalid move")
        elif(direction == 3):
            print("moving player " + playerToMove.name + " left to room index " + str(playerRoomIndex - 1) + " from room index " + str(playerRoomIndex))
            print(self.roomList[playerRoomIndex].connectedLeft)
            if(self.roomList[playerRoomIndex].connectedLeft == True):
                self.remove_player(playerToMove, playerRoomIndex)
                self.insert_player(playerToMove, playerRoomIndex - 1)
                newRoomIndex = playerRoomIndex - 1
            else:
                print("invalid move")

        if(newRoomIndex != -1):
            if(self.roomList[newRoomIndex].roomDiscovered == False):
                self.roomList[newRoomIndex].roomDiscovered = True
                for newItem in self.roomList[newRoomIndex].itemList:
                    playerToMove.dumpStats()
                    playerToMove.pickup(newItem)
                    print(playerToMove.name + " picked up " + newItem.name)
                    playerToMove.dumpStats()


    def insert_player(self, newPlayer, roomNum):
        print("roomnum",roomNum)
        # if(len(self.roomList[roomNum].playerList) > 8):
        #     print("too many players in room")
        # else:
        self.roomList[roomNum].playerList.append(newPlayer)
        print("players now in room:")
        for i in range(0, len(self.roomList[roomNum].playerList)):
            print(self.roomList[roomNum].playerList[i].name)

    def remove_player(self, playerToRemove, roomNum):
        self.roomList[roomNum].playerList.remove(playerToRemove)

    def insert_item(self, newItem, room):
        room.itemList.append(newItem)

    def create_room(self, room):
        # go through the tiles in the rectangle and make them passable
        self.map[room.x1][room.y1].charToken = "/"
        self.map[room.x1+1][room.y1].charToken = "N"
        self.map[room.x1+2][room.y1].charToken = "N"
        self.map[room.x1+3][room.y1].charToken = "N"
        self.map[room.x1+4][room.y1].charToken = "\\"
        self.map[room.x1+4][room.y1+1].charToken = "E"
        self.map[room.x1+4][room.y1+2].charToken = "E"
        self.map[room.x1+4][room.y1+3].charToken = "E"
        self.map[room.x1+4][room.y1+4].charToken = ">"
        self.map[room.x1+3][room.y1+4].charToken = "S"
        self.map[room.x1+2][room.y1+4].charToken = "S"
        self.map[room.x1+1][room.y1+4].charToken = "S"
        self.map[room.x1][room.y1+4].charToken = "<"
        self.map[room.x1][room.y1+3].charToken = "W"
        self.map[room.x1][room.y1+2].charToken = "W"
        self.map[room.x1][room.y1+1].charToken = "W"
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

    def create_ndoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "n"

    def create_sdoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "s"

    def create_wdoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "w"

    def create_edoor(self, x, y):
        self.map[x][y].blocked = False
        self.map[x][y].charToken = "e"

    def connectRooms(self, r1, r2):
        numRoomsSqrd = int(math.sqrt(self.numRooms))
        # connect to above room
        if(r2 == r1 - numRoomsSqrd):
            self.create_ndoor(self.roomList[r1].x1+2, self.roomList[r1].y1)
            self.roomList[r1].connectedUp = True
            self.create_sdoor(self.roomList[r2].x1+2, self.roomList[r2].y2)
            self.roomList[r2].connectedDown = True
        # connect to right room
        if(r2 == r1 + 1):
            self.create_edoor(self.roomList[r1].x2, self.roomList[r1].y1+2)
            self.roomList[r1].connectedRight = True
            self.create_wdoor(self.roomList[r2].x1, self.roomList[r2].y1+2)
            self.roomList[r2].connectedLeft = True
        # connect to room below
        if(r2 == r1 + numRoomsSqrd):
            self.create_sdoor(self.roomList[r1].x1+2, self.roomList[r1].y2)
            self.roomList[r1].connectedDown = True
            self.create_ndoor(self.roomList[r2].x1+2, self.roomList[r2].y1)
            self.roomList[r2].connectedUp = True
        # connect to room to left
        if(r2 == r1 - 1):
            self.create_wdoor(self.roomList[r1].x1, self.roomList[r1].y1+2)
            self.roomList[r1].connectedLeft = True
            self.create_edoor(self.roomList[r2].x2, self.roomList[r2].y1+2)
            self.roomList[r2].connectedRight = True

    def make_map(self):
        # fill map with "blocked" tiles
        self.map = [
            [Tile(True) for y in range(self.maxHeight)]
            for x in range(self.maxWidth)
         ]

        numRoomsSqrd = int(math.sqrt(self.numRooms))
        xStart = 0
        xEnd = 4
        yStart = 0
        yEnd = 4
        for i in range(1, self.numRooms+1):
            # print(xStart, xEnd, yStart, yEnd)
            newRoom = Room(xStart, xEnd, yStart, yEnd, roomNameList[i-1])
            self.create_room(newRoom)
            self.roomList.append(newRoom)
            xStart += 5
            xEnd += 5
            if(i > 0 and i % numRoomsSqrd == 0):
                yStart += 5
                yEnd += 5
                xStart = 0
                xEnd = 4
        for r in range(0, len(self.roomList)):
            if(r-numRoomsSqrd >= 0):
                self.connectRooms(r, r-numRoomsSqrd)
            if(r-1 >= 0 and r % numRoomsSqrd != 0):
                self.connectRooms(r, r-1)
            if(r+1 < len(self.roomList) and r % numRoomsSqrd != 0):
                self.connectRooms(r, r+1)
            if(r+numRoomsSqrd < len(self.roomList)):
                self.connectRooms(r, r+numRoomsSqrd)
