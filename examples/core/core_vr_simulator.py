# core_vr_simulator.py
# ******************************************************************************************
# 
#   raylib [core] example - VR Simulator (Oculus Rift CV1 parameters)
# 
#   This example has been created using raylib 3.7 (www.raylib.com)
#   raylib is licensed under an unmodified zlib/libpng license (View raylib.h for details)
# 
#   Copyright (c) 2017-2021 Ramon Santamaria (@raysan5)
# 
# *******************************************************************************************/

from raylibpy.colors import *
from raylibpy.spartan import *
from raylibpy.consts import *

GLSL_VERSION = 330


def main() -> int:
    # Initialization
    # --------------------------------------------------------------------------------------
    screen_width: int = 800
    screen_height: int = 450

    # NOTE: screenWidth/screenHeight should match VR device aspect ratio
    init_window(screen_width, screen_height, "raylib [core] example - vr simulator")

    # VR device parameters definition
    device: VrDeviceInfo = VrDeviceInfo(
        # Oculus Rift CV1 parameters for simulator
        2160,  # Horizontal resolution in pixels
        1200,  # Vertical resolution in pixels
        0.133793,  # Horizontal size in meters
        0.0669,  # Vertical size in meters
        0.04678,  # Screen center in meters
        0.041,  # Distance between eye and display in meters
        0.07,  # Lens separation distance in meters
        0.07,  # IPD (distance between pupils) in meters

        # NOTE: CV1 uses fresnel-hybrid-asymmetric lenses with specific compute shaders
        # Following parameters are just an approximation to CV1 distortion stereo rendering
        [1.0,  # Lens distortion constant parameter 0
         0.22,  # Lens distortion constant parameter 1
         0.24,  # Lens distortion constant parameter 2
         0.0],  # Lens distortion constant parameter 3
        [0.996,  # Chromatic aberration correction parameter 0
         -0.004,  # Chromatic aberration correction parameter 1
         1.014,  # Chromatic aberration correction parameter 2
         0.0]  # Chromatic aberration correction parameter 3
    )
    # Load VR stereo config for VR device parameteres (Oculus Rift CV1 parameters)
    config: VrStereoConfig = load_vr_stereo_config(device)

    # Distortion shader (uses device lens distortion and chroma)
    distortion: Shader = load_shader(None, f"resources/distortion{GLSL_VERSION}.fs")

    # Update distortion shader with lens and distortion-scale parameters
    set_shader_value(distortion, get_shader_location(distortion, "leftLensCenter"),
                     config.leftLensCenter, SHADER_UNIFORM_VEC2)
    set_shader_value(distortion, get_shader_location(distortion, "rightLensCenter"),
                     config.rightLensCenter, SHADER_UNIFORM_VEC2)
    set_shader_value(distortion, get_shader_location(distortion, "leftScreenCenter"),
                     config.leftScreenCenter, SHADER_UNIFORM_VEC2)
    set_shader_value(distortion, get_shader_location(distortion, "rightScreenCenter"),
                     config.rightScreenCenter, SHADER_UNIFORM_VEC2)

    set_shader_value(distortion, get_shader_location(distortion, "scale"),
                     config.scale, SHADER_UNIFORM_VEC2)
    set_shader_value(distortion, get_shader_location(distortion, "scaleIn"),
                     config.scaleIn, SHADER_UNIFORM_VEC2)
    set_shader_value(distortion, get_shader_location(distortion, "deviceWarpParam"),
                     device.lensDistortionValues, SHADER_UNIFORM_VEC4)
    set_shader_value(distortion, get_shader_location(distortion, "chromaAbParam"),
                     device.chromaAbCorrection, SHADER_UNIFORM_VEC4)

    # Initialize framebuffer for stereo rendering
    # NOTE: Screen size should match HMD aspect ratio
    target: RenderTexture2D = load_render_texture(get_screen_width(), get_screen_height())

    # Define the camera to look into our 3d world
    camera: Camera = Camera()
    camera.position = Vector3(5.0, 2.0, 5.0)  # Camera position
    camera.target = Vector3(0.0, 2.0, 0.0)  # Camera looking at point
    camera.up = Vector3(0.0, 1.0, 0.0)  # Camera up vector
    camera.fovy = 60.0  # Camera field-of-view Y
    camera.projection = CAMERA_PERSPECTIVE  # Camera type

    cube_position: Vector3 = Vector3(0.0, 0.0, 0.0)

    set_camera_mode(camera, CAMERA_FIRST_PERSON)  # Set first person camera mode

    set_target_fps(90)  # Set our game to run at 90 frames-per-second
    # --------------------------------------------------------------------------------------

    # Main game loop
    while not window_should_close():  # Detect window close button or ESC key
        # Update
        # ----------------------------------------------------------------------------------
        update_camera(camera)  # Update camera (simulator mode)
        # ----------------------------------------------------------------------------------

        # Draw
        # ----------------------------------------------------------------------------------
        with drawing():
            clear_background(RAYWHITE)

            with texture_mode(target):
                clear_background(RAYWHITE)
                with vr_stereo_mode(config):
                    with mode3d(camera):
                        draw_cube(cube_position, 2.0, 2.0, 2.0, RED)
                        draw_cube_wires(cube_position, 2.0, 2.0, 2.0, MAROON)
                        draw_grid(40, 1.0)

            #       End mode3D()
            #   End vr stereo mode()
            # End texture mode()

            with shader_mode(distortion):
                draw_texture_rec(target.texture,
                                 Rectangle(0, 0, target.texture.width, -target.texture.height),
                                 Vector2(0.0, 0.0), WHITE)
            # EndShaderMode()

            draw_fps(10, 10)

        # EndDrawing()
        # ----------------------------------------------------------------------------------

    # De-Initialization
    # --------------------------------------------------------------------------------------
    unload_vr_stereo_config(config)  # Unload stereo config

    unload_render_texture(target)  # Unload stereo render fbo
    unload_shader(distortion)  # Unload distortion shader

    close_window()  # Close window and OpenGL context
    # --------------------------------------------------------------------------------------

    return 0


if __name__ == '__main__':
    main()
