
import sys
import os
from ctypes import byref
from raylibpy import *

def main():
    """Transpiled function."""
    screenWidth = 800
    screenHeight = 450
    init_window(screenWidth, screenHeight, "raylib [models] example - models loading")
    camera = Camera(0)
    camera.position  = Vector3(50.0, 50.0, 50.0)
    camera.target  = Vector3(0.0, 10.0, 0.0)
    camera.up  = Vector3(0.0, 1.0, 0.0)
    camera.fovy  = 45.0
    camera.projection  = CAMERA_PERSPECTIVE
    model = load_model("resources/models/obj/castle.obj")
    texture = load_texture("resources/models/obj/castle_diffuse.png")
    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture
    position = Vector3(0.0, 0.0, 0.0)
    bounds = get_mesh_bounding_box(model.meshes[0])
    selected = False
    disable_cursor()
    set_target_fps(60)
    
    while not window_should_close():
        update_camera(byref(camera), CAMERA_FIRST_PERSON)
        
        if is_file_dropped():
            droppedFiles = load_dropped_files()
            
            if droppedFiles.count == 1:
                if (is_file_extension(droppedFiles.paths[0], ".obj")
                        or is_file_extension(droppedFiles.paths[0], ".gltf")
                        or is_file_extension(droppedFiles.paths[0], ".glb")
                        or is_file_extension(droppedFiles.paths[0], ".vox")
                        or is_file_extension(droppedFiles.paths[0], ".iqm")
                        or is_file_extension(droppedFiles.paths[0], ".m3d")):
                    unload_model(model)
                    model  = load_model(droppedFiles.paths[0])
                    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture
                    bounds  = get_mesh_bounding_box(model.meshes[0])

                elif is_file_extension(droppedFiles.paths[0], ".png"):
                    unload_texture(texture)
                    texture  = load_texture(droppedFiles.paths[0])
                    model.materials[0].maps[MATERIAL_MAP_ALBEDO].texture  = texture

            unload_dropped_files(droppedFiles)
        
        if is_mouse_button_pressed(MOUSE_BUTTON_LEFT):
            if get_ray_collision_box(get_mouse_ray(get_mouse_position(), camera), bounds).hit:
                selected  = not selected
            else:
                selected  = False

        begin_drawing()
        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_model(model, position, 1.0, WHITE)
        draw_grid(20, 10.0)
        
        if selected:
            draw_bounding_box(bounds, GREEN)

        end_mode3d()

        draw_text("Drag & drop model to load mesh/texture.", 10, get_screen_height() - 20, 10, DARKGRAY)
        
        if selected:
            draw_text("MODEL SELECTED", get_screen_width() - 110, 10, 10, GREEN)

        draw_text("(c) Castle 3D model by Alberto Cano", screenWidth - 200, screenHeight - 20, 10, GRAY)
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