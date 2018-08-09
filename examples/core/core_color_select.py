# core_color_select.py

from raylibpy import *
from typing import List


def main():

    init_window(800, 450, "raylib [core] example - color selection")

    colors: List[Color] = [
        DARKGRAY, MAROON, ORANGE, DARKGREEN, DARKBLUE, DARKPURPLE, DARKBROWN,
        GRAY, RED, GOLD, LIME, BLUE, VIOLET, BROWN, LIGHTGRAY, PINK, YELLOW,
        GREEN, SKYBLUE, PURPLE, BEIGE
    ]

    color_rects: List[Rectangle] = []

    for i in range(21):
        y, x = divmod(i, 7)
        rect = Rectangle(
            20 + 110 * x,
            60 + 110 * y,
            100,
            100
        )
        print(rect)
        color_rects.append(rect)

    selected: List[bool] = [False for i in range(21)]
    mouse_point: Vector2

    set_target_fps(60)

    while not window_should_close():

        mouse_point = get_mouse_position()

        for i in range(21):
            if check_collision_point_rec(mouse_point, color_rects[i]):
                colors[i].a = 120

                if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
                    selected[i] = not selected[i]
            else:
                colors[i].a = 255


        begin_drawing()

        clear_background(RAYWHITE)

        for i in range(21):
            draw_rectangle_rec(color_rects[i], colors[i])

            if selected[i]:
                draw_rectangle(color_rects[i].x, color_rects[i].y, 100, 10, RAYWHITE)
                draw_rectangle(color_rects[i].x, color_rects[i].y, 10, 100, RAYWHITE)
                draw_rectangle(color_rects[i].x + 90, color_rects[i].y, 10, 100, RAYWHITE)
                draw_rectangle(color_rects[i].x, color_rects[i].y + 90, 100, 10, RAYWHITE)

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()