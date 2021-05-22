# textures_particles_blending.py
# ******************************************************************************************
#
#   raylib example - particles blending
#
#   This example has been created using raylib 1.7 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
#
#   Copyright (c) 2017 Ramon Santamaria (@raysan5)
#
# *******************************************************************************************/

from ctypes import Structure, c_float, c_bool
from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

MAX_PARTICLES = 200


# Particle structure with basic data
class Particle(Structure):
    _fields_ = [
        ('position', Vector2),
        ('color', Color),
        ('alpha', c_float),
        ('size', c_float),
        ('rotation', c_float),
        ('active', c_bool),  # NOTE: Use it to activate/deactive particle
    ]


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - particles blending")

    # Particles pool, reuse them!
    mouse_tail: Array[Particle] = (Particle * MAX_PARTICLES)(*[Particle() for _ in range(MAX_PARTICLES)])

    # Initialize particles
    for i in range(MAX_PARTICLES):
        mouse_tail[i].position = Vector2(0, 0)
        mouse_tail[i].color = Color(get_random_value(0, 255), get_random_value(0, 255), get_random_value(0, 255), 255)
        mouse_tail[i].alpha = 1.0
        mouse_tail[i].size = get_random_value(1, 30) / 20.0
        mouse_tail[i].rotation = get_random_value(0, 360)
        mouse_tail[i].active = False

    gravity: float = 3.0

    smoke: Texture2D = load_texture("resources/spark_flame.png")

    blending: int = BLEND_ALPHA

    set_target_fps(60)
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------

        # Activate one particle every frame and Update active particles
        # NOTE: Particles initial position should be mouse position when activated
        # NOTE: Particles fall down with gravity and rotation... and disappear after 2 seconds (alpha = 0)
        # NOTE: When a particle disappears, active = False and it can be reused.
        for i in range(MAX_PARTICLES):
            if not mouse_tail[i].active:
                mouse_tail[i].active = True
                mouse_tail[i].alpha = 1.0
                mouse_tail[i].position = get_mouse_position()
                break

        for i in range(MAX_PARTICLES):
            if mouse_tail[i].active:
                mouse_tail[i].position.y += gravity / 2
                mouse_tail[i].alpha -= 0.005

                if mouse_tail[i].alpha <= 0.0:
                    mouse_tail[i].active = False

                mouse_tail[i].rotation += 2.0

        if is_key_pressed(KEY_SPACE):
            if blending == BLEND_ALPHA:
                blending = BLEND_ADDITIVE
            else:
                blending = BLEND_ALPHA
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():

            clear_background(DARKGRAY)

            with blend_mode(blending):

                # Draw active particles
                for i in range(MAX_PARTICLES):
                    if mouse_tail[i].active:
                        draw_texture_pro(smoke, Rectangle(0.0, 0.0, smoke.width, smoke.height),
                                         Rectangle(mouse_tail[i].position.x, mouse_tail[i].position.y,
                                                   smoke.width * mouse_tail[i].size, smoke.height * mouse_tail[i].size),
                                         Vector2((smoke.width * mouse_tail[i].size / 2.0),
                                                 (smoke.height * mouse_tail[i].size / 2.0)), mouse_tail[i].rotation,
                                         fade(mouse_tail[i].color, mouse_tail[i].alpha))

            # end blend mode

            draw_text("PRESS SPACE to CHANGE BLENDING MODE", 180, 20, 20, BLACK)

            if blending == BLEND_ALPHA:
                draw_text("ALPHA BLENDING", 290, screen_height - 40, 20, BLACK)
            else:
                draw_text("ADDITIVE BLENDING", 280, screen_height - 40, 20, RAYWHITE)

        # end drawing
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_texture(smoke)

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
