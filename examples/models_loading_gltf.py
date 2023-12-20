
import sys
import os
from ctypes import byref
from raylibpy import *

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - loading gltf")

    camera = Camera()
    camera.position  = Vector3(5.0, 5.0, 5.0)
    camera.target  = Vector3(0.0, 2.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    model = load_model("resources/models/gltf/robot.glb")
    animsCount = 0
    animIndex = 0
    animCurrentFrame = 0

    modelAnimations = load_model_animations("resources/models/gltf/robot.glb", 0)
    animsCount = len(modelAnimations)
    position = Vector3(0.0, 0.0, 0.0)

    disable_cursor()

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_THIRD_PERSON)
        
        if is_mouse_button_pressed(MOUSE_BUTTON_RIGHT):
            animIndex  = (animIndex + 1) % animsCount
        elif is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            animIndex  = (animIndex + animsCount - 1) % animsCount

        anim = modelAnimations[animIndex]
        animCurrentFrame  = (animCurrentFrame + 1) % anim.frame_count

        update_model_animation(model, anim, animCurrentFrame)

        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)
        draw_model(model, position, 1.0, WHITE)
        draw_grid(10, 1.0)
        end_mode3d()

        draw_text("Use the LEFT/RIGHT mouse buttons to switch animation", 10, 10, 20, GRAY)
        draw_text(f"Animation: {anim.name}", 10, get_screen_height() - 20, 10, DARKGRAY)

        end_drawing()

    unload_model(model)
    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())