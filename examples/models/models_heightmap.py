# *******************************************************************************************
# 
#    raylib [models] example - Heightmap loading and drawing
# 
#    This example has been created using raylib 1.8 (www.raylib.com)
#    raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#    Copyright (c) 2015 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************

from raylibpy import *

def main() -> int:

    # Initialization
    # -------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [models] example - heightmap loading and drawing")

    camera: Camera3D = Camera3D(Vector3(18., 16., 18.), Vector3.zero(), Vector3(0., 1., 0.), 45., 0)

    image: Image = load_image("resources/heightmap.png")
    texture: Texture2D = load_texture_from_image(image)

    mesh: Mesh = gen_mesh_heightmap(image, Vector3(16., 8., 16.))
    model: Model = load_model_from_mesh(mesh)

    model.material.maps[MAP_DIFFUSE].texture = texture
    map_position: Vector3 = Vector3(-8., 0., -8.)

    unload_image(image)

    set_camera_mode(camera, CAMERA_ORBITAL)

    set_target_fps(60)
    # -------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():
        update_camera(byref(camera))

        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_model(model, map_position, 1., RED)
        draw_grid(20, 1.)

        end_mode3d()

        draw_texture(texture, screen_width - texture.width - 20, 20, WHITE)
        draw_rectangle_lines(screen_width - texture.width - 20, 20, texture.width, texture.height, GREEN)

        draw_fps(5, 5)

        end_drawing()

    unload_texture(texture)
    unload_model(model)

    close_window()

    return 0


if __name__ == '__main__':
    main()