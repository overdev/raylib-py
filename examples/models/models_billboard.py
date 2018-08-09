# models_billboard.py

from raylibpy import *

def main() -> int:

    # Initialization
    # -------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylibpy [models] example - drawing billboard")

    # Define the camera to look into our 3d world
    camera: Camera = Camera()
    camera.position = Vector3(5., 4., 5.)
    camera.target = Vector3(0., 2., 0.)
    camera.up = Vector3(0., 1., 0.)
    camera.fovy = 45.0
    camera.type = CAMERA_PERSPECTIVE

    print(camera)


    bill: Texture2D = load_texture("resources/billboard.png")
    bill_position = Vector3(0., 2., 0.)

    set_camera_mode(camera, CAMERA_ORBITAL)

    set_target_fps(60)

    # Main game loop
    while not window_should_close():
        # Update
        # ---------------------------------------------------------------------------------
        update_camera(byref(camera))
        # ----------------------------------------------------------------------------------

        # Draw
        # ---------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_billboard(camera, bill, bill_position, 2., WHITE)
        
        draw_grid(10, 1.0)

        end_mode3d()

        draw_fps(10, 10)

        end_drawing()
        # ---------------------------------------------------------------------------------

    # De-Initialization
    # -------------------------------------------------------------------------------------
    unload_texture(bill)

    close_window()
    # -------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()