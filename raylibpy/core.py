from structures import *
from ctypes import byref
from typing import Tuple
from library import rl as _rl

__all__ = [
    # window
    'init_window',
    'close_window',
    'is_window_ready',
    'window_should_close',
    'is_window_minimized',
    'toggle_fullscreen',
    'set_window_icon',
    'set_window_title',
    'set_window_position',
    'set_window_monitor',
    'set_window_min_size',
    'set_window_size',
    'get_screen_width',
    'get_screen_height',
    'show_cursor',
    'hide_cursor',
    'is_cursor_hidden',
    'enable_cursor',
    'disable_cursor',
    'clear_background',
    'begin_drawing',
    'end_drawing',
    'begin_mode2d',
    'end_mode2d',
    'begin_mode3d',
    'end_mode3d',
    'begin_texture_mode',
    'end_texture_mode',
    'get_mouse_ray',
    'get_world_to_screen',
    'get_camera_matrix',
    'set_target_fps',
    'get_fps',
    'get_frame_time',
    'get_time',
    'color_to_int',
    'color_normalize',
    'color_to_hsv',
    'get_color',
    'fade',
    'show_logo',
    'set_config_flags',
    'set_trace_log',
    'trace_log',
    'take_screenshot',
    'get_random_value',
    'is_file_extension',
    'get_extension',
    'get_file_name',
    'get_directory_path',
    'get_working_directory',
    'change_directory',
    'is_file_dropped',
    'get_dropped_files',
    'clear_dropped_files',
    'storage_save_value',
    'storage_load_value',
    # input
    'is_key_pressed',
    'is_key_down',
    'is_key_released',
    'is_key_up',
    'get_key_pressed',
    'set_exit_key',
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
    'is_mouse_button_pressed',
    'is_mouse_button_down',
    'is_mouse_button_released',
    'is_mouse_button_up',
    'get_mouse_x',
    'get_mouse_y',
    'get_mouse_position',
    'set_mouse_position',
    'set_mouse_scale',
    'get_mouse_wheel_move',
    'get_touch_x',
    'get_touch_y',
    'get_touch_position',

    'byref',
]


_NOARGS = []


# -----------------------------------------------------------------------------------
# Window and Graphics Device Functions (Module: core)
# ----------------------------------------------------------------------------------

# Window-related functions
_rl.InitWindow.argtypes = [Int, Int, CharPtr]
_rl.InitWindow.restype = None
def init_window(width: int, height: int, title: bytes) -> None:
    """Initialize window and OpenGL context"""
    return _rl.InitWindow(width, height, title)


_rl.CloseWindow.argtypes = _NOARGS
_rl.CloseWindow.restype = None
def close_window() -> None:
    """Close window and unload OpenGL context"""
    return _rl.CloseWindow()


_rl.IsWindowReady.argtypes = _NOARGS
_rl.IsWindowReady.restype = Bool
def is_window_ready() -> None:
    """Check if window has been initialized successfully"""
    return _rl.IsWindowReady()


_rl.WindowShouldClose.argtypes = _NOARGS
_rl.WindowShouldClose.restype = Bool
def window_should_close() -> bool:
    """Check if KEY_ESCAPE pressed or Close icon pressed"""
    return _rl.WindowShouldClose()


_rl.IsWindowMinimized.argtypes = _NOARGS
_rl.IsWindowMinimized.restype = Bool
def is_window_minimized() -> bool:
    """Check if window has been minimized (or lost focus)"""
    return _rl.IsWindowMinimized()


_rl.ToggleFullscreen.argtypes = []
_rl.ToggleFullscreen.restype = None
def toggle_fullscreen() -> None:
    """Toggle fullscreen mode (only PLATFORM_DESKTOP)"""
    return _rl.ToggleFullscreen()


