# core_input_keys.py
from raylibpy import *


def main():

    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - keyboard input")

    ball_position: Vector2 = Vector2(screen_width / 2., screen_height / 2.)

    set_target_fps(60)

    while not window_should_close():

        if is_key_down(KEY_RIGHT):
            ball_position.x += 2.0
        if is_key_down(KEY_LEFT):
            ball_position.x -= 2.0
        if is_key_down(KEY_UP):
            ball_position.y -= 2.0
        if is_key_down(KEY_DOWN):
            ball_position.y += 2.0

        begin_drawing()

        clear_background(RAYWHITE)
        
        draw_text("move the ball with arrow keys", 10, 10, 20, DARKGRAY)

        draw_circle_v(ball_position, 50, MAROON)
        
        end_drawing()

    close_window()


if __name__ == '__main__':
    main()