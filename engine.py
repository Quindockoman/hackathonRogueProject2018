import tcod
import csv
import sys
from theMap import *
from Item import *
from Monster import *
from Event import *

color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)

GAME_HEIGHT = 16
GAME_WIDTH = 16

itemList = []
# csv item reader
with open('items.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        itemList.append(row)
# print(itemList)

playerList = []
# csv item reader
with open('players.csv','r') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        playerList.append(row)
# print(playerList)

def render_all(mapToUse, con):
    global color_light_wall
    global color_light_ground

    # for y in range(GAME_HEIGHT):
    #     for x in range(GAME_WIDTH):
    #         tcod.console_put_char(con, x, y, " ", tcod.BKGND_NONE)

    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            if(mapToUse.map[x][y].charToken != ""):
                # newCharCode = 7
                img = None
                # print(mapToUse.map[x][y].charToken)
                if(mapToUse.map[x][y].charToken == "S"):
                    # newCharCode += 1
                    img = tcod.image_load("LargeWallS.png")
                if(mapToUse.map[x][y].charToken == "N"):
                    # newCharCode += 2
                    img = tcod.image_load("LargeWallN.png")
                if(mapToUse.map[x][y].charToken == "E"):
                    # newCharCode += 3
                    img = tcod.image_load("largeWallE.png")
                if(mapToUse.map[x][y].charToken == "W"):
                    # newCharCode += 4
                    img = tcod.image_load("largeWallW.png")
                if(mapToUse.map[x][y].charToken == "<"):
                    # newCharCode += 5
                    img = tcod.image_load("LargeSW.png")
                if(mapToUse.map[x][y].charToken == ">"):
                    # newCharCode += 6
                    img = tcod.image_load("LargeSE.png")
                if(mapToUse.map[x][y].charToken == "/"):
                    # newCharCode += 7
                    img = tcod.image_load("LargeNW.png")
                if(mapToUse.map[x][y].charToken == "\\"):
                    # newCharCode += 8
                    img = tcod.image_load("LargeNE.png")
                if(mapToUse.map[x][y].charToken == "."):
                    # newCharCode += 9
                    img = tcod.image_load("LargeFloor.png")
                if(mapToUse.map[x][y].charToken == "w"):
                    # newCharCode += 10
                    img = tcod.image_load("DoorW.png")
                if(mapToUse.map[x][y].charToken == "s"):
                    # newCharCode += 11
                    img = tcod.image_load("DoorS.png")
                if(mapToUse.map[x][y].charToken == "n"):
                    # newCharCode += 12
                    img = tcod.image_load("DoorN.png")
                if(mapToUse.map[x][y].charToken == "e"):
                    # newCharCode += 13
                    img = tcod.image_load("DoorE.png")
                # tcod.console_put_char_ex(con, x, y, newCharCode, tcod.white, tcod.black)
                tcod.image_blit_rect(img, con, x, y, 64, 64, tcod.BKGND_NONE)
                # else:
                #      tcod.console_put_char(con, x, y, "#", tcod.BKGND_NONE)
    for roomIndex in mapToUse.roomList:
        # print("room " + roomIndex.roomName + " player list:")
        # print(roomIndex.playerList)
        # print()
        placeX = roomIndex.x1
        placeY = roomIndex.y1
        for i in range(0, len(roomIndex.playerList)):
            # newCharCode = -1
            img = None
            if(roomIndex.playerList[i].playerNum == "0"):
                print("got here")
                img = tcod.image_load("isaiah.png")
                # newCharCode += 1
            if(roomIndex.playerList[i].playerNum == "1"):
                # newCharCode += 3
                img = tcod.image_load("dave.png")
            if(roomIndex.playerList[i].playerNum == "2"):
                # newCharCode += 4
                img = tcod.image_load("ian.png")
            if(roomIndex.playerList[i].playerNum == "3"):
                # newCharCode += 5
                img = tcod.image_load("richard.png")
            if(roomIndex.playerList[i].playerNum == "4"):
                # newCharCode += 6
                img = tcod.image_load("josh.png")
            if(roomIndex.playerList[i].playerNum == "5"):
                # newCharCode += 7
                img = tcod.image_load("dylan.png")
            if(roomIndex.playerList[i].playerNum == "6"):
                # newCharCode += 8
                img = tcod.image_load("will.png")
            # print(roomIndex.playerList[i].playerNum)
            # print(roomIndex.playerList[i].name[0])
            # print(placeX+1, placeY+1)
            # tcod.console_put_char_ex(con, placeX+1, placeY+1, newCharCode, tcod.white, tcod.black)
            tcod.image_blit_rect(img, con, placeX, placeY, 64, 64, tcod.BKGND_SET)
            if(placeX < roomIndex.x2-2):
                placeX += 1
            else:
                placeX = roomIndex.x1
                if(placeY < roomIndex.y2-1):
                    placeY += 1
                else:
                    placeY = roomIndex.y1

    # blit the contents of "con" to the root console
    tcod.console_blit(con, 0, 0, GAME_WIDTH, GAME_HEIGHT, 0, 0, 0)

def handle_keys(currPlayer, mapToUse):
    global fov_recompute

    #key = tcod.console_check_for_keypress()  #real-time
    key = tcod.console_wait_for_keypress(True)  #turn-based

    if key.vk == tcod.KEY_ESCAPE:
        sys.exit()

    # if key.vk == tcod.KEY_ENTER and key.lalt:
    #     #Alt+Enter: toggle fullscreen
    #     tcod.console_set_fullscreen(not tcod.console_is_fullscreen())

    #movement keys
    if tcod.console_is_key_pressed(tcod.KEY_UP):
        mapToUse.movePlayer(currPlayer, 0)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_DOWN):
        mapToUse.movePlayer(currPlayer, 2)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_LEFT):
        mapToUse.movePlayer(currPlayer, 3)
        fov_recompute = True

    elif tcod.console_is_key_pressed(tcod.KEY_RIGHT):
        mapToUse.movePlayer(currPlayer, 1)
        fov_recompute = True


