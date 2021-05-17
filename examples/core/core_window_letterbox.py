# ******************************************************************************************
# 
#   raylib [core] example - window scale letterbox (and virtual mouse)
# 
#   This example has been created using raylib 2.5 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Example contributed by Anata (@anatagawa) and reviewed by Ramon Santamaria (@raysan5)
# 
#   Copyright (c) 2019 Anata (@anatagawa) and Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from typing import List
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *


# Clamp Vector2 value with min and max and return a new vector2
# NOTE: Required for virtual mouse, to clamp inside virtual game size
def clamp_value(value: Vector2, min_: Vector2, max_: Vector2) -> Vector2:
    result: Vector2 = value
    result.x = max_.x if result.x > max_.x else result.x
    result.x = min_.x if result.x < min_.x else result.x
    result.y = max_.y if result.y > max_.y else result.y
    result.y = min_.y if result.y < min_.y else result.y
    return result


def main() -> int:
    windowWidth: int = 800
    windowHeight: int = 450

    # Enable config flags for resizable window and vertical synchro
    set_config_flags(FLAG_WINDOW_RESIZABLE | FLAG_VSYNC_HINT)
    init_window(windowWidth, windowHeight, "raylib [core] example - window scale letterbox")
    set_window_min_size(320, 240)

    gameScreenWidth: int = 640
    gameScreenHeight: int = 480

    # Render texture initialization, used to hold the rendering result so we can easily resize it
    target: RenderTexture2D = load_render_texture(gameScreenWidth, gameScreenHeight)
    set_texture_filter(target.texture, TEXTURE_FILTER_BILINEAR)  # Texture scale filter to use

    colors: List[Color] = []
    for i in range(10):
        colors.append(Color(get_random_value(100, 250), get_random_value(50, 150), get_random_value(10, 100), 255))

    set_target_fps(60)  # Set our game to run at 60 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        # Compute required framebuffer scaling
        scale: float = min(get_screen_width() / gameScreenWidth, get_screen_height() / gameScreenHeight)

        if is_key_pressed(KEY_SPACE):
            # Recalculate random colors for the bars
            for color in colors:
                colors.rgba = get_random_value(100, 250), get_random_value(50, 150), get_random_value(10, 100), 255

        # Update virtual mouse (clamped mouse value behind game screen)
        mouse: Vector2 = get_mouse_position()
        virtualMouse: Vector2 = Vector2()
        virtualMouse.x = (mouse.x - (get_screen_width() - (gameScreenWidth * scale)) * 0.5) / scale
        virtualMouse.y = (mouse.y - (get_screen_height() - (gameScreenHeight * scale)) * 0.5) / scale
        virtualMouse = clamp_value(virtualMouse, Vector2(0, 0), Vector2(gameScreenWidth, gameScreenHeight))

        # Apply the same transformation as the virtual mouse to the real mouse (i.e. to work with raygui)
        # SetMouseOffset(-(get_screen_width() - (gameScreenWidth*scale))*0.5, -(get_screen_height() - (gameScreenHeight*scale))*0.5)
        # SetMouseScale(1/scale, 1/scale)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(BLACK)

            # Draw everything in the render texture, note this will not be rendered on screen, yet
            with texture_mode(target):
                clear_background(RAYWHITE)  # Clear render texture background color

                for i in range(10):
                    draw_rectangle(0, (gameScreenHeight // 10) * i, gameScreenWidth, gameScreenHeight // 10, colors[i])

                draw_text("If executed inside a window,\nyou can resize the window,\nand see the screen scaling!", 10,
                          25, 20, WHITE)

                draw_text(f"Default Mouse: [{mouse.x}, {mouse.y}]", 350, 25, 20, GREEN)
                draw_text(f"Virtual Mouse: [{virtualMouse.x}, {virtualMouse.y}]", 350, 55, 20, YELLOW)

            # EndTextureMode()

            # Draw RenderTexture2D to window, properly scaled
            draw_texture_pro(target.texture,
                             Rectangle(0.0, 0.0, target.texture.width, -target.texture.height),
                             Rectangle((get_screen_width() - (gameScreenWidth * scale)) * 0.5,
                                       (get_screen_height() - (gameScreenHeight * scale)) * 0.5,
                                       gameScreenWidth * scale, gameScreenHeight * scale),
                             Vector2(), 0.0, WHITE)

        # EndDrawing()
        # --------------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_render_texture(target)  # Unload render texture

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
