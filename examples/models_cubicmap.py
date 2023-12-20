
import sys
import os
from ctypes import byref
from raylibpy import *

def main():
    """Transpiled function."""
    screenWidth = 800
    screenHeight = 450
    init_window(screenWidth, screenHeight, "raylib [models] example - cubesmap loading and drawing")

    camera = Camera()
    camera.position  = Vector3(16.0, 14.0, 16.0)
    camera.target  = Vector3(0.0, 0.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    image = load_image("resources/cubicmap.png")
    cubicmap = load_texture_from_image(image)
    mesh = gen_mesh_cubicmap(image, Vector3(1.0, 1.0, 1.0))
    model = load_model_from_mesh(mesh)
    texture = load_texture("resources/cubicmap_atlas.png")

    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture
    mapPosition = Vector3(-16.0, 0.0, -8.0)

    unload_image(image)

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(camera.byref, CAMERA_ORBITAL)

        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_model(model, mapPosition, 1.0, WHITE)
            # end_mode3d()

            draw_texture_ex(cubicmap, Vector2(screenWidth - cubicmap.width * 4.0 - 20, 20.0), 0.0, 4.0, WHITE)
            draw_rectangle_lines(screenWidth - cubicmap.width * 4 - 20, 20, cubicmap.width * 4, cubicmap.height * 4, GREEN)
            draw_text("cubicmap image used to", 658, 90, 10, GRAY)
            draw_text("generate map 3d model", 658, 104, 10, GRAY)
            draw_fps(10, 10)

        # end_drawing()

    unload_texture(cubicmap)
    unload_texture(texture)
    unload_model(model)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())