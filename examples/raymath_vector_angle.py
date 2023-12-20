
import sys
import os
from ctypes import byref
from raylibpy import *
# import raymath.h

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [math] example - vector angle")

    v0 = Vector2(screenWidth / 2, screenHeight / 2)
    v1 = v0 + Vector2(100.0, 80.0)
    v2 = Vector2()
    angle = 0.0
    angleMode = 0

    set_target_fps(60)
    
    while not window_should_close():
        startangle = 0.0
        
        if angleMode == 0:
            startangle  = -vector2_line_angle(v0, v1) * RAD2DEG
        
        if angleMode == 1:
            startangle  = 0.0
        v2  = get_mouse_position()
        
        if is_key_pressed(KEY_SPACE):
            angleMode = not angleMode
        
        if angleMode == 0 and is_mouse_button_down(MOUSE_BUTTON_RIGHT):
            v1  = get_mouse_position()
        
        if angleMode == 0:
            v1Normal = vector2_normalize(vector2_subtract(v1, v0))
            v2Normal = vector2_normalize(vector2_subtract(v2, v0))
            angle  = vector2_angle(v1Normal, v2Normal) * RAD2DEG
        elif angleMode == 1:
            angle  = vector2_line_angle(v0, v2) * RAD2DEG

        begin_drawing()

        clear_background(RAYWHITE)
        
        if angleMode == 0:
            draw_text("MODE 0: Angle between V1 and V2", 10, 10, 20, BLACK)
            draw_text("Right Click to Move V2", 10, 30, 20, DARKGRAY)
            draw_line_ex(v0, v1, 2.0, BLACK)
            draw_line_ex(v0, v2, 2.0, RED)
            draw_circle_sector(v0, 40.0, startangle, startangle + angle, 32, fade(GREEN, 0.6))

        elif angleMode == 1:
            draw_text("MODE 1: Angle formed by line V1 to V2", 10, 10, 20, BLACK)
            draw_line(0, screenHeight / 2, screenWidth, screenHeight / 2, LIGHTGRAY)
            draw_line_ex(v0, v2, 2.0, RED)
            draw_circle_sector(v0, 40.0, startangle, startangle - angle, 32, fade(GREEN, 0.6))

        draw_text("v0", v0.x, v0.y, 10, DARKGRAY)
        
        if angleMode == 0 and vector2_subtract(v0, v1).y > 0.0:
            draw_text("v1", v1.x, v1.y - 10.0, 10, DARKGRAY)
        
        if angleMode == 0 and vector2_subtract(v0, v1).y < 0.0:
            draw_text("v1", v1.x, v1.y, 10, DARKGRAY)
        
        if angleMode == 1:
            draw_text("v1", v0.x + 40.0, v0.y, 10, DARKGRAY)

        draw_text("v2", v2.x - 10.0, v2.y - 10.0, 10, DARKGRAY)
        draw_text("Press SPACE to change MODE", 460, 10, 20, DARKGRAY)
        draw_text(text_format("ANGLE: %2.2f", Float(angle)), 10, 70, 20, LIME)

        end_drawing()

    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())