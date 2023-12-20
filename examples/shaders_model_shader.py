
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    set_config_flags(FLAG_MSAA_4X_HINT)

    init_window(screenWidth, screenHeight, "raylib [shaders] example - model shader")

    camera = Camera()
    camera.position  = Vector3(4.0, 4.0, 4.0)
    camera.target  = Vector3(0.0, 1.0, -1.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    model = load_model("resources/models/watermill.obj")
    texture = load_texture("resources/models/watermill_diffuse.png")
    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/grayscale.fs")
    model.materials[0].shader  = shader
    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture

    position = Vector3(0.0, 0.0, 0.0)

    disable_cursor()

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(camera.byref, CAMERA_FIRST_PERSON)

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode3d(camera)
        draw_model(model, position, 0.2, WHITE)
        draw_grid(10, 1.0)
        end_mode3d()

        draw_text("(c) Watermill 3D model by Alberto Cano", screenWidth - 210, screenHeight - 20, 10, GRAY)
        draw_fps(10, 10)

        end_drawing()

    unload_shader(shader)
    unload_texture(texture)
    unload_model(model)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())