def load_customfont():
    print("did not crash")
    #The index of the first custom tile in the file
    a = 160

    #The "y" is the row index, here we load the sixth row in the font file. Increase the "6" to load any new rows from the file
    for y in range(5, 6):
        tcod.console_map_ascii_codes_to_font(a, 32, 0, y)
        a += 32

def main():
    # player_x = int(screen_width / 2)
    # player_y = int(screen_height / 2)

    # tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)
    # tcod.console_set_custom_font('hontfont.png', tcod.FONT_TYPE_GRAYSCALE | tcod.FONT_LAYOUT_TCOD, 32, 10)
    tcod.console_set_custom_font('hontfont.png', tcod.FONT_LAYOUT_ASCII_INROW, 32, 9)
    load_customfont()
    print("here")
    tcod.console_init_root(GAME_WIDTH, GAME_HEIGHT, 'tcod tutorial revised', False)
    con = tcod.console_new(GAME_WIDTH, GAME_HEIGHT)

    key = tcod.Key()
    mouse = tcod.Mouse()

    gameMap = Map(GAME_WIDTH, GAME_HEIGHT, 9)
    gameMap.make_map()
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i])

    newItem = item(itemList[0])
    gameMap.insert_item(newItem, gameMap.roomList[1])
    # print(gameMap.roomList[0].itemList)

    playersToTakeTurn = []
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i].playerList)
    p1 = player(playerList[0])
    gameMap.insert_player(p1, 0)
    playersToTakeTurn.append(p1)
    p2 = player(playerList[1])
    gameMap.insert_player(p2, 0)
    playersToTakeTurn.append(p2)
    p3 = player(playerList[2])
    gameMap.insert_player(p3, 0)
    playersToTakeTurn.append(p3)
    p4 = player(playerList[3])
    gameMap.insert_player(p4, 0)
    playersToTakeTurn.append(p4)
    p5 = player(playerList[4])
    gameMap.insert_player(p5, 0)
    playersToTakeTurn.append(p5)
    p6 = player(playerList[5])
    gameMap.insert_player(p6, 0)
    playersToTakeTurn.append(p6)
    p7 = player(playerList[6])
    gameMap.insert_player(p7, 0)
    playersToTakeTurn.append(p7)
    # for i in range(0, len(gameMap.roomList)):
    #     print(gameMap.roomList[i].playerList)

    while not tcod.console_is_window_closed():
        # tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        # tcod.console_set_default_foreground(0, tcod.white)
        render_all(gameMap, con)

        tcod.console_flush()

        # key = tcod.console_check_for_keypress()

        for i in range(0, len(gameMap.roomList)):
            print("room: ", i, " has ", len(gameMap.roomList[i].playerList), " players")
            for j in range(0, len(gameMap.roomList[i].playerList)):
                print(gameMap.roomList[i].playerList[j].name)

        # print(playersToTakeTurn)
        for p in playersToTakeTurn:
            print(p.name + "'s  turn")
            handle_keys(p, gameMap)
            # render_all(gameMap, con)


if __name__ == '__main__':
    main()
