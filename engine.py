import tcod
from theMap import *
from Item import *
from Monster import *
from Event import *

color_dark_wall = tcod.Color(0, 0, 100)
color_dark_ground = tcod.Color(50, 50, 150)

GAME_HEIGHT = 50
GAME_WIDTH = 50

def render_all(mapToUse, con):
    global color_light_wall
    global color_light_ground

    #go through all tiles, and set their background color
    for y in range(GAME_HEIGHT):
        for x in range(GAME_WIDTH):
            wall = mapToUse.map[x][y].blocked
            if wall:
                # tcod.console_set_char_background(con, x, y, color_dark_wall, tcod.BKGND_SET)
                tcod.console_put_char(con, x, y, "#", tcod.BKGND_NONE)
            else:
                # tcod.console_set_char_background(con, x, y, color_dark_ground, tcod.BKGND_SET)
                if(mapToUse.map[x][y].charToken != ""):
                    tcod.console_put_char(con, x, y, mapToUse.map[x][y].charToken, tcod.BKGND_NONE)
    # blit the contents of "con" to the root console
    tcod.console_blit(con, 0, 0, GAME_WIDTH, GAME_HEIGHT, 0, 0, 0)

def main():
    # player_x = int(screen_width / 2)
    # player_y = int(screen_height / 2)

    tcod.console_set_custom_font('arial10x10.png', tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    tcod.console_init_root(GAME_WIDTH, GAME_HEIGHT, 'libtcod tutorial revised', False)
    con = tcod.console_new(GAME_WIDTH, GAME_HEIGHT)

    key = tcod.Key()
    mouse = tcod.Mouse()

    gameMap = Map(GAME_WIDTH, GAME_HEIGHT, 9)
    gameMap.make_map()

    while not tcod.console_is_window_closed():
        # tcod.sys_check_for_event(tcod.EVENT_KEY_PRESS, key, mouse)

        tcod.console_set_default_foreground(0, tcod.white)
        # tcod.console_put_char(0, player_x, player_y, '@', tcod.BKGND_NONE)
        render_all(gameMap, con)

        tcod.console_flush()

        key = tcod.console_check_for_keypress()

        if key.vk == tcod.KEY_ESCAPE:
            return True


if __name__ == '__main__':
    main()
