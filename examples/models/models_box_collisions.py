# models_box_collisions.py

from raylibpy import *

def main() -> int:

    # Initialization
    # -------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [models] example - box collision")

    # Define the camera to look into our 3d world
    camera: Camera = Camera()
    camera.position = Vector3(0., 10., 10.)
    camera.target = Vector3(0., 0., 0.)
    camera.up = Vector3(0., 1., 0.)
    camera.fovy = 45.0
    camera.type = CAMERA_PERSPECTIVE

    player_position: Vector3 = Vector3(0., 1., 2.)
    player_size: Vector3 = Vector3(1., 2., 1.)
    player_color: Color = GREEN

    enemy_box_pos: Vector3 = Vector3(-4, 1., 0.)
    enemy_box_size: Vector3 = Vector3(2., 2., 2.)

    enemy_sphere_pos: Vector3 = Vector3(4, 1.5, 0.)
    enemy_sphere_size: float = 1.5

    collision: bool = False

    set_target_fps(60)

    # Main game loop
    while not window_should_close():
        # Update
        # ---------------------------------------------------------------------------------
        
        # Mode player
        if is_key_down(KEY_RIGHT):
            player_position.x += 0.2
        elif is_key_down(KEY_LEFT):
            player_position.x -= 0.2
        elif is_key_down(KEY_DOWN):
            player_position.z += 0.2
        elif is_key_down(KEY_UP):
            player_position.z -= 0.2

        collision = False

        #
        player_bbox = BoundingBox(
                    Vector3(player_position.x - player_size.x / 2,
                            player_position.y - player_size.y / 2,
                            player_position.z - player_size.z / 2),
                    Vector3(player_position.x + player_size.x / 2,
                            player_position.y + player_size.y / 2,
                            player_position.z + player_size.z / 2),
        )
        if check_collision_boxes(
                player_bbox,
                BoundingBox(
                    Vector3(enemy_box_pos.x - enemy_box_size.x / 2,
                            enemy_box_pos.y - enemy_box_size.y / 2,
                            enemy_box_pos.z - enemy_box_size.z / 2),
                    Vector3(enemy_box_pos.x + enemy_box_size.x / 2,
                            enemy_box_pos.y + enemy_box_size.y / 2,
                            enemy_box_pos.z + enemy_box_size.z / 2))):
            collision = True

        if check_collision_box_sphere(player_bbox, enemy_sphere_pos, enemy_sphere_size):
            collision = True

        if collision:
            player_color = RED
        else:
            player_color = GREEN

        update_camera(byref(camera))
        # ----------------------------------------------------------------------------------

        # Draw
        # ---------------------------------------------------------------------------------
        begin_drawing()

        clear_background(RAYWHITE)

        begin_mode3d(camera)

        draw_cube(enemy_box_pos, enemy_box_size.x, enemy_box_size.y, enemy_box_size.z, GRAY)
        draw_cube_wires(enemy_box_pos, enemy_box_size.x, enemy_box_size.y, enemy_box_size.z, DARKGRAY)

        draw_sphere(enemy_sphere_pos, enemy_sphere_size, GRAY)
        draw_sphere_wires(enemy_sphere_pos, enemy_sphere_size, 16, 16, DARKGRAY)

        draw_cube_v(player_position, player_size, player_color)

        draw_grid(10, 1.0)

        end_mode3d()

        draw_text("Move player with cursors to collide", 220, 40, 20, GRAY)

        draw_fps(10, 10)

        end_drawing()
        # ---------------------------------------------------------------------------------

    # De-Initialization
    # -------------------------------------------------------------------------------------
    close_window()
    # -------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()