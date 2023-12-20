
import sys
import os
from ctypes import byref
from raylibpy import *

GLSL_VERSION = 330

def main():

    screenWidth = 800
    screenHeight = 450

    set_config_flags(FLAG_MSAA_4X_HINT)

    init_window(screenWidth, screenHeight, "raylib [shaders] example - custom uniform variable")

    camera = Camera(0)
    camera.position  = Vector3(8.0, 8.0, 8.0)
    camera.target  = Vector3(0.0, 1.5, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE

    model = load_model("resources/models/barracks.obj")
    texture = load_texture("resources/models/barracks_diffuse.png")
    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture

    position = Vector3(0.0, 0.0, 0.0)

    shader = load_shader(None, f"resources/shaders/glsl{GLSL_VERSION}/swirl.fs")
    swirlCenterLoc = get_shader_location(shader, "center")

    swirlCenter = (Float * 2)(screenWidth / 2, screenHeight / 2)

    target = load_render_texture(screenWidth, screenHeight)

    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_ORBITAL)
    
        mousePosition = get_mouse_position()
        swirlCenter[0]  = mousePosition.x
        swirlCenter[1]  = screenHeight - mousePosition.y

        set_shader_value(shader, swirlCenterLoc, swirlCenter, SHADER_UNIFORM_VEC2)
    
        with texture_mode(target):
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_model(model, position, 0.5, WHITE)
                draw_grid(10, 1.0)
            # end_mode3d()

            draw_text("TEXT DRAWN IN RENDER TEXTURE", 200, 10, 30, RED)
        # end_texture_mode()

        with drawing():
            clear_background(RAYWHITE)

            with shader_mode(shader):
                draw_texture_rec(target.texture, Rectangle(0, 0, target.texture.width, target.texture.height), Vector2(0, 0), WHITE)
            # end_shader_mode()

            draw_text("(c) Barracks 3D model by Alberto Cano", screenWidth - 220, screenHeight - 20, 10, GRAY)
            draw_fps(10, 10)

        # end_drawing()

    unload_shader(shader)
    unload_texture(texture)
    unload_model(model)
    unload_render_texture(target)

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())