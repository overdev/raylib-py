from contextlib import contextmanager
from ctypes import byref
from typing import Sequence, Tuple, Union, Optional
import raylibpy.core as core
from raylibpy import _rl
from raylibpy._types import *
from raylibpy.wrapper import _init
from raylibpy.core import *


__all__ = [
    'TraceLogCallback',
    'LoadFileDataCallback',
    'SaveFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileTextCallback',

    'clamp',
    'init_window',
    'window_should_close',
    'close_window',
    'is_window_ready',
    'is_window_fullscreen',
    'is_window_hidden',
    'is_window_minimized',
    'is_window_maximized',
    'is_window_focused',
    'is_window_resized',
    'is_window_state',
    'set_window_state',
    'clear_window_state',
    'toggle_fullscreen',
    'maximize_window',
    'minimize_window',
    'restore_window',
    'set_window_icon',
    'set_window_title',
    'set_window_position',
    'set_window_monitor',
    'set_window_min_size',
    'set_window_size',
    'get_window_handle',
    'get_screen_width',
    'get_screen_height',
    'get_monitor_count',
    'get_current_monitor',
    'get_monitor_position',
    'get_monitor_width',
    'get_monitor_height',
    'get_monitor_physical_width',
    'get_monitor_physical_height',
    'get_monitor_refresh_rate',
    'get_window_position',
    'get_window_scale_dpi',
    'get_monitor_name',
    'set_clipboard_text',
    'get_clipboard_text',
    'show_cursor',
    'hide_cursor',
    'is_cursor_hidden',
    'enable_cursor',
    'disable_cursor',
    'is_cursor_on_screen',
    'clear_background',
    'begin_drawing',
    'end_drawing',
    'drawing',
    'begin_mode2d',
    'end_mode2d',
    'mode2d',
    'begin_mode3d',
    'end_mode3d',
    'mode3d',
    'begin_texture_mode',
    'end_texture_mode',
    'texture_mode',
    'begin_shader_mode',
    'end_shader_mode',
    'shader_mode',
    'begin_blend_mode',
    'end_blend_mode',
    'blend_mode',
    'begin_scissor_mode',
    'end_scissor_mode',
    'scissor_mode',
    'begin_vr_stereo_mode',
    'end_vr_stereo_mode',
    'vr_stereo_mode',
    'load_vr_stereo_config',
    'unload_vr_stereo_config',
    'load_shader',
    'load_shader_from_memory',
    'get_shader_location',
    'get_shader_location_attrib',
    'set_shader_value',
    'set_shader_value_v',
    'set_shader_value_matrix',
    'set_shader_value_texture',
    'unload_shader',
    'get_mouse_ray',
    'get_camera_matrix',
    'get_camera_matrix2d',
    'get_world_to_screen',
    'get_world_to_screen_ex',
    'get_world_to_screen2d',
    'get_screen_to_world2d',
    'set_target_fps',
    'get_fps',
    'get_frame_time',
    'get_time',
    'get_random_value',
    'take_screenshot',
    'set_config_flags',
    'trace_log',
    'set_trace_log_level',
    'mem_alloc',
    'mem_realloc',
    'mem_free',
    'set_trace_log_callback',
    'set_load_file_data_callback',
    'set_save_file_data_callback',
    'set_load_file_text_callback',
    'set_save_file_text_callback',
    'load_file_data',
    'unload_file_data',
    'save_file_data',
    'load_file_text',
    'unload_file_text',
    'save_file_text',
    'file_exists',
    'directory_exists',
    'is_file_extension',
    'get_file_extension',
    'get_file_name',
    'get_file_name_without_ext',
    'get_directory_path',
    'get_prev_directory_path',
    'get_working_directory',
    'get_directory_files',
    'clear_directory_files',
    'change_directory',
    'is_file_dropped',
    'get_dropped_files',
    'clear_dropped_files',
    'get_file_mod_time',
    'compress_data',
    'decompress_data',
    'save_storage_value',
    'load_storage_value',
    'open_url',
    'is_key_pressed',
    'is_key_down',
    'is_key_released',
    'is_key_up',
    'set_exit_key',
    'get_key_pressed',
    'get_char_pressed',
    'is_gamepad_available',
    'is_gamepad_name',
    'get_gamepad_name',
    'is_gamepad_button_pressed',
    'is_gamepad_button_down',
    'is_gamepad_button_released',
    'is_gamepad_button_up',
    'get_gamepad_button_pressed',
    'get_gamepad_axis_count',
    'get_gamepad_axis_movement',
    'set_gamepad_mappings',
    'is_mouse_button_pressed',
    'is_mouse_button_down',
    'is_mouse_button_released',
    'is_mouse_button_up',
    'get_mouse_x',
    'get_mouse_y',
    'get_mouse_position',
    'set_mouse_position',
    'set_mouse_offset',
    'set_mouse_scale',
    'get_mouse_wheel_move',
    'set_mouse_cursor',
    'get_touch_x',
    'get_touch_y',
    'get_touch_position',
    'set_gestures_enabled',
    'is_gesture_detected',
    'get_gesture_detected',
    'get_touch_points_count',
    'get_gesture_hold_duration',
    'get_gesture_drag_vector',
    'get_gesture_drag_angle',
    'get_gesture_pinch_vector',
    'get_gesture_pinch_angle',
    'set_camera_mode',
    'update_camera',
    'set_camera_pan_control',
    'set_camera_alt_control',
    'set_camera_smooth_zoom_control',
    'set_camera_move_controls',
    'set_shapes_texture',
    'draw_pixel',
    'draw_pixel_v',
    'draw_line',
    'draw_line_v',
    'draw_line_ex',
    'draw_line_bezier',
    'draw_line_bezier_quad',
    'draw_line_strip',
    'draw_circle',
    'draw_circle_sector',
    'draw_circle_sector_lines',
    'draw_circle_gradient',
    'draw_circle_v',
    'draw_circle_lines',
    'draw_ellipse',
    'draw_ellipse_lines',
    'draw_ring',
    'draw_ring_lines',
    'draw_rectangle',
    'draw_rectangle_v',
    'draw_rectangle_rec',
    'draw_rectangle_pro',
    'draw_rectangle_gradient_v',
    'draw_rectangle_gradient_h',
    'draw_rectangle_gradient_ex',
    'draw_rectangle_lines',
    'draw_rectangle_lines_ex',
    'draw_rectangle_rounded',
    'draw_rectangle_rounded_lines',
    'draw_triangle',
    'draw_triangle_lines',
    'draw_triangle_fan',
    'draw_triangle_strip',
    'draw_poly',
    'draw_poly_lines',
    'check_collision_recs',
    'check_collision_circles',
    'check_collision_circle_rec',
    'check_collision_point_rec',
    'check_collision_point_circle',
    'check_collision_point_triangle',
    'check_collision_lines',
    'get_collision_rec',
    'load_image',
    'load_image_raw',
    'load_image_anim',
    'load_image_from_memory',
    'unload_image',
    'export_image',
    'export_image_as_code',
    'gen_image_color',
    'gen_image_gradient_v',
    'gen_image_gradient_h',
    'gen_image_gradient_radial',
    'gen_image_checked',
    'gen_image_white_noise',
    'gen_image_perlin_noise',
    'gen_image_cellular',
    'image_copy',
    'image_from_image',
    'image_text',
    'image_text_ex',
    'image_format',
    'image_to_pot',
    'image_crop',
    'image_alpha_crop',
    'image_alpha_clear',
    'image_alpha_mask',
    'image_alpha_premultiply',
    'image_resize',
    'image_resize_nn',
    'image_resize_canvas',
    'image_mipmaps',
    'image_dither',
    'image_flip_vertical',
    'image_flip_horizontal',
    'image_rotate_cw',
    'image_rotate_ccw',
    'image_color_tint',
    'image_color_invert',
    'image_color_grayscale',
    'image_color_contrast',
    'image_color_brightness',
    'image_color_replace',
    'load_image_colors',
    'load_image_palette',
    'unload_image_colors',
    'unload_image_palette',
    'get_image_alpha_border',
    'image_clear_background',
    'image_draw_pixel',
    'image_draw_pixel_v',
    'image_draw_line',
    'image_draw_line_v',
    'image_draw_circle',
    'image_draw_circle_v',
    'image_draw_rectangle',
    'image_draw_rectangle_v',
    'image_draw_rectangle_rec',
    'image_draw_rectangle_lines',
    'image_draw',
    'image_draw_text',
    'image_draw_text_ex',
    'load_texture',
    'load_texture_from_image',
    'load_texture_cubemap',
    'load_render_texture',
    'unload_texture',
    'unload_render_texture',
    'update_texture',
    'update_texture_rec',
    'get_texture_data',
    'get_screen_data',
    'gen_texture_mipmaps',
    'set_texture_filter',
    'set_texture_wrap',
    'draw_texture',
    'draw_texture_v',
    'draw_texture_ex',
    'draw_texture_rec',
    'draw_texture_quad',
    'draw_texture_tiled',
    'draw_texture_pro',
    'draw_texture_npatch',
    'draw_texture_poly',
    'fade',
    'color_to_int',
    'color_normalize',
    'color_from_normalized',
    'color_to_hsv',
    'color_from_hsv',
    'color_alpha',
    'color_alpha_blend',
    'get_color',
    'get_pixel_color',
    'set_pixel_color',
    'get_pixel_data_size',
    'get_font_default',
    'load_font',
    'load_font_ex',
    'load_font_from_image',
    'load_font_from_memory',
    'load_font_data',
    'gen_image_font_atlas',
    'unload_font_data',
    'unload_font',
    'draw_fps',
    'draw_text',
    'draw_text_ex',
    'draw_text_rec',
    'draw_text_rec_ex',
    'draw_text_codepoint',
    'measure_text',
    'measure_text_ex',
    'get_glyph_index',
    'text_copy',
    'text_is_equal',
    'text_length',
    'text_format',
    'text_subtext',
    'text_replace',
    'text_insert',
    'text_join',
    'text_split',
    'text_append',
    'text_find_index',
    'text_to_upper',
    'text_to_lower',
    'text_to_pascal',
    'text_to_integer',
    'text_to_utf8',
    'get_codepoints',
    'get_codepoints_count',
    'get_next_codepoint',
    'codepoint_to_utf8',
    'draw_line3d',
    'draw_point3d',
    'draw_circle3d',
    'draw_triangle3d',
    'draw_triangle_strip3d',
    'draw_cube',
    'draw_cube_v',
    'draw_cube_wires',
    'draw_cube_wires_v',
    'draw_cube_texture',
    'draw_sphere',
    'draw_sphere_ex',
    'draw_sphere_wires',
    'draw_cylinder',
    'draw_cylinder_wires',
    'draw_plane',
    'draw_ray',
    'draw_grid',
    'load_model',
    'load_model_from_mesh',
    'unload_model',
    'unload_model_keep_meshes',
    'upload_mesh',
    'update_mesh_buffer',
    'draw_mesh',
    'draw_mesh_instanced',
    'unload_mesh',
    'export_mesh',
    'load_materials',
    'load_material_default',
    'unload_material',
    'set_material_texture',
    'set_model_mesh_material',
    'load_model_animations',
    'update_model_animation',
    'unload_model_animation',
    'unload_model_animations',
    'is_model_animation_valid',
    'gen_mesh_poly',
    'gen_mesh_plane',
    'gen_mesh_cube',
    'gen_mesh_sphere',
    'gen_mesh_hemisphere',
    'gen_mesh_cylinder',
    'gen_mesh_torus',
    'gen_mesh_knot',
    'gen_mesh_heightmap',
    'gen_mesh_cubicmap',
    'mesh_bounding_box',
    'mesh_tangents',
    'mesh_binormals',
    'draw_model',
    'draw_model_ex',
    'draw_model_wires',
    'draw_model_wires_ex',
    'draw_bounding_box',
    'draw_billboard',
    'draw_billboard_rec',
    'check_collision_spheres',
    'check_collision_boxes',
    'check_collision_box_sphere',
    'check_collision_ray_sphere',
    'check_collision_ray_sphere_ex',
    'check_collision_ray_box',
    'get_collision_ray_mesh',
    'get_collision_ray_model',
    'get_collision_ray_triangle',
    'get_collision_ray_ground',
    'init_audio_device',
    'close_audio_device',
    'is_audio_device_ready',
    'set_master_volume',
    'load_wave',
    'load_wave_from_memory',
    'load_sound',
    'load_sound_from_wave',
    'update_sound',
    'unload_wave',
    'unload_sound',
    'export_wave',
    'export_wave_as_code',
    'play_sound',
    'stop_sound',
    'pause_sound',
    'resume_sound',
    'play_sound_multi',
    'stop_sound_multi',
    'get_sounds_playing',
    'is_sound_playing',
    'set_sound_volume',
    'set_sound_pitch',
    'wave_format',
    'wave_copy',
    'wave_crop',
    'load_wave_samples',
    'unload_wave_samples',
    'load_music_stream',
    'load_music_stream_from_memory',
    'unload_music_stream',
    'play_music_stream',
    'is_music_playing',
    'update_music_stream',
    'stop_music_stream',
    'pause_music_stream',
    'resume_music_stream',
    'set_music_volume',
    'set_music_pitch',
    'get_music_time_length',
    'get_music_time_played',
    'init_audio_stream',
    'update_audio_stream',
    'close_audio_stream',
    'is_audio_stream_processed',
    'play_audio_stream',
    'pause_audio_stream',
    'resume_audio_stream',
    'is_audio_stream_playing',
    'stop_audio_stream',
    'set_audio_stream_volume',
    'set_audio_stream_pitch',
    'set_audio_stream_buffer_size_default',
    *core.__all__
]

