# shapes_easings_rectangle_array.py
# ******************************************************************************************
# 
#   raylib [shapes] example - easings rectangle array
# 
#   NOTE: This example requires 'easings.h' library, provided on raylib/src. Just copy
#   the library to same directory as example or make sure it's available on include path.
# 
#   This example has been created using raylib 2.0 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2014-2019 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/


from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *
from raylibpy.easings import *

RECS_WIDTH = 50
RECS_HEIGHT = 50

MAX_RECS_X = 800 // RECS_WIDTH
MAX_RECS_Y = 450 // RECS_HEIGHT

PLAY_TIME_IN_FRAMES = 240  # At 60 fps = 4 seconds


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [shapes] example - easings rectangle array")

    size: int = MAX_RECS_X * MAX_RECS_Y
    recs: Array[Rectangle] = (Rectangle * size)(*[Rectangle() for _ in range(size)])

    for y in range(MAX_RECS_Y):
        for x in range(MAX_RECS_X):
            recs[y * MAX_RECS_X + x].x = RECS_WIDTH / 2 + RECS_WIDTH * x
            recs[y * MAX_RECS_X + x].y = RECS_HEIGHT / 2 + RECS_HEIGHT * y
            recs[y * MAX_RECS_X + x].width = RECS_WIDTH
            recs[y * MAX_RECS_X + x].height = RECS_HEIGHT

    rotation: float = 0.0
    frames_counter: int = 0
    state: int = 0  # Rectangles animation state: 0-Playing, 1-Finished

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        if state == 0:
            frames_counter += 1

            for i in range(size):
                recs[i].height = ease_circ_out(frames_counter, RECS_HEIGHT, -RECS_HEIGHT, PLAY_TIME_IN_FRAMES)
                recs[i].width = ease_circ_out(frames_counter, RECS_WIDTH, -RECS_WIDTH, PLAY_TIME_IN_FRAMES)

                if recs[i].height < 0:
                    recs[i].height = 0
                if recs[i].width < 0:
                    recs[i].width = 0

                if recs[i].height == 0 and recs[i].width == 0:
                    state = 1  # Finish playing

                rotation = ease_linear_in(frames_counter, 0.0, 360.0, PLAY_TIME_IN_FRAMES)

        elif state == 1 and is_key_pressed(KEY_SPACE):
            # When animation has finished, press space to restart
            frames_counter = 0

            for i in range(size):
                recs[i].height = RECS_HEIGHT
                recs[i].width = RECS_WIDTH

            state = 0
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(RAYWHITE)

            if state == 0:
                for i in range(size):
                    draw_rectangle_pro(recs[i], Vector2(recs[i].width / 2, recs[i].height / 2), rotation, RED)
            elif state == 1:
                draw_text("PRESS [SPACE] TO PLAY AGAIN!", 240, 200, 20, GRAY)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
