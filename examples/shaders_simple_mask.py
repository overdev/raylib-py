
import sys
import os
from ctypes import byref
from raylibpy import *


GLSL_VERSION = 330

def main():
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [shaders] example - simple shader mask")

    camera = Camera()
    camera.position  = Vector3(0.0, 1.0, 2.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    torus = gen_mesh_torus(0.3, 1, 16, 32)
    model1 = load_model_from_mesh(torus)
    cube = gen_mesh_cube(0.8, 0.8, 0.8)
    model2 = load_model_from_mesh(cube)
    sphere = gen_mesh_sphere(1, 16, 16)
    model3 = load_model_from_mesh(sphere)
    shader = load_shader(None, "resources/shaders/glsl{GLSL_VERSION}/mask.fs")

    texDiffuse = load_texture("resources/plasma.png")
    model1.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texDiffuse
    model2.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texDiffuse

    texMask = load_texture("resources/mask.png")
    model1.materials[0].maps[MATERIAL_MAP_EMISSION].texture  = texMask
    model2.materials[0].maps[MATERIAL_MAP_EMISSION].texture  = texMask

    shader.locs[SHADER_LOC_MAP_EMISSION]  = get_shader_location(shader, "mask")
    shaderFrame = get_shader_location(shader, "frame")

    model1.materials[0].shader  = shader
    model2.materials[0].shader  = shader

    framesCounter = 0
    rotation = Vector3(0)

    disable_cursor()

    set_target_fps(60)

    while not window_should_close():
        update_camera(camera.byref, CAMERA_FIRST_PERSON)

        framesCounter += 1

        rotation.x  += 0.01
        rotation.y  += 0.005
        rotation.z  -= 0.0025

        set_shader_value(shader, shaderFrame, byref(Int(framesCounter)), SHADER_UNIFORM_INT)
        model1.transform  = matrix_rotate_xyz(rotation)

        with drawing():
            clear_background(DARKBLUE)

            with mode3d(camera):
                draw_model(model1, Vector3(0.5, 0.0, 0.0), 1, WHITE)
                draw_model_ex(model2, Vector3(-0.5, 0.0, 0.0), Vector3(1.0, 1.0, 0.0), 50, Vector3(1.0, 1.0, 1.0), WHITE)
                draw_model(model3, Vector3(0.0, 0.0, -1.5), 1, WHITE)

                draw_grid(10, 1.0)

            # end_mode3d()

            draw_rectangle(16, 698, measure_text(f"Frame: {framesCounter}", 20) + 8, 42, BLUE)
            draw_text(f"Frame: {framesCounter}", 20, 700, 20, WHITE)

            draw_fps(10, 10)

        # end_drawing()

    unload_model(model1)
    unload_model(model2)
    unload_model(model3)

    unload_texture(texDiffuse)
    unload_texture(texMask)

    unload_shader(shader)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())