_init()


def clamp(value: float, min_: float, max_: float) -> float:
    return _rl.Clamp(float(value), float(min_), float(max_))


def init_window(width: int, height: int, title: str) -> None:
    """Initialize window and OpenGL context"""
    return _rl.InitWindow(int(width), int(height), _str_in(title))


def window_should_close() -> bool:
    """Check if KEY_ESCAPE pressed or Close icon pressed"""
    return _rl.WindowShouldClose()


def close_window() -> None:
    """Close window and unload OpenGL context"""
    return _rl.CloseWindow()


def is_window_ready() -> bool:
    """Check if window has been initialized successfully"""
    return _rl.IsWindowReady()


def is_window_fullscreen() -> bool:
    """Check if window is currently fullscreen"""
    return _rl.IsWindowFullscreen()


def is_window_hidden() -> bool:
    """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
    return _rl.IsWindowHidden()


def is_window_minimized() -> bool:
    """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
    return _rl.IsWindowMinimized()


def is_window_maximized() -> bool:
    """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
    return _rl.IsWindowMaximized()


def is_window_focused() -> bool:
    """Check if window is currently focused (only PLATFORM_DESKTOP)"""
    return _rl.IsWindowFocused()


def is_window_resized() -> bool:
    """Check if window has been resized last frame"""
    return _rl.IsWindowResized()


def is_window_state(flag: int) -> bool:
    """Check if one specific window flag is enabled"""
    return _rl.IsWindowState(int(flag))


def set_window_state(flags: int) -> None:
    """Set window configuration state using flags"""
    return _rl.SetWindowState(int(flags))


def clear_window_state(flags: int) -> None:
    """Clear window configuration state flags"""
    return _rl.ClearWindowState(int(flags))


def toggle_fullscreen() -> None:
    """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
    return _rl.ToggleFullscreen()


def maximize_window() -> None:
    """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
    return _rl.MaximizeWindow()


def minimize_window() -> None:
    """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
    return _rl.MinimizeWindow()


def restore_window() -> None:
    """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
    return _rl.RestoreWindow()


def set_window_icon(image: Image) -> None:
    """Set icon for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowIcon(image)


def set_window_title(title: str) -> None:
    """Set title for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowTitle(_str_in(title))


def set_window_position(x: int, y: int) -> None:
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowPosition(int(x), int(y))


def set_window_monitor(monitor: int) -> None:
    """Set monitor for the current window (fullscreen mode)"""
    return _rl.SetWindowMonitor(int(monitor))


def set_window_min_size(width: int, height: int) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    return _rl.SetWindowMinSize(int(width), int(height))


def set_window_size(width: int, height: int) -> None:
    """Set window dimensions"""
    return _rl.SetWindowSize(int(width), int(height))


def get_window_handle() -> bytes:
    """Get native window handle"""
    return _rl.GetWindowHandle()


def get_screen_width() -> int:
    """Get current screen width"""
    return _rl.GetScreenWidth()


def get_screen_height() -> int:
    """Get current screen height"""
    return _rl.GetScreenHeight()


def get_monitor_count() -> int:
    """Get number of connected monitors"""
    return _rl.GetMonitorCount()


def get_current_monitor() -> int:
    """Get current connected monitor"""
    return _rl.GetCurrentMonitor()


def get_monitor_position(monitor: int) -> Vector2:
    """Get specified monitor position"""
    return _rl.GetMonitorPosition(int(monitor))


def get_monitor_width(monitor: int) -> int:
    """Get specified monitor width (max available by monitor)"""
    return _rl.GetMonitorWidth(int(monitor))


def get_monitor_height(monitor: int) -> int:
    """Get specified monitor height (max available by monitor)"""
    return _rl.GetMonitorHeight(int(monitor))


def get_monitor_physical_width(monitor: int) -> int:
    """Get specified monitor physical width in millimetres"""
    return _rl.GetMonitorPhysicalWidth(int(monitor))


def get_monitor_physical_height(monitor: int) -> int:
    """Get specified monitor physical height in millimetres"""
    return _rl.GetMonitorPhysicalHeight(int(monitor))


def get_monitor_refresh_rate(monitor: int) -> int:
    """Get specified monitor refresh rate"""
    return _rl.GetMonitorRefreshRate(int(monitor))


def get_window_position() -> Vector2:
    """Get window position XY on monitor"""
    return _rl.GetWindowPosition()


def get_window_scale_dpi() -> Vector2:
    """Get window scale DPI factor"""
    return _rl.GetWindowScaleDPI()


def get_monitor_name(monitor: int) -> str:
    """Get the human-readable, UTF-8 encoded name of the primary monitor"""
    return _rl.GetMonitorName(int(monitor))


def set_clipboard_text(text: str) -> None:
    """Set clipboard text content"""
    return _rl.SetClipboardText(_str_in(text))


def get_clipboard_text() -> str:
    """Get clipboard text content"""
    return _rl.GetClipboardText()


def show_cursor() -> None:
    """Shows cursor"""
    return _rl.ShowCursor()


def hide_cursor() -> None:
    """Hides cursor"""
    return _rl.HideCursor()


def is_cursor_hidden() -> bool:
    """Check if cursor is not visible"""
    return _rl.IsCursorHidden()


def enable_cursor() -> None:
    """Enables cursor (unlock cursor)"""
    return _rl.EnableCursor()


def disable_cursor() -> None:
    """Disables cursor (lock cursor)"""
    return _rl.DisableCursor()


def is_cursor_on_screen() -> bool:
    """Check if cursor is on the current screen."""
    return _rl.IsCursorOnScreen()


def clear_background(color: AnyRGB) -> None:
    """Set background color (framebuffer clear color)"""
    return _rl.ClearBackground(_color(color))


def begin_drawing() -> None:
    """Setup canvas (framebuffer) to start drawing"""
    _rl.BeginDrawing()


def end_drawing() -> None:
    """End canvas drawing and swap buffers (double buffering)"""
    _rl.EndDrawing()


@contextmanager
def drawing():
    """Context of canvas (framebuffer) to start drawing"""
    _rl.BeginDrawing()
    yield
    _rl.EndDrawing()


def begin_mode2d(camera: Camera2D) -> None:
    """Initialize 2D mode with custom camera (2D)"""
    _rl.BeginMode2D(camera)


def end_mode2d() -> None:
    """Ends 2D mode with custom camera"""
    return _rl.EndMode2D()


@contextmanager
def mode2d(camera: Camera2D):
    """Context of 2D mode with custom camera (2D)"""
    _rl.BeginMode2D(camera)
    yield
    _rl.EndMode2D()


def begin_mode3d(camera: Camera3D) -> None:
    """Initializes 3D mode with custom camera (3D)"""
    _rl.BeginMode3D(camera)


def end_mode3d() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode"""
    _rl.EndMode3D()


@contextmanager
def mode3d(camera: Camera3D):
    """Context of 3D mode with custom camera (3D)"""
    _rl.BeginMode3D(camera)
    yield
    _rl.EndMode3D()


def begin_texture_mode(target: RenderTexture2D) -> None:
    """Initializes render texture for drawing"""
    _rl.BeginTextureMode(target)


def end_texture_mode() -> None:
    """Ends drawing to render texture"""
    _rl.EndTextureMode()


@contextmanager
def texture_mode(target: RenderTexture2D):
    """Context of render texture for drawing"""
    _rl.BeginTextureMode(target)
    yield
    _rl.EndTextureMode()


def begin_shader_mode(shader: Shader) -> None:
    """Begin custom shader drawing"""
    _rl.BeginShaderMode(shader)


def end_shader_mode() -> None:
    """End custom shader drawing (use default shader)"""
    _rl.EndShaderMode()


@contextmanager
def shader_mode(shader: Shader):
    """Context of custom shader drawing"""
    _rl.BeginShaderMode(shader)
    yield
    _rl.EndShaderMode()


def begin_blend_mode(mode: int) -> None:
    """Begin blending mode (alpha, additive, multiplied)"""
    _rl.BeginBlendMode(int(mode))


def end_blend_mode() -> None:
    """End blending mode (reset to default: alpha blending)"""
    _rl.EndBlendMode()


@contextmanager
def blend_mode(mode: int):
    """Context of blending (alpha, additive, multiplied)"""
    _rl.BeginBlendMode(int(mode))
    yield
    _rl.EndBlendMode()


def begin_scissor_mode(x: int, y: int, width: int, height: int) -> None:
    """Begin scissor mode (define screen area for following drawing)"""
    _rl.BeginScissorMode(int(x), int(y), int(width), int(height))


def end_scissor_mode() -> None:
    """End scissor mode"""
    _rl.EndScissorMode()


@contextmanager
def scissor_mode(x: int, y: int, width: int, height: int):
    """Context of scissor mode (define screen area for following drawing)"""
    _rl.BeginScissorMode(int(x), int(y), int(width), int(height))
    yield
    _rl.EndScissorMode()


def begin_vr_stereo_mode(config: VrStereoConfig) -> None:
    """Begin stereo rendering (requires VR simulator)"""
    _rl.BeginVrStereoMode(config)


def end_vr_stereo_mode() -> None:
    """End stereo rendering (requires VR simulator)"""
    _rl.EndVrStereoMode()


@contextmanager
def vr_stereo_mode(config: VrStereoConfig):
    """Context of stereo rendering (requires VR simulator)"""
    _rl.BeginVrStereoMode(config)
    yield
    _rl.EndVrStereoMode()


def load_vr_stereo_config(device: VrDeviceInfo) -> VrStereoConfig:
    """Load VR stereo config for VR simulator device parameters"""
    return _rl.LoadVrStereoConfig(device)


def unload_vr_stereo_config(config: VrStereoConfig) -> None:
    """Unload VR stereo config"""
    return _rl.UnloadVrStereoConfig(config)


def load_shader(vs_file_name: Optional[str], fs_file_name: Optional[str]) -> Shader:
    """Load shader from files and bind default locations"""
    return _rl.LoadShader(_str_in(vs_file_name) if vs_file_name else b"\00",
                          _str_in(fs_file_name) if fs_file_name else b"\00")


def load_shader_from_memory(vs_code: str, fs_code: str) -> Shader:
    """Load shader from code strings and bind default locations"""
    return _rl.LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))


def get_shader_location(shader: Shader, uniform_name: str) -> int:
    """Get shader uniform location"""
    return _rl.GetShaderLocation(shader, _str_in(uniform_name))


def get_shader_location_attrib(shader: Shader, attrib_name: str) -> int:
    """Get shader attribute location"""
    return _rl.GetShaderLocationAttrib(shader, _str_in(attrib_name))


def set_shader_value(shader: Shader, loc_index: int, value: bytes, uniform_type: int) -> None:
    """Set shader uniform value"""
    return _rl.SetShaderValue(shader, int(loc_index), value, int(uniform_type))


def set_shader_value_v(shader: Shader, loc_index: int, value: bytes, uniform_type: int, count: int) -> None:
    """Set shader uniform value vector"""
    return _rl.SetShaderValueV(shader, int(loc_index), value, int(uniform_type), int(count))


def set_shader_value_matrix(shader: Shader, loc_index: int, mat: Matrix) -> None:
    """Set shader uniform value (matrix 4x4)"""
    return _rl.SetShaderValueMatrix(shader, int(loc_index), mat)


def set_shader_value_texture(shader: Shader, loc_index: int, texture: Texture2D) -> None:
    """Set shader uniform value for texture (sampler2d)"""
    return _rl.SetShaderValueTexture(shader, int(loc_index), texture)


def unload_shader(shader: Shader) -> None:
    """Unload shader from GPU memory (VRAM)"""
    return _rl.UnloadShader(shader)


def get_mouse_ray(mouse_position: AnyVec2, camera: Camera) -> Ray:
    """Returns a ray trace from mouse position"""
    return _rl.GetMouseRay(_vec2(mouse_position), camera)


def get_camera_matrix(camera: Camera) -> Matrix:
    """Returns camera transform matrix (view matrix)"""
    return _rl.GetCameraMatrix(camera)


