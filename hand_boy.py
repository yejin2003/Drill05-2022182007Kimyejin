import random
import math
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

hand = load_image('hand_arrow.png')
TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

char_x, char_y = TUK_WIDTH // 2, TUK_HEIGHT // 2
char_speed = 5


direction = 0


def move_character_to_target(char_x, char_y, target_x, target_y):
    global direction

    dir_x = target_x - char_x
    dir_y = target_y - char_y

    angle = math.degrees(math.atan2(dir_y, dir_x))

    char_x += char_speed * math.cos(math.radians(angle))
    char_y += char_speed * math.sin(math.radians(angle))

    char_x = clamp(0, char_x, TUK_WIDTH)
    char_y = clamp(0, char_y, TUK_HEIGHT)

    if 90 < angle < 270:
        direction = 1
    else:
        direction = 0

    return char_x, char_y, angle

while True:
    hand_x, hand_y = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

    while True:
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        char_x, char_y, angle = move_character_to_target(char_x, char_y, hand_x, hand_y)

        if direction == 0:
            character.clip_draw(0, 100, 100, 100, char_x, char_y)
        else:
            character.clip_draw(0, 0, 100, 100, char_x, char_y)

        hand.draw(hand_x, hand_y)

        update_canvas()
        delay(0.03)

        if abs(char_x - hand_x) < char_speed and abs(char_y - hand_y) < char_speed:
            break

close_canvas()