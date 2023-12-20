
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - texture tiling")

    camera = Camera3D()
    camera.position  = Vector3(4.0, 4.0, 4.0)
    camera.target  = Vector3(0.0, 0.5, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    cube = gen_mesh_cube(1.0, 1.0, 1.0)
    model = load_model_from_mesh(cube)
    texture = load_texture("resources/cubicmap_atlas.png")
    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture

    tiling = (Float * 2)(3.0, 3.0)
    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/tiling.fs")
    set_shader_value(shader, get_shader_location(shader, "tiling"), tiling, SHADER_UNIFORM_VEC2)
    model.materials[0].shader  = shader

    disable_cursor()

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_FREE)
        
        if is_key_pressed(KEY_Z):
            camera.target = Vector3(0.0, 0.5, 0.0)

        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                begin_shader_mode(shader)
                draw_model(model, Vector3(0.0, 0.0, 0.0), 2.0, WHITE)
                end_shader_mode()

                draw_grid(10, 1.0)

            # end_mode3d()

            draw_text("Use mouse to rotate the camera", 10, 10, 20, DARKGRAY)

        # end_drawing()

    unload_model(model)
    unload_shader(shader)
    unload_texture(texture)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())