def get_camera_matrix2d(camera: Camera2D) -> Matrix:
    """Returns camera 2d transform matrix"""
    return _rl.GetCameraMatrix2D(camera)


def get_world_to_screen(position: AnyVec3, camera: Camera) -> Vector2:
    """Returns the screen space position for a 3d world space position"""
    return _rl.GetWorldToScreen(_vec3(position), camera)


def get_world_to_screen_ex(position: AnyVec3, camera: Camera, width: int, height: int) -> Vector2:
    """Returns size position for a 3d world space position"""
    return _rl.GetWorldToScreenEx(_vec3(position), camera, int(width), int(height))


def get_world_to_screen2d(position: AnyVec2, camera: Camera2D) -> Vector2:
    """Returns the screen space position for a 2d camera world space position"""
    return _rl.GetWorldToScreen2D(_vec2(position), camera)


def get_screen_to_world2d(position: AnyVec2, camera: Camera2D) -> Vector2:
    """Returns the world space position for a 2d camera screen space position"""
    return _rl.GetScreenToWorld2D(_vec2(position), camera)


def set_target_fps(fps: int) -> None:
    """Set target FPS (maximum)"""
    return _rl.SetTargetFPS(int(fps))


def get_fps() -> int:
    """Returns current FPS"""
    return _rl.GetFPS()


def get_frame_time() -> float:
    """Returns time in seconds for last frame drawn (delta time)"""
    return _rl.GetFrameTime()


def get_time() -> float:
    """Returns elapsed time in seconds since InitWindow()"""
    return _rl.GetTime()


def get_random_value(min_: int, max_: int) -> int:
    """Returns a random value between min and max (both included)"""
    return _rl.GetRandomValue(int(min_), int(max_))


def take_screenshot(file_name: str) -> None:
    """Takes a screenshot of current screen (filename extension defines format)"""
    return _rl.TakeScreenshot(_str_in(file_name))


def set_config_flags(flags: int) -> None:
    """Setup init configuration flags (view FLAGS)"""
    return _rl.SetConfigFlags(int(flags))


def trace_log(log_level: int, text: str) -> None:
    """Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR)"""
    return _rl.TraceLog(int(log_level), _str_in(text))


def set_trace_log_level(log_level: int) -> None:
    """Set the current threshold (minimum) log level"""
    return _rl.SetTraceLogLevel(int(log_level))


def mem_alloc(size: int) -> bytes:
    """Internal memory allocator"""
    return _rl.MemAlloc(int(size))


def mem_realloc(ptr: bytes, size: int) -> bytes:
    """Internal memory reallocator"""
    return _rl.MemRealloc(ptr, int(size))


def mem_free(ptr: bytes) -> None:
    """Internal memory free"""
    return _rl.MemFree(ptr)


def set_trace_log_callback(callback: TraceLogCallback) -> None:
    """Set custom trace log"""
    return _rl.SetTraceLogCallback(callback)


def set_load_file_data_callback(callback: LoadFileDataCallback) -> None:
    """Set custom file binary data loader"""
    return _rl.SetLoadFileDataCallback(callback)


def set_save_file_data_callback(callback: SaveFileDataCallback) -> None:
    """Set custom file binary data saver"""
    return _rl.SetSaveFileDataCallback(callback)


def set_load_file_text_callback(callback: LoadFileTextCallback) -> None:
    """Set custom file text data loader"""
    return _rl.SetLoadFileTextCallback(callback)


def set_save_file_text_callback(callback: SaveFileTextCallback) -> None:
    """Set custom file text data saver"""
    return _rl.SetSaveFileTextCallback(callback)


def load_file_data(file_name: str, bytes_read: Sequence[int]) -> bytes:
    """Load file data as byte array (read)"""
    return _rl.LoadFileData(_str_in(file_name), _arr(Int, bytes_read))


def unload_file_data(data: bytes) -> None:
    """Unload file data allocated by LoadFileData()"""
    return _rl.UnloadFileData(data)


def save_file_data(file_name: str, data: bytes, bytes_to_write: int) -> bool:
    """Save data to file from byte array (write), returns true on success"""
    return _rl.SaveFileData(_str_in(file_name), data, int(bytes_to_write))


def load_file_text(file_name: str) -> str:
    """Load text data from file (read), returns a '\0' terminated string"""
    return _rl.LoadFileText(_str_in(file_name))


def unload_file_text(text: bytes) -> None:
    """Unload file text data allocated by LoadFileText()"""
    return _rl.UnloadFileText(text)


def save_file_text(file_name: str, text: str) -> bool:
    """Save text data to file (write), string must be '\0' terminated, returns true on success"""
    return _rl.SaveFileText(_str_in(file_name), _str_in(text))


def file_exists(file_name: str) -> bool:
    """Check if file exists"""
    return _rl.FileExists(_str_in(file_name))


def directory_exists(dir_path: str) -> bool:
    """Check if a directory path exists"""
    return _rl.DirectoryExists(_str_in(dir_path))


def is_file_extension(file_name: str, ext: str) -> bool:
    """Check file extension (including point: .png, .wav)"""
    return _rl.IsFileExtension(_str_in(file_name), _str_in(ext))


def get_file_extension(file_name: str) -> str:
    """Get pointer to extension for a filename string (includes dot: ".png")"""
    return _rl.GetFileExtension(_str_in(file_name))


def get_file_name(file_path: str) -> str:
    """Get pointer to filename for a path string"""
    return _rl.GetFileName(_str_in(file_path))


def get_file_name_without_ext(file_path: str) -> str:
    """Get filename string without extension (uses static string)"""
    return _rl.GetFileNameWithoutExt(_str_in(file_path))


def get_directory_path(file_path: str) -> str:
    """Get full path for a given fileName with path (uses static string)"""
    return _rl.GetDirectoryPath(_str_in(file_path))


def get_prev_directory_path(dir_path: str) -> str:
    """Get previous directory path for a given path (uses static string)"""
    return _rl.GetPrevDirectoryPath(_str_in(dir_path))


def get_working_directory() -> str:
    """Get current working directory (uses static string)"""
    return _rl.GetWorkingDirectory()


def get_directory_files(dir_path: str) -> Sequence[str]:
    """Get filenames in a directory path (memory should be freed)"""
    count = IntPtr(0)
    result = _rl.GetDirectoryFiles(_str_in(dir_path), count)
    files = []
    for i in range(count.value):
        files.append(result[i].decode('utf-8'))
    mem_free(result)
    return tuple(files)


def clear_directory_files() -> None:
    """Clear directory files paths buffers (free memory)"""
    return _rl.ClearDirectoryFiles()


def change_directory(dir_: str) -> bool:
    """Change working directory, return true on success"""
    return _rl.ChangeDirectory(_str_in(dir_))


def is_file_dropped() -> bool:
    """Check if a file has been dropped into window"""
    return _rl.IsFileDropped()


def get_dropped_files() -> Sequence[str]:
    """Get dropped files names (memory should be freed)"""
    count = Long(0)
    result = _rl.GetDroppedFiles(byref(count))
    files = []
    for i in range(count.value):
        files.append(result[i].decode('utf-8'))
    return tuple(files)


def clear_dropped_files() -> None:
    """Clear dropped files paths buffer (free memory)"""
    return _rl.ClearDroppedFiles()


def get_file_mod_time(file_name: str) -> int:
    """Get file modification time (last write time)"""
    return _rl.GetFileModTime(_str_in(file_name))


def compress_data(data: bytes) -> Tuple[bytes, int]:
    """Compress data (DEFLATE algorithm)"""
    compressed_length = IntPtr(0)
    compressed_data = _rl.CompressData(data, len(data), compressed_length)
    return compressed_data, compressed_length.contents


def decompress_data(comp_data: bytes) -> Tuple[bytes, int]:
    """Decompress data (DEFLATE algorithm)"""
    decompressed_length = IntPtr(0)
    decompressed_data = _rl.DecompressData(comp_data, len(comp_data), decompressed_length)
    return decompressed_data, decompressed_length.contents


def save_storage_value(position: int, value: int) -> bool:
    """Save integer value to storage file (to defined position), returns true on success"""
    return _rl.SaveStorageValue(int(position), int(value))


def load_storage_value(position: int) -> int:
    """Load integer value from storage file (from defined position)"""
    return _rl.LoadStorageValue(int(position))


def open_url(url: str) -> None:
    """Open URL with default system browser (if available)"""
    return _rl.OpenURL(_str_in(url))


def is_key_pressed(key: int) -> bool:
    """Detect if a key has been pressed once"""
    return _rl.IsKeyPressed(int(key))


def is_key_down(key: int) -> bool:
    """Detect if a key is being pressed"""
    return _rl.IsKeyDown(int(key))


def is_key_released(key: int) -> bool:
    """Detect if a key has been released once"""
    return _rl.IsKeyReleased(int(key))


def is_key_up(key: int) -> bool:
    """Detect if a key is NOT being pressed"""
    return _rl.IsKeyUp(int(key))


def set_exit_key(key: int) -> None:
    """Set a custom key to exit program (default is ESC)"""
    return _rl.SetExitKey(int(key))


def get_key_pressed() -> int:
    """Get key pressed (keycode), call it multiple times for keys queued"""
    return _rl.GetKeyPressed()


def get_char_pressed() -> int:
    """Get char pressed (unicode), call it multiple times for chars queued"""
    return _rl.GetCharPressed()


def is_gamepad_available(gamepad: int) -> bool:
    """Detect if a gamepad is available"""
    return _rl.IsGamepadAvailable(int(gamepad))


def is_gamepad_name(gamepad: int, name: str) -> bool:
    """Check gamepad name (if available)"""
    return _rl.IsGamepadName(int(gamepad), _str_in(name))


def get_gamepad_name(gamepad: int) -> str:
    """Return gamepad internal name id"""
    return _str_out(_rl.GetGamepadName(int(gamepad)))