_rl.SetWindowIcon.argtypes = [Image]
_rl.SetWindowIcon.restype = None
def set_window_icon(image: Image) -> None:
    """Set icon for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowIcon(image)


_rl.SetWindowTitle.argtypes = [CharPtr]
_rl.SetWindowTitle.restype = None
def set_window_title(title: bytes) -> None:
    """Set title for window (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowTitle(title)


_rl.SetWindowPosition.argtypes = [Int, Int]
_rl.SetWindowPosition.restype = None
def set_window_position(x: int, y: int) -> None:
    """Set window position on screen (only PLATFORM_DESKTOP)"""
    return _rl.SetWindowPosition(x, y)


_rl.SetWindowMonitor.argtypes = [Int]
_rl.SetWindowMonitor.restype = None
def set_window_monitor(monitor: int) -> None:
    """Set monitor for the current window (fullscreen mode)"""
    return _rl.SetWindowMonitor(monitor)


_rl.SetWindowMinSize.argtypes = [Int, Int]
_rl.SetWindowMinSize.restype = None
def set_window_min_size(width: int, height: int) -> None:
    """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
    return _rl.SetWindowMinSize(width, height)


_rl.SetWindowSize.argtypes = [Int, Int]
_rl.SetWindowSize.restype = None
def set_window_size(width: int, height: int):
    """Set window dimensions"""
    return _rl.SetWindowSize(width, height)


_rl.GetScreenWidth.argtypes = _NOARGS
_rl.GetScreenWidth.restype = Int
def get_screen_width() -> int:
    """Get current screen width"""
    return _rl.GetScreenWidth()


_rl.GetScreenHeight.argtypes = _NOARGS
_rl.GetScreenHeight.restype = Int
def get_screen_height() -> int:
    """Get current screen height"""
    return _rl.GetScreenHeight()


# Cursor-related functions
_rl.ShowCursor.argtypes = _NOARGS
_rl.ShowCursor.restype = None
def show_cursor() -> None:
    """Shows cursor"""
    return _rl.ShowCursor()


_rl.HideCursor.argtypes = _NOARGS
_rl.HideCursor.restype = None
def hide_cursor() -> None:
    """Hides cursor"""
    return _rl.HideCursor()


_rl.IsCursorHidden.argtypes = _NOARGS
_rl.IsCursorHidden.restype = Bool
def is_cursor_hidden() -> bool:
    """Check if cursor is not visible"""
    return _rl.IsCursorHidden()


_rl.EnableCursor.argtypes = _NOARGS
_rl.EnableCursor.restype = None
def enable_cursor() -> None:
    """Enables cursor (unlock cursor)"""
    return _rl.EnableCursor()


_rl.DisableCursor.argtypes = _NOARGS
_rl.DisableCursor.restype = None
def disable_cursor() -> None:
    """Disables cursor (lock cursor)"""
    return _rl.DisableCursor()


# Drawing-related functions
_rl.ClearBackground.argtypes = [Color]
_rl.ClearBackground.restype = None
def clear_background(color: Color) -> None:
    """Set background color (framebuffer clear color)"""
    return _rl.ClearBackground(color)


_rl.BeginDrawing.argtypes = _NOARGS
_rl.BeginDrawing.restype = None
def begin_drawing() -> None:
    """Setup canvas (framebuffer) to start drawing"""
    return _rl.BeginDrawing()


_rl.EndDrawing.argtypes = _NOARGS
_rl.EndDrawing.restype = None
def end_drawing() -> None:
    """End canvas drawing and swap buffers (double buffering)"""
    return _rl.EndDrawing()


_rl.BeginMode2D.argtypes = [Camera2D]
_rl.BeginMode2D.restype = None
def begin_mode2d(camera: Camera2D) -> None:
    """Initialize 2D mode with custom camera (2D)"""
    return _rl.BeginMode2D(camera)


_rl.EndMode2D.argtypes = _NOARGS
_rl.EndMode2D.restype = None
def end_mode2d() -> None:
    """Ends 2D mode with custom camera"""
    return _rl.EndMode2D()


_rl.BeginMode3D.argtypes = [Camera3D]
_rl.BeginMode3D.restype = None
def begin_mode3d(camera: Camera3D) -> None:
    """Initializes 3D mode with custom camera (3D)"""
    return _rl.BeginMode3D(camera)


_rl.EndMode3D.argtypes = _NOARGS
_rl.EndMode3D.restype = None
def end_mode3d() -> None:
    """Ends 3D mode and returns to default 2D orthographic mode"""
    return _rl.EndMode3D()


_rl.BeginTextureMode.argtypes = [RenderTexture2D]
_rl.BeginTextureMode.restype = None
def begin_texture_mode(target: RenderTexture2D) -> None:
    """Initializes render texture for drawing"""
    return _rl.BeginTextureMode(target)


_rl.EndTextureMode.argtypes = _NOARGS
_rl.EndTextureMode.restype = None
def end_texture_mode() -> None:
    """Ends drawing to render texture"""
    return _rl.EndTextureMode()


# Screen-space-related functions
_rl.GetMouseRay.argtypes = [Vector2, Camera]
_rl.GetMouseRay.restype = Ray
def get_mouse_ray(mouse_position: Vector2, camera: Camera) -> Ray:
    """Returns a ray trace from mouse position"""
    return _rl.GetMouseRay(mouse_position, camera)


_rl.GetWorldToScreen.argtypes = [Vector3, Camera]
_rl.GetWorldToScreen.restype = Vector2
def get_world_to_screen(position: Vector3, camera: Camera) -> Vector2:
    """Returns the screen space position for a 3d world space position"""
    return _rl.GetWorldToScreen(position, camera)


_rl.GetCameraMatrix.argtypes = [Camera]
_rl.GetCameraMatrix.restype = Matrix
def get_camera_matrix(camera: Camera) -> Matrix:
    """Returns camera transform matrix (view matrix)"""
    return _rl.GetCameraMatrix(camera)


# Timming-related functions
_rl.SetTargetFPS.argtypes = [Int]
_rl.SetTargetFPS.restype = None
def set_target_fps(fps: int) -> None:
    """Set target FPS (maximum)"""
    return _rl.SetTargetFPS(fps)


_rl.GetFPS.argtypes = _NOARGS
_rl.GetFPS.restype = Int
def get_fps() -> int:
    """Returns current FPS"""
    return _rl.GetFPS()


_rl.GetFrameTime.argtypes = _NOARGS
_rl.GetFrameTime.restype = Float
def get_frame_time() -> float:
    """Returns time in seconds for last frame drawn"""
    return _rl.GetFrameTime()


_rl.GetTime.argtypes = _NOARGS
_rl.GetTime.restype = Double
def get_time() -> float:
    """Returns elapsed time in seconds since InitWindow()"""
    return _rl.GetTime()


# Color-related functions
_rl.ColorToInt.argtypes = [Color]
_rl.ColorToInt.restype = Int
def color_to_int(color: Color) -> int:
    """Returns hexadecimal value for a Color"""
    return _rl.ColorToInt(color)


_rl.ColorNormalize.argtypes = [Color]
_rl.ColorNormalize.restype = Vector4
def color_normalize(color: Color) -> Vector4:
    """Returns color normalized as float [0..1]"""
    return _rl.ColorNormalize(color)


_rl.ColorToHSV.argtypes = [Color]
_rl.ColorToHSV.restype = Vector3
def color_to_hsv(color: Color) -> Vector3:
    """Returns HSV values for a Color"""
    return _rl.ColorToHSV(color)


_rl.GetColor.argtypes = [Int]
_rl.GetColor.restype = Color
def get_color(hex_value: int) -> Color:
    """Returns a Color struct from hexadecimal value"""
    return _rl.GetColor(hex_value)


_rl.Fade.argtypes = [Color, Float]
_rl.Fade.restype = Color
def fade(color: Color, alpha: float) -> Color:
    """Color fade-in or fade-out, alpha goes from 0.0f to 1.0f"""
    return _rl.Fade(color, alpha)


# Misc. functions
_rl.ShowLogo.argtypes = _NOARGS
_rl.ShowLogo.restype = None
def show_logo() -> None:
    """Activate raylib logo at startup (can be done with flags)"""
    return _rl.ShowLogo()


_rl.SetConfigFlags.argtypes = [UChar]
_rl.SetConfigFlags.restype = None
def set_config_flags(flags: int) -> None:
    """Setup window configuration flags (view FLAGS)"""
    return _rl.SetConfigFlags(flags)


_rl.SetTraceLog.argtypes = [UChar]
_rl.SetTraceLog.restype = None
def set_trace_log(types: int) -> None:
    """Enable trace log message types (bit flags based)"""
    return _rl.SetTraceLog(types)


_rl.TraceLog.argtypes = [Int, CharPtr]
_rl.TraceLog.restype = None
def trace_log(log_type: int, text: bytes, *args) -> None:
    """Show trace log messages (LOG_INFO, LOG_WARNING, LOG_ERROR, LOG_DEBUG)"""
    return _rl.TraceLog(log_type, text, *args)


_rl.TakeScreenshot.argtypes = [CharPtr]
_rl.TakeScreenshot.restype = None
def take_screenshot(file_name: bytes):
    """Takes a screenshot of current screen (saved a .png)"""
    return _rl.TakeScreenshot(file_name)


_rl.GetRandomValue.argtypes = [Int, Int]
_rl.GetRandomValue.restype = Int
def get_random_value(min_val: int, max_val: int) -> int:
    """Returns a random value between min and max (both included)"""
    return _rl.GetRandomValue(min_val, max_val)

# Files management functions
_rl.IsFileExtension.argtypes = [CharPtr, CharPtr]
_rl.IsFileExtension.restype = Bool
def is_file_extension(file_name: bytes, ext: bytes) -> bool:
    """Check file extension"""
    return _rl.IsFileExtension(file_name, ext)


_rl.GetExtension.argtypes = [CharPtr]
_rl.GetExtension.restype = CharPtr
def get_extension(file_name: bytes) -> bytes:
    """Get pointer to extension for a filename string"""
    return _rl.GetExtension(file_name)


_rl.GetFileName.argtypes = [CharPtr]
_rl.GetFileName.restype = CharPtr
def get_file_name(file_path: bytes) -> bytes:
    """Get pointer to filename for a path string"""
    return _rl.GetFileName(file_path)


_rl.GetDirectoryPath.argtypes = [CharPtr]
_rl.GetDirectoryPath.restype = CharPtr
def get_directory_path(file_name: bytes) -> bytes:
    """Get full path for a given fileName (uses static string)"""
    return _rl.GetDirectoryPath(file_name)


_rl.GetWorkingDirectory.argtypes = _NOARGS
_rl.GetWorkingDirectory.restype = CharPtr
def get_working_directory() -> bytes:
    """Get current working directory (uses static string)"""
    return _rl.GetWorkingDirectory()


_rl.ChangeDirectory.argtypes = [CharPtr]
_rl.ChangeDirectory.restype = Bool
def change_directory(directory: bytes) -> bool:
    """Change working directory, returns true if success"""
    return _rl.ChangeDirectory(directory)


_rl.IsFileDropped.argtypes = _NOARGS
_rl.IsFileDropped.restype = Bool
def is_file_dropped() -> bool:
    """Check if a file has been dropped into window"""
    return _rl.IsFileDropped()


_rl.GetDroppedFiles.argtypes = [IntPtr]
_rl.GetDroppedFiles.restype = CharPtrPrt
def get_dropped_files() -> Tuple[int, bytes]:
    """Get dropped files names"""
    count = Int(0)
    files: bytes = _rl.GetDroppedFiles(byref(count))
    return count.value, files


_rl.ClearDroppedFiles.argtypes = _NOARGS
_rl.ClearDroppedFiles.restype = None
def clear_dropped_files() -> None:
    """Clear dropped files paths buffer"""
    return _rl.ClearDroppedFiles()


# Persistent storage management
_rl.StorageSaveValue.argtypes = [Int, Int]
_rl.StorageSaveValue.restype = None
def storage_save_value(position: int, value: int) -> None:
    """Save integer value to storage file (to defined position)"""
    return _rl.StorageSaveValue(position, value)


_rl.StorageLoadValue.argtypes = [Int]
_rl.StorageLoadValue.restype = Int
def storage_load_value(position: int) -> int:
    """Load integer value from storage file (from defined position)"""
    return _rl.StorageLoadValue(position)


#------------------------------------------------------------------------------------
# Input Handling Functions (Module: core)
# -----------------------------------------------------------------------------------

# Input-related functions: keyboard
_rl.IsKeyPressed.argtypes = [Int]
_rl.IsKeyPressed.restype = Bool
def is_key_pressed(key: int) -> bool:
    """Detect if a key has been pressed once"""
    return _rl.IsKeyPressed(key)


_rl.IsKeyDown.argtypes = [Int]
_rl.IsKeyDown.restype = Bool
def is_key_down(key: int) -> bool:
    """Detect if a key is being pressed"""
    return _rl.IsKeyDown(key)


_rl.IsKeyReleased.argtypes = [Int]
_rl.IsKeyReleased.restype = Bool
def is_key_released(key: int) -> bool:
    """Detect if a key has been released once"""
    return _rl.IsKeyReleased(key)


_rl.IsKeyUp.argtypes = [Int]
_rl.IsKeyUp.restype = Bool
def is_key_up(key: int) -> bool:
    """Detect if a key is NOT being pressed"""
    return _rl.IsKeyUp(key)


_rl.GetKeyPressed.argtypes = _NOARGS
_rl.GetKeyPressed.restype = Int
def get_key_pressed() -> int:
    """Get latest key pressed"""
    return _rl.GetKeyPressed()


_rl.SetExitKey.argtypes = [Int]
_rl.SetExitKey.restype = None
def set_exit_key(key: int) -> None:
    """Set a custom key to exit program (default is ESC)"""
    return _rl.SetExitKey(key)


_rl.IsGamepadAvailable.argtypes = [Int]
_rl.IsGamepadAvailable.restype = Bool
def is_gamepad_available(gamepad: int) -> bool:
    """Detect if a gamepad is available"""
    return _rl.IsGamepadAvailable(gamepad)


_rl.IsGamepadName.argtypes = [Int, CharPtr]
_rl.IsGamepadName.restype = Bool
def is_gamepad_name(gamepad: int, name: bytes) -> bool:
    """Check gamepad name (if available)"""
    return _rl.IsGamepadName(gamepad, name)


_rl.GetGamepadName.argtypes = [Int]
_rl.GetGamepadName.restype = CharPtr
def get_gamepad_name(gamepad: int) -> bytes:
    """Return gamepad internal name id"""
    return _rl.GetGamepadName(gamepad)


_rl.IsGamepadButtonPressed.argtypes = [Int, Int]
_rl.IsGamepadButtonPressed.restype = Bool
def is_gamepad_button_pressed(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been pressed once"""
    return _rl.IsGamepadButtonPressed(gamepad, button)


_rl.IsGamepadButtonDown.argtypes = [Int, Int]
_rl.IsGamepadButtonDown.restype = Bool
def is_gamepad_button_down(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is being pressed"""
    return _rl.IsGamepadButtonDown(gamepad, button)


_rl.IsGamepadButtonReleased.argtypes = [Int, Int]
_rl.IsGamepadButtonReleased.restype = Bool
def is_gamepad_button_released(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button has been released once"""
    return _rl.IsGamepadButtonReleased(gamepad, button)


_rl.IsGamepadButtonUp.argtypes = [Int, Int]
_rl.IsGamepadButtonUp.restype = Bool
def is_gamepad_button_up(gamepad: int, button: int) -> bool:
    """Detect if a gamepad button is NOT being pressed"""
    return _rl.IsGamepadButtonUp(gamepad, button)


_rl.GetGamepadButtonPressed.argtypes = _NOARGS
_rl.GetGamepadButtonPressed.restype = Int
def get_gamepad_button_pressed():
    """Get the last gamepad button pressed"""
    return _rl.GetGamepadButtonPressed()


_rl.GetGamepadAxisCount.argtypes = [Int]
_rl.GetGamepadAxisCount.restype = Int
def get_gamepad_axis_count(gamepad: int) -> int:
    """Return gamepad axis count for a gamepad"""
    return _rl.GetGamepadAxisCount(gamepad)


_rl.GetGamepadAxisMovement.argtypes = [Int, Int]
_rl.GetGamepadAxisMovement.restype = Float
def get_gamepad_axis_movement(gamepad: int, axis: int) -> float:
    """Return axis movement value for a gamepad axis"""
    return _rl.GetGamepadAxisMovement(gamepad, axis)


_rl.IsMouseButtonPressed.argtypes = [Int]
_rl.IsMouseButtonPressed.restype = Bool
def is_mouse_button_pressed(button: int) -> bool:
    """Detect if a mouse button has been pressed once"""
    return _rl.IsMouseButtonPressed(button)


_rl.IsMouseButtonDown.argtypes = [Int]
_rl.IsMouseButtonDown.restype = Bool
def is_mouse_button_down(button: int) -> bool:
    """Detect if a mouse button is being pressed"""
    return _rl.IsMouseButtonDown(button)


_rl.IsMouseButtonReleased.argtypes = [Int]
_rl.IsMouseButtonReleased.restype = Bool
def is_mouse_button_released(button: int) -> bool:
    """Detect if a mouse button has been released once"""
    return _rl.IsMouseButtonReleased(button)


_rl.IsMouseButtonUp.argtypes = [Int]
_rl.IsMouseButtonUp.restype = Bool
def is_mouse_button_up(button: int) -> bool:
    """Detect if a mouse button is NOT being pressed"""
    return _rl.IsMouseButtonUp(button)


_rl.GetMouseX.argtypes = _NOARGS
_rl.GetMouseX.restype = Int
def get_mouse_x() -> int:
    """Returns mouse position X"""
    return _rl.GetMouseX()


_rl.GetMouseY.argtypes = _NOARGS
_rl.GetMouseY.restype = Int
def get_mouse_y() -> int:
    """Returns mouse position Y"""
    return _rl.GetMouseY()


_rl.GetMousePosition.argtypes = _NOARGS
_rl.GetMousePosition.restype = Vector2
def get_mouse_position() -> Vector2:
    """Returns mouse position XY"""
    return _rl.GetMousePosition()


_rl.SetMousePosition.argtypes = [Vector2]
_rl.SetMousePosition.restype = None
def set_mouse_position(position: Vector2) -> None:
    """Set mouse position XY"""
    return _rl.SetMousePosition(position)


_rl.SetMouseScale.argtypes = [Float]
_rl.SetMouseScale.restype = None
def set_mouse_scale(scale: float) -> None:
    """Set mouse scaling"""
    return _rl.SetMouseScale(scale)


_rl.GetMouseWheelMove.argtypes = _NOARGS
_rl.GetMouseWheelMove.restype = Int
def get_mouse_wheel_move() -> int:
    """Returns mouse wheel movement Y"""
    return _rl.GetMouseWheelMove()


_rl.GetTouchX.argtypes = _NOARGS
_rl.GetTouchX.restype = Int
def get_touch_x() -> int:
    """Returns touch position X for touch point 0 (relative to screen size)"""
    return _rl.GetTouchX()


_rl.GetTouchY.argtypes = _NOARGS
_rl.GetTouchY.restype = Int
def get_touch_y() -> int:
    """Returns touch position Y for touch point 0 (relative to screen size)"""
    return _rl.GetTouchY()


_rl.GetTouchPosition.argtypes = [Int]
_rl.GetTouchPosition.restype = Vector2
def get_touch_position(index: int) -> Vector2:
    """Returns touch position XY for a touch point index (relative to screen size)"""
    return _rl.GetTouchPosition(index)
