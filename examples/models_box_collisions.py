
import sys
import os
from ctypes import byref
from raylibpy import *

def main():
    screenWidth = 800
    screenHeight = 450

    init_window(screenWidth, screenHeight, "raylib [models] example - box collisions")

    camera = Camera((0.0, 10.0, 10.0), (0.0, 0.0, 0.0), (0.0, 1.0, 0.0), 45.0, 0)

    playerPosition = Vector3(0.0, 1.0, 2.0)
    playerSize = Vector3(1.0, 2.0, 1.0)
    playerColor = GREEN

    enemyBoxPos = Vector3(-4.0, 1.0, 0.0)
    enemyBoxSize = Vector3(2.0, 2.0, 2.0)
    enemySpherePos = Vector3(4.0, 0.0, 0.0)
    enemySphereSize = 1.5

    collision = False

    set_target_fps(60)
    
    while not window_should_close():

        if is_key_down(KEY_RIGHT):
            playerPosition.x  += 0.2
        elif is_key_down(KEY_LEFT):
            playerPosition.x  -= 0.2
        elif is_key_down(KEY_DOWN):
            playerPosition.z  += 0.2
        elif is_key_down(KEY_UP):
            playerPosition.z  -= 0.2

        collision  = False
        
        if check_collision_boxes(
                BoundingBox(
                    Vector3(playerPosition.x - playerSize.x / 2, playerPosition.y - playerSize.y / 2, playerPosition.z - playerSize.z / 2), 
                    Vector3(playerPosition.x + playerSize.x / 2, playerPosition.y + playerSize.y / 2, playerPosition.z + playerSize.z / 2)),
                BoundingBox(
                    Vector3(enemyBoxPos.x - enemyBoxSize.x / 2, enemyBoxPos.y - enemyBoxSize.y / 2, enemyBoxPos.z - enemyBoxSize.z / 2), 
                    Vector3(enemyBoxPos.x + enemyBoxSize.x / 2, enemyBoxPos.y + enemyBoxSize.y / 2, enemyBoxPos.z + enemyBoxSize.z / 2))):
            collision  = True
        
        if check_collision_box_sphere(
                BoundingBox(
                    Vector3(playerPosition.x - playerSize.x / 2, playerPosition.y - playerSize.y / 2, playerPosition.z - playerSize.z / 2), 
                    Vector3(playerPosition.x + playerSize.x / 2, playerPosition.y + playerSize.y / 2, playerPosition.z + playerSize.z / 2)), enemySpherePos, enemySphereSize):
            collision  = True
        
        if collision:
            playerColor  = RED
        else:
            playerColor  = GREEN

        with drawing():
            clear_background(RAYWHITE)

            with mode3d(camera):
                draw_cube(enemyBoxPos, enemyBoxSize.x, enemyBoxSize.y, enemyBoxSize.z, GRAY)
                draw_cube_wires(enemyBoxPos, enemyBoxSize.x, enemyBoxSize.y, enemyBoxSize.z, DARKGRAY)
                draw_sphere(enemySpherePos, enemySphereSize, GRAY)
                draw_sphere_wires(enemySpherePos, enemySphereSize, 16, 16, DARKGRAY)
                draw_cube_v(playerPosition, playerSize, playerColor)
                draw_grid(10, 1.0)
            # end_mode3d()

            draw_text("Move player with cursors to collide", 220, 40, 20, GRAY)
            draw_fps(10, 10)

        # end_drawing()

    close_window()

    return 0


if __name__ == "__main__":
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        os.chdir(sys.argv[1])
    print("Working dir:", os.getcwd())
    sys.exit(main())