def is_gamepad_button_pressed(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been pressed once"""
    return _rl.IsGamepadButtonPressed(int(gamepad), int(button))


def is_gamepad_button_down(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is being pressed"""
    return _rl.IsGamepadButtonDown(int(gamepad), int(button))


def is_gamepad_button_released(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been released once"""
    return _rl.IsGamepadButtonReleased(int(gamepad), int(button))


def is_gamepad_button_up(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is NOT being pressed"""
    return _rl.IsGamepadButtonUp(int(gamepad), int(button))


def get_gamepad_button_pressed() -> int:
    """Get the last gamepad button pressed"""
    return _rl.GetGamepadButtonPressed()


def get_gamepad_axis_count(gamepad: int) -> int:
    """Return gamepad axis count for a gamepad"""
    return _rl.GetGamepadAxisCount(int(gamepad))


def get_gamepad_axis_movement(gamepad: int, axis: int) -> float:
    """Return axis movement value for a gamepad axis"""
    return _rl.GetGamepadAxisMovement(int(gamepad), int(axis))


def set_gamepad_mappings(mappings: str) -> int:
    """Set internal gamepad mappings (SDL_GameControllerDB)"""
    return _rl.SetGamepadMappings(_str_in(mappings))


def is_mouse_button_pressed(button: int) -> bool:
    """Detect if a mouse button has been pressed once"""
    return _rl.IsMouseButtonPressed(int(button))


def is_mouse_button_down(button: int) -> bool:
    """Detect if a mouse button is being pressed"""
    return _rl.IsMouseButtonDown(int(button))


def is_mouse_button_released(button: int) -> bool:
    """Detect if a mouse button has been released once"""
    return _rl.IsMouseButtonReleased(int(button))


def is_mouse_button_up(button: int) -> bool:
    """Detect if a mouse button is NOT being pressed"""
    return _rl.IsMouseButtonUp(int(button))


def get_mouse_x() -> int:
    """Returns mouse position X"""
    return _rl.GetMouseX()


def get_mouse_y() -> int:
    """Returns mouse position Y"""
    return _rl.GetMouseY()


def get_mouse_position() -> Vector2:
    """Returns mouse position XY"""
    return _rl.GetMousePosition()


def set_mouse_position(x: int, y: int) -> None:
    """Set mouse position XY"""
    return _rl.SetMousePosition(int(x), int(y))


def set_mouse_offset(offset_x: int, offset_y: int) -> None:
    """Set mouse offset"""
    return _rl.SetMouseOffset(int(offset_x), int(offset_y))


def set_mouse_scale(scale_x: float, scale_y: float) -> None:
    """Set mouse scaling"""
    return _rl.SetMouseScale(float(scale_x), float(scale_y))


def get_mouse_wheel_move() -> float:
    """Returns mouse wheel movement Y"""
    return _rl.GetMouseWheelMove()


def set_mouse_cursor(cursor: int) -> None:
    """Set mouse cursor"""
    return _rl.SetMouseCursor(int(cursor))


def get_touch_x() -> int:
    """Returns touch position X for touch point 0 (relative to screen size)"""
    return _rl.GetTouchX()


def get_touch_y() -> int:
    """Returns touch position Y for touch point 0 (relative to screen size)"""
    return _rl.GetTouchY()


def get_touch_position(index: int) -> Vector2:
    """Returns touch position XY for a touch point index (relative to screen size)"""
    return _rl.GetTouchPosition(int(index))


def set_gestures_enabled(flags: int) -> None:
    """Enable a set of gestures using flags"""
    return _rl.SetGesturesEnabled(int(flags))


def is_gesture_detected(gesture: int) -> bool:
    """Check if a gesture have been detected"""
    return _rl.IsGestureDetected(int(gesture))


def get_gesture_detected() -> int:
    """Get latest detected gesture"""
    return _rl.GetGestureDetected()


def get_touch_points_count() -> int:
    """Get touch points count"""
    return _rl.GetTouchPointsCount()


def get_gesture_hold_duration() -> float:
    """Get gesture hold time in milliseconds"""
    return _rl.GetGestureHoldDuration()


def get_gesture_drag_vector() -> Vector2:
    """Get gesture drag vector"""
    return _rl.GetGestureDragVector()


def get_gesture_drag_angle() -> float:
    """Get gesture drag angle"""
    return _rl.GetGestureDragAngle()


def get_gesture_pinch_vector() -> Vector2:
    """Get gesture pinch delta"""
    return _rl.GetGesturePinchVector()


def get_gesture_pinch_angle() -> float:
    """Get gesture pinch angle"""
    return _rl.GetGesturePinchAngle()


def set_camera_mode(camera: Union[Camera, Camera3D], mode: int) -> None:
    """Set camera mode (multiple camera modes available)"""
    return _rl.SetCameraMode(camera, int(mode))


def update_camera(camera: Union[Camera, Camera3D]) -> None:
    """Update camera position for selected mode"""
    return _rl.UpdateCamera(byref(camera))


def set_camera_pan_control(key_pan: int) -> None:
    """Set camera pan key to combine with mouse movement (free camera)"""
    return _rl.SetCameraPanControl(int(key_pan))


def set_camera_alt_control(key_alt: int) -> None:
    """Set camera alt key to combine with mouse movement (free camera)"""
    return _rl.SetCameraAltControl(int(key_alt))


def set_camera_smooth_zoom_control(key_smooth_zoom: int) -> None:
    """Set camera smooth zoom key to combine with mouse (free camera)"""
    return _rl.SetCameraSmoothZoomControl(int(key_smooth_zoom))


def set_camera_move_controls(key_front: int, key_back: int, key_right: int, key_left: int, key_up: int,
                             key_down: int) -> None:
    """Set camera move controls (1st person and 3rd person cameras)"""
    return _rl.SetCameraMoveControls(int(key_front), int(key_back), int(key_right), int(key_left),
                                     int(key_up), int(key_down))


def set_shapes_texture(texture: Texture2D, source: AnyRect) -> None:
    """Set texture and rectangle to be used on shapes drawing

    It can be useful when using basic shapes and one single font,
    defining a font char white rectangle would allow drawing everything in a single draw call
    """
    return _rl.SetShapesTexture(texture, _rect(source))


def draw_pixel(pos_x: int, pos_y: int, color: AnyRGB) -> None:
    """Draw a pixel"""
    return _rl.DrawPixel(int(pos_x), int(pos_y), _color(color))


def draw_pixel_v(position: AnyVec2, color: AnyRGB) -> None:
    """Draw a pixel (Vector version)"""
    return _rl.DrawPixelV(_vec2(position), _color(color))


def draw_line(start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: AnyRGB) -> None:
    """Draw a line"""
    return _rl.DrawLine(int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y), _color(color))


def draw_line_v(start_pos: AnyVec2, end_pos: AnyVec2, color: AnyRGB) -> None:
    """Draw a line (Vector version)"""
    return _rl.DrawLineV(_vec2(start_pos), _vec2(end_pos), _color(color))


def draw_line_ex(start_pos: AnyVec2, end_pos: AnyVec2, thick: float, color: AnyRGB) -> None:
    """Draw a line defining thickness"""
    return _rl.DrawLineEx(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))


def draw_line_bezier(start_pos: AnyVec2, end_pos: AnyVec2, thick: float, color: AnyRGB) -> None:
    """Draw a line using cubic-bezier curves in-out"""
    return _rl.DrawLineBezier(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))


def draw_line_bezier_quad(start_pos: AnyVec2, end_pos: AnyVec2, control_pos: AnyVec2, thick: float,
                          color: AnyRGB) -> None:
    """Draw line using quadratic bezier curves with a control point"""
    return _rl.DrawLineBezierQuad(_vec2(start_pos), _vec2(end_pos), _vec2(control_pos), float(thick),
                                  _color(color))


def draw_line_strip(points: Sequence[Vector2], points_count: int, color: AnyRGB) -> None:
    """Draw lines sequence"""
    return _rl.DrawLineStrip(_arr(Vector2, points), int(points_count), _color(color))


def draw_circle(center_x: int, center_y: int, radius: float, color: AnyRGB) -> None:
    """Draw a color-filled circle"""
    return _rl.DrawCircle(int(center_x), int(center_y), float(radius), _color(color))


def draw_circle_sector(center: AnyVec2, radius: float, start_angle: float, end_angle: float,
                       segments: int, color: AnyRGB) -> None:
    """Draw a piece of a circle"""
    return _rl.DrawCircleSector(_vec2(center), float(radius), float(start_angle), float(end_angle), int(segments),
                                _color(color))


def draw_circle_sector_lines(center: AnyVec2, radius: float, start_angle: float, end_angle: float, segments: int,
                             color: AnyRGB) -> None:
    """Draw circle sector outline"""
    return _rl.DrawCircleSectorLines(_vec2(center), float(radius), float(start_angle), float(end_angle), int(segments),
                                     _color(color))


def draw_circle_gradient(center_x: int, center_y: int, radius: float, color1: AnyRGB, color2: AnyRGB) -> None:
    """Draw a gradient-filled circle"""
    return _rl.DrawCircleGradient(int(center_x), int(center_y), float(radius), _color(color1), _color(color2))


def draw_circle_v(center: AnyVec2, radius: float, color: AnyRGB) -> None:
    """Draw a color-filled circle (Vector version)"""
    return _rl.DrawCircleV(_vec2(center), float(radius), _color(color))


def draw_circle_lines(center_x: int, center_y: int, radius: float, color: AnyRGB) -> None:
    """Draw circle outline"""
    return _rl.DrawCircleLines(int(center_x), int(center_y), float(radius), _color(color))


def draw_ellipse(center_x: int, center_y: int, radius_h: float, radius_v: float, color: AnyRGB) -> None:
    """Draw ellipse"""
    return _rl.DrawEllipse(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))


def draw_ellipse_lines(center_x: int, center_y: int, radius_h: float, radius_v: float, color: AnyRGB) -> None:
    """Draw ellipse outline"""
    return _rl.DrawEllipseLines(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))


def draw_ring(center: AnyVec2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float,
              segments: int, color: AnyRGB) -> None:
    """Draw ring"""
    return _rl.DrawRing(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle), float(end_angle),
                        int(segments), _color(color))


def draw_ring_lines(center: AnyVec2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float,
                    segments: int, color: AnyRGB) -> None:
    """Draw ring outline"""
    return _rl.DrawRingLines(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle),
                             float(end_angle), int(segments), _color(color))


def draw_rectangle(pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
    """Draw a color-filled rectangle"""
    return _rl.DrawRectangle(int(pos_x), int(pos_y), int(width), int(height), _color(color))


def draw_rectangle_v(position: AnyVec2, size: AnyVec2, color: AnyRGB) -> None:
    """Draw a color-filled rectangle (Vector version)"""
    return _rl.DrawRectangleV(_vec2(position), _vec2(size), _color(color))


def draw_rectangle_rec(rec: AnyRect, color: AnyRGB) -> None:
    """Draw a color-filled rectangle"""
    return _rl.DrawRectangleRec(_rect(rec), _color(color))


def draw_rectangle_pro(rec: AnyRect, origin: AnyVec2, rotation: float, color: AnyRGB) -> None:
    """Draw a color-filled rectangle with pro parameters"""
    return _rl.DrawRectanglePro(_rect(rec), _vec2(origin), float(rotation), _color(color))


def draw_rectangle_gradient_v(pos_x: int, pos_y: int, width: int, height: int, color1: AnyRGB, color2: AnyRGB) -> None:
    """Draw a vertical-gradient-filled rectangle"""
    return _rl.DrawRectangleGradientV(int(pos_x), int(pos_y), int(width), int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_h(pos_x: int, pos_y: int, width: int, height: int, color1: AnyRGB, color2: AnyRGB) -> None:
    """Draw a horizontal-gradient-filled rectangle"""
    return _rl.DrawRectangleGradientH(int(pos_x), int(pos_y), int(width), int(height), _color(color1), _color(color2))


def draw_rectangle_gradient_ex(rec: AnyRect, col1: AnyRGB, col2: AnyRGB, col3: AnyRGB, col4: AnyRGB) -> None:
    """Draw a gradient-filled rectangle with custom vertex colors"""
    return _rl.DrawRectangleGradientEx(_rect(rec), _color(col1), _color(col2), _color(col3), _color(col4))


def draw_rectangle_lines(pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
    """Draw rectangle outline"""
    return _rl.DrawRectangleLines(int(pos_x), int(pos_y), int(width), int(height), _color(color))


def draw_rectangle_lines_ex(rec: AnyRect, line_thick: int, color: AnyRGB) -> None:
    """Draw rectangle outline with extended parameters"""
    return _rl.DrawRectangleLinesEx(_rect(rec), int(line_thick), _color(color))


def draw_rectangle_rounded(rec: AnyRect, roundness: float, segments: int, color: AnyRGB) -> None:
    """Draw rectangle with rounded edges"""
    return _rl.DrawRectangleRounded(_rect(rec), float(roundness), int(segments), _color(color))


def draw_rectangle_rounded_lines(rec: AnyRect, roundness: float, segments: int, line_thick: int, color: AnyRGB) -> None:
    """Draw rectangle with rounded edges outline"""
    return _rl.DrawRectangleRoundedLines(_rect(rec), float(roundness), int(segments), int(line_thick), _color(color))


def draw_triangle(v1: AnyVec2, v2: AnyVec2, v3: AnyVec2, color: AnyRGB) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    return _rl.DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_lines(v1: AnyVec2, v2: AnyVec2, v3: AnyVec2, color: AnyRGB) -> None:
    """Draw triangle outline (vertex in counter-clockwise order!)"""
    return _rl.DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))


def draw_triangle_fan(points: Sequence[Vector2], points_count: int, color: AnyRGB) -> None:
    """Draw a triangle fan defined by points (first vertex is the center)"""
    return _rl.DrawTriangleFan(_arr(Vector2, points), int(points_count), _color(color))


def draw_triangle_strip(points: Sequence[Vector2], points_count: int, color: AnyRGB) -> None:
    """Draw a triangle strip defined by points"""
    return _rl.DrawTriangleStrip(_arr(Vector2, points), int(points_count), _color(color))


def draw_poly(center: AnyVec2, sides: int, radius: float, rotation: float, color: AnyRGB) -> None:
    """Draw a regular polygon (Vector version)"""
    return _rl.DrawPoly(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def draw_poly_lines(center: AnyVec2, sides: int, radius: float, rotation: float, color: AnyRGB) -> None:
    """Draw a polygon outline of n sides"""
    return _rl.DrawPolyLines(_vec2(center), int(sides), float(radius), float(rotation), _color(color))


def check_collision_recs(rec1: AnyRect, rec2: AnyRect) -> bool:
    """Check collision between two rectangles"""
    return _rl.CheckCollisionRecs(_rect(rec1), _rect(rec2))


def check_collision_circles(center1: AnyVec2, radius1: float, center2: AnyVec2, radius2: float) -> bool:
    """Check collision between two circles"""
    return _rl.CheckCollisionCircles(_vec2(center1), float(radius1), _vec2(center2), float(radius2))


def check_collision_circle_rec(center: AnyVec2, radius: float, rec: AnyRect) -> bool:
    """Check collision between circle and rectangle"""
    return _rl.CheckCollisionCircleRec(_vec2(center), float(radius), _rect(rec))


def check_collision_point_rec(point: AnyVec2, rec: AnyRect) -> bool:
    """Check if point is inside rectangle"""
    return _rl.CheckCollisionPointRec(_vec2(point), _rect(rec))


def check_collision_point_circle(point: AnyVec2, center: AnyVec2, radius: float) -> bool:
    """Check if point is inside circle"""
    return _rl.CheckCollisionPointCircle(_vec2(point), _vec2(center), float(radius))


def check_collision_point_triangle(point: AnyVec2, p1: AnyVec2, p2: AnyVec2, p3: AnyVec2) -> bool:
    """Check if point is inside a triangle"""
    return _rl.CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))


