# core_3d_picking.py

from raylibpy import *

def main() -> int:

    # Initialization
    # -------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [core] example - 3d picking")

    # Define the camera to look into our 3d world
    camera: Camera = Camera()
    camera.position = Vector3(10., 10., 10.)
    camera.target = Vector3(0., 0., 0.)
    camera.up = Vector3(0., 1., 0.)
    camera.fovy = 45.0
    camera.type = CAMERA_PERSPECTIVE

    cube_position: Vector3 = Vector3(0., 1., 0.)
    cube_size: Vector3 = Vector3(2., 2., 2.)

    ray: Ray = Ray(Vector3(0., 0., 0.))

    collision: bool = False

    set_camera_mode(camera, CAMERA_FREE)

    set_target_fps(60)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():
        # Update
        # ---------------------------------------------------------------------------------
        update_camera(byref(camera))

        if (is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
            ray = get_mouse_ray(get_mouse_position(), camera)

            #
            collision = check_collision_ray_box(
                ray,
                BoundingBox(
                    Vector3(
                        cube_position.x - cube_size.x / 2,
                        cube_position.y - cube_size.y / 2,
                        cube_position.z - cube_size.z / 2,
                    ),
                    Vector3(
                        cube_position.x + cube_size.x / 2,
                        cube_position.y + cube_size.y / 2,
                        cube_position.z + cube_size.z / 2,
                    )
                )
            )
        # ----------------------------------------------------------------------------------

        # Draw
        # ---------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        if collision:
            draw_cube(cube_position, cube_size.x, cube_size.y, cube_size.z, RED)
            draw_cube_wires(cube_position, cube_size.x, cube_size.y, cube_size.z, MAROON)

            draw_cube_wires(cube_position, cube_size.x + .2, cube_size.y + .2, cube_size.z + .2, GREEN)
        else:
            draw_cube(cube_position, cube_size.x, cube_size.y, cube_size.z, GRAY)
            draw_cube_wires(cube_position, cube_size.x, cube_size.y, cube_size.z, DARKGRAY)

        draw_ray(ray, MAROON)
        draw_grid(10, 1.0)

        end_mode3d()

        draw_text("Try Selecting the box with mouse!", 240, 10, 20, DARKGRAY)

        if collision:
            draw_text("BOX SELECTED", (screen_width - measure_text("BOX SELECTED", 30)) // 2, int(screen_height * .1), 30, GREEN)

        end_drawing()
        # ---------------------------------------------------------------------------------

    # De-Initialization
    # -------------------------------------------------------------------------------------
    close_window()
    # -------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()