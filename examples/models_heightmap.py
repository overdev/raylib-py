
import sys
import os
from ctypes import byref
from raylibpy import *

def main():

    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - heightmap loading and drawing")

    camera = Camera()
    camera.position  = Vector3(18.0, 21.0, 18.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    image = load_image("resources/heightmap.png")
    texture = load_texture_from_image(image)
    mesh = gen_mesh_heightmap(image, Vector3(16, 8, 16))
    model = load_model_from_mesh(mesh)
    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture

    mapPosition = Vector3(-8.0, 0.0, -8.0)

    unload_image(image)

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(camera.byref, CAMERA_ORBITAL)

        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)
        draw_model(model, mapPosition, 1.0, RED)
        draw_grid(20, 1.0)

        end_mode3d()

        draw_texture(texture, screenWidth - texture.width - 20, 20, WHITE)
        draw_rectangle_lines(screenWidth - texture.width - 20, 20, texture.width, texture.height, GREEN)
        draw_fps(10, 10)

        end_drawing()

    # end loop
    unload_texture(texture)
    unload_model(model)
    close_window()
    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())