def check_collision_lines(start_pos1: AnyVec2, end_pos1: AnyVec2, start_pos2: AnyVec2, end_pos2: AnyVec2,
                          collision_point: Sequence[Vector2]) -> bool:
    """Check the collision between two lines defined by two points each, returns collision point by reference"""
    return _rl.CheckCollisionLines(_vec2(start_pos1), _vec2(end_pos1), _vec2(start_pos2), _vec2(end_pos2),
                                   _arr(Vector2, collision_point))


def get_collision_rec(rec1: AnyRect, rec2: AnyRect) -> Rectangle:
    """Get collision rectangle for two rectangles collision"""
    return _rl.GetCollisionRec(_rect(rec1), _rect(rec2))


def load_image(file_name: str) -> Image:
    """Load image from file into CPU memory (RAM)"""
    return _rl.LoadImage(_str_in(file_name))


def load_image_raw(file_name: str, width: int, height: int, format_: int, header_size: int) -> Image:
    """Load image from RAW file data"""
    return _rl.LoadImageRaw(_str_in(file_name), int(width), int(height), int(format_), int(header_size))


def load_image_anim(file_name: str) -> Tuple[Image, int]:
    """Load image sequence from file (frames appended to image.data)"""
    frames = IntPtr(0)
    image = _rl.LoadImageAnim(_str_in(file_name), frames)
    return image, frames.contents


def load_image_from_memory(file_type: str, file_data: bytes, data_size: int) -> Image:
    """Load image from memory buffer, fileType refers to extension: i.e. ".png"."""
    return _rl.LoadImageFromMemory(_str_in(file_type), file_data, int(data_size))


def unload_image(image: Image) -> None:
    """Unload image from CPU memory (RAM)"""
    return _rl.UnloadImage(image)


def export_image(image: Image, file_name: str) -> bool:
    """Export image data to file, returns true on success"""
    return _rl.ExportImage(image, _str_in(file_name))


def export_image_as_code(image: Image, file_name: str) -> bool:
    """Export image as code file defining an array of bytes, returns true on success"""
    return _rl.ExportImageAsCode(image, _str_in(file_name))


def gen_image_color(width: int, height: int, color: AnyRGB) -> Image:
    """Generate image: plain color"""
    return _rl.GenImageColor(int(width), int(height), _color(color))


def gen_image_gradient_v(width: int, height: int, top: AnyRGB, bottom: AnyRGB) -> Image:
    """Generate image: vertical gradient"""
    return _rl.GenImageGradientV(int(width), int(height), _color(top), _color(bottom))


def gen_image_gradient_h(width: int, height: int, left: AnyRGB, right: AnyRGB) -> Image:
    """Generate image: horizontal gradient"""
    return _rl.GenImageGradientH(int(width), int(height), _color(left), _color(right))


def gen_image_gradient_radial(width: int, height: int, density: float, inner: AnyRGB, outer: AnyRGB) -> Image:
    """Generate image: radial gradient"""
    return _rl.GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))


def gen_image_checked(width: int, height: int, checks_x: int, checks_y: int, col1: AnyRGB, col2: AnyRGB) -> Image:
    """Generate image: checked"""
    return _rl.GenImageChecked(int(width), int(height), int(checks_x), int(checks_y), _color(col1), _color(col2))


def gen_image_white_noise(width: int, height: int, factor: float) -> Image:
    """Generate image: white noise"""
    return _rl.GenImageWhiteNoise(int(width), int(height), float(factor))


def gen_image_perlin_noise(width: int, height: int, offset_x: int, offset_y: int, scale: float) -> Image:
    """Generate image: perlin noise"""
    return _rl.GenImagePerlinNoise(int(width), int(height), int(offset_x), int(offset_y), float(scale))


def gen_image_cellular(width: int, height: int, tile_size: int) -> Image:
    """Generate image: cellular algorithm. Bigger tileSize means bigger cells"""
    return _rl.GenImageCellular(int(width), int(height), int(tile_size))


def image_copy(image: Image) -> Image:
    """Create an image duplicate (useful for transformations)"""
    return _rl.ImageCopy(image)


def image_from_image(image: Image, rec: AnyRect) -> Image:
    """Create an image from another image piece"""
    return _rl.ImageFromImage(image, _rect(rec))


def image_text(text: str, font_size: int, color: AnyRGB) -> Image:
    """Create an image from text (default font)"""
    return _rl.ImageText(_str_in(text), int(font_size), _color(color))


def image_text_ex(font: Font, text: str, font_size: float, spacing: float, tint: AnyRGB) -> Image:
    """Create an image from text (custom sprite font)"""
    return _rl.ImageTextEx(font, _str_in(text), float(font_size), float(spacing), _color(tint))


def image_format(image: Image, new_format: int) -> None:
    """Convert image data to desired format"""
    return _rl.ImageFormat(byref(image), int(new_format))


def image_to_pot(image: Image, fill: AnyRGB) -> None:
    """Convert image to POT (power-of-two)"""
    return _rl.ImageToPOT(byref(image), _color(fill))


def image_crop(image: Image, crop: AnyRect) -> None:
    """Crop an image to a defined rectangle"""
    return _rl.ImageCrop(byref(image), _rect(crop))


def image_alpha_crop(image: Image, threshold: float) -> None:
    """Crop image depending on alpha value"""
    return _rl.ImageAlphaCrop(byref(image), float(threshold))


def image_alpha_clear(image: Image, color: AnyRGB, threshold: float) -> None:
    """Clear alpha channel to desired color"""
    return _rl.ImageAlphaClear(byref(image), _color(color), float(threshold))


def image_alpha_mask(image: Image, alpha_mask: Image) -> None:
    """Apply alpha mask to image"""
    return _rl.ImageAlphaMask(byref(image), alpha_mask)


def image_alpha_premultiply(image: Image) -> None:
    """Premultiply alpha channel"""
    return _rl.ImageAlphaPremultiply(byref(image))


def image_resize(image: Image, new_width: int, new_height: int) -> None:
    """Resize image (Bicubic scaling algorithm)"""
    return _rl.ImageResize(byref(image), int(new_width), int(new_height))


def image_resize_nn(image: Image, new_width: int, new_height: int) -> None:
    """Resize image (Nearest-Neighbor scaling algorithm)"""
    return _rl.ImageResizeNN(byref(image), int(new_width), int(new_height))


def image_resize_canvas(image: Image, new_width: int, new_height: int, offset_x: int, offset_y: int,
                        fill: AnyRGB) -> None:
    """Resize canvas and fill with color"""
    return _rl.ImageResizeCanvas(byref(image), int(new_width), int(new_height), int(offset_x), int(offset_y),
                                 _color(fill))


def image_mipmaps(image: Image) -> None:
    """Generate all mipmap levels for a provided image"""
    return _rl.ImageMipmaps(byref(image))


