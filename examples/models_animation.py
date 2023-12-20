
import sys
import os
from ctypes import byref
from raylibpy import *

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - model animation")
    camera = Camera(0)
    camera.position  = Vector3(10.0, 10.0, 10.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    model = load_model("resources/models/iqm/guy.iqm")
    texture = load_texture("resources/models/iqm/guytex.png")
    set_material_texture(byref(model.materials[0]), MATERIAL_MAP_ALBEDO, texture)

    position = Vector3(0.0, 0.0, 0.0)

    anims = load_model_animations("resources/models/iqm/guyanim.iqm", 0)
    animsCount = len(anims)
    animFrameCounter = 0

    disable_cursor()

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_FIRST_PERSON)
        
        if is_key_down(KEY_SPACE):
            animFrameCounter += 1
            update_model_animation(model, anims[0], animFrameCounter)
            
            if animFrameCounter >= anims[0].frame_count:
                animFrameCounter  = 0
    
        with drawing():

            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_model_ex(model, position, Vector3(1.0, 0.0, 0.0), -90.0, Vector3(1.0, 1.0, 1.0), WHITE)
                draw_grid(10, 1.0)

            # end_mode3d()

            draw_text("PRESS SPACE to PLAY MODEL ANIMATION", 10, 10, 20, MAROON)
            draw_text("(c) Guy IQM 3D model by @culacant", screenWidth - 200, screenHeight - 20, 10, GRAY)

        # end_drawing()
    
    unload_texture(texture)
    unload_model_animations(anims, animsCount)
    unload_model(model)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())