def image_dither(image: Image, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None:
    """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
    return _rl.ImageDither(byref(image), int(r_bpp), int(g_bpp), int(b_bpp), int(a_bpp))


def image_flip_vertical(image: Image) -> None:
    """Flip image vertically"""
    return _rl.ImageFlipVertical(byref(image))


def image_flip_horizontal(image: Image) -> None:
    """Flip image horizontally"""
    return _rl.ImageFlipHorizontal(byref(image))


def image_rotate_cw(image: Image) -> None:
    """Rotate image clockwise 90deg"""
    return _rl.ImageRotateCW(byref(image))


def image_rotate_ccw(image: Image) -> None:
    """Rotate image counter-clockwise 90deg"""
    return _rl.ImageRotateCCW(byref(image))


def image_color_tint(image: Image, color: AnyRGB) -> None:
    """Modify image color: tint"""
    return _rl.ImageColorTint(byref(image), _color(color))


def image_color_invert(image: Image) -> None:
    """Modify image color: invert"""
    return _rl.ImageColorInvert(byref(image))


def image_color_grayscale(image: Image) -> None:
    """Modify image color: grayscale"""
    return _rl.ImageColorGrayscale(byref(image))


def image_color_contrast(image: Image, contrast: float) -> None:
    """Modify image color: contrast (-100 to 100)"""
    return _rl.ImageColorContrast(byref(image), float(contrast))


def image_color_brightness(image: Image, brightness: int) -> None:
    """Modify image color: brightness (-255 to 255)"""
    return _rl.ImageColorBrightness(byref(image), int(brightness))


def image_color_replace(image: Image, color: AnyRGB, replace: AnyRGB) -> None:
    """Modify image color: replace color"""
    return _rl.ImageColorReplace(byref(image), _color(color), _color(replace))


def load_image_colors(image: Image) -> Sequence[Color]:
    """Load color data from image as a Color array (RGBA - 32bit)"""
    result = _rl.LoadImageColors(image)
    colors = []
    i = 0
    while result[i] is not None:
        colors.append(result[i])
    return tuple(colors)


def load_image_palette(image: Image, max_palette_size: int) -> Sequence[Color]:
    """Load colors palette from image as a Color array (RGBA - 32bit)"""
    colors_count = IntPtr(0)
    result = _rl.LoadImagePalette(image, int(max_palette_size), colors_count)
    colors = [color for color in result[:colors_count.contents[0]]]
    return tuple(colors)


def unload_image_colors(colors: Sequence[Color]) -> None:
    """Unload color data loaded with LoadImageColors()"""
    return _rl.UnloadImageColors(_arr(Color, colors))


def unload_image_palette(colors: Sequence[Color]) -> None:
    """Unload colors palette loaded with LoadImagePalette()"""
    return _rl.UnloadImagePalette(_arr(Color, colors))


def get_image_alpha_border(image: Image, threshold: float) -> Rectangle:
    """Get image alpha border rectangle"""
    return _rl.GetImageAlphaBorder(image, float(threshold))


def image_clear_background(dst: Image, color: AnyRGB) -> None:
    """Clear image background with given color"""
    return _rl.ImageClearBackground(byref(dst), _color(color))


def image_draw_pixel(dst: Image, pos_x: int, pos_y: int, color: AnyRGB) -> None:
    """Draw pixel within an image"""
    return _rl.ImageDrawPixel(byref(dst), int(pos_x), int(pos_y), _color(color))


def image_draw_pixel_v(dst: Image, position: AnyVec2, color: AnyRGB) -> None:
    """Draw pixel within an image (Vector version)"""
    return _rl.ImageDrawPixelV(byref(dst), _vec2(position), _color(color))


def image_draw_line(dst: Image, start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int,
                    color: AnyRGB) -> None:
    """Draw line within an image"""
    return _rl.ImageDrawLine(byref(dst), int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y),
                             _color(color))


def image_draw_line_v(dst: Image, start: AnyVec2, end: AnyVec2, color: AnyRGB) -> None:
    """Draw line within an image (Vector version)"""
    return _rl.ImageDrawLineV(byref(dst), _vec2(start), _vec2(end), _color(color))


def image_draw_circle(dst: Image, center_x: int, center_y: int, radius: int, color: AnyRGB) -> None:
    """Draw circle within an image"""
    return _rl.ImageDrawCircle(byref(dst), int(center_x), int(center_y), int(radius), _color(color))


def image_draw_circle_v(dst: Image, center: AnyVec2, radius: int, color: AnyRGB) -> None:
    """Draw circle within an image (Vector version)"""
    return _rl.ImageDrawCircleV(byref(dst), _vec2(center), int(radius), _color(color))


def image_draw_rectangle(dst: Image, pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
    """Draw rectangle within an image"""
    return _rl.ImageDrawRectangle(byref(dst), int(pos_x), int(pos_y), int(width), int(height), _color(color))


def image_draw_rectangle_v(dst: Image, position: AnyVec2, size: AnyVec2, color: AnyRGB) -> None:
    """Draw rectangle within an image (Vector version)"""
    return _rl.ImageDrawRectangleV(byref(dst), _vec2(position), _vec2(size), _color(color))


def image_draw_rectangle_rec(dst: Image, rec: AnyRect, color: AnyRGB) -> None:
    """Draw rectangle within an image"""
    return _rl.ImageDrawRectangleRec(byref(dst), _rect(rec), _color(color))


def image_draw_rectangle_lines(dst: Image, rec: AnyRect, thick: int, color: AnyRGB) -> None:
    """Draw rectangle lines within an image"""
    return _rl.ImageDrawRectangleLines(byref(dst), _rect(rec), int(thick), _color(color))


def image_draw(dst: Image, src: Image, src_rec: AnyRect, dst_rec: AnyRect, tint: AnyRGB) -> None:
    """Draw a source image within a destination image (tint applied to source)"""
    return _rl.ImageDraw(byref(dst), src, _rect(src_rec), _rect(dst_rec), _color(tint))


def image_draw_text(dst: Image, text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
    """Draw text (using default font) within an image (destination)"""
    return _rl.ImageDrawText(byref(dst), _str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))


def image_draw_text_ex(dst: Image, font: Font, text: str, position: AnyVec2, font_size: float, spacing: float,
                       tint: AnyRGB) -> None:
    """Draw text (custom sprite font) within an image (destination)"""
    return _rl.ImageDrawTextEx(byref(dst), font, _str_in(text), _vec2(position), float(font_size), float(spacing),
                               _color(tint))


def load_texture(file_name: str) -> Texture2D:
    """Load texture from file into GPU memory (VRAM)"""
    return _rl.LoadTexture(_str_in(file_name))


def load_texture_from_image(image: Image) -> Texture2D:
    """Load texture from image data"""
    return _rl.LoadTextureFromImage(image)


def load_texture_cubemap(image: Image, layout: int) -> TextureCubemap:
    """Load cubemap from image, multiple image cubemap layouts supported"""
    return _rl.LoadTextureCubemap(image, int(layout))


def load_render_texture(width: int, height: int) -> RenderTexture2D:
    """Load texture for rendering (framebuffer)"""
    return _rl.LoadRenderTexture(int(width), int(height))


def unload_texture(texture: Texture2D) -> None:
    """Unload texture from GPU memory (VRAM)"""
    return _rl.UnloadTexture(texture)


def unload_render_texture(target: RenderTexture2D) -> None:
    """Unload render texture from GPU memory (VRAM)"""
    return _rl.UnloadRenderTexture(target)


def update_texture(texture: Texture2D, pixels: bytes) -> None:
    """Update GPU texture with new data"""
    return _rl.UpdateTexture(texture, pixels)


def update_texture_rec(texture: Texture2D, rec: AnyRect, pixels: bytes) -> None:
    """Update GPU texture rectangle with new data"""
    return _rl.UpdateTextureRec(texture, _rect(rec), pixels)


def get_texture_data(texture: Texture2D) -> Image:
    """Get pixel data from GPU texture and return an Image"""
    return _rl.GetTextureData(texture)


def get_screen_data() -> Image:
    """Get pixel data from screen buffer and return an Image (screenshot)"""
    return _rl.GetScreenData()


def gen_texture_mipmaps(texture: Texture2D) -> None:
    """Generate GPU mipmaps for a texture"""
    return _rl.GenTextureMipmaps(byref(texture))


def set_texture_filter(texture: Texture2D, filter_: int) -> None:
    """Set texture scaling filter mode"""
    return _rl.SetTextureFilter(texture, int(filter_))


def set_texture_wrap(texture: Texture2D, wrap: int) -> None:
    """Set texture wrapping mode"""
    return _rl.SetTextureWrap(texture, int(wrap))


def draw_texture(texture: Texture2D, pos_x: int, pos_y: int, tint: AnyRGB) -> None:
    """Draw a Texture2D"""
    return _rl.DrawTexture(texture, int(pos_x), int(pos_y), _color(tint))


def draw_texture_v(texture: Texture2D, position: AnyVec2, tint: AnyRGB) -> None:
    """Draw a Texture2D with position defined as Vector2"""
    return _rl.DrawTextureV(texture, _vec2(position), _color(tint))


def draw_texture_ex(texture: Texture2D, position: AnyVec2, rotation: float, scale: float, tint: AnyRGB) -> None:
    """Draw a Texture2D with extended parameters"""
    return _rl.DrawTextureEx(texture, _vec2(position), float(rotation), float(scale), _color(tint))


def draw_texture_rec(texture: Texture2D, source: AnyRect, position: AnyVec2, tint: AnyRGB) -> None:
    """Draw a part of a texture defined by a rectangle"""
    return _rl.DrawTextureRec(texture, _rect(source), _vec2(position), _color(tint))


def draw_texture_quad(texture: Texture2D, tiling: AnyVec2, offset: AnyVec2, quad: AnyRect, tint: AnyRGB) -> None:
    """Draw texture quad with tiling and offset parameters"""
    return _rl.DrawTextureQuad(texture, _vec2(tiling), _vec2(offset), _rect(quad), _color(tint))


def draw_texture_tiled(texture: Texture2D, source: AnyRect, dest: AnyRect, origin: AnyVec2, rotation: float,
                       scale: float, tint: AnyRGB) -> None:
    """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
    return _rl.DrawTextureTiled(texture, _rect(source), _rect(dest), _vec2(origin), float(rotation), float(scale),
                                _color(tint))


def draw_texture_pro(texture: Texture2D, source: AnyRect, dest: AnyRect, origin: AnyVec2, rotation: float,
                     tint: AnyRGB) -> None:
    """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
    return _rl.DrawTexturePro(texture, _rect(source), _rect(dest), _vec2(origin), float(rotation), _color(tint))


def draw_texture_npatch(texture: Texture2D, n_patch_info: NPatchInfo, dest: AnyRect, origin: AnyVec2, rotation: float,
                        tint: AnyRGB) -> None:
    """Draws a texture (or part of it) that stretches or shrinks nicely"""
    return _rl.DrawTextureNPatch(texture, n_patch_info, _rect(dest), _vec2(origin), float(rotation), _color(tint))


def draw_texture_poly(texture: Texture2D, center: AnyVec2, points: Sequence[Vector2], texcoords: Sequence[Vector2],
                      points_count: int, tint: AnyRGB) -> None:
    """Draw a textured polygon"""
    return _rl.DrawTexturePoly(texture, _vec2(center), _arr(Vector2, points), _arr(Vector2, texcoords),
                               int(points_count), _color(tint))


def fade(color: AnyRGB, alpha: float) -> Color:
    """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
    return _rl.Fade(_color(color), float(alpha))


def color_to_int(color: AnyRGB) -> int:
    """Returns hexadecimal value for a Color"""
    return _rl.ColorToInt(_color(color))


def color_normalize(color: AnyRGB) -> Vector4:
    """Returns Color normalized as float [0..1]"""
    return _rl.ColorNormalize(_color(color))


def color_from_normalized(normalized: AnyVec4) -> Color:
    """Returns Color from normalized values [0..1]"""
    return _rl.ColorFromNormalized(_vec4(normalized))


def color_to_hsv(color: AnyRGB) -> Vector3:
    """Returns HSV values for a Color, hue [0..360], saturation/value [0..1]"""
    return _rl.ColorToHSV(_color(color))


def color_from_hsv(hue: float, saturation: float, value: float) -> Color:
    """Returns a Color from HSV values, hue [0..360], saturation/value [0..1]"""
    return _rl.ColorFromHSV(float(hue), float(saturation), float(value))


def color_alpha(color: AnyRGB, alpha: float) -> Color:
    """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
    return _rl.ColorAlpha(_color(color), float(alpha))


def color_alpha_blend(dst: AnyRGB, src: AnyRGB, tint: AnyRGB) -> Color:
    """Returns src alpha-blended into dst color with tint"""
    return _rl.ColorAlphaBlend(_color(dst), _color(src), _color(tint))


def get_color(hex_value: int) -> Color:
    """Get Color structure from hexadecimal value"""
    return _rl.GetColor(int(hex_value))


def get_pixel_color(src_ptr: bytes, format_: int) -> Color:
    """Get Color from a source pixel pointer of certain format"""
    return _rl.GetPixelColor(src_ptr, int(format_))


def set_pixel_color(dst_ptr: bytes, color: AnyRGB, format_: int) -> None:
    """Set color formatted into destination pixel pointer"""
    return _rl.SetPixelColor(dst_ptr, _color(color), int(format_))


def get_pixel_data_size(width: int, height: int, format_: int) -> int:
    """Get pixel data size in bytes for certain format"""
    return _rl.GetPixelDataSize(int(width), int(height), int(format_))


def get_font_default() -> Font:
    """Get the default Font"""
    return _rl.GetFontDefault()


def load_font(file_name: str) -> Font:
    """Load font from file into GPU memory (VRAM)"""
    return _rl.LoadFont(_str_in(file_name))


def load_font_ex(file_name: str, font_size: int, font_chars: str) -> Font:
    """Load font from file with extended parameters"""
    chars_count = [ord(ch) for ch in font_chars]
    chars = _arr(Int, chars_count)
    return _rl.LoadFontEx(_str_in(file_name), int(font_size), chars, chars_count)


def load_font_from_image(image: Image, key: AnyRGB, first_char: int) -> Font:
    """Load font from Image (XNA style)"""
    return _rl.LoadFontFromImage(image, _color(key), int(first_char))


def load_font_from_memory(file_type: str, file_data: bytes, font_size: int, font_chars: str) -> Font:
    """Load font from memory buffer, fileType refers to extension: i.e. ".ttf"."""
    chars_count = [ord(ch) for ch in font_chars]
    chars = _arr(Int, chars_count)
    return _rl.LoadFontFromMemory(_str_in(file_type), file_data, len(file_data), int(font_size), chars, chars_count)


def load_font_data(file_data: bytes, data_size: int, font_size: int, font_chars: str, type_: int) -> Sequence[CharInfo]:
    """Load font data for further use"""
    chars_count = [ord(ch) for ch in font_chars]
    chars = _arr(Int, chars_count)
    result = _rl.LoadFontData(file_data, int(data_size), int(font_size), chars, len(chars_count), int(type_))
    return tuple(char_info for char_info in result[:len(chars_count)])


def gen_image_font_atlas(chars: Sequence[CharInfo], recs: Sequence[Sequence[Rectangle]], chars_count: int,
                         font_size: int, padding: int, pack_method: int) -> Image:
    """Generate image font atlas using chars info"""
    return _rl.GenImageFontAtlas(_arr(CharInfo, chars), _arr2(Rectangle, recs), int(chars_count), int(font_size),
                                 int(padding), int(pack_method))


def unload_font_data(chars: Sequence[CharInfo], chars_count: int) -> None:
    """Unload font chars info data (RAM)"""
    return _rl.UnloadFontData(_arr(CharInfo, chars), int(chars_count))


def unload_font(font: Font) -> None:
    """Unload Font from GPU memory (VRAM)"""
    return _rl.UnloadFont(font)


def draw_fps(pos_x: int, pos_y: int) -> None:
    """Draw current FPS"""
    return _rl.DrawFPS(int(pos_x), int(pos_y))


def draw_text(text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
    """Draw text (using default font)"""
    return _rl.DrawText(_str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))


def draw_text_ex(font: Font, text: str, position: AnyVec2, font_size: float, spacing: float, tint: AnyRGB) -> None:
    """Draw text using font and additional parameters"""
    return _rl.DrawTextEx(font, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))


def draw_text_rec(font: Font, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                  tint: AnyRGB) -> None:
    """Draw text using font inside rectangle limits"""
    return _rl.DrawTextRec(font, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                           _color(tint))


def draw_text_rec_ex(font: Font, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                     tint: AnyRGB, select_start: int, select_length: int, select_tint: AnyRGB,
                     select_back_tint: AnyRGB) -> None:
    """Draw text using font inside rectangle limits with support for text selection"""
    return _rl.DrawTextRecEx(font, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                             _color(tint), int(select_start), int(select_length), _color(select_tint),
                             _color(select_back_tint))


def draw_text_codepoint(font: Font, codepoint: int, position: AnyVec2, font_size: float, tint: AnyRGB) -> None:
    """Draw one character (codepoint)"""
    return _rl.DrawTextCodepoint(font, int(codepoint), _vec2(position), float(font_size), _color(tint))


def measure_text(text: str, font_size: int) -> int:
    """Measure string width for default font"""
    return _rl.MeasureText(_str_in(text), int(font_size))


def measure_text_ex(font: Font, text: str, font_size: float, spacing: float) -> Vector2:
    """Measure string size for Font"""
    return _rl.MeasureTextEx(font, _str_in(text), float(font_size), float(spacing))


def get_glyph_index(font: Font, codepoint: int) -> int:
    """Get index position for a unicode character on font"""
    return _rl.GetGlyphIndex(font, int(codepoint))


def text_copy(dst: str, src: str) -> int:
    """Copy one string to another, returns bytes copied"""
    return _rl.TextCopy(_str_in(dst), _str_in(src))


def text_is_equal(text1: str, text2: str) -> bool:
    """Check if two text string are equal"""
    return _rl.TextIsEqual(_str_in(text1), _str_in(text2))


def text_length(text: str) -> int:
    """Get text length, checks for '\0' ending"""
    return _rl.TextLength(_str_in(text))


def text_format(text: str, *args, **kwargs) -> str:
    """Text formatting with variables (Python formatting rules)"""
    # return _rl.TextFormat(_str_in(text), ...)
    return text.format(*args, **kwargs)


def text_subtext(text: str, position: int, length: int) -> str:
    """Get a piece of a text string"""
    return _rl.TextSubtext(_str_in(text), int(position), int(length))


def text_replace(text: str, replace: str, by: str) -> str:
    """Replace text string (memory must be freed!)"""
    return _rl.TextReplace(_str_in(text), _str_in(replace), _str_in(by))


def text_insert(text: str, insert: str, position: int) -> str:
    """Insert text in a position (memory must be freed!)"""
    return _rl.TextInsert(_str_in(text), _str_in(insert), int(position))


def text_join(text_list: Sequence[str], count: int, delimiter: str) -> str:
    """Join text strings with delimiter"""
    return _rl.TextJoin(_str_in2(text_list), int(count), _str_in(delimiter))


def text_split(text: str, delimiter: int) -> Sequence[bytes]:
    """Split text into multiple strings"""
    count = IntPtr(0)
    splits = _rl.TextSplit(_str_in(text), int(delimiter), count)
    return tuple(split for split in splits[:count.contents[0]])


def text_append(text: str, append: str, position: int) -> int:
    """Append text at specific position and move cursor!"""
    ptr = IntPtr(position)
    _rl.TextAppend(_str_in(text), _str_in(append), ptr)
    return ptr.contents[0]


def text_find_index(text: str, find: str) -> int:
    """Find first text occurrence within a string"""
    return _rl.TextFindIndex(_str_in(text), _str_in(find))


def text_to_upper(text: str) -> str:
    """Get upper case version of provided string"""
    return _rl.TextToUpper(_str_in(text))


def text_to_lower(text: str) -> str:
    """Get lower case version of provided string"""
    return _rl.TextToLower(_str_in(text))


def text_to_pascal(text: str) -> str:
    """Get Pascal case notation version of provided string"""
    return _rl.TextToPascal(_str_in(text))


def text_to_integer(text: str) -> int:
    """Get integer value from text (negative values not supported)"""
    return _rl.TextToInteger(_str_in(text))


def text_to_utf8(codepoints: Sequence[int], length: int) -> str:
    """Encode text codepoint into utf8 text (memory must be freed!)"""
    return _rl.TextToUtf8(_arr(Int, codepoints), int(length))


def get_codepoints(text: str) -> Tuple[int, int]:
    """Get all codepoints in a string, codepoints count returned by parameters"""
    count = IntPtr(0)
    result = _rl.GetCodepoints(_str_in(text), count)
    return result, count.contents[0]


def get_codepoints_count(text: str) -> int:
    """Get total number of characters (codepoints) in a UTF8 encoded string"""
    return _rl.GetCodepointsCount(_str_in(text))


def get_next_codepoint(text: str) -> Tuple[int, int]:
    """Returns next codepoint in a UTF8 encoded string; 0x3f('?') is returned on failure"""
    bytes_processed = IntPtr(0)
    result = _rl.GetNextCodepoint(_str_in(text), bytes_processed)
    return result, bytes_processed.contents[0]


def codepoint_to_utf8(codepoint: int) -> Tuple[str, int]:
    """Encode codepoint into utf8 text (char array length returned as parameter)"""
    byte_length = IntPtr(0)
    result = _rl.CodepointToUtf8(int(codepoint), byte_length)
    return result, byte_length.contents[0]


def draw_line3d(start_pos: AnyVec3, end_pos: AnyVec3, color: AnyRGB) -> None:
    """Draw a line in 3D world space"""
    return _rl.DrawLine3D(_vec3(start_pos), _vec3(end_pos), _color(color))


def draw_point3d(position: AnyVec3, color: AnyRGB) -> None:
    """Draw a point in 3D space, actually a small line"""
    return _rl.DrawPoint3D(_vec3(position), _color(color))


def draw_circle3d(center: AnyVec3, radius: float, rotation_axis: AnyVec3, rotation_angle: float, color: AnyRGB) -> None:
    """Draw a circle in 3D world space"""
    return _rl.DrawCircle3D(_vec3(center), float(radius), _vec3(rotation_axis), float(rotation_angle), _color(color))


def draw_triangle3d(v1: AnyVec3, v2: AnyVec3, v3: AnyVec3, color: AnyRGB) -> None:
    """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
    return _rl.DrawTriangle3D(_vec3(v1), _vec3(v2), _vec3(v3), _color(color))


def draw_triangle_strip3d(points: Sequence[Vector3], points_count: int, color: AnyRGB) -> None:
    """Draw a triangle strip defined by points"""
    return _rl.DrawTriangleStrip3D(_arr(Vector3, points), int(points_count), _color(color))


def draw_cube(position: AnyVec3, width: float, height: float, length: float, color: AnyRGB) -> None:
    """Draw cube"""
    return _rl.DrawCube(_vec3(position), float(width), float(height), float(length), _color(color))


def draw_cube_v(position: AnyVec3, size: AnyVec3, color: AnyRGB) -> None:
    """Draw cube (Vector version)"""
    return _rl.DrawCubeV(_vec3(position), _vec3(size), _color(color))


def draw_cube_wires(position: AnyVec3, width: float, height: float, length: float, color: AnyRGB) -> None:
    """Draw cube wires"""
    return _rl.DrawCubeWires(_vec3(position), float(width), float(height), float(length), _color(color))


def draw_cube_wires_v(position: AnyVec3, size: AnyVec3, color: AnyRGB) -> None:
    """Draw cube wires (Vector version)"""
    return _rl.DrawCubeWiresV(_vec3(position), _vec3(size), _color(color))


def draw_cube_texture(texture: Texture2D, position: AnyVec3, width: float, height: float, length: float,
                      color: AnyRGB) -> None:
    """Draw cube textured"""
    return _rl.DrawCubeTexture(texture, _vec3(position), float(width), float(height), float(length), _color(color))


def draw_sphere(center_pos: AnyVec3, radius: float, color: AnyRGB) -> None:
    """Draw sphere"""
    return _rl.DrawSphere(_vec3(center_pos), float(radius), _color(color))


def draw_sphere_ex(center_pos: AnyVec3, radius: float, rings: int, slices: int, color: AnyRGB) -> None:
    """Draw sphere with extended parameters"""
    return _rl.DrawSphereEx(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))


def draw_sphere_wires(center_pos: AnyVec3, radius: float, rings: int, slices: int, color: AnyRGB) -> None:
    """Draw sphere wires"""
    return _rl.DrawSphereWires(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))


def draw_cylinder(position: AnyVec3, radius_top: float, radius_bottom: float, height: float, slices: int,
                  color: AnyRGB) -> None:
    """Draw a cylinder/cone"""
    return _rl.DrawCylinder(_vec3(position), float(radius_top), float(radius_bottom), float(height), int(slices),
                            _color(color))


def draw_cylinder_wires(position: AnyVec3, radius_top: float, radius_bottom: float, height: float, slices: int,
                        color: AnyRGB) -> None:
    """Draw a cylinder/cone wires"""
    return _rl.DrawCylinderWires(_vec3(position), float(radius_top), float(radius_bottom), float(height), int(slices),
                                 _color(color))


def draw_plane(center_pos: AnyVec3, size: AnyVec2, color: AnyRGB) -> None:
    """Draw a plane XZ"""
    return _rl.DrawPlane(_vec3(center_pos), _vec2(size), _color(color))


def draw_ray(ray: Ray, color: AnyRGB) -> None:
    """Draw a ray line"""
    return _rl.DrawRay(ray, _color(color))


def draw_grid(slices: int, spacing: float) -> None:
    """Draw a grid (centered at (0, 0, 0))"""
    return _rl.DrawGrid(int(slices), float(spacing))


def load_model(file_name: str) -> Model:
    """Load model from files (meshes and materials)"""
    return _rl.LoadModel(_str_in(file_name))


def load_model_from_mesh(mesh: Mesh) -> Model:
    """Load model from generated mesh (default material)"""
    return _rl.LoadModelFromMesh(mesh)


def unload_model(model: Model) -> None:
    """Unload model (including meshes) from memory (RAM and/or VRAM)"""
    return _rl.UnloadModel(model)


def unload_model_keep_meshes(model: Model) -> None:
    """Unload model (but not meshes) from memory (RAM and/or VRAM)"""
    return _rl.UnloadModelKeepMeshes(model)


def upload_mesh(mesh: Mesh, dynamic: bool) -> None:
    """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
    return _rl.UploadMesh(byref(mesh), bool(dynamic))


def update_mesh_buffer(mesh: Mesh, index: int, data: bytes, data_size: int, offset: int) -> None:
    """Update mesh vertex data in GPU for a specific buffer index"""
    return _rl.UpdateMeshBuffer(mesh, int(index), data, int(data_size), int(offset))


def draw_mesh(mesh: Mesh, material: Material, transform: Matrix) -> None:
    """Draw a 3d mesh with material and transform"""
    return _rl.DrawMesh(mesh, material, transform)


def draw_mesh_instanced(mesh: Mesh, material: Material, transforms: Sequence[Matrix], instances: int) -> None:
    """Draw multiple mesh instances with material and different transforms"""
    return _rl.DrawMeshInstanced(mesh, material, _arr(Matrix, transforms), int(instances))


def unload_mesh(mesh: Mesh) -> None:
    """Unload mesh data from CPU and GPU"""
    return _rl.UnloadMesh(mesh)


def export_mesh(mesh: Mesh, file_name: str) -> bool:
    """Export mesh data to file, returns true on success"""
    return _rl.ExportMesh(mesh, _str_in(file_name))


def load_materials(file_name: str) -> Tuple[MaterialPtr, int]:
    """Load materials from model file"""
    material_count = IntPtr(0)
    material = _rl.LoadMaterials(_str_in(file_name), material_count)
    return material, material_count.contents[0]


def load_material_default() -> Material:
    """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
    return _rl.LoadMaterialDefault()


def unload_material(material: Material) -> None:
    """Unload material from GPU memory (VRAM)"""
    return _rl.UnloadMaterial(material)


def set_material_texture(material: Material, map_type: int, texture: Texture2D) -> None:
    """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
    return _rl.SetMaterialTexture(byref(material), int(map_type), texture)


def set_model_mesh_material(model: Model, mesh_id: int, material_id: int) -> None:
    """Set material for a mesh"""
    return _rl.SetModelMeshMaterial(byref(model), int(mesh_id), int(material_id))


def load_model_animations(file_name: str) -> Tuple[ModelAnimationPtr, int]:
    """Load model animations from file"""
    anims_count = IntPtr(0)
    model_anim = _rl.LoadModelAnimations(_str_in(file_name), anims_count)
    return model_anim, anims_count.contents


def update_model_animation(model: Model, anim: ModelAnimation, frame: int) -> None:
    """Update model animation pose"""
    return _rl.UpdateModelAnimation(model, anim, int(frame))


def unload_model_animation(anim: ModelAnimation) -> None:
    """Unload animation data"""
    return _rl.UnloadModelAnimation(anim)


def unload_model_animations(animations: ModelAnimationPtr, count: int) -> None:
    """Unload animation array data"""
    return _rl.UnloadModelAnimations(animations, int(count))


def is_model_animation_valid(model: Model, anim: ModelAnimation) -> bool:
    """Check model animation skeleton match"""
    return _rl.IsModelAnimationValid(model, anim)


def gen_mesh_poly(sides: int, radius: float) -> Mesh:
    """Generate polygonal mesh"""
    return _rl.GenMeshPoly(int(sides), float(radius))


def gen_mesh_plane(width: float, length: float, res_x: int, res_z: int) -> Mesh:
    """Generate plane mesh (with subdivisions)"""
    return _rl.GenMeshPlane(float(width), float(length), int(res_x), int(res_z))


def gen_mesh_cube(width: float, height: float, length: float) -> Mesh:
    """Generate cuboid mesh"""
    return _rl.GenMeshCube(float(width), float(height), float(length))


def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate sphere mesh (standard sphere)"""
    return _rl.GenMeshSphere(float(radius), int(rings), int(slices))


def gen_mesh_hemisphere(radius: float, rings: int, slices: int) -> Mesh:
    """Generate half-sphere mesh (no bottom cap)"""
    return _rl.GenMeshHemiSphere(float(radius), int(rings), int(slices))


def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh:
    """Generate cylinder mesh"""
    return _rl.GenMeshCylinder(float(radius), float(height), int(slices))


def gen_mesh_torus(radius: float, size: float, rad_seg: int, sides: int) -> Mesh:
    """Generate torus mesh"""
    return _rl.GenMeshTorus(float(radius), float(size), int(rad_seg), int(sides))


def gen_mesh_knot(radius: float, size: float, rad_seg: int, sides: int) -> Mesh:
    """Generate trefoil knot mesh"""
    return _rl.GenMeshKnot(float(radius), float(size), int(rad_seg), int(sides))


def gen_mesh_heightmap(heightmap: Image, size: AnyVec3) -> Mesh:
    """Generate heightmap mesh from image data"""
    return _rl.GenMeshHeightmap(heightmap, _vec3(size))


def gen_mesh_cubicmap(cubicmap: Image, cube_size: AnyVec3) -> Mesh:
    """Generate cubes-based map mesh from image data"""
    return _rl.GenMeshCubicmap(cubicmap, _vec3(cube_size))


def mesh_bounding_box(mesh: Mesh) -> BoundingBox:
    """Compute mesh bounding box limits"""
    return _rl.MeshBoundingBox(mesh)


def mesh_tangents(mesh: Mesh) -> None:
    """Compute mesh tangents"""
    return _rl.MeshTangents(byref(mesh))


def mesh_binormals(mesh: Mesh) -> None:
    """Compute mesh binormals"""
    return _rl.MeshBinormals(byref(mesh))


def draw_model(model: Model, position: AnyVec3, scale: float, tint: AnyRGB) -> None:
    """Draw a model (with texture if set)"""
    return _rl.DrawModel(model, _vec3(position), float(scale), _color(tint))


def draw_model_ex(model: Model, position: AnyVec3, rotation_axis: AnyVec3, rotation_angle: float, scale: AnyVec3,
                  tint: AnyRGB) -> None:
    """Draw a model with extended parameters"""
    return _rl.DrawModelEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale),
                           _color(tint))


def draw_model_wires(model: Model, position: AnyVec3, scale: float, tint: AnyRGB) -> None:
    """Draw a model wires (with texture if set)"""
    return _rl.DrawModelWires(model, _vec3(position), float(scale), _color(tint))


def draw_model_wires_ex(model: Model, position: AnyVec3, rotation_axis: AnyVec3, rotation_angle: float, scale: AnyVec3,
                        tint: AnyRGB) -> None:
    """Draw a model wires (with texture if set) with extended parameters"""
    return _rl.DrawModelWiresEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale),
                                _color(tint))


def draw_bounding_box(box: BoundingBox, color: AnyRGB) -> None:
    """Draw bounding box (wires)"""
    return _rl.DrawBoundingBox(box, _color(color))


def draw_billboard(camera: Camera, texture: Texture2D, center: AnyVec3, size: float, tint: AnyRGB) -> None:
    """Draw a billboard texture"""
    return _rl.DrawBillboard(camera, texture, _vec3(center), float(size), _color(tint))


def draw_billboard_rec(camera: Camera, texture: Texture2D, source: AnyRect, center: AnyVec3, size: float,
                       tint: AnyRGB) -> None:
    """Draw a billboard texture defined by source"""
    return _rl.DrawBillboardRec(camera, texture, _rect(source), _vec3(center), float(size), _color(tint))


def check_collision_spheres(center1: AnyVec3, radius1: float, center2: AnyVec3, radius2: float) -> bool:
    """Detect collision between two spheres"""
    return _rl.CheckCollisionSpheres(_vec3(center1), float(radius1), _vec3(center2), float(radius2))


def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool:
    """Detect collision between two bounding boxes"""
    return _rl.CheckCollisionBoxes(box1, box2)


def check_collision_box_sphere(box: BoundingBox, center: AnyVec3, radius: float) -> bool:
    """Detect collision between box and sphere"""
    return _rl.CheckCollisionBoxSphere(box, _vec3(center), float(radius))


def check_collision_ray_sphere(ray: Ray, center: AnyVec3, radius: float) -> bool:
    """Detect collision between ray and sphere"""
    return _rl.CheckCollisionRaySphere(ray, _vec3(center), float(radius))


def check_collision_ray_sphere_ex(ray: Ray, center: AnyVec3, radius: float, collision_point: Sequence[Vector3]) -> bool:
    """Detect collision between ray and sphere, returns collision point"""
    return _rl.CheckCollisionRaySphereEx(ray, _vec3(center), float(radius), _arr(Vector3, collision_point))


def check_collision_ray_box(ray: Ray, box: BoundingBox) -> bool:
    """Detect collision between ray and box"""
    return _rl.CheckCollisionRayBox(ray, box)


def get_collision_ray_mesh(ray: Ray, mesh: Mesh, transform: Matrix) -> RayHitInfo:
    """Get collision info between ray and mesh"""
    return _rl.GetCollisionRayMesh(ray, mesh, transform)


def get_collision_ray_model(ray: Ray, model: Model) -> RayHitInfo:
    """Get collision info between ray and model"""
    return _rl.GetCollisionRayModel(ray, model)


def get_collision_ray_triangle(ray: Ray, p1: AnyVec3, p2: AnyVec3, p3: AnyVec3) -> RayHitInfo:
    """Get collision info between ray and triangle"""
    return _rl.GetCollisionRayTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))


def get_collision_ray_ground(ray: Ray, ground_height: float) -> RayHitInfo:
    """Get collision info between ray and ground plane (Y-normal plane)"""
    return _rl.GetCollisionRayGround(ray, float(ground_height))


def init_audio_device() -> None:
    """Initialize audio device and context"""
    return _rl.InitAudioDevice()


def close_audio_device() -> None:
    """Close the audio device and context"""
    return _rl.CloseAudioDevice()


def is_audio_device_ready() -> bool:
    """Check if audio device has been initialized successfully"""
    return _rl.IsAudioDeviceReady()


def set_master_volume(volume: float) -> None:
    """Set master volume (listener)"""
    return _rl.SetMasterVolume(float(volume))


def load_wave(file_name: str) -> Wave:
    """Load wave data from file"""
    return _rl.LoadWave(_str_in(file_name))


def load_wave_from_memory(file_type: str, file_data: bytes, data_size: int) -> Wave:
    """Load wave from memory buffer, fileType refers to extension: i.e. ".wav"."""
    return _rl.LoadWaveFromMemory(_str_in(file_type), file_data, int(data_size))


def load_sound(file_name: str) -> Sound:
    """Load sound from file"""
    return _rl.LoadSound(_str_in(file_name))


def load_sound_from_wave(wave: Wave) -> Sound:
    """Load sound from wave data"""
    return _rl.LoadSoundFromWave(wave)


def update_sound(sound: Sound, data: bytes, samples_count: int) -> None:
    """Update sound buffer with new data"""
    return _rl.UpdateSound(sound, data, int(samples_count))


def unload_wave(wave: Wave) -> None:
    """Unload wave data"""
    return _rl.UnloadWave(wave)


def unload_sound(sound: Sound) -> None:
    """Unload sound"""
    return _rl.UnloadSound(sound)


def export_wave(wave: Wave, file_name: str) -> bool:
    """Export wave data to file, returns true on success"""
    return _rl.ExportWave(wave, _str_in(file_name))


def export_wave_as_code(wave: Wave, file_name: str) -> bool:
    """Export wave sample data to code (.h), returns true on success"""
    return _rl.ExportWaveAsCode(wave, _str_in(file_name))


def play_sound(sound: Sound) -> None:
    """Play a sound"""
    return _rl.PlaySound(sound)


def stop_sound(sound: Sound) -> None:
    """Stop playing a sound"""
    return _rl.StopSound(sound)


def pause_sound(sound: Sound) -> None:
    """Pause a sound"""
    return _rl.PauseSound(sound)


def resume_sound(sound: Sound) -> None:
    """Resume a paused sound"""
    return _rl.ResumeSound(sound)


def play_sound_multi(sound: Sound) -> None:
    """Play a sound (using multichannel buffer pool)"""
    return _rl.PlaySoundMulti(sound)


def stop_sound_multi() -> None:
    """Stop any sound playing (using multichannel buffer pool)"""
    return _rl.StopSoundMulti()


def get_sounds_playing() -> int:
    """Get number of sounds playing in the multichannel"""
    return _rl.GetSoundsPlaying()


def is_sound_playing(sound: Sound) -> bool:
    """Check if a sound is currently playing"""
    return _rl.IsSoundPlaying(sound)


def set_sound_volume(sound: Sound, volume: float) -> None:
    """Set volume for a sound (1.0 is max level)"""
    return _rl.SetSoundVolume(sound, float(volume))


def set_sound_pitch(sound: Sound, pitch: float) -> None:
    """Set pitch for a sound (1.0 is base level)"""
    return _rl.SetSoundPitch(sound, float(pitch))


def wave_format(wave: Wave, sample_rate: int, sample_size: int, channels: int) -> None:
    """Convert wave data to desired format"""
    return _rl.WaveFormat(wave, int(sample_rate), int(sample_size), int(channels))


def wave_copy(wave: Wave) -> Wave:
    """Copy a wave to a new wave"""
    return _rl.WaveCopy(wave)


def wave_crop(wave: Wave, init_sample: int, final_sample: int) -> None:
    """Crop a wave to defined samples range"""
    return _rl.WaveCrop(wave, int(init_sample), int(final_sample))


def load_wave_samples(wave: Wave) -> Sequence[float]:
    """Load samples data from wave as a floats array"""
    return _rl.LoadWaveSamples(wave)


def unload_wave_samples(samples: Sequence[float]) -> None:
    """Unload samples data loaded with LoadWaveSamples()"""
    return _rl.UnloadWaveSamples(_arr(Float, samples))


def load_music_stream(file_name: str) -> Music:
    """Load music stream from file"""
    return _rl.LoadMusicStream(_str_in(file_name))


def load_music_stream_from_memory(file_type: str, data: bytes, data_size: int) -> Music:
    """Load music stream from data"""
    return _rl.LoadMusicStreamFromMemory(_str_in(file_type), data, int(data_size))


def unload_music_stream(music: Music) -> None:
    """Unload music stream"""
    return _rl.UnloadMusicStream(music)


def play_music_stream(music: Music) -> None:
    """Start music playing"""
    return _rl.PlayMusicStream(music)


def is_music_playing(music: Music) -> bool:
    """Check if music is playing"""
    return _rl.IsMusicPlaying(music)


def update_music_stream(music: Music) -> None:
    """Updates buffers for music streaming"""
    return _rl.UpdateMusicStream(music)


def stop_music_stream(music: Music) -> None:
    """Stop music playing"""
    return _rl.StopMusicStream(music)


def pause_music_stream(music: Music) -> None:
    """Pause music playing"""
    return _rl.PauseMusicStream(music)


def resume_music_stream(music: Music) -> None:
    """Resume playing paused music"""
    return _rl.ResumeMusicStream(music)


def set_music_volume(music: Music, volume: float) -> None:
    """Set volume for music (1.0 is max level)"""
    return _rl.SetMusicVolume(music, float(volume))


def set_music_pitch(music: Music, pitch: float) -> None:
    """Set pitch for a music (1.0 is base level)"""
    return _rl.SetMusicPitch(music, float(pitch))


def get_music_time_length(music: Music) -> float:
    """Get music time length (in seconds)"""
    return _rl.GetMusicTimeLength(music)


def get_music_time_played(music: Music) -> float:
    """Get current music time played (in seconds)"""
    return _rl.GetMusicTimePlayed(music)


def init_audio_stream(sample_rate: int, sample_size: int, channels: int) -> AudioStream:
    """Init audio stream (to stream raw audio pcm data)"""
    return _rl.InitAudioStream(int(sample_rate), int(sample_size), int(channels))


def update_audio_stream(stream: AudioStream, data: bytes, samples_count: int) -> None:
    """Update audio stream buffers with data"""
    return _rl.UpdateAudioStream(stream, data, int(samples_count))


def close_audio_stream(stream: AudioStream) -> None:
    """Close audio stream and free memory"""
    return _rl.CloseAudioStream(stream)


def is_audio_stream_processed(stream: AudioStream) -> bool:
    """Check if any audio stream buffers requires refill"""
    return _rl.IsAudioStreamProcessed(stream)


def play_audio_stream(stream: AudioStream) -> None:
    """Play audio stream"""
    return _rl.PlayAudioStream(stream)


def pause_audio_stream(stream: AudioStream) -> None:
    """Pause audio stream"""
    return _rl.PauseAudioStream(stream)


def resume_audio_stream(stream: AudioStream) -> None:
    """Resume audio stream"""
    return _rl.ResumeAudioStream(stream)


def is_audio_stream_playing(stream: AudioStream) -> bool:
    """Check if audio stream is playing"""
    return _rl.IsAudioStreamPlaying(stream)


def stop_audio_stream(stream: AudioStream) -> None:
    """Stop audio stream"""
    return _rl.StopAudioStream(stream)


def set_audio_stream_volume(stream: AudioStream, volume: float) -> None:
    """Set volume for audio stream (1.0 is max level)"""
    return _rl.SetAudioStreamVolume(stream, float(volume))


def set_audio_stream_pitch(stream: AudioStream, pitch: float) -> None:
    """Set pitch for audio stream (1.0 is base level)"""
    return _rl.SetAudioStreamPitch(stream, float(pitch))


def set_audio_stream_buffer_size_default(size: int) -> None:
    """Default size for new audio streams"""
    return _rl.SetAudioStreamBufferSizeDefault(int(size))
