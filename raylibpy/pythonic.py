import re
import contextlib
from ctypes import byref
from raylibpy import _rl
from typing import Any, Dict, Union, Tuple, List, Sequence, TypeVar, Optional, NamedTuple, MutableSequence
from ctypes import (
    Structure,
    c_bool,
    c_ubyte,
    c_int,
    c_uint,
    c_ushort,
    c_void_p,
    c_float,
    c_char,
    POINTER,
    Array,
)
from raylibpy._types import *

__all__ = [
    'Singleton',
    'Window',
    'Clipboard',
    'Mouse',
    'Gesture',
    'Monitor',
    'Gamepad',
    'AudioDevice',
    'Collision3D',
    'Collision',
    'Key',
    'Draw',
    'PixelData',
    'Text',
    'Cursor',
    'Mem',
    'TraceLog',
    'System',

    'TraceLogCallback',
    'LoadFileDataCallback',
    'SaveFileDataCallback',
    'LoadFileTextCallback',
    'SaveFileTextCallback',

    'Vector2',
    'Vector2Ptr',
    'Vector3',
    'Vector3Ptr',
    'Vector4',
    'Vector4Ptr',
    'Quaternion',
    'Matrix',
    'Color',
    'Rectangle',
    'Image',
    'Texture',
    'TextureCubemap',
    'Texture2D',
    'RenderTexture',
    'RenderTexture2D',
    'NPatchInfo',
    'CharInfo',
    'Font',
    'SpriteFont',
    'Camera3D',
    'Camera',
    'Camera2D',
    'Mesh',
    'Shader',
    'MaterialMap',
    'Material',
    'Transform',
    'BoneInfo',
    'Model',
    'ModelAnimation',
    'ModelAnimationPtr',
    'Ray',
    'RayHitInfo',
    'BoundingBox',
    'Wave',
    'rAudioBuffer',
    'AudioStream',
    'Sound',
    'Music',
    'VrDeviceInfo',
    'VrStereoConfig',

    # Pointer Types
    'CharInfoPtr',
    'CameraPtr',
    'Camera3DPtr',
    'ModelPtr',
    'MeshPtr',
    'RayHitInfoPtr',
    'WavePtr',
    'Vector2Ptr',
    # 'Vector3Ptr',
    # 'Vector4Ptr',
    # 'QuaternionPtr',
    'MatrixPtr',
    'ColorPtr',
    'RectanglePtr',
    'RectanglePtrPtr',
    'ImagePtr',
    # 'TexturePtr',
    # 'TextureCubemapPtr',
    'Texture2DPtr',
    # 'RenderTexturePtr',
    # 'RenderTexture2DPtr',
    # 'NPatchInfoPtr',
    'CharInfoPtr',
    # 'FontPtr',
    # 'SpriteFontPtr',
    'Camera3DPtr',
    'CameraPtr',
    # 'Camera2DPtr',
    'MeshPtr',
    # 'ShaderPtr',
    # 'MaterialMapPtr',
    'MaterialPtr',
    # 'TransformPtr',
    # 'BoneInfoPtr',
    'ModelPtr',
    # 'ModelAnimationPtr',
    # 'RayPtr',
    # 'BoundingBoxPtr',
    'WavePtr',
    'rAudioBufferPtr',
    # 'AudioStreamPtr',
    # 'SoundPtr',

    # TYPE CASTS
    '_vec2',
    '_vec3',
    '_vec4',
    '_rect',
    '_color',
    '_arr',
    '_arr2',
    '_str_in',
    '_str_in2',
    '_str_out',
]

# ---------------------------------------------------------
# region CONSTANTS & ENUMS

# region HELPER CONSTS

_VEC2_GET_SWZL = re.compile(r'[xy]{,4}')
_VEC3_GET_SWZL = re.compile(r'[xyz]{1,4}|[rgb]{1,4}')
_VEC4_GET_SWZL = re.compile(r'[xyzw]{1,4}|[rgba]{1,4}')
_RGBA_GET_SWZL = re.compile(r'[rgba]{1,4}')

_number = (int, float)

_RGBA_TO_XYZW = {'r': 'x', 'g': 'y', 'b': 'z', 'a': 'w'}

T = TypeVar('T')
U = TypeVar('U')


# endregion (helper consts)

# endregion (constants)
# ---------------------------------------------------------
# region FUNCTIONS


def is_number(obj) -> bool:
    return isinstance(obj, _number)


def is_component(value) -> bool:
    return isinstance(value, int) and 0 <= value <= 255


def _clsname(obj: Any) -> str:
    return obj.__class__.__name__


def _clamp_rgba(*args) -> Union[int, Sequence[int]]:
    return tuple(value & 255 for value in args)


def _str_in(value: Union[str, bytes]) -> bytes:
    return value.encode('utf-8', 'ignore') if isinstance(value, str) else value


def _str_in2(values: Sequence[Union[str, bytes]]) -> MutableSequence[bytes]:
    return _arr(CharPtr, tuple(_str_in(value) for value in values))


def _str_out(value: Union[str, bytes]) -> str:
    return value.decode('utf-8', 'ignore') if isinstance(value, bytes) else value


def _arr(typ: Any, data: Sequence[U]) -> MutableSequence[U]:
    return (typ * len(data))(*data)


def _arr2(typ: Any, data: Sequence[U]) -> MutableSequence[U]:
    arr = typ * len(data[0])
    return (arr * len(data))(*data)


# region TYPE CAST FUNCS


def _float(value) -> float:
    return float(value)


def _int(value, ranged: Optional[Tuple[int, int]] = None) -> int:
    if ranged:
        return max(ranged[0], min(int(value), ranged[1]))
    return int(value)


def _vec2(seq: AnyVec2) -> 'Vector2':
    if isinstance(seq, Vector2):
        return seq
    x, y = seq
    return Vector2(_float(x), _float(y))


def _vec3(seq: AnyVec3) -> 'Vector3':
    if isinstance(seq, Vector3):
        return seq
    x, y, z = seq
    return Vector3(float(x), float(y), float(z))


def _vec4(seq: AnyVec3) -> 'Vector4':
    if isinstance(seq, Vector4):
        return seq
    x, y, z, w = seq
    return Vector4(float(x), float(y), float(z), float(w))


def _rect(seq: AnyRect) -> 'Rectangle':
    if isinstance(seq, Rectangle):
        return seq
    x, y, w, h = seq
    return Rectangle(float(x), float(y), float(w), float(h))


def _color(seq: AnyRGB) -> 'Color':
    if isinstance(seq, Color):
        return seq
    r, g, b, q = seq
    rng = 0, 255
    return Color(_int(r, rng), _int(r, rng), _int(b, rng), _int(q, rng))


# endregion (type cast funcs)

# endregion (functions)
# ---------------------------------------------------------
# region CLASSES


# region SINGLETONS


class Singleton(type):
    """
    Define an Instance operation that lets clients access its unique
    instance.
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance: Optional[Singleton] = None

    def __call__(cls, *args, **kwargs) -> Optional['Singleton']:
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Window(metaclass=Singleton):

    # region CLASSMETHODS

    @staticmethod
    def set_config_flags(flags: int) -> None:
        """Setup init configuration flags (view FLAGS)"""
        return _rl.SetConfigFlags(int(flags))

    # endregion (classmethods)

    def __init__(self, width: int, height: int, title: str):
        self._ctx: bool = False
        self._state: Tuple[int, int, str] = width, height, title
        if not _rl.IsWindowReady():
            _rl.InitWindow(int(width), int(height), _str_in(title))
        else:
            _rl.SetWindowSize(int(width), int(height))
            _rl.SetWindowTitle(_str_in(title))

    # region REPRESENTATION

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    # endregion (repersentation)

    # region CONTEXT

    def __enter__(self) -> 'Window':
        if not _rl.IsWindowReady():
            raise RuntimeError("The window is closed.")
        elif self._ctx:
            raise RuntimeError("Window contexts cannot be nested.")
        else:
            # reopens the window
            width, height, title = self._state
            _rl.SetWindowMinSize(int(width), int(height))
            _rl.SetWindowTitle(_str_in(title))
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._ctx = False
        _rl.CloseWindow()

    # endregion (context)

    # region PROPERTIES

    @property
    def should_close(self) -> bool:
        """Check if KEY_ESCAPE pressed or Close icon pressed"""
        return _rl.WindowShouldClose()

    @property
    def is_ready(self) -> bool:
        """Check if window has been initialized successfully"""
        return _rl.IsWindowReady()

    @property
    def is_fullscreen(self) -> bool:
        """Check if window is currently fullscreen"""
        return _rl.IsWindowFullscreen()

    @property
    def is_hidden(self):
        """Check if window is currently hidden (only PLATFORM_DESKTOP)"""
        return _rl.IsWindowHidden()

    @property
    def is_minimized(self) -> bool:
        """Check if window is currently minimized (only PLATFORM_DESKTOP)"""
        return _rl.IsWindowMinimized()

    @property
    def is_maximized(self) -> bool:
        """Check if window is currently maximized (only PLATFORM_DESKTOP)"""
        return _rl.IsWindowMaximized()

    @property
    def is_focused(self) -> bool:
        """Check if window is currently focused (only PLATFORM_DESKTOP)"""
        return _rl.IsWindowFocused()

    @property
    def is_resized(self) -> bool:
        """Check if window has been resized last frame"""
        return _rl.IsWindowResized()

    @property
    def handle(self) -> int:
        """Get native window handle"""
        return _rl.GetWindowHandle().contents[0]

    @property
    def screen_width(self) -> int:
        """Get current screen width"""
        return _rl.GetScreenWidth()

    @property
    def screen_height(self) -> int:
        """Get current screen height"""
        return _rl.GetScreenHeight()

    @property
    def fps(self) -> int:
        """Returns current FPS"""
        return _rl.GetFPS()

    @fps.setter
    def fps(self, fps: int) -> None:
        """Set target FPS (maximum)"""
        _rl.SetTargetFPS(int(fps))

    @property
    def frame_time(self) -> float:
        """Returns time in seconds for last frame drawn (delta time)"""
        return _rl.GetFrameTime()

    @property
    def time(self) -> float:
        """Returns elapsed time in seconds since InitWindow()"""
        return _rl.GetTime()

    # endregion (properties)

    # region METHODS

    @staticmethod
    def get_random_value(min_: int, max_: int) -> int:
        """Returns a random value between min and max (both included)"""
        return _rl.GetRandomValue(int(min_), int(max_))

    @staticmethod
    def clear_background(color: AnyRGB) -> None:
        """Set background color (framebuffer clear color)"""
        return _rl.ClearBackground(_color(color))

    @staticmethod
    def is_state(flag: int) -> bool:
        """Check if one specific window flag is enabled"""
        return _rl.IsWindowState(int(flag))

    @staticmethod
    def set_state(flags: int) -> None:
        """Set window configuration state using flags"""
        return _rl.SetWindowState(int(flags))

    @staticmethod
    def clear_state(flags: int) -> None:
        """Clear window configuration state flags"""
        return _rl.ClearWindowState(int(flags))

    @staticmethod
    def toggle_fullscreen(self) -> None:
        """Toggle window state: fullscreen/windowed (only PLATFORM_DESKTOP)"""
        return _rl.ToggleFullscreen()

    @staticmethod
    def maximize(self) -> None:
        """Set window state: maximized, if resizable (only PLATFORM_DESKTOP)"""
        return _rl.MaximizeWindow()

    @staticmethod
    def minimize(self) -> None:
        """Set window state: minimized, if resizable (only PLATFORM_DESKTOP)"""
        return _rl.MinimizeWindow()

    @staticmethod
    def restore(self) -> None:
        """Set window state: not minimized/maximized (only PLATFORM_DESKTOP)"""
        return _rl.RestoreWindow()

    @staticmethod
    def set_icon(image: 'Image') -> None:
        """Set icon for window (only PLATFORM_DESKTOP)"""
        return _rl.SetWindowIcon(image)

    @staticmethod
    def set_title(title: str) -> None:
        """Set title for window (only PLATFORM_DESKTOP)"""
        return _rl.SetWindowTitle(_str_in(title))

    @staticmethod
    def set_position(x: int, y: int) -> None:
        """Set window position on screen (only PLATFORM_DESKTOP)"""
        return _rl.SetWindowPosition(int(x), int(y))

    @staticmethod
    def set_monitor(monitor: Union[int, 'Monitor']) -> None:
        """Set monitor for the current window (fullscreen mode)"""
        return _rl.SetWindowMonitor(int(monitor.index if isinstance(monitor, Monitor) else monitor))

    @staticmethod
    def set_min_size(width: int, height: int) -> None:
        """Set window minimum dimensions (for FLAG_WINDOW_RESIZABLE)"""
        return _rl.SetWindowMinSize(int(width), int(height))

    @staticmethod
    def set_size(width: int, height: int) -> None:
        """Set window dimensions"""
        return _rl.SetWindowSize(int(width), int(height))

    @staticmethod
    def take_screenshot(file_name: str) -> None:
        """Takes a screenshot of current screen (filename extension defines format)"""
        return _rl.TakeScreenshot(_str_in(file_name))

    # endregion (methods)


class Clipboard(metaclass=Singleton):

    def __init__(self, text: str):
        self.text = text

    @property
    def text(self) -> str:
        """Get clipboard text content"""
        return _rl.GetClipboardText()

    @text.setter
    def text(self, text: str) -> None:
        """Set clipboard text content"""
        _rl.SetClipboardText(_str_in(text))


class Mouse(metaclass=Singleton):

    # region PROPERTIES

    @property
    def mouse_x(self) -> int:
        """Returns mouse position X"""
        return _rl.GetMouseX()

    @property
    def mouse_y(self) -> int:
        """Returns mouse position Y"""
        return _rl.GetMouseY()

    @property
    def mouse_position(self) -> 'Vector2':
        """Returns mouse position XY"""
        return _rl.GetMousePosition()

    @mouse_position.setter
    def mouse_position(self, value: AnyVec2) -> None:
        """Gets or sets mouse position XY"""
        _rl.SetMousePosition(int(value[0]), int(value[1]))

    @property
    def get_mouse_wheel_move(self) -> float:
        """Returns mouse wheel movement Y"""
        return _rl.GetMouseWheelMove()

    # endregion (properties)

    # region METHODS

    @staticmethod
    def set_offset(offset_x: int, offset_y: int) -> None:
        """Set mouse offset"""
        return _rl.SetMouseOffset(int(offset_x), int(offset_y))

    @staticmethod
    def set_scale(scale_x: float, scale_y: float) -> None:
        """Set mouse scaling"""
        return _rl.SetMouseScale(float(scale_x), float(scale_y))

    @staticmethod
    def set_cursor(cursor: int) -> None:
        """Set mouse cursor"""
        return _rl.SetMouseCursor(int(cursor))

    @staticmethod
    def is_button_pressed(button: int) -> bool:
        """Detect if a mouse button has been pressed once"""
        return _rl.IsMouseButtonPressed(int(button))

    @staticmethod
    def is_button_down(button: int) -> bool:
        """Detect if a mouse button is being pressed"""
        return _rl.IsMouseButtonDown(int(button))

    @staticmethod
    def is_button_released(button: int) -> bool:
        """Detect if a mouse button has been released once"""
        return _rl.IsMouseButtonReleased(int(button))

    @staticmethod
    def is_button_up(button: int) -> bool:
        """Detect if a mouse button is NOT being pressed"""
        return _rl.IsMouseButtonUp(int(button))

    # endregion (methods)


class Gesture(metaclass=Singleton):

    # region PROPERTIES

    @property
    def touch_x(self) -> int:
        """Returns touch position X for touch point 0 (relative to screen size)"""
        return _rl.GetTouchX()

    @property
    def touch_y(self) -> int:
        """Returns touch position Y for touch point 0 (relative to screen size)"""
        return _rl.GetTouchY()

    @property
    def touch_points_count(self) -> int:
        """Get touch points count"""
        return _rl.GetTouchPointsCount()

    @property
    def detected(self) -> int:
        """Get latest detected gesture"""
        return _rl.GetGestureDetected()

    @property
    def hold_duration(self) -> float:
        """Get gesture hold time in milliseconds"""
        return _rl.GetGestureHoldDuration()

    @property
    def drag_vector(self) -> 'Vector2':
        """Get gesture drag vector"""
        return _rl.GetGestureDragVector()

    @property
    def drag_angle(self) -> float:
        """Get gesture drag angle"""
        return _rl.GetGestureDragAngle()

    @property
    def pinch_vector(self) -> 'Vector2':
        """Get gesture pinch delta"""
        return _rl.GetGesturePinchVector()

    @property
    def pinch_angle(self) -> float:
        """Get gesture pinch angle"""
        return _rl.GetGesturePinchAngle()

    # endregion (properties)

    # region METHODS

    @staticmethod
    def get_touch_position(index: int) -> 'Vector2':
        """Returns touch position XY for a touch point index (relative to screen size)"""
        return _rl.GetTouchPosition(int(index))

    @staticmethod
    def set_enabled(flags: int) -> None:
        """Enable a set of gestures using flags"""
        return _rl.SetGesturesEnabled(int(flags))

    @staticmethod
    def is_detected(gesture: int) -> bool:
        """Check if a gesture have been detected"""
        return _rl.IsGestureDetected(int(gesture))

    # endregion (methods)


# endregion (singletons)


class Monitor(NamedTuple):
    index: int

    # region CLASSMETHODS

    @staticmethod
    def get_count() -> int:
        """Get number of connected monitors"""
        return _rl.GetMonitorCount()

    @classmethod
    def get_current(cls) -> 'Monitor':
        """Get current connected monitor"""
        return cls(_rl.GetCurrentMonitor())

    # endregion (classmethods)

    # region PROPERTIES

    @property
    def position(self) -> 'Vector2':
        """Get specified monitor position"""
        return _rl.GetMonitorPosition(int(self.index))

    @property
    def width(self) -> int:
        """Get specified monitor width (max available by monitor)"""
        return _rl.GetMonitorWidth(int(self.index))

    @property
    def height(self) -> int:
        """Get specified monitor height (max available by monitor)"""
        return _rl.GetMonitorHeight(int(self.index))

    @property
    def physical_width(self) -> int:
        """Get specified monitor physical width in millimetres"""
        return _rl.GetMonitorPhysicalWidth(int(self.index))

    @property
    def physical_height(self) -> int:
        """Get specified monitor physical height in millimetres"""
        return _rl.GetMonitorPhysicalHeight(int(self.index))

    @property
    def refresh_rate(self) -> int:
        """Get specified monitor refresh rate"""
        return _rl.GetMonitorRefreshRate(int(self.index))

    @property
    def window_position(self) -> 'Vector2':
        """Get window position XY on monitor"""
        return _rl.GetWindowPosition()

    @property
    def scale_dpi(self) -> 'Vector2':
        """Get window scale DPI factor"""
        return _rl.GetWindowScaleDPI()

    @property
    def name(self) -> str:
        """Get the human-readable, UTF-8 encoded name of the primary monitor"""
        return _rl.GetMonitorName(int(self.index))

    # endregion (properties)


class Gamepad(NamedTuple):
    index: int

    # region PROPERTIES

    @property
    def is_available(self) -> bool:
        """Detect if a gamepad is available"""
        return _rl.IsGamepadAvailable(int(self.index))

    @property
    def button_pressed(self) -> int:
        """Get the last gamepad button pressed"""
        return _rl.GetGamepadButtonPressed()

    @property
    def name(self) -> str:
        """Return gamepad internal name id"""
        return _str_out(_rl.GetGamepadName(int(self.index)))

    @property
    def axis_count(self) -> int:
        """Return gamepad axis count for a gamepad"""
        return _rl.GetGamepadAxisCount(int(self.index))

    # endregion (properties)

    # region METHODS

    def is_name(self, name: str) -> bool:
        """Check gamepad name (if available)"""
        return _rl.IsGamepadName(int(self.index), _str_in(name))

    def is_pressed(self, button: int) -> bool:
        """Detect if a gamepad button has been pressed once"""
        return _rl.IsGamepadButtonPressed(int(self.index), int(button))

    def is_down(self, button: int) -> bool:
        """Detect if a gamepad button is being pressed"""
        return _rl.IsGamepadButtonDown(int(self.index), int(button))

    def is_released(self, button: int) -> bool:
        """Detect if a gamepad button has been released once"""
        return _rl.IsGamepadButtonReleased(int(self.index), int(button))

    def is_up(self, button: int) -> bool:
        """Detect if a gamepad button is NOT being pressed"""
        return _rl.IsGamepadButtonUp(int(self.index), int(button))

    def get_axis_movement(self, axis: int) -> float:
        """Return axis movement value for a gamepad axis"""
        return _rl.GetGamepadAxisMovement(int(self.index), int(axis))

    @staticmethod
    def set_mappings(mappings: str) -> int:
        """Set internal gamepad mappings (SDL_GameControllerDB)"""
        return _rl.SetGamepadMappings(_str_in(mappings))

    # endregion (methods)


class AudioDevice:

    # region CLASSMETHODS

    @staticmethod
    def init() -> None:
        """Initialize audio device and context"""
        return _rl.InitAudioDevice()

    @staticmethod
    def close() -> None:
        """Close the audio device and context"""
        return _rl.CloseAudioDevice()

    @staticmethod
    def is_ready() -> bool:
        """Check if audio device has been initialized successfully"""
        return _rl.IsAudioDeviceReady()

    @staticmethod
    def set_master_volume(volume: float) -> None:
        """Set master volume (listener)"""
        return _rl.SetMasterVolume(float(volume))

    # endregion (classmethods)

    def __init__(self):
        raise TypeError("AudioDevice class is not meant to be instantiated.")


class Collision3D:

    def __init__(self):
        raise TypeError("Collision3D class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def check_spheres(center1: AnyVec3, radius1: float, center2: AnyVec3, radius2: float) -> bool:
        """Detect collision between two spheres"""
        return _rl.CheckCollisionSpheres(_vec3(center1), float(radius1), _vec3(center2), float(radius2))

    @staticmethod
    def check_boxes(box1: 'BoundingBox', box2: 'BoundingBox') -> bool:
        """Detect collision between two bounding boxes"""
        return _rl.CheckCollisionBoxes(box1, box2)

    @staticmethod
    def check_box_sphere(box: 'BoundingBox', center: AnyVec3, radius: float) -> bool:
        """Detect collision between box and sphere"""
        return _rl.CheckCollisionBoxSphere(box, _vec3(center), float(radius))

    @staticmethod
    def check_ray_sphere(ray: 'Ray', center: AnyVec3, radius: float) -> bool:
        """Detect collision between ray and sphere"""
        return _rl.CheckCollisionRaySphere(ray, _vec3(center), float(radius))

    @staticmethod
    def check_ray_sphere_ex(ray: 'Ray', center: AnyVec3, radius: float,
                            collision_point: Sequence['Vector3']) -> bool:
        """Detect collision between ray and sphere, returns collision point"""
        return _rl.CheckCollisionRaySphereEx(ray, _vec3(center), float(radius), _arr(Vector3, collision_point))

    @staticmethod
    def check_ray_box(ray: 'Ray', box: 'BoundingBox') -> bool:
        """Detect collision between ray and box"""
        return _rl.CheckCollisionRayBox(ray, box)

    @staticmethod
    def get_ray_mesh(ray: 'Ray', mesh: 'Mesh', transform: 'Matrix') -> 'RayHitInfo':
        """Get collision info between ray and mesh"""
        return _rl.GetCollisionRayMesh(ray, mesh, transform)

    @staticmethod
    def get_ray_model(ray: 'Ray', model: 'Model') -> 'RayHitInfo':
        """Get collision info between ray and model"""
        return _rl.GetCollisionRayModel(ray, model)

    @staticmethod
    def get_ray_triangle(ray: 'Ray', p1: AnyVec3, p2: AnyVec3, p3: AnyVec3) -> 'RayHitInfo':
        """Get collision info between ray and triangle"""
        return _rl.GetCollisionRayTriangle(ray, _vec3(p1), _vec3(p2), _vec3(p3))

    @staticmethod
    def get_ray_ground(ray: 'Ray', ground_height: float) -> 'RayHitInfo':
        """Get collision info between ray and ground plane (Y-normal plane)"""
        return _rl.GetCollisionRayGround(ray, float(ground_height))

    # endregion (methods)


class Collision:

    def __init__(self):
        raise TypeError("Collision class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def check_recs(rec1: AnyRect, rec2: AnyRect) -> bool:
        """Check collision between two rectangles"""
        return _rl.CheckCollisionRecs(_rect(rec1), _rect(rec2))

    @staticmethod
    def check_circles(center1: AnyVec2, radius1: float, center2: AnyVec2, radius2: float) -> bool:
        """Check collision between two circles"""
        return _rl.CheckCollisionCircles(_vec2(center1), float(radius1), _vec2(center2), float(radius2))

    @staticmethod
    def check_circle_rec(center: AnyVec2, radius: float, rec: AnyRect) -> bool:
        """Check collision between circle and rectangle"""
        return _rl.CheckCollisionCircleRec(_vec2(center), float(radius), _rect(rec))

    @staticmethod
    def check_point_rec(point: AnyVec2, rec: AnyRect) -> bool:
        """Check if point is inside rectangle"""
        return _rl.CheckCollisionPointRec(_vec2(point), _rect(rec))

    @staticmethod
    def check_point_circle(point: AnyVec2, center: AnyVec2, radius: float) -> bool:
        """Check if point is inside circle"""
        return _rl.CheckCollisionPointCircle(_vec2(point), _vec2(center), float(radius))

    @staticmethod
    def check_point_triangle(point: AnyVec2, p1: AnyVec2, p2: AnyVec2, p3: AnyVec2) -> bool:
        """Check if point is inside a triangle"""
        return _rl.CheckCollisionPointTriangle(_vec2(point), _vec2(p1), _vec2(p2), _vec2(p3))

    @staticmethod
    def check_lines(start_pos1: AnyVec2, end_pos1: AnyVec2, start_pos2: AnyVec2, end_pos2: AnyVec2,
                    collision_point: Sequence['Vector2']) -> bool:
        """Check the collision between two lines defined by two points each, returns collision point by reference"""
        return _rl.CheckCollisionLines(_vec2(start_pos1), _vec2(end_pos1), _vec2(start_pos2), _vec2(end_pos2),
                                       _arr(Vector2, collision_point))

    @staticmethod
    def get_rec(rec1: AnyRect, rec2: AnyRect) -> 'Rectangle':
        """Get collision rectangle for two rectangles collision"""
        return _rl.GetCollisionRec(_rect(rec1), _rect(rec2))

    # endregion (methods


class Key:

    def __init__(self):
        raise TypeError("Key class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def is_pressed(key: int) -> bool:
        """Detect if a key has been pressed once"""
        return _rl.IsKeyPressed(int(key))

    @staticmethod
    def is_down(key: int) -> bool:
        """Detect if a key is being pressed"""
        return _rl.IsKeyDown(int(key))

    @staticmethod
    def is_released(key: int) -> bool:
        """Detect if a key has been released once"""
        return _rl.IsKeyReleased(int(key))

    @staticmethod
    def is_up(key: int) -> bool:
        """Detect if a key is NOT being pressed"""
        return _rl.IsKeyUp(int(key))

    @staticmethod
    def set_exit_key(key: int) -> None:
        """Set a custom key to exit program (default is ESC)"""
        return _rl.SetExitKey(int(key))

    @staticmethod
    def get_pressed() -> int:
        """Get key pressed (keycode), call it multiple times for keys queued"""
        return _rl.GetKeyPressed()

    @staticmethod
    def get_char() -> int:
        """Get char pressed (unicode), call it multiple times for chars queued"""
        return _rl.GetCharPressed()

    # endregion (methods)


class Draw:

    def __init__(self):
        raise TypeError("Draw class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def set_shapes_texture(texture: 'Texture2D', source: AnyRect) -> None:
        """Set texture and rectangle to be used on shapes drawing

        It can be useful when using basic shapes and one single font,
        defining a font char white rectangle would allow drawing everything in a single draw call
        """
        return _rl.SetShapesTexture(texture, _rect(source))

    # region DRAWING 2D

    @staticmethod
    def pixel(pos_x: int, pos_y: int, color: AnyRGB) -> None:
        """Draw a pixel"""
        return _rl.DrawPixel(int(pos_x), int(pos_y), _color(color))

    @staticmethod
    def pixel_v(position: AnyVec2, color: AnyRGB) -> None:
        """Draw a pixel (Vector version)"""
        return _rl.DrawPixelV(_vec2(position), _color(color))

    @staticmethod
    def line(start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: AnyRGB) -> None:
        """Draw a line"""
        return _rl.DrawLine(int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y), _color(color))

    @staticmethod
    def line_v(start_pos: AnyVec2, end_pos: AnyVec2, color: AnyRGB) -> None:
        """Draw a line (Vector version)"""
        return _rl.DrawLineV(_vec2(start_pos), _vec2(end_pos), _color(color))

    @staticmethod
    def line_ex(start_pos: AnyVec2, end_pos: AnyVec2, thick: float, color: AnyRGB) -> None:
        """Draw a line defining thickness"""
        return _rl.DrawLineEx(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))

    @staticmethod
    def line_bezier(start_pos: AnyVec2, end_pos: AnyVec2, thick: float, color: AnyRGB) -> None:
        """Draw a line using cubic-bezier curves in-out"""
        return _rl.DrawLineBezier(_vec2(start_pos), _vec2(end_pos), float(thick), _color(color))

    @staticmethod
    def line_bezier_quad(start_pos: AnyVec2, end_pos: AnyVec2, control_pos: AnyVec2, thick: float,
                         color: AnyRGB) -> None:
        """Draw line using quadratic bezier curves with a control point"""
        return _rl.DrawLineBezierQuad(_vec2(start_pos), _vec2(end_pos), _vec2(control_pos), float(thick),
                                      _color(color))

    @staticmethod
    def line_strip(points: Sequence['Vector2'], points_count: int, color: AnyRGB) -> None:
        """Draw lines sequence"""
        return _rl.DrawLineStrip(_arr(Vector2, points), int(points_count), _color(color))

    @staticmethod
    def circle(center_x: int, center_y: int, radius: float, color: AnyRGB) -> None:
        """Draw a color-filled circle"""
        return _rl.DrawCircle(int(center_x), int(center_y), float(radius), _color(color))

    @staticmethod
    def circle_sector(center: AnyVec2, radius: float, start_angle: float, end_angle: float,
                      segments: int, color: AnyRGB) -> None:
        """Draw a piece of a circle"""
        return _rl.DrawCircleSector(_vec2(center), float(radius), float(start_angle), float(end_angle), int(segments),
                                    _color(color))

    @staticmethod
    def circle_sector_lines(center: AnyVec2, radius: float, start_angle: float, end_angle: float, segments: int,
                            color: AnyRGB) -> None:
        """Draw circle sector outline"""
        return _rl.DrawCircleSectorLines(_vec2(center), float(radius), float(start_angle), float(end_angle),
                                         int(segments),
                                         _color(color))

    @staticmethod
    def circle_gradient(center_x: int, center_y: int, radius: float, color1: AnyRGB, color2: AnyRGB) -> None:
        """Draw a gradient-filled circle"""
        return _rl.DrawCircleGradient(int(center_x), int(center_y), float(radius), _color(color1), _color(color2))

    @staticmethod
    def circle_v(center: AnyVec2, radius: float, color: AnyRGB) -> None:
        """Draw a color-filled circle (Vector version)"""
        return _rl.DrawCircleV(_vec2(center), float(radius), _color(color))

    @staticmethod
    def circle_lines(center_x: int, center_y: int, radius: float, color: AnyRGB) -> None:
        """Draw circle outline"""
        return _rl.DrawCircleLines(int(center_x), int(center_y), float(radius), _color(color))

    @staticmethod
    def ellipse(center_x: int, center_y: int, radius_h: float, radius_v: float, color: AnyRGB) -> None:
        """Draw ellipse"""
        return _rl.DrawEllipse(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))

    @staticmethod
    def ellipse_lines(center_x: int, center_y: int, radius_h: float, radius_v: float, color: AnyRGB) -> None:
        """Draw ellipse outline"""
        return _rl.DrawEllipseLines(int(center_x), int(center_y), float(radius_h), float(radius_v), _color(color))

    @staticmethod
    def ring(center: AnyVec2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float,
             segments: int, color: AnyRGB) -> None:
        """Draw ring"""
        return _rl.DrawRing(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle),
                            float(end_angle),
                            int(segments), _color(color))

    @staticmethod
    def ring_lines(center: AnyVec2, inner_radius: float, outer_radius: float, start_angle: float, end_angle: float,
                   segments: int, color: AnyRGB) -> None:
        """Draw ring outline"""
        _rl.DrawRingLines(_vec2(center), float(inner_radius), float(outer_radius), float(start_angle),
                          float(end_angle), int(segments), _color(color))

    @staticmethod
    def rectangle(pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
        """Draw a color-filled rectangle"""
        _rl.DrawRectangle(int(pos_x), int(pos_y), int(width), int(height), _color(color))

    @staticmethod
    def rectangle_v(position: AnyVec2, size: AnyVec2, color: AnyRGB) -> None:
        """Draw a color-filled rectangle (Vector version)"""
        _rl.DrawRectangleV(_vec2(position), _vec2(size), _color(color))

    @staticmethod
    def rectangle_rec(rec: AnyRect, color: AnyRGB) -> None:
        """Draw a color-filled rectangle"""
        _rl.DrawRectangleRec(_rect(rec), _color(color))

    @staticmethod
    def rectangle_pro(rec: AnyRect, origin: AnyVec2, rotation: float, color: AnyRGB) -> None:
        """Draw a color-filled rectangle with pro parameters"""
        _rl.DrawRectanglePro(_rect(rec), _vec2(origin), float(rotation), _color(color))

    @staticmethod
    def rectangle_gradient_v(pos_x: int, pos_y: int, width: int, height: int, color1: AnyRGB,
                             color2: AnyRGB) -> None:
        """Draw a vertical-gradient-filled rectangle"""
        _rl.DrawRectangleGradientV(int(pos_x), int(pos_y), int(width), int(height), _color(color1),
                                   _color(color2))

    @staticmethod
    def rectangle_gradient_h(pos_x: int, pos_y: int, width: int, height: int, color1: AnyRGB,
                             color2: AnyRGB) -> None:
        """Draw a horizontal-gradient-filled rectangle"""
        _rl.DrawRectangleGradientH(int(pos_x), int(pos_y), int(width), int(height), _color(color1),
                                   _color(color2))

    @staticmethod
    def rectangle_gradient_ex(rec: AnyRect, col1: AnyRGB, col2: AnyRGB, col3: AnyRGB, col4: AnyRGB) -> None:
        """Draw a gradient-filled rectangle with custom vertex colors"""
        _rl.DrawRectangleGradientEx(_rect(rec), _color(col1), _color(col2), _color(col3), _color(col4))

    @staticmethod
    def rectangle_lines(pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
        """Draw rectangle outline"""
        _rl.DrawRectangleLines(int(pos_x), int(pos_y), int(width), int(height), _color(color))

    @staticmethod
    def rectangle_lines_ex(rec: AnyRect, line_thick: int, color: AnyRGB) -> None:
        """Draw rectangle outline with extended parameters"""
        _rl.DrawRectangleLinesEx(_rect(rec), int(line_thick), _color(color))

    @staticmethod
    def rectangle_rounded(rec: AnyRect, roundness: float, segments: int, color: AnyRGB) -> None:
        """Draw rectangle with rounded edges"""
        _rl.DrawRectangleRounded(_rect(rec), float(roundness), int(segments), _color(color))

    @staticmethod
    def rectangle_rounded_lines(rec: AnyRect, roundness: float, segments: int, line_thick: int,
                                color: AnyRGB) -> None:
        """Draw rectangle with rounded edges outline"""
        _rl.DrawRectangleRoundedLines(_rect(rec), float(roundness), int(segments), int(line_thick),
                                      _color(color))

    @staticmethod
    def triangle(v1: AnyVec2, v2: AnyVec2, v3: AnyVec2, color: AnyRGB) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        _rl.DrawTriangle(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))

    @staticmethod
    def triangle_lines(v1: AnyVec2, v2: AnyVec2, v3: AnyVec2, color: AnyRGB) -> None:
        """Draw triangle outline (vertex in counter-clockwise order!)"""
        _rl.DrawTriangleLines(_vec2(v1), _vec2(v2), _vec2(v3), _color(color))

    @staticmethod
    def triangle_fan(points: Sequence['Vector2'], points_count: int, color: AnyRGB) -> None:
        """Draw a triangle fan defined by points (first vertex is the center)"""
        _rl.DrawTriangleFan(_arr(Vector2, points), int(points_count), _color(color))

    @staticmethod
    def triangle_strip(points: Sequence['Vector2'], points_count: int, color: AnyRGB) -> None:
        """Draw a triangle strip defined by points"""
        _rl.DrawTriangleStrip(_arr(Vector2, points), int(points_count), _color(color))

    @staticmethod
    def poly(center: AnyVec2, sides: int, radius: float, rotation: float, color: AnyRGB) -> None:
        """Draw a regular polygon (Vector version)"""
        _rl.DrawPoly(_vec2(center), int(sides), float(radius), float(rotation), _color(color))

    @staticmethod
    def poly_lines(center: AnyVec2, sides: int, radius: float, rotation: float, color: AnyRGB) -> None:
        """Draw a polygon outline of n sides"""
        _rl.DrawPolyLines(_vec2(center), int(sides), float(radius), float(rotation), _color(color))

    # endregion (drawing 2d)

    # region DRAWING 3D

    @staticmethod
    def line3d(start_pos: AnyVec3, end_pos: AnyVec3, color: AnyRGB) -> None:
        """Draw a line in 3D world space"""
        return _rl.DrawLine3D(_vec3(start_pos), _vec3(end_pos), _color(color))

    @staticmethod
    def point3d(position: AnyVec3, color: AnyRGB) -> None:
        """Draw a point in 3D space, actually a small line"""
        return _rl.DrawPoint3D(_vec3(position), _color(color))

    @staticmethod
    def circle3d(center: AnyVec3, radius: float, rotation_axis: AnyVec3, rotation_angle: float,
                 color: AnyRGB) -> None:
        """Draw a circle in 3D world space"""
        return _rl.DrawCircle3D(_vec3(center), float(radius), _vec3(rotation_axis), float(rotation_angle),
                                _color(color))

    @staticmethod
    def triangle3d(v1: AnyVec3, v2: AnyVec3, v3: AnyVec3, color: AnyRGB) -> None:
        """Draw a color-filled triangle (vertex in counter-clockwise order!)"""
        return _rl.DrawTriangle3D(_vec3(v1), _vec3(v2), _vec3(v3), _color(color))

    @staticmethod
    def triangle_strip3d(points: Sequence['Vector3'], points_count: int, color: AnyRGB) -> None:
        """Draw a triangle strip defined by points"""
        return _rl.DrawTriangleStrip3D(_arr(Vector3, points), int(points_count), _color(color))

    @staticmethod
    def cube(position: AnyVec3, width: float, height: float, length: float, color: AnyRGB) -> None:
        """Draw cube"""
        return _rl.DrawCube(_vec3(position), float(width), float(height), float(length), _color(color))

    @staticmethod
    def cube_v(position: AnyVec3, size: AnyVec3, color: AnyRGB) -> None:
        """Draw cube (Vector version)"""
        return _rl.DrawCubeV(_vec3(position), _vec3(size), _color(color))

    @staticmethod
    def cube_wires(position: AnyVec3, width: float, height: float, length: float, color: AnyRGB) -> None:
        """Draw cube wires"""
        return _rl.DrawCubeWires(_vec3(position), float(width), float(height), float(length), _color(color))

    @staticmethod
    def cube_wires_v(position: AnyVec3, size: AnyVec3, color: AnyRGB) -> None:
        """Draw cube wires (Vector version)"""
        return _rl.DrawCubeWiresV(_vec3(position), _vec3(size), _color(color))

    @staticmethod
    def cube_texture(texture: 'Texture2D', position: AnyVec3, width: float, height: float, length: float,
                     color: AnyRGB) -> None:
        """Draw cube textured"""
        return _rl.DrawCubeTexture(texture, _vec3(position), float(width), float(height), float(length), _color(color))

    @staticmethod
    def sphere(center_pos: AnyVec3, radius: float, color: AnyRGB) -> None:
        """Draw sphere"""
        return _rl.DrawSphere(_vec3(center_pos), float(radius), _color(color))

    @staticmethod
    def sphere_ex(center_pos: AnyVec3, radius: float, rings: int, slices: int, color: AnyRGB) -> None:
        """Draw sphere with extended parameters"""
        return _rl.DrawSphereEx(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))

    @staticmethod
    def sphere_wires(center_pos: AnyVec3, radius: float, rings: int, slices: int, color: AnyRGB) -> None:
        """Draw sphere wires"""
        return _rl.DrawSphereWires(_vec3(center_pos), float(radius), int(rings), int(slices), _color(color))

    @staticmethod
    def cylinder(position: AnyVec3, radius_top: float, radius_bottom: float, height: float, slices: int,
                 color: AnyRGB) -> None:
        """Draw a cylinder/cone"""
        return _rl.DrawCylinder(_vec3(position), float(radius_top), float(radius_bottom), float(height), int(slices),
                                _color(color))

    @staticmethod
    def cylinder_wires(position: AnyVec3, radius_top: float, radius_bottom: float, height: float, slices: int,
                       color: AnyRGB) -> None:
        """Draw a cylinder/cone wires"""
        return _rl.DrawCylinderWires(_vec3(position), float(radius_top), float(radius_bottom), float(height),
                                     int(slices),
                                     _color(color))

    @staticmethod
    def plane(center_pos: AnyVec3, size: AnyVec2, color: AnyRGB) -> None:
        """Draw a plane XZ"""
        return _rl.DrawPlane(_vec3(center_pos), _vec2(size), _color(color))

    @staticmethod
    def ray(ray: 'Ray', color: AnyRGB) -> None:
        """Draw a ray line"""
        return _rl.DrawRay(ray, _color(color))

    @staticmethod
    def grid(slices: int, spacing: float) -> None:
        """Draw a grid (centered at (0, 0, 0))"""
        return _rl.DrawGrid(int(slices), float(spacing))

    @staticmethod
    def model(model: 'Model', position: AnyVec3, scale: float, tint: AnyRGB) -> None:
        """Draw a model (with texture if set)"""
        return _rl.DrawModel(model, _vec3(position), float(scale), _color(tint))

    @staticmethod
    def model_ex(model: 'Model', position: AnyVec3, rotation_axis: AnyVec3, rotation_angle: float, scale: AnyVec3,
                 tint: AnyRGB) -> None:
        """Draw a model with extended parameters"""
        return _rl.DrawModelEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale),
                               _color(tint))

    @staticmethod
    def model_wires(model: 'Model', position: AnyVec3, scale: float, tint: AnyRGB) -> None:
        """Draw a model wires (with texture if set)"""
        return _rl.DrawModelWires(model, _vec3(position), float(scale), _color(tint))

    @staticmethod
    def model_wires_ex(model: 'Model', position: AnyVec3, rotation_axis: AnyVec3, rotation_angle: float,
                       scale: AnyVec3,
                       tint: AnyRGB) -> None:
        """Draw a model wires (with texture if set) with extended parameters"""
        return _rl.DrawModelWiresEx(model, _vec3(position), _vec3(rotation_axis), float(rotation_angle), _vec3(scale),
                                    _color(tint))

    @staticmethod
    def bounding_box(box: 'BoundingBox', color: AnyRGB) -> None:
        """Draw bounding box (wires)"""
        return _rl.DrawBoundingBox(box, _color(color))

    @staticmethod
    def billboard(camera: 'Camera', texture: 'Texture2D', center: AnyVec3, size: float, tint: AnyRGB) -> None:
        """Draw a billboard texture"""
        return _rl.DrawBillboard(camera, texture, _vec3(center), float(size), _color(tint))

    @staticmethod
    def billboard_rec(camera: 'Camera', texture: 'Texture2D', source: AnyRect, center: AnyVec3, size: float,
                      tint: AnyRGB) -> None:
        """Draw a billboard texture defined by source"""
        return _rl.DrawBillboardRec(camera, texture, _rect(source), _vec3(center), float(size), _color(tint))

    # endregion (drawing 3D)

    # region DRAWING TEXT

    @staticmethod
    def draw_fps(pos_x: int, pos_y: int) -> None:
        """Draw current FPS"""
        return _rl.DrawFPS(int(pos_x), int(pos_y))

    @staticmethod
    def draw_text(text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
        """Draw text (using default font)"""
        return _rl.DrawText(_str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    @staticmethod
    def draw_text_ex(font: 'Font', text: str, position: AnyVec2, font_size: float, spacing: float,
                     tint: AnyRGB) -> None:
        """Draw text using font and additional parameters"""
        return _rl.DrawTextEx(font, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))

    @staticmethod
    def draw_text_rec(font: 'Font', text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                      tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits"""
        return _rl.DrawTextRec(font, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                               _color(tint))

    @staticmethod
    def draw_text_rec_ex(font: 'Font', text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                         tint: AnyRGB, select_start: int, select_length: int, select_tint: AnyRGB,
                         select_back_tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits with support for text selection"""
        return _rl.DrawTextRecEx(font, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                                 _color(tint), int(select_start), int(select_length), _color(select_tint),
                                 _color(select_back_tint))

    @staticmethod
    def draw_text_codepoint(font: 'Font', codepoint: int, position: AnyVec2, font_size: float, tint: AnyRGB) -> None:
        """Draw one character (codepoint)"""
        return _rl.DrawTextCodepoint(font, int(codepoint), _vec2(position), float(font_size), _color(tint))

    # endregion (drawing text)

    # endregion (methods)


class PixelData:

    def __init__(self):
        raise TypeError("PixelData class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def get_color(src_ptr: bytes, format_: int) -> 'Color':
        """Get Color from a source pixel pointer of certain format"""
        return _rl.GetPixelColor(src_ptr, int(format_))

    @staticmethod
    def set_color(dst_ptr: bytes, color: AnyRGB, format_: int) -> None:
        """Set color formatted into destination pixel pointer"""
        return _rl.SetPixelColor(dst_ptr, _color(color), int(format_))

    @staticmethod
    def get_data_size(width: int, height: int, format_: int) -> int:
        """Get pixel data size in bytes for certain format"""
        return _rl.GetPixelDataSize(int(width), int(height), int(format_))

    # endregion (methods)


class Text:

    def __init__(self):
        raise TypeError("Text class is not meant to be instantiated.")

    # region STATICMETHODS

    @staticmethod
    def copy(dst: str, src: str) -> int:
        """Copy one string to another, returns bytes copied"""
        return _rl.TextCopy(_str_in(dst), _str_in(src))

    @staticmethod
    def is_equal(text1: str, text2: str) -> bool:
        """Check if two text string are equal"""
        return _rl.TextIsEqual(_str_in(text1), _str_in(text2))

    @staticmethod
    def length(text: str) -> int:
        """Get text length, checks for '\0' ending"""
        return _rl.TextLength(_str_in(text))

    @staticmethod
    def format(text: str, *args, **kwargs) -> str:
        """Text formatting with variables (Python formatting rules)"""
        # return _rl.TextFormat(_str_in(text), ...)
        return _str_out(text.format(*args, **kwargs))

    @staticmethod
    def subtext(text: str, position: int, length: int) -> str:
        """Get a piece of a text string"""
        return _str_out(_rl.TextSubtext(_str_in(text), int(position), int(length)))

    @staticmethod
    def replace(text: str, replace: str, by: str) -> str:
        """Replace text string (memory must be freed!)"""
        return _str_out(_rl.TextReplace(_str_in(text), _str_in(replace), _str_in(by)))

    @staticmethod
    def insert(text: str, insert: str, position: int) -> str:
        """Insert text in a position (memory must be freed!)"""
        return _str_out(_rl.TextInsert(_str_in(text), _str_in(insert), int(position)))

    @staticmethod
    def join(text_list: Sequence[str], count: int, delimiter: str) -> str:
        """Join text strings with delimiter"""
        return _str_out(_rl.TextJoin(_str_in2(text_list), int(count), _str_in(delimiter)))

    @staticmethod
    def split(text: str, delimiter: str) -> Sequence[bytes]:
        """Split text into multiple strings"""
        count = IntPtr(0)
        splits = _rl.TextSplit(_str_in(text), ord(delimiter[0]), count)
        return tuple(split for split in splits[:count.contents[0]])

    @staticmethod
    def append(text: str, append: str, position: int) -> int:
        """Append text at specific position and move cursor!"""
        ptr = IntPtr(position)
        _rl.TextAppend(_str_in(text), _str_in(append), ptr)
        return ptr.contents[0]

    @staticmethod
    def find_index(text: str, find: str) -> int:
        """Find first text occurrence within a string"""
        return _rl.TextFindIndex(_str_in(text), _str_in(find))

    @staticmethod
    def to_upper(text: str) -> str:
        """Get upper case version of provided string"""
        return _str_out(_rl.TextToUpper(_str_in(text)))

    @staticmethod
    def to_lower(text: str) -> str:
        """Get lower case version of provided string"""
        return _str_out(_rl.TextToLower(_str_in(text)))

    @staticmethod
    def to_pascal(text: str) -> str:
        """Get Pascal case notation version of provided string"""
        return _str_out(_rl.TextToPascal(_str_in(text)))

    @staticmethod
    def to_integer(text: str) -> int:
        """Get integer value from text (negative values not supported)"""
        return _rl.TextToInteger(_str_in(text))

    @staticmethod
    def to_utf8(codepoints: Sequence[int], length: int) -> str:
        """Encode text codepoint into utf8 text (memory must be freed!)"""
        return _str_out(_rl.TextToUtf8(_arr(Int, codepoints), int(length)))

    @staticmethod
    def get_codepoints(text: str) -> Tuple[int, int]:
        """Get all codepoints in a string, codepoints count returned by parameters"""
        count = IntPtr(0)
        result = _rl.GetCodepoints(_str_in(text), count)
        return result, count.contents[0]

    @staticmethod
    def get_codepoints_count(text: str) -> int:
        """Get total number of characters (codepoints) in a UTF8 encoded string"""
        return _rl.GetCodepointsCount(_str_in(text))

    @staticmethod
    def get_next_codepoint(text: str) -> Tuple[int, int]:
        """Returns next codepoint in a UTF8 encoded string; 0x3f('?') is returned on failure"""
        bytes_processed = IntPtr(0)
        result = _rl.GetNextCodepoint(_str_in(text), bytes_processed)
        return result, bytes_processed.contents[0]

    @staticmethod
    def codepoint_to_utf8(codepoint: int) -> Tuple[str, int]:
        """Encode codepoint into utf8 text (char array length returned as parameter)"""
        byte_length = IntPtr(0)
        result = _rl.CodepointToUtf8(int(codepoint), byte_length)
        return result, byte_length.contents[0]

    # endregion (staticmethods)


class Cursor:

    def __init__(self):
        raise TypeError("Cursor class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def show() -> None:
        """Shows cursor"""
        _rl.ShowCursor()

    @staticmethod
    def hide() -> None:
        """Hides cursor"""
        _rl.HideCursor()

    @staticmethod
    def is_hidden() -> bool:
        """Check if cursor is not visible"""
        return _rl.IsCursorHidden()

    @staticmethod
    def enable() -> None:
        """Enables cursor (unlock cursor)"""
        _rl.EnableCursor()

    @staticmethod
    def disable() -> None:
        """Disables cursor (lock cursor)"""
        _rl.DisableCursor()

    @staticmethod
    def is_on_screen() -> bool:
        """Check if cursor is on the current screen."""
        return _rl.IsCursorOnScreen()

    # endregion (methods)


class Mem:

    def __init__(self):
        raise TypeError("Mem class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def alloc(size: int) -> bytes:
        """Internal memory allocator"""
        return _rl.MemAlloc(int(size))

    @staticmethod
    def realloc(ptr: bytes, size: int) -> bytes:
        """Internal memory reallocator"""
        return _rl.MemRealloc(ptr, int(size))

    @staticmethod
    def free(ptr: bytes) -> None:
        """Internal memory free"""
        return _rl.MemFree(ptr)

    # endregion (methods)


class TraceLog:

    def __init__(self):
        raise TypeError("TraceLog class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def set_callback(callback: TraceLogCallback) -> None:
        """Set custom trace log"""
        return _rl.SetTraceLogCallback(callback)

    @staticmethod
    def trace_log(log_level: int, text: str) -> None:
        """Show trace log messages (LOG_DEBUG, LOG_INFO, LOG_WARNING, LOG_ERROR)"""
        return _rl.TraceLog(int(log_level), _str_in(text))

    @staticmethod
    def set_level(log_level: int) -> None:
        """Set the current threshold (minimum) log level"""
        return _rl.SetTraceLogLevel(int(log_level))

    # endregion (methods)


class System:

    def __init__(self):
        raise TypeError("System class is not meant to be instantiated.")

    # region METHODS

    @staticmethod
    def set_load_file_data_callback(callback: LoadFileDataCallback) -> None:
        """Set custom file binary data loader"""
        return _rl.SetLoadFileDataCallback(callback)

    @staticmethod
    def set_save_file_data_callback(callback: SaveFileDataCallback) -> None:
        """Set custom file binary data saver"""
        return _rl.SetSaveFileDataCallback(callback)

    @staticmethod
    def set_load_file_text_callback(callback: LoadFileTextCallback) -> None:
        """Set custom file text data loader"""
        return _rl.SetLoadFileTextCallback(callback)

    @staticmethod
    def set_save_file_text_callback(callback: SaveFileTextCallback) -> None:
        """Set custom file text data saver"""
        return _rl.SetSaveFileTextCallback(callback)

    @staticmethod
    def load_file_data(file_name: str, bytes_read: Sequence[int]) -> bytes:
        """Load file data as byte array (read)"""
        return _rl.LoadFileData(_str_in(file_name), _arr(Int, bytes_read))

    @staticmethod
    def unload_file_data(data: bytes) -> None:
        """Unload file data allocated by LoadFileData()"""
        return _rl.UnloadFileData(data)

    @staticmethod
    def save_file_data(file_name: str, data: bytes, bytes_to_write: int) -> bool:
        """Save data to file from byte array (write), returns true on success"""
        return _rl.SaveFileData(_str_in(file_name), data, int(bytes_to_write))

    @staticmethod
    def load_file_text(file_name: str) -> str:
        """Load text data from file (read), returns a '\0' terminated string"""
        return _rl.LoadFileText(_str_in(file_name))

    @staticmethod
    def unload_file_text(text: bytes) -> None:
        """Unload file text data allocated by LoadFileText()"""
        return _rl.UnloadFileText(text)

    @staticmethod
    def save_file_text(file_name: str, text: str) -> bool:
        """Save text data to file (write), string must be '\0' terminated, returns true on success"""
        return _rl.SaveFileText(_str_in(file_name), _str_in(text))

    @staticmethod
    def file_exists(file_name: str) -> bool:
        """Check if file exists"""
        return _rl.FileExists(_str_in(file_name))

    @staticmethod
    def directory_exists(dir_path: str) -> bool:
        """Check if a directory path exists"""
        return _rl.DirectoryExists(_str_in(dir_path))

    @staticmethod
    def is_file_extension(file_name: str, ext: str) -> bool:
        """Check file extension (including point: .png, .wav)"""
        return _rl.IsFileExtension(_str_in(file_name), _str_in(ext))

    @staticmethod
    def get_file_extension(file_name: str) -> str:
        """Get pointer to extension for a filename string (includes dot: ".png")"""
        return _rl.GetFileExtension(_str_in(file_name))

    @staticmethod
    def get_file_name(file_path: str) -> str:
        """Get pointer to filename for a path string"""
        return _rl.GetFileName(_str_in(file_path))

    @staticmethod
    def get_file_name_without_ext(file_path: str) -> str:
        """Get filename string without extension (uses static string)"""
        return _rl.GetFileNameWithoutExt(_str_in(file_path))

    @staticmethod
    def get_directory_path(file_path: str) -> str:
        """Get full path for a given fileName with path (uses static string)"""
        return _rl.GetDirectoryPath(_str_in(file_path))

    @staticmethod
    def get_prev_directory_path(dir_path: str) -> str:
        """Get previous directory path for a given path (uses static string)"""
        return _rl.GetPrevDirectoryPath(_str_in(dir_path))

    @staticmethod
    def get_working_directory() -> str:
        """Get current working directory (uses static string)"""
        return _rl.GetWorkingDirectory()

    @staticmethod
    @contextlib.contextmanager
    def get_directory_files(dir_path: str):
        """Get filenames in a directory path (memory should be freed)"""
        count = IntPtr(0)
        result = _rl.GetDirectoryFiles(_str_in(dir_path), count)
        files = []
        for i in range(count.value):
            files.append(result[i].decode('utf-8'))
        yield files
        _rl.ClearDirectoryFiles()

    @staticmethod
    def change_directory(dir_: str) -> bool:
        """Change working directory, return true on success"""
        return _rl.ChangeDirectory(_str_in(dir_))

    @staticmethod
    def is_file_dropped() -> bool:
        """Check if a file has been dropped into window"""
        return _rl.IsFileDropped()

    @staticmethod
    @contextlib.contextmanager
    def get_dropped_files():
        """Get dropped files names (memory should be freed)"""
        count = IntPtr(0)
        result = _rl.GetDroppedFiles(count)
        files = []
        for i in range(count.value):
            files.append(result[i].decode('utf-8'))
        yield tuple(files)
        _rl.ClearDroppedFiles()

    @staticmethod
    def get_file_mod_time(file_name: str) -> int:
        """Get file modification time (last write time)"""
        return _rl.GetFileModTime(_str_in(file_name))

    @staticmethod
    def compress_data(data: bytes) -> Tuple[bytes, int]:
        """Compress data (DEFLATE algorithm)"""
        compressed_length = IntPtr(0)
        compressed_data = _rl.CompressData(data, len(data), compressed_length)
        return compressed_data, compressed_length.contents

    @staticmethod
    def decompress_data(comp_data: bytes) -> Tuple[bytes, int]:
        """Decompress data (DEFLATE algorithm)"""
        decompressed_length = IntPtr(0)
        decompressed_data = _rl.DecompressData(comp_data, len(comp_data), decompressed_length)
        return decompressed_data, decompressed_length.contents

    @staticmethod
    def save_storage_value(position: int, value: int) -> bool:
        """Save integer value to storage file (to defined position), returns true on success"""
        return _rl.SaveStorageValue(int(position), int(value))

    @staticmethod
    def load_storage_value(position: int) -> int:
        """Load integer value from storage file (from defined position)"""
        return _rl.LoadStorageValue(int(position))

    @staticmethod
    def open_url(url: str) -> None:
        """Open URL with default system browser (if available)"""
        return _rl.OpenURL(_str_in(url))

    # endregion (methods)


# region VECTORS


class Vector2(Structure):
    """Wraps raylib's Vector2 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing

    """

    _fields_ = [
        ('x', c_float),
        ('y', c_float)
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0):
        super().__init__(x, y)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict()
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC2_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector2, self).__setattr__(ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector2, self).__setattr__(attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector2':
        return Vector2(-self.x, -self.y)

    def __abs__(self) -> 'Vector2':
        return Vector2(abs(self.x), abs(self.y))

    def __round__(self, n=None) -> 'Vector2':
        return Vector2(round(self.x, n), round(self.y, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        return Vector2((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector2':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 2

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as index key.")
        return getattr(self, 'xy'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as index key.")
        setattr(self, 'xy'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self) -> Dict[str, float]:
        return {'x': self.x, 'y': self.y}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))

    def totuple(self) -> Tuple[Number, Number]:
        return (self.x, self.y)

    def tolist(self) -> List[Number]:
        return [self.x, self.y]

    # endregion (methods)


Vector2Ptr = POINTER(Vector2)


class Vector3(Structure):
    """Wraps raylib's Vector3 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0):
        super().__init__(x, y, z)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC3_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector3, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector3, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector3':
        return Vector3(-self.x, -self.y, -self.z)

    def __abs__(self) -> 'Vector3':
        return Vector3(abs(self.x), abs(self.y), abs(self.z))

    def __round__(self, n=None) -> 'Vector3':
        return Vector3(round(self.x, n), round(self.y, n), round(self.z, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]),
                       self.z + (other if is_num else other[2]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y,
                       (other if is_num else other[2]) + self.z)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]),
                       self.z - (other if is_num else other[2]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y,
                       (other if is_num else other[2]) - self.z)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        return self

    def __mul__(self, other: Union[Number, VectorN, 'Matrix']) -> 'Vector3':
        if isinstance(other, Matrix):
            return _rl.Vector3Transform(self, other)
        is_num = is_number(other)
        return Vector3(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]),
                       self.z * (other if is_num else other[2]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y,
                       (other if is_num else other[2]) * self.z)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]),
                       self.z / (other if is_num else other[2]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y,
                       (other if is_num else other[2]) / self.z)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]),
                       self.z // (other if is_num else other[2]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y,
                       (other if is_num else other[2]) // self.z)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]),
                       self.z % (other if is_num else other[2]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        return Vector3((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y,
                       (other if is_num else other[2]) % self.z)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector3':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 3

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyz'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyz'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z}
        return {'x': self.x, 'y': self.y, 'z': self.z}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number]:
        return self.x, self.y, self.z

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z]

    # endregion (methods)


Vector3Ptr = POINTER(Vector3)


class Vector4(Structure):
    """Wraps raylib's Vector4 struct.

    Extended support for:
    - string representation with str and repr;
    - attribute swizzling of x and y axes;
    - math operations (+, -, *, /, //, %, abs, negation, rounding)
    - subscript access for reading and writing
    """
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0, w: Number = 0.0):
        super().__init__(x, y, z, w)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z}, {self.w})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', float]:
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Vector4}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr or 'a' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Vector4, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Vector4, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Vector4':
        return Vector4(-self.x, -self.y, -self.z, -self.w)

    def __abs__(self) -> 'Vector4':
        return Vector4(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __round__(self, n=None) -> 'Vector4':
        return Vector4(round(self.x, n), round(self.y, n), round(self.z, n), round(self.w, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x + (other if is_num else other[0]),
                       self.y + (other if is_num else other[1]),
                       self.z + (other if is_num else other[2]),
                       self.w + (other if is_num else other[3]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) + self.x,
                       (other if is_num else other[1]) + self.y,
                       (other if is_num else other[2]) + self.z,
                       (other if is_num else other[3]) + self.w)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        self.w += other if is_num else other[3]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x - (other if is_num else other[0]),
                       self.y - (other if is_num else other[1]),
                       self.z - (other if is_num else other[2]),
                       self.w - (other if is_num else other[3]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) - self.x,
                       (other if is_num else other[1]) - self.y,
                       (other if is_num else other[2]) - self.z,
                       (other if is_num else other[3]) - self.w)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        self.w -= other if is_num else other[3]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x * (other if is_num else other[0]),
                       self.y * (other if is_num else other[1]),
                       self.z * (other if is_num else other[2]),
                       self.w * (other if is_num else other[3]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) * self.x,
                       (other if is_num else other[1]) * self.y,
                       (other if is_num else other[2]) * self.z,
                       (other if is_num else other[3]) * self.w)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        self.w *= other if is_num else other[3]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x / (other if is_num else other[0]),
                       self.y / (other if is_num else other[1]),
                       self.z / (other if is_num else other[2]),
                       self.w / (other if is_num else other[3]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) / self.x,
                       (other if is_num else other[1]) / self.y,
                       (other if is_num else other[2]) / self.z,
                       (other if is_num else other[3]) / self.w)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        self.w /= other if is_num else other[3]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x // (other if is_num else other[0]),
                       self.y // (other if is_num else other[1]),
                       self.z // (other if is_num else other[2]),
                       self.w // (other if is_num else other[3]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) // self.x,
                       (other if is_num else other[1]) // self.y,
                       (other if is_num else other[2]) // self.z,
                       (other if is_num else other[3]) // self.w)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        self.w //= other if is_num else other[3]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4(self.x % (other if is_num else other[0]),
                       self.y % (other if is_num else other[1]),
                       self.z % (other if is_num else other[2]),
                       self.w % (other if is_num else other[3]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        return Vector4((other if is_num else other[0]) % self.x,
                       (other if is_num else other[1]) % self.y,
                       (other if is_num else other[2]) % self.z,
                       (other if is_num else other[3]) % self.w)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Vector4':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        self.w %= other if is_num else other[3]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2] and self.w == other[3]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2] or self.w != other[3]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z, 'a': self.w}
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))
        self.w = float(d.get('w', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.x, self.y, self.z, self.w

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z, self.w]

    # endregion (methods)


Vector4Ptr = POINTER(Vector4)


class Quaternion(Structure):
    """Same as Vector4"""
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('z', c_float),
        ('w', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, z: Number = 0.0, w: Number = 0.0):
        super().__init__(x, y, z, w)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z}, {self.w})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.z}, {self.w})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union['Vector2', 'Vector3', 'Vector4', 'Quaternion', float]:
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: Vector2, 3: Vector3, 4: Quaternion}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: VectorN):
        m = _VEC4_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        as_color = 'r' in attr or 'g' in attr or 'b' in attr or 'a' in attr
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                super(Quaternion, self).__setattr__(_RGBA_TO_XYZW[ch] if as_color else ch, value[i])
        else:
            if not is_number(value):
                raise ValueError(f"int or float expected, got {_clsname(value)}.")
            super(Quaternion, self).__setattr__(_RGBA_TO_XYZW[attr] if as_color else attr, float(value))

    # endregion (attribute swizzling)

    # region VECTOR MATH

    def __neg__(self) -> 'Quaternion':
        return Quaternion(-self.x, -self.y, -self.z, -self.w)

    def __abs__(self) -> 'Quaternion':
        return Quaternion(abs(self.x), abs(self.y), abs(self.z), abs(self.w))

    def __round__(self, n=None) -> 'Quaternion':
        return Quaternion(round(self.x, n), round(self.y, n), round(self.z, n), round(self.w, n))

    def __add__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x + (other if is_num else other[0]),
                          self.y + (other if is_num else other[1]),
                          self.z + (other if is_num else other[2]),
                          self.w + (other if is_num else other[3]))

    def __radd__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) + self.x,
                          (other if is_num else other[1]) + self.y,
                          (other if is_num else other[2]) + self.z,
                          (other if is_num else other[3]) + self.w)

    def __iadd__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x += other if is_num else other[0]
        self.y += other if is_num else other[1]
        self.z += other if is_num else other[2]
        self.w += other if is_num else other[3]
        return self

    def __sub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x - (other if is_num else other[0]),
                          self.y - (other if is_num else other[1]),
                          self.z - (other if is_num else other[2]),
                          self.w - (other if is_num else other[3]))

    def __rsub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) - self.x,
                          (other if is_num else other[1]) - self.y,
                          (other if is_num else other[2]) - self.z,
                          (other if is_num else other[3]) - self.w)

    def __isub__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x -= other if is_num else other[0]
        self.y -= other if is_num else other[1]
        self.z -= other if is_num else other[2]
        self.w -= other if is_num else other[3]
        return self

    def __mul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x * (other if is_num else other[0]),
                          self.y * (other if is_num else other[1]),
                          self.z * (other if is_num else other[2]),
                          self.w * (other if is_num else other[3]))

    def __rmul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) * self.x,
                          (other if is_num else other[1]) * self.y,
                          (other if is_num else other[2]) * self.z,
                          (other if is_num else other[3]) * self.w)

    def __imul__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x *= other if is_num else other[0]
        self.y *= other if is_num else other[1]
        self.z *= other if is_num else other[2]
        self.w *= other if is_num else other[3]
        return self

    def __truediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x / (other if is_num else other[0]),
                          self.y / (other if is_num else other[1]),
                          self.z / (other if is_num else other[2]),
                          self.w / (other if is_num else other[3]))

    def __rtruediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) / self.x,
                          (other if is_num else other[1]) / self.y,
                          (other if is_num else other[2]) / self.z,
                          (other if is_num else other[3]) / self.w)

    def __itruediv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x /= other if is_num else other[0]
        self.y /= other if is_num else other[1]
        self.z /= other if is_num else other[2]
        self.w /= other if is_num else other[3]
        return self

    def __floordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x // (other if is_num else other[0]),
                          self.y // (other if is_num else other[1]),
                          self.z // (other if is_num else other[2]),
                          self.w // (other if is_num else other[3]))

    def __rfloordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) // self.x,
                          (other if is_num else other[1]) // self.y,
                          (other if is_num else other[2]) // self.z,
                          (other if is_num else other[3]) // self.w)

    def __ifloordiv__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x //= other if is_num else other[0]
        self.y //= other if is_num else other[1]
        self.z //= other if is_num else other[2]
        self.w //= other if is_num else other[3]
        return self

    def __mod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion(self.x % (other if is_num else other[0]),
                          self.y % (other if is_num else other[1]),
                          self.z % (other if is_num else other[2]),
                          self.w % (other if is_num else other[3]))

    def __rmod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        return Quaternion((other if is_num else other[0]) % self.x,
                          (other if is_num else other[1]) % self.y,
                          (other if is_num else other[2]) % self.z,
                          (other if is_num else other[3]) % self.w)

    def __imod__(self, other: Union[Number, VectorN]) -> 'Quaternion':
        is_num = is_number(other)
        self.x %= other if is_num else other[0]
        self.y %= other if is_num else other[1]
        self.z %= other if is_num else other[2]
        self.w %= other if is_num else other[3]
        return self

    # endregion (vector math)

    # region COMPARISSON

    def __eq__(self, other: VectorN) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.x == other[0] and self.y == other[1] and self.z == other[2] and self.w == other[3]
        return False

    def __ne__(self, other: VectorN) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.x != other[0] or self.y != other[1] or self.z != other[2] or self.w != other[3]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    def todict(self, as_color: bool = False) -> Dict[str, float]:
        if as_color:
            return {'r': self.x, 'g': self.y, 'b': self.z, 'a': self.w}
        return {'x': self.x, 'y': self.y, 'z': self.z, 'w': self.w}

    def fromdict(self, d: Dict[str, float]):
        self.x = float(d.get('x', 0.0))
        self.y = float(d.get('y', 0.0))
        self.z = float(d.get('z', 0.0))
        self.w = float(d.get('w', 0.0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.x, self.y, self.z, self.w

    def tolist(self) -> List[Number]:
        return [self.x, self.y, self.z, self.w]

    # endregion (methods)


# endregion (vectors)


class Matrix(Structure):
    _fields_ = [
        ('m0', c_float),
        ('m4', c_float),
        ('m8', c_float),
        ('m12', c_float),
        ('m1', c_float),
        ('m5', c_float),
        ('m9', c_float),
        ('m13', c_float),
        ('m2', c_float),
        ('m6', c_float),
        ('m10', c_float),
        ('m14', c_float),
        ('m3', c_float),
        ('m7', c_float),
        ('m11', c_float),
        ('m15', c_float),
    ]

    # region CLASSMETHODS

    @classmethod
    def join(cls, col1: Vec4, col2: Vec4, col3: Vec4, col4: Vec4) -> 'Matrix':
        return cls(col1.x, col2.x, col3.x, col4.x,
                   col1.y, col2.y, col3.y, col4.y,
                   col1.z, col2.z, col3.z, col4.z,
                   col1.w, col2.w, col3.w, col4.w)

    @classmethod
    def diag(cls, value: float = 1.0) -> 'Matrix':
        return cls(value, 0.0, 0.0, 0.0,
                   0.0, value, 0.0, 0.0,
                   0.0, 0.0, value, 0.0,
                   0.0, 0.0, 0.0, value)

    @staticmethod
    def identity() -> 'Matrix':
        return _rl.MatrixIdentity()

    @staticmethod
    def translate(x: float, y: float, z: float) -> 'Matrix':
        """Returns translation matrix"""
        return _rl.MatrixTranslate(x, y, z)

    @staticmethod
    def rotate(axis: Vector3, angle: float) -> 'Matrix':
        """Create rotation matrix from axis and angle

        NOTE: Angle should be provided in radians
        """
        return _rl.MatrixRotate(axis, angle)

    @staticmethod
    def rotate_x(angle: float) -> 'Matrix':
        """Returns x-rotation matrix (angle in radians)"""
        return _rl.MatrixRotateX(angle)

    @staticmethod
    def rotate_y(angle: float) -> 'Matrix':
        """Returns y-rotation matrix (angle in radians)"""
        return _rl.MatrixRotateY(angle)

    @staticmethod
    def rotate_z(angle: float) -> 'Matrix':
        """Returns z-rotation matrix (angle in radians)"""
        return _rl.MatrixRotateZ(angle)

    @staticmethod
    def rotate_xyz(ang: Vector3) -> 'Matrix':
        """Returns xyz-rotation matrix (angles in radians)"""
        return _rl.MatrixRotateXYZ(ang)

    @staticmethod
    def rotate_zyx(ang: Vector3) -> 'Matrix':
        """Returns zyx-rotation matrix (angles in radians)"""
        return _rl.MatrixRotateZYX(ang)

    @staticmethod
    def scale(x: float, y: float, z: float) -> 'Matrix':
        """Returns scaling matrix"""
        return _rl.MatrixScale(x, y, z)

    @staticmethod
    def frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> 'Matrix':
        """Returns perspective projection matrix"""
        return _rl.MatrixFrustum(left, right, bottom, top, near, far)

    @staticmethod
    def perspective(fovy: float, aspect: float, near: float, far: float) -> 'Matrix':
        """Returns perspective projection matrix

        NOTE: Angle should be provided in radians
        """
        return _rl.MatrixPerspective(fovy, aspect, near, far)

    @staticmethod
    def ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> 'Matrix':
        """Returns orthographic projection matrix"""
        return _rl.MatrixOrtho(left, right, bottom, top, near, far)

    @staticmethod
    def look_at(eye: Vector3, target: Vector3, up: Vector3) -> 'Matrix':
        """Returns camera look-at matrix (matrix: view)"""
        return _rl.MatrixLookAt(eye, target, up)

    # endregion (classmethods)

    def __init__(self,
                 m0: Number, m4: Number, m8: Number, m12: Number,
                 m1: Number, m5: Number, m9: Number, m13: Number,
                 m2: Number, m6: Number, m10: Number, m14: Number,
                 m3: Number, m7: Number, m11: Number, m15: Number):
        super().__init__(m0, m4, m8, m12,
                         m1, m5, m9, m13,
                         m2, m6, m10, m14,
                         m3, m7, m11, m15)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"\n[{self.column1}\n {self.column2}\n {self.column3}\n {self.column4}]"

    def __repr__(self) -> str:
        return (f"{_clsname(self)}("
                f"{self.m0}, {self.m1}, {self.m2}, {self.m3}, "
                f"{self.m4}, {self.m5}, {self.m6}, {self.m7}, "
                f"{self.m8}, {self.m9}, {self.m10}, {self.m11}, "
                f"{self.m12}, {self.m13}, {self.m14}, {self.m15})")

    # endregion (representation)

    # region ARITHMETIC

    def __add__(self, other: 'Matrix') -> 'Matrix':
        return _rl.MatrixAdd(self, other)

    def __sub__(self, other: 'Matrix') -> 'Matrix':
        return _rl.MatrixSubtract(self, other)

    def __mul__(self, other: Union['Matrix', Vector3]) -> Union['Matrix', Vector3]:
        if isinstance(other, Vector3):
            return _rl.Vector3Transform(other, self)
        return _rl.MatrixMultiply(self, other)

    # endregion (arithmetic)

    # region PROPERTIES

    @property
    def trace(self) -> float:
        """Returns the trace of the matrix (sum of the values along diagonal)"""
        return _rl.MatrixTrace(self)

    # region COLUMNS

    @property
    def column1(self) -> 'Quaternion':
        return Quaternion(self.m0, self.m1, self.m2, self.m3)

    @column1.setter
    def column1(self, value: Vec4):
        self.m0, self.m1, self.m2, self.m3 = value

    @property
    def column2(self) -> 'Quaternion':
        return Quaternion(self.m4, self.m5, self.m6, self.m7)

    @column2.setter
    def column2(self, value: Vec4):
        self.m4, self.m5, self.m6, self.m7 = value

    @property
    def column3(self) -> 'Quaternion':
        return Quaternion(self.m8, self.m9, self.m10, self.m11)

    @column3.setter
    def column3(self, value: Vec4):
        self.m8, self.m9, self.m10, self.m11 = value

    @property
    def column4(self) -> 'Quaternion':
        return Quaternion(self.m12, self.m13, self.m14, self.m15)

    @column4.setter
    def column4(self, value: Vec4):
        self.m12, self.m13, self.m14, self.m15 = value

    # endregion (columns)

    # region ROWS

    @property
    def row1(self) -> 'Quaternion':
        return Quaternion(self.m0, self.m4, self.m8, self.m12)

    @row1.setter
    def row1(self, value: Vec4):
        self.m0, self.m4, self.m8, self.m12 = value

    @property
    def row2(self) -> 'Quaternion':
        return Quaternion(self.m1, self.m5, self.m9, self.m13)

    @row2.setter
    def row2(self, value: Vec4):
        self.m1, self.m5, self.m9, self.m13 = value

    @property
    def row3(self) -> 'Quaternion':
        return Quaternion(self.m2, self.m6, self.m10, self.m14)

    @row3.setter
    def row3(self, value: Vec4):
        self.m2, self.m6, self.m10, self.m14 = value

    @property
    def row4(self) -> 'Quaternion':
        return Quaternion(self.m3, self.m7, self.m11, self.m15)

    @row4.setter
    def row4(self, value: Vec4):
        self.m3, self.m7, self.m11, self.m15 = value

    # endregion (rows)

    # endregion (properties)

    # region METHODS

    def determinant(self) -> float:
        """Compute matrix determinant"""
        return _rl.MatrixDeterminant(self)

    def transpose(self) -> 'Matrix':
        """Transposes provided matrix"""
        return _rl.MatrixTranspose(self)

    def invert(self) -> 'Matrix':
        """Invert provided matrix"""
        return _rl.MatrixInvert(self)

    def normalize(self) -> 'Matrix':
        """Normalize provided matrix"""
        return _rl.MatrixNormalize(self)

    # endregion (methos)


MatrixPtr = POINTER(Matrix)


class Color(Structure):
    _fields_ = [
        ('r', c_ubyte),
        ('g', c_ubyte),
        ('b', c_ubyte),
        ('a', c_ubyte),
    ]

    def __init__(self, r: int = 0, g: int = 0, b: int = 0, a: int = 0):
        super().__init__(r, g, b, a)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.r}, {self.g}, {self.b}, {self.a})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.r}, {self.g}, {self.b}, {self.a})"

    # endregion (representation)

    # region ATTRIBUTE SWIZZLING

    def __getattr__(self, attr: str) -> Union[int, Tuple[int, int], Tuple[int, int, int], 'Color']:
        m = _RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        cls: type = {1: float, 2: tuple, 3: tuple, 4: Color}.get(len(attr))
        v = self.todict('r' in attr or 'g' in attr or 'b' in attr or 'a' in attr)
        return cls(*(v[ch] for ch in attr))

    def __setattr__(self, attr: str, value: RGBA):
        m = _RGBA_GET_SWZL.fullmatch(attr)
        if not m:
            raise AttributeError(f"{_clsname(self)} object does not have attribute '{attr}'.")
        n2 = len(attr)
        if n2 > 1:
            n = len(value)
            if n != n2:
                raise ValueError(f"Too {'many' if n > n2 else 'few'} values to assign (expected {n2}).")
            for i, ch in enumerate(attr):
                if not is_component(value[i]):
                    raise ValueError(f"int expected in 0..255 range, got {_clsname(value[i])} ({value[i]}).")
                super(Color, self).__setattr__(ch, value[i])
        else:
            if not is_component(value):
                raise ValueError(f"int expected in 0..255 range, got {_clsname(value)} ({value}).")
            super(Color, self).__setattr__(attr, value)

    # endregion (attribute swizzling)

    # region COLOR MATH

    def __neg__(self, other: Union[int, RGBA]) -> 'Color':
        return Color(255 - self.r, 255 - self.g, 255 - self.b, self.a)

    def __add__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r + (other if is_num else other[0]),
                                  self.g + (other if is_num else other[1]),
                                  self.b + (other if is_num else other[2]),
                                  self.a))

    def __radd__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) + self.r,
                                  (other if is_num else other[1]) + self.g,
                                  (other if is_num else other[2]) + self.b,
                                  self.a))

    def __iadd__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r + (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g + (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b + (other if is_num else other[2]))
        return self

    def __sub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r - (other if is_num else other[0]),
                                  self.g - (other if is_num else other[1]),
                                  self.b - (other if is_num else other[2]),
                                  self.a))

    def __rsub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) - self.r,
                                  (other if is_num else other[1]) - self.g,
                                  (other if is_num else other[2]) - self.b,
                                  self.a))

    def __isub__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r - (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g - (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b - (other if is_num else other[2]))
        return self

    def __and__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r & (other if is_num else other[0]),
                                  self.g & (other if is_num else other[1]),
                                  self.b & (other if is_num else other[2]),
                                  self.a))

    def __rand__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) & self.r,
                                  (other if is_num else other[1]) & self.g,
                                  (other if is_num else other[2]) & self.b,
                                  self.a))

    def __iand__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r & (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g & (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b & (other if is_num else other[2]))
        return self

    def __or__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r | (other if is_num else other[0]),
                                  self.g | (other if is_num else other[1]),
                                  self.b | (other if is_num else other[2]),
                                  self.a))

    def __ror__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) | self.r,
                                  (other if is_num else other[1]) | self.g,
                                  (other if is_num else other[2]) | self.b,
                                  self.a))

    def __ior__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r | (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g | (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b | (other if is_num else other[2]))
        return self

    def __xor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba(self.r ^ (other if is_num else other[0]),
                                  self.g ^ (other if is_num else other[1]),
                                  self.b ^ (other if is_num else other[2]),
                                  self.a))

    def __rxor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        return Color(*_clamp_rgba((other if is_num else other[0]) ^ self.r,
                                  (other if is_num else other[1]) ^ self.g,
                                  (other if is_num else other[2]) ^ self.b,
                                  self.a))

    def __ixor__(self, other: Union[int, RGBA]) -> 'Color':
        is_num = is_number(other)
        self.r = _clamp_rgba(self.r ^ (other if is_num else other[0]))
        self.g = _clamp_rgba(self.g ^ (other if is_num else other[1]))
        self.b = _clamp_rgba(self.b ^ (other if is_num else other[2]))
        return self

    # endregion (color math)

    # region COMPARISSON

    def __eq__(self, other: RGBA) -> bool:
        if is_number(other):
            return False
        if len(other) == len(self):
            return self.r == other[0] and self.g == other[1] and self.b == other[2]
        return False

    def __ne__(self, other: RGBA) -> bool:
        if is_number(other):
            return True
        if len(other) == len(self):
            return self.r != other[0] or self.g != other[1] or self.b != other[2]
        return True

    # endregion (comparisson)

    # region CONTAINER SUPPORT

    def __len__(self) -> int:
        return 4

    def __getitem__(self, key: int) -> float:
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        return getattr(self, 'xyzw'[key])

    def __setitem__(self, key: int, value: Number):
        if not isinstance(key, int):
            raise KeyError(f"{_clsname(key)} is not supported as element index.")
        setattr(self, 'xyzw'[key], value)

    # endregion (container support)

    # region METHODS

    # region UTILS

    def todict(self) -> Dict[str, int]:
        return {'r': self.r, 'g': self.g, 'b': self.b, 'a': self.a}

    def fromdict(self, d: Dict[str, int]):
        self.r = int(d.get('r', 0))
        self.g = int(d.get('g', 0))
        self.b = int(d.get('b', 0))
        self.a = int(d.get('a', 0))

    def totuple(self) -> Tuple[Number, Number, Number, Number]:
        return self.r, self.g, self.b, self.a

    def tolist(self) -> List[Number]:
        return [self.r, self.g, self.b, self.a]

    # endregion (utils)

    # region COLORSPACE CONVERSION

    def fade(self, alpha: float) -> 'Color':
        """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _rl.Fade(self, float(alpha))

    def to_int(self) -> int:
        """Returns hexadecimal value for a Color"""
        return _rl.ColorToInt(self)

    def normalize(self) -> Vector4:
        """Returns Color normalized as float [0..1]"""
        return _rl.ColorNormalize(self)

    @staticmethod
    def from_normalized(normalized: AnyVec4):
        """Returns Color from normalized values [0..1]"""
        return _rl.ColorFromNormalized(_vec4(normalized))

    def to_hsv(self) -> Vector3:
        """Returns HSV values for a Color, hue [0..360], saturation/value [0..1]"""
        return _rl.ColorToHSV(self)

    @staticmethod
    def from_hsv(hue: float, saturation: float, value: float) -> 'Color':
        """Returns a Color from HSV values, hue [0..360], saturation/value [0..1]"""
        return _rl.ColorFromHSV(float(hue), float(saturation), float(value))

    def color_alpha(self, alpha: float) -> 'Color':
        """Returns color with alpha applied, alpha goes from 0.0f to 1.0f"""
        return _rl.ColorAlpha(self, float(alpha))

    @staticmethod
    def color_alpha_blend(dst: AnyRGB, src: AnyRGB, tint: AnyRGB) -> 'Color':
        """Returns src alpha-blended into dst color with tint"""
        return _rl.ColorAlphaBlend(_color(dst), _color(src), _color(tint))

    @staticmethod
    def get_color(hex_value: int) -> 'Color':
        """Get Color structure from hexadecimal value"""
        return _rl.GetColor(int(hex_value))

    # endregion (colorspace conversion)

    # endregion (methods)


ColorPtr = POINTER(Color)


class Rectangle(Structure):
    _fields_ = [
        ('x', c_float),
        ('y', c_float),
        ('width', c_float),
        ('height', c_float),
    ]

    def __init__(self, x: Number = 0.0, y: Number = 0.0, width: Number = 0.0, height: Number = 0.0):
        super().__init__(x, y, width, height)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.width}, {self.height})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.x}, {self.y}, {self.width}, {self.height})"

    # endregion

    # region PROPERTIES

    @property
    def left(self) -> float:
        return self.x

    @left.setter
    def left(self, value: Number):
        self.x = value

    @property
    def top(self) -> float:
        return self.y

    @top.setter
    def top(self, value: Number):
        self.y = value

    @property
    def right(self) -> float:
        return self.x + self.width

    @right.setter
    def right(self, value: Number):
        self.x = value - self.width

    @property
    def bottom(self) -> float:
        return self.y - self.height

    @bottom.setter
    def bottom(self, value: Number):
        self.y = value + self.height

    # endregion (properties)


RectanglePtr = POINTER(Rectangle)
RectanglePtrPtr = POINTER(RectanglePtr)


class Image(Structure):
    _fields_ = [
        ('data', c_void_p),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Image':
        """Load image from file into CPU memory (RAM)"""
        return _rl.LoadImage(_str_in(file_name))

    @staticmethod
    def load_raw(file_name: str, width: int, height: int, format_: int, header_size: int) -> 'Image':
        """Load image from RAW file data"""
        return _rl.LoadImageRaw(_str_in(file_name), int(width), int(height), int(format_), int(header_size))

    @staticmethod
    def load_anim(file_name: str) -> Tuple['Image', int]:
        """Load image sequence from file (frames appended to image.data)"""
        frames = IntPtr(0)
        image = _rl.LoadImageAnim(_str_in(file_name), frames)
        return image, frames.contents

    @staticmethod
    def load_from_memory(file_type: str, file_data: bytes, data_size: int) -> 'Image':
        """Load image from memory buffer, fileType refers to extension: i.e. ".png"."""
        return _rl.LoadImageFromMemory(_str_in(file_type), file_data, int(data_size))

    @staticmethod
    def get_screen_data() -> 'Image':
        """Get pixel data from screen buffer and return an Image (screenshot)"""
        return _rl.GetScreenData()

    @staticmethod
    def gen_plain_color(width: int, height: int, color: AnyRGB) -> 'Image':
        """Generate image: plain color"""
        return _rl.GenImageColor(int(width), int(height), _color(color))

    @staticmethod
    def gen_gradient_v(width: int, height: int, top: AnyRGB, bottom: AnyRGB) -> 'Image':
        """Generate image: vertical gradient"""
        return _rl.GenImageGradientV(int(width), int(height), _color(top), _color(bottom))

    @staticmethod
    def gen_gradient_h(width: int, height: int, left: AnyRGB, right: AnyRGB) -> 'Image':
        """Generate image: horizontal gradient"""
        return _rl.GenImageGradientH(int(width), int(height), _color(left), _color(right))

    @staticmethod
    def gen_gradient_radial(width: int, height: int, density: float, inner: AnyRGB, outer: AnyRGB) -> 'Image':
        """Generate image: radial gradient"""
        return _rl.GenImageGradientRadial(int(width), int(height), float(density), _color(inner), _color(outer))

    @staticmethod
    def gen_checked(width: int, height: int, checks_x: int, checks_y: int, col1: AnyRGB, col2: AnyRGB) -> 'Image':
        """Generate image: checked"""
        return _rl.GenImageChecked(int(width), int(height), int(checks_x), int(checks_y), _color(col1), _color(col2))

    @staticmethod
    def gen_white_noise(width: int, height: int, factor: float) -> 'Image':
        """Generate image: white noise"""
        return _rl.GenImageWhiteNoise(int(width), int(height), float(factor))

    @staticmethod
    def gen_perlin_noise(width: int, height: int, offset_x: int, offset_y: int, scale: float) -> 'Image':
        """Generate image: perlin noise"""
        return _rl.GenImagePerlinNoise(int(width), int(height), int(offset_x), int(offset_y), float(scale))

    @staticmethod
    def gen_cellular(width: int, height: int, tile_size: int) -> 'Image':
        """Generate image: cellular algorithm. Bigger tileSize means bigger cells"""
        return _rl.GenImageCellular(int(width), int(height), int(tile_size))

    @staticmethod
    def from_image(image: 'Image', rec: AnyRect) -> 'Image':
        """Create an image from another image piece"""
        return _rl.ImageFromImage(image, _rect(rec))

    @staticmethod
    def text(text: str, font_size: int, color: AnyRGB) -> 'Image':
        """Create an image from text (default font)"""
        return _rl.ImageText(_str_in(text), int(font_size), _color(color))

    @staticmethod
    def text_ex(font: 'Font', text: str, font_size: float, spacing: float, tint: AnyRGB) -> 'Image':
        """Create an image from text (custom sprite font)"""
        return _rl.ImageTextEx(font, _str_in(text), float(font_size), float(spacing), _color(tint))

    # endregion (classmethods)

    def __init__(self, data: VoidPtr, width: int, height: int, mipmaps: int, format_: int):
        super().__init__(data, width, height, mipmaps, format_)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.data}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.data}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    # endregion

    # region NO REFS

    def __del__(self) -> None:
        """Unload image from CPU memory (RAM)"""
        return _rl.UnloadImage(self)

    # endregion (no refs)

    # region METHODS

    def copy(self) -> 'Image':
        """Create an image duplicate (useful for transformations)"""
        return _rl.ImageCopy(self)

    def export_image(self, file_name: str) -> bool:
        """Export image data to file, returns true on success"""
        return _rl.ExportImage(self, _str_in(file_name))

    def export_image_as_code(self, file_name: str) -> bool:
        """Export image as code file defining an array of bytes, returns true on success"""
        return _rl.ExportImageAsCode(self, _str_in(file_name))

    # region MANIPULATION

    def format(self, new_format: int) -> None:
        """Convert image data to desired format"""
        return _rl.ImageFormat(byref(self), int(new_format))

    def to_pot(self, fill: AnyRGB) -> None:
        """Convert image to POT (power-of-two)"""
        return _rl.ImageToPOT(byref(self), _color(fill))

    def crop(self, crop: AnyRect) -> None:
        """Crop an image to a defined rectangle"""
        return _rl.ImageCrop(byref(self), _rect(crop))

    def alpha_crop(self, threshold: float) -> None:
        """Crop image depending on alpha value"""
        return _rl.ImageAlphaCrop(byref(self), float(threshold))

    def alpha_clear(self, color: AnyRGB, threshold: float) -> None:
        """Clear alpha channel to desired color"""
        return _rl.ImageAlphaClear(byref(self), _color(color), float(threshold))

    def alpha_mask(self, alpha_mask: 'Image') -> None:
        """Apply alpha mask to image"""
        return _rl.ImageAlphaMask(byref(self), alpha_mask)

    def alpha_premultiply(self) -> None:
        """Premultiply alpha channel"""
        return _rl.ImageAlphaPremultiply(byref(self))

    def resize(self, new_width: int, new_height: int) -> None:
        """Resize image (Bicubic scaling algorithm)"""
        return _rl.ImageResize(byref(self), int(new_width), int(new_height))

    def resize_nn(self, new_width: int, new_height: int) -> None:
        """Resize image (Nearest-Neighbor scaling algorithm)"""
        return _rl.ImageResizeNN(byref(self), int(new_width), int(new_height))

    def resize_canvas(self, new_width: int, new_height: int, offset_x: int, offset_y: int,
                      fill: AnyRGB) -> None:
        """Resize canvas and fill with color"""
        return _rl.ImageResizeCanvas(byref(self), int(new_width), int(new_height), int(offset_x), int(offset_y),
                                     _color(fill))

    def mipmaps(self) -> None:
        """Generate all mipmap levels for a provided image"""
        return _rl.ImageMipmaps(byref(self))

    def dither(self, r_bpp: int, g_bpp: int, b_bpp: int, a_bpp: int) -> None:
        """Dither image data to 16bpp or lower (Floyd-Steinberg dithering)"""
        return _rl.ImageDither(byref(self), int(r_bpp), int(g_bpp), int(b_bpp), int(a_bpp))

    def flip_vertical(self) -> None:
        """Flip image vertically"""
        return _rl.ImageFlipVertical(byref(self))

    def flip_horizontal(self) -> None:
        """Flip image horizontally"""
        return _rl.ImageFlipHorizontal(byref(self))

    def rotate_cw(self) -> None:
        """Rotate image clockwise 90deg"""
        return _rl.ImageRotateCW(byref(self))

    def rotate_ccw(self) -> None:
        """Rotate image counter-clockwise 90deg"""
        return _rl.ImageRotateCCW(byref(self))

    def color_tint(self, color: AnyRGB) -> None:
        """Modify image color: tint"""
        return _rl.ImageColorTint(byref(self), _color(color))

    def color_invert(self) -> None:
        """Modify image color: invert"""
        return _rl.ImageColorInvert(byref(self))

    def color_grayscale(self) -> None:
        """Modify image color: grayscale"""
        return _rl.ImageColorGrayscale(byref(self))

    def color_contrast(self, contrast: float) -> None:
        """Modify image color: contrast (-100 to 100)"""
        return _rl.ImageColorContrast(byref(self), float(contrast))

    def color_brightness(self, brightness: int) -> None:
        """Modify image color: brightness (-255 to 255)"""
        return _rl.ImageColorBrightness(byref(self), int(brightness))

    def color_replace(self, color: AnyRGB, replace: AnyRGB) -> None:
        """Modify image color: replace color"""
        return _rl.ImageColorReplace(byref(self), _color(color), _color(replace))

    def load_colors(self) -> Sequence[Color]:
        """Load color data from image as a Color array (RGBA - 32bit)"""
        result = _rl.LoadImageColors(self)
        colors = []
        i = 0
        while result[i] is not None:
            colors.append(result[i])
        return tuple(colors)

    def load_palette(self, max_palette_size: int) -> Sequence[Color]:
        """Load colors palette from image as a Color array (RGBA - 32bit)"""
        colors_count = IntPtr(0)
        result = _rl.LoadImagePalette(self, int(max_palette_size), colors_count)
        colors = [color for color in result[:colors_count.contents[0]]]
        return tuple(colors)

    @staticmethod
    def unload_colors(colors: Sequence[Color]) -> None:
        """Unload color data loaded with LoadImageColors()"""
        return _rl.UnloadImageColors(_arr(Color, colors))

    @staticmethod
    def unload_palette(colors: Sequence[Color]) -> None:
        """Unload colors palette loaded with LoadImagePalette()"""
        return _rl.UnloadImagePalette(_arr(Color, colors))

    def get_alpha_border(self, threshold: float) -> Rectangle:
        """Get image alpha border rectangle"""
        return _rl.GetImageAlphaBorder(self, float(threshold))

    # endregion (manipulation)

    # region DRAWING

    def clear_background(self, color: AnyRGB) -> None:
        """Clear image background with given color"""
        return _rl.ImageClearBackground(byref(self), _color(color))

    def draw_pixel(self, pos_x: int, pos_y: int, color: AnyRGB) -> None:
        """Draw pixel within an image"""
        return _rl.ImageDrawPixel(byref(self), int(pos_x), int(pos_y), _color(color))

    def draw_pixel_v(self, position: AnyVec2, color: AnyRGB) -> None:
        """Draw pixel within an image (Vector version)"""
        return _rl.ImageDrawPixelV(byref(self), _vec2(position), _color(color))

    def draw_line(self, start_pos_x: int, start_pos_y: int, end_pos_x: int, end_pos_y: int, color: AnyRGB) -> None:
        """Draw line within an image"""
        return _rl.ImageDrawLine(byref(self), int(start_pos_x), int(start_pos_y), int(end_pos_x), int(end_pos_y),
                                 _color(color))

    def draw_line_v(self, start: AnyVec2, end: AnyVec2, color: AnyRGB) -> None:
        """Draw line within an image (Vector version)"""
        return _rl.ImageDrawLineV(byref(self), _vec2(start), _vec2(end), _color(color))

    def draw_circle(self, center_x: int, center_y: int, radius: int, color: AnyRGB) -> None:
        """Draw circle within an image"""
        return _rl.ImageDrawCircle(byref(self), int(center_x), int(center_y), int(radius), _color(color))

    def draw_circle_v(self, center: AnyVec2, radius: int, color: AnyRGB) -> None:
        """Draw circle within an image (Vector version)"""
        return _rl.ImageDrawCircleV(byref(self), _vec2(center), int(radius), _color(color))

    def draw_rectangle(self, pos_x: int, pos_y: int, width: int, height: int, color: AnyRGB) -> None:
        """Draw rectangle within an image"""
        return _rl.ImageDrawRectangle(byref(self), int(pos_x), int(pos_y), int(width), int(height), _color(color))

    def draw_rectangle_v(self, position: AnyVec2, size: AnyVec2, color: AnyRGB) -> None:
        """Draw rectangle within an image (Vector version)"""
        return _rl.ImageDrawRectangleV(byref(self), _vec2(position), _vec2(size), _color(color))

    def draw_rectangle_rec(self, rec: AnyRect, color: AnyRGB) -> None:
        """Draw rectangle within an image"""
        return _rl.ImageDrawRectangleRec(byref(self), _rect(rec), _color(color))

    def draw_rectangle_lines(self, rec: AnyRect, thick: int, color: AnyRGB) -> None:
        """Draw rectangle lines within an image"""
        return _rl.ImageDrawRectangleLines(byref(self), _rect(rec), int(thick), _color(color))

    def draw_image(self, src: 'Image', src_rec: AnyRect, dst_rec: AnyRect, tint: AnyRGB) -> None:
        """Draw a source image within a destination image (tint applied to source)"""
        return _rl.ImageDraw(byref(self), src, _rect(src_rec), _rect(dst_rec), _color(tint))

    def draw_text(self, text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
        """Draw text (using default font) within an image (destination)"""
        return _rl.ImageDrawText(byref(self), _str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    def draw_text_ex(self, font: 'Font', text: str, position: AnyVec2, font_size: float, spacing: float,
                     tint: AnyRGB) -> None:
        """Draw text (custom sprite font) within an image (destination)"""
        return _rl.ImageDrawTextEx(byref(self), font, _str_in(text), _vec2(position), float(font_size), float(spacing),
                                   _color(tint))

    # endregion (drawing)

    # endregion (methods)


ImagePtr = POINTER(Image)


class Texture(Structure):
    _fields_ = [
        ('id', c_uint),
        ('width', c_int),
        ('height', c_int),
        ('mipmaps', c_int),
        ('format', c_int),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Texture2D':
        """Load texture from file into GPU memory (VRAM)"""
        return _rl.LoadTexture(_str_in(file_name))

    @staticmethod
    def load_from_image(image: Image) -> 'Texture2D':
        """Load texture from image data"""
        return _rl.LoadTextureFromImage(image)

    @staticmethod
    def load_cubemap(image: Image, layout: int) -> 'TextureCubemap':
        """Load cubemap from image, multiple image cubemap layouts supported"""
        return _rl.LoadTextureCubemap(image, int(layout))

    # endregion

    def __init__(self, id: int, width: int, height: int, mipmaps: int, format_: int):
        super().__init__(id, width, height, mipmaps, format_)

    def __del__(self):
        _rl.UnloadTexture(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.width}, {self.height}, {self.mipmaps}, {self.format})"

    # endregion

    # region METHODS

    def update_texture(self, pixels: bytes) -> None:
        """Update GPU texture with new data"""
        _rl.UpdateTexture(self, pixels)

    def update_texture_rec(self, rec: AnyRect, pixels: bytes) -> None:
        """Update GPU texture rectangle with new data"""
        _rl.UpdateTextureRec(self, _rect(rec), pixels)

    def get_texture_data(self) -> 'Image':
        """Get pixel data from GPU texture and return an Image"""
        return _rl.GetTextureData(self)

    def gen_texture_mipmaps(self) -> None:
        """Generate GPU mipmaps for a texture"""
        return _rl.GenTextureMipmaps(byref(self))

    def set_texture_filter(self, filter_: int) -> None:
        """Set texture scaling filter mode"""
        return _rl.SetTextureFilter(self, int(filter_))

    def set_texture_wrap(self, wrap: int) -> None:
        """Set texture wrapping mode"""
        return _rl.SetTextureWrap(self, int(wrap))

    # region DRAWING

    def draw_texture(self, pos_x: int, pos_y: int, tint: AnyRGB) -> None:
        """Draw a Texture2D"""
        return _rl.DrawTexture(self, int(pos_x), int(pos_y), _color(tint))

    def draw_texture_v(self, position: AnyVec2, tint: AnyRGB) -> None:
        """Draw a Texture2D with position defined as Vector2"""
        return _rl.DrawTextureV(self, _vec2(position), _color(tint))

    def draw_texture_ex(self, position: AnyVec2, rotation: float, scale: float, tint: AnyRGB) -> None:
        """Draw a Texture2D with extended parameters"""
        return _rl.DrawTextureEx(self, _vec2(position), float(rotation), float(scale), _color(tint))

    def draw_texture_rec(self, source: AnyRect, position: AnyVec2, tint: AnyRGB) -> None:
        """Draw a part of a texture defined by a rectangle"""
        return _rl.DrawTextureRec(self, _rect(source), _vec2(position), _color(tint))

    def draw_texture_quad(self, tiling: AnyVec2, offset: AnyVec2, quad: AnyRect, tint: AnyRGB) -> None:
        """Draw texture quad with tiling and offset parameters"""
        return _rl.DrawTextureQuad(self, _vec2(tiling), _vec2(offset), _rect(quad), _color(tint))

    def draw_texture_tiled(self, source: AnyRect, dest: AnyRect, origin: AnyVec2, rotation: float,
                           scale: float, tint: AnyRGB) -> None:
        """Draw part of a texture (defined by a rectangle) with rotation and scale tiled into dest."""
        return _rl.DrawTextureTiled(self, _rect(source), _rect(dest), _vec2(origin), float(rotation), float(scale),
                                    _color(tint))

    def draw_texture_pro(self, source: AnyRect, dest: AnyRect, origin: AnyVec2, rotation: float,
                         tint: AnyRGB) -> None:
        """Draw a part of a texture defined by a rectangle with 'pro' parameters"""
        return _rl.DrawTexturePro(self, _rect(source), _rect(dest), _vec2(origin), float(rotation), _color(tint))

    def draw_texture_npatch(self, n_patch_info: 'NPatchInfo', dest: AnyRect, origin: AnyVec2,
                            rotation: float,
                            tint: AnyRGB) -> None:
        """Draws a texture (or part of it) that stretches or shrinks nicely"""
        return _rl.DrawTextureNPatch(self, n_patch_info, _rect(dest), _vec2(origin), float(rotation), _color(tint))

    def draw_texture_poly(self, center: AnyVec2, points: Sequence[Vector2], texcoords: Sequence[Vector2],
                          points_count: int, tint: AnyRGB) -> None:
        """Draw a textured polygon"""
        return _rl.DrawTexturePoly(self, _vec2(center), _arr(Vector2, points), _arr(Vector2, texcoords),
                                   int(points_count), _color(tint))

    # endregion (drawing)

    # endregion (methods)


TextureCubemap = Texture
Texture2D = Texture
Texture2DPtr = POINTER(Texture2D)


class RenderTexture2D(Structure):
    _fields_ = [
        ('id', c_uint),
        ('texture', Texture2D),
        ('depth', Texture2D),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load_render_texture(width: int, height: int) -> 'RenderTexture2D':
        """Load texture for rendering (framebuffer)"""
        return _rl.LoadRenderTexture(int(width), int(height))

    # endregion (classmethods)

    def __init__(self, id: int, texture: Texture2D, depth: Texture2D):
        super().__init__(id, texture, depth)

    def __del__(self):
        _rl.UnloadRenderTexture(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.texture}, {self.depth})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.texture}, {self.depth})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginTextureMode(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndTextureMode()

    # endregion (context)


RenderTexture = RenderTexture2D


class NPatchInfo(Structure):
    _fields_ = [
        ('source', Rectangle),
        ('left', c_int),
        ('top', c_int),
        ('right', c_int),
        ('bottom', c_int),
        ('layout', c_int),
    ]

    def __init__(self, source: Rectangle, left: int, top: int, right: int, bottom: int, layout: int):
        super().__init__(source, left, top, right, bottom, layout)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.source}, {self.left}, {self.top}, {self.right}, {self.bottom}, {self.layout})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.source}, {self.left}, {self.top}, {self.right}, {self.bottom}, {self.layout})"

    # endregion


class CharInfo(Structure):
    _fields_ = [
        ('value', c_int),
        ('offsetX', c_int),
        ('offsetY', c_int),
        ('advanceX', c_int),
        ('image', Image),
    ]

    def __init__(self, value: int, offset_x: int, offset_y: int, advance_x: int, image: Image):
        super().__init__(value, offset_x, offset_y, advance_x, image)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.value}, {self.offsetX}, {self.offsetY}, {self.advanceX}, {self.image})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.value}, {self.offsetX}, {self.offsetY}, {self.advanceX}, {self.image})"

    # endregion


CharInfoPtr = POINTER(CharInfo)


class Font(Structure):
    _fields_ = [
        ('baseSize', c_int),
        ('charsCount', c_int),
        ('charsPadding', c_int),
        ('texture', Texture2D),
        ('recs', POINTER(Rectangle)),
        ('chars', POINTER(CharInfo)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def get_default() -> 'Font':
        """Get the default Font"""
        return _rl.GetFontDefault()

    @staticmethod
    def load(file_name: str) -> 'Font':
        """Load font from file into GPU memory (VRAM)"""
        return _rl.LoadFont(_str_in(file_name))

    @staticmethod
    def load_ex(file_name: str, font_size: int, font_chars: str) -> 'Font':
        """Load font from file with extended parameters"""
        chars_count = [ord(ch) for ch in font_chars]
        chars = _arr(Int, chars_count)
        return _rl.LoadFontEx(_str_in(file_name), int(font_size), chars, chars_count)

    @staticmethod
    def load_from_image(image: Image, key: AnyRGB, first_char: int) -> 'Font':
        """Load font from Image (XNA style)"""
        return _rl.LoadFontFromImage(image, _color(key), int(first_char))

    @staticmethod
    def load_from_memory(file_type: str, file_data: bytes, font_size: int, font_chars: str) -> 'Font':
        """Load font from memory buffer, fileType refers to extension: i.e. ".ttf"."""
        chars_count = [ord(ch) for ch in font_chars]
        chars = _arr(Int, chars_count)
        return _rl.LoadFontFromMemory(_str_in(file_type), file_data, len(file_data), int(font_size), chars, chars_count)

    # endregion (classmethos)

    def __init__(self, base_size: int, chars_count: int, chars_padding: int, texture: int, image: Image,
                 recs: Sequence[Rectangle], chars: Sequence[CharInfo]):
        super().__init__(base_size, chars_count, chars_padding, texture, image, recs, chars)
        self._font_data: Optional[CharInfoPtr] = None
        self._chars_count: int = -1

    def __del__(self):
        return _rl.UnloadFont(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return (f"({self.baseSize}, {self.charsCount}, {self.charsPadding}, {self.texture}, {self.image}, {self.recs},"
                f" {self.chars})")

    def __repr__(self) -> str:
        return (f"{_clsname(self)}({self.baseSize}, {self.charsCount}, {self.charsPadding}, {self.texture},"
                f" {self.image}, {self.recs}, {self.chars})")

    # endregion

    # region METHODS

    def load_data(self, file_data: bytes, data_size: int, font_size: int, font_chars: str, type_: int) -> None:
        """Load font data for further use"""
        if self._font_data is None:
            chars_count = [ord(ch) for ch in font_chars]
            chars = _arr(Int, chars_count)
            self._chars_count = len(chars_count)
            self._font_data = _rl.LoadFontData(file_data, int(data_size), int(font_size), chars, self._chars_count,
                                               int(type_))

    def unload_data(self) -> None:
        """Unload font chars info data (RAM)"""
        if self._font_data is not None:
            _rl.UnloadFontData(self._font_data, self._chars_count)

    @staticmethod
    def gen_image_font_atlas(chars: Sequence[CharInfo], recs: Sequence[Sequence[Rectangle]], chars_count: int,
                             font_size: int, padding: int, pack_method: int) -> Image:
        """Generate image font atlas using chars info"""
        return _rl.GenImageFontAtlas(_arr(CharInfo, chars), _arr2(Rectangle, recs), int(chars_count), int(font_size),
                                     int(padding), int(pack_method))

    @staticmethod
    def draw_fps(pos_x: int, pos_y: int) -> None:
        """Draw current FPS"""
        return _rl.DrawFPS(int(pos_x), int(pos_y))

    @staticmethod
    def draw_text(text: str, pos_x: int, pos_y: int, font_size: int, color: AnyRGB) -> None:
        """Draw text (using default font)"""
        return _rl.DrawText(_str_in(text), int(pos_x), int(pos_y), int(font_size), _color(color))

    def draw_text_ex(self, text: str, position: AnyVec2, font_size: float, spacing: float, tint: AnyRGB) -> None:
        """Draw text using font and additional parameters"""
        return _rl.DrawTextEx(self, _str_in(text), _vec2(position), float(font_size), float(spacing), _color(tint))

    def draw_text_rec(self, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                      tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits"""
        return _rl.DrawTextRec(self, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                               _color(tint))

    def draw_text_rec_ex(self, text: str, rec: AnyRect, font_size: float, spacing: float, word_wrap: bool,
                         tint: AnyRGB, select_start: int, select_length: int, select_tint: AnyRGB,
                         select_back_tint: AnyRGB) -> None:
        """Draw text using font inside rectangle limits with support for text selection"""
        return _rl.DrawTextRecEx(self, _str_in(text), _rect(rec), float(font_size), float(spacing), bool(word_wrap),
                                 _color(tint), int(select_start), int(select_length), _color(select_tint),
                                 _color(select_back_tint))

    def draw_text_codepoint(self, codepoint: int, position: AnyVec2, font_size: float, tint: AnyRGB) -> None:
        """Draw one character (codepoint)"""
        return _rl.DrawTextCodepoint(self, int(codepoint), _vec2(position), float(font_size), _color(tint))

    @staticmethod
    def measure_text(text: str, font_size: int) -> int:
        """Measure string width for default font"""
        return _rl.MeasureText(_str_in(text), int(font_size))

    def measure_text_ex(self, text: str, font_size: float, spacing: float) -> Vector2:
        """Measure string size for Font"""
        return _rl.MeasureTextEx(self, _str_in(text), float(font_size), float(spacing))

    def get_glyph_index(self, codepoint: int) -> int:
        """Get index position for a unicode character on font"""
        return _rl.GetGlyphIndex(self, int(codepoint))

    # endregion (methods)


SpriteFont = Font


# region CAMERAS


class Camera3D(Structure):
    _fields_ = [
        ('position', Vector3),
        ('target', Vector3),
        ('up', Vector3),
        ('fovy', c_float),
        ('projection', c_int),
    ]

    # region CLASSMETHODS

    @staticmethod
    def set_pan_control(key_pan: int) -> None:
        """Set camera pan key to combine with mouse movement (free camera)"""
        return _rl.SetCameraPanControl(int(key_pan))

    @staticmethod
    def set_alt_control(key_alt: int) -> None:
        """Set camera alt key to combine with mouse movement (free camera)"""
        return _rl.SetCameraAltControl(int(key_alt))

    @staticmethod
    def set_smooth_zoom_control(key_smooth_zoom: int) -> None:
        """Set camera smooth zoom key to combine with mouse (free camera)"""
        return _rl.SetCameraSmoothZoomControl(int(key_smooth_zoom))

    @staticmethod
    def set_move_controls(key_front: int, key_back: int, key_right: int, key_left: int, key_up: int,
                          key_down: int) -> None:
        """Set camera move controls (1st person and 3rd person cameras)"""
        return _rl.SetCameraMoveControls(int(key_front), int(key_back), int(key_right), int(key_left),
                                         int(key_up), int(key_down))

    # endregion (classmethods)

    def __init__(self, position: Optional[Vector3] = None, target: Optional[Vector3] = None,
                 up: Optional[Vector3] = None, fovy: float = 0.0, projection: int = 0):
        super().__init__(position if position else Vector3(), target if target else Vector3(),
                         up if up else Vector3(), fovy, projection)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.position}, {self.target}, {self.up}, {self.fovy}, {self.projection})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginMode3D(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndMode3D()

    # endregion (context)

    # region METHODS

    def set_mode(self, mode: int) -> None:
        """Set camera mode (multiple camera modes available)"""
        return _rl.SetCameraMode(self, int(mode))

    def update(self) -> None:
        """Update camera position for selected mode"""
        return _rl.UpdateCamera(byref(self))

    def get_matrix(self) -> Matrix:
        """Returns camera transform matrix (view matrix)"""
        return _rl.GetCameraMatrix(self)

    def get_world_to_screen(self, position: AnyVec3) -> Vector2:
        """Returns the screen space position for a 3d world space position"""
        return _rl.GetWorldToScreen(_vec3(position), self)

    def get_world_to_screen_ex(self, position: AnyVec3, width: int, height: int) -> Vector2:
        """Returns size position for a 3d world space position"""
        return _rl.GetWorldToScreenEx(_vec3(position), self, int(width), int(height))

    def get_mouse_ray(self, mouse_position: AnyVec2) -> 'Ray':
        """Returns a ray trace from mouse position"""
        return _rl.GetMouseRay(_vec2(mouse_position), self)

    # endregion (methods)


Camera = Camera3D
Camera3DPtr = POINTER(Camera3D)
CameraPtr = Camera3DPtr


class Camera2D(Structure):
    _fields_ = [
        ('offset', Vector2),
        ('target', Vector2),
        ('rotation', c_float),
        ('zoom', c_float),
    ]

    def __init__(self, offset: Optional[Vector2] = None, target: Optional[Vector2] = None, rotation: float = 0.0,
                 zoom: float = 1.0):
        super().__init__(offset if offset else Vector2(), target if target else Vector2(), rotation, zoom)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.offset}, {self.target}, {self.rotation}, {self.zoom})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.offset}, {self.target}, {self.rotation}, {self.zoom})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginMode2D(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndMode2D()

    # endregion (context)

    # region METHODS

    def get_matrix2d(self) -> Matrix:
        """Returns camera 2d transform matrix"""
        return _rl.GetCameraMatrix2D(self)

    def get_world_to_screen(self, position: AnyVec2) -> Vector2:
        """Returns the screen space position for a 2d camera world space position"""
        return _rl.GetWorldToScreen2D(_vec2(position), self)

    def get_screen_to_world(self, position: AnyVec2) -> Vector2:
        """Returns the world space position for a 2d camera screen space position"""
        return _rl.GetScreenToWorld2D(_vec2(position), self)

    # endregion (methods)


# endregion (cameras)


class Mesh(Structure):
    _fields_ = [
        ('vertexCount', c_int),
        ('triangleCount', c_int),

        # Default vertex data
        ('vertices', POINTER(c_float)),
        ('texcoords', POINTER(c_float)),
        ('texcoords2', POINTER(c_float)),
        ('normals', POINTER(c_float)),
        ('tangents', POINTER(c_float)),
        ('colors', POINTER(c_ubyte)),
        ('indices', POINTER(c_ushort)),

        # Animation vertex data
        ('animVertices', POINTER(c_float)),
        ('animNormals', POINTER(c_float)),
        ('boneIds', POINTER(c_int)),
        ('boneWeights', POINTER(c_float)),

        # OpenGL identifiers
        ('vaoId', c_uint),
        ('vboId', POINTER(c_uint)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def gen_poly(sides: int, radius: float) -> 'Mesh':
        """Generate polygonal mesh"""
        return _rl.GenMeshPoly(int(sides), float(radius))

    @staticmethod
    def gen_plane(width: float, length: float, res_x: int, res_z: int) -> 'Mesh':
        """Generate plane mesh (with subdivisions)"""
        return _rl.GenMeshPlane(float(width), float(length), int(res_x), int(res_z))

    @staticmethod
    def gen_cube(width: float, height: float, length: float) -> 'Mesh':
        """Generate cuboid mesh"""
        return _rl.GenMeshCube(float(width), float(height), float(length))

    @staticmethod
    def gen_sphere(radius: float, rings: int, slices: int) -> 'Mesh':
        """Generate sphere mesh (standard sphere)"""
        return _rl.GenMeshSphere(float(radius), int(rings), int(slices))

    @staticmethod
    def gen_hemisphere(radius: float, rings: int, slices: int) -> 'Mesh':
        """Generate half-sphere mesh (no bottom cap)"""
        return _rl.GenMeshHemiSphere(float(radius), int(rings), int(slices))

    @staticmethod
    def gen_cylinder(radius: float, height: float, slices: int) -> 'Mesh':
        """Generate cylinder mesh"""
        return _rl.GenMeshCylinder(float(radius), float(height), int(slices))

    @staticmethod
    def gen_torus(radius: float, size: float, rad_seg: int, sides: int) -> 'Mesh':
        """Generate torus mesh"""
        return _rl.GenMeshTorus(float(radius), float(size), int(rad_seg), int(sides))

    @staticmethod
    def gen_knot(radius: float, size: float, rad_seg: int, sides: int) -> 'Mesh':
        """Generate trefoil knot mesh"""
        return _rl.GenMeshKnot(float(radius), float(size), int(rad_seg), int(sides))

    @staticmethod
    def gen_heightmap(heightmap: Image, size: AnyVec3) -> 'Mesh':
        """Generate heightmap mesh from image data"""
        return _rl.GenMeshHeightmap(heightmap, _vec3(size))

    @staticmethod
    def gen_cubicmap(cubicmap: Image, cube_size: AnyVec3) -> 'Mesh':
        """Generate cubes-based map mesh from image data"""
        return _rl.GenMeshCubicmap(cubicmap, _vec3(cube_size))

    # endregion (classmethods)

    def __init__(self, vertex_count: int, triangle_count: int, vertices: Sequence[float], texcoords: Sequence[float],
                 texcoords2: Sequence[float], normals: Sequence[float], tangents: Sequence[float],
                 colors: Sequence[int],
                 indices: Sequence[int], anim_vertices: Sequence[float], anim_normals: Sequence[float],
                 bone_ids: Sequence[int], bone_weights: Sequence[float], vao_id: int, vbo_id: IntPtr):
        super().__init__(vertex_count, triangle_count, _arr(c_float, vertices), _arr(c_float, texcoords),
                         _arr(c_float, texcoords2), _arr(c_float, normals), _arr(c_float, tangents),
                         _arr(c_ubyte, colors), _arr(c_ushort, indices), _arr(c_float, anim_vertices),
                         _arr(c_float, anim_normals), _arr(c_int, bone_ids), _arr(c_float, bone_weights), vao_id,
                         vbo_id)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.vertexCount}, {self.triangleCount}, {self.vaoId}, {self.vboId})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.vertexCount}, {self.triangleCount}, {self.vaoId}, {self.vboId})"

    # endregion

    # region METHODS

    def upload(self, dynamic: bool) -> None:
        """Upload mesh vertex data in GPU and provide VAO/VBO ids"""
        return _rl.UploadMesh(byref(self), bool(dynamic))

    def update_buffer(self, index: int, data: bytes, data_size: int, offset: int) -> None:
        """Update mesh vertex data in GPU for a specific buffer index"""
        return _rl.UpdateMeshBuffer(self, int(index), data, int(data_size), int(offset))

    def draw(self, material: 'Material', transform: Matrix) -> None:
        """Draw a 3d mesh with material and transform"""
        return _rl.DrawMesh(self, material, transform)

    def draw_instanced(self, material: 'Material', transforms: Sequence[Matrix], instances: int) -> None:
        """Draw multiple mesh instances with material and different transforms"""
        return _rl.DrawMeshInstanced(self, material, _arr(Matrix, transforms), int(instances))

    def unload(self) -> None:
        """Unload mesh data from CPU and GPU"""
        return _rl.UnloadMesh(self)

    def export(self, file_name: str) -> bool:
        """Export mesh data to file, returns true on success"""
        return _rl.ExportMesh(self, _str_in(file_name))

    def bounding_box(self) -> 'BoundingBox':
        """Compute mesh bounding box limits"""
        return _rl.MeshBoundingBox(self)

    def tangents(self) -> None:
        """Compute mesh tangents"""
        return _rl.MeshTangents(byref(self))

    def binormals(self) -> None:
        """Compute mesh binormals"""
        return _rl.MeshBinormals(byref(self))

    # endregion (methods)


MeshPtr = POINTER(Mesh)


class Shader(Structure):
    _fields_ = [
        ('id', c_uint),
        ('locs', POINTER(c_int)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(vs_file_name: str, fs_file_name: str) -> 'Shader':
        """Load shader from files and bind default locations"""
        return _rl.LoadShader(_str_in(vs_file_name), _str_in(fs_file_name))

    @staticmethod
    def load_from_memory(vs_code: str, fs_code: str) -> 'Shader':
        """Load shader from code strings and bind default locations"""
        return _rl.LoadShaderFromMemory(_str_in(vs_code), _str_in(fs_code))

    # endregion (classmethods)

    def __init__(self, id: int, locs: Sequence[int]):
        super().__init__(id, (c_int * len(locs))(*locs))

    def __del__(self):
        return _rl.UnloadShader(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.id}, {self.locs})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.id}, {self.locs})"

    # endregion

    # region CONTEXT

    def __enter__(self):
        _rl.BeginShaderMode(self)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        _rl.EndShaderMode()

    # endregion (context)

    # region METHODS

    def get_location(self, uniform_name: str) -> int:
        """Get shader uniform location"""
        return _rl.GetShaderLocation(self, _str_in(uniform_name))

    def get_location_attrib(self, attrib_name: str) -> int:
        """Get shader attribute location"""
        return _rl.GetShaderLocationAttrib(self, _str_in(attrib_name))

    def set_value(self, loc_index: int, value: bytes, uniform_type: int) -> None:
        """Set shader uniform value"""
        return _rl.SetShaderValue(self, int(loc_index), value, int(uniform_type))

    def set_value_v(self, loc_index: int, value: bytes, uniform_type: int, count: int) -> None:
        """Set shader uniform value vector"""
        return _rl.SetShaderValueV(self, int(loc_index), value, int(uniform_type), int(count))

    def set_value_matrix(self, loc_index: int, mat: Matrix) -> None:
        """Set shader uniform value (matrix 4x4)"""
        return _rl.SetShaderValueMatrix(self, int(loc_index), mat)

    def set_value_texture(self, loc_index: int, texture: Texture2D) -> None:
        """Set shader uniform value for texture (sampler2d)"""
        return _rl.SetShaderValueTexture(self, int(loc_index), texture)

    # endregion (methods)


class MaterialMap(Structure):
    _fields_ = [
        ('texture', Texture2D),
        ('color', Color),
        ('value', c_float),
    ]

    def __init__(self, texture: int, color: Color, value: float):
        super().__init__(texture, color, value)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.texture}, {self.color}, {self.value})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.texture}, {self.color}, {self.value})"

    # endregion


class Material(Structure):
    _fields_ = [
        ('shader', Shader),
        ('maps', POINTER(MaterialMap)),
        ('params', c_float * 4),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> Sequence['Material']:
        """Load materials from model file"""
        material_count = IntPtr(0)
        material: MaterialPtr = _rl.LoadMaterials(_str_in(file_name), material_count)
        return [material.contents[i] for i in range(material_count.contents[0])]

    @staticmethod
    def load_default() -> 'Material':
        """Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)"""
        return _rl.LoadMaterialDefault()

    # endregion (classmethods)

    def __init__(self, shader: int, maps: Sequence[MaterialMap], params: Sequence[float]):
        n_params = len(params)
        if n_params > 4:
            raise ValueError(f"Expected up to 4 param values, got {n_params}.")
        super().__init__(shader, maps, (c_float * n_params)(*params))

    def __del__(self):
        _rl.UnloadMaterial(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.shader}, {self.maps}, {self.params})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.shader}, {self.maps}, {self.params})"

    # endregion

    # region METHODS

    def set_texture(self, map_type: int, texture: Texture2D) -> None:
        """Set texture for a material map type (MATERIAL_MAP_DIFFUSE, MATERIAL_MAP_SPECULAR...)"""
        return _rl.SetMaterialTexture(byref(self), int(map_type), texture)

    # endregion (methods)


MaterialPtr = POINTER(Material)


class Transform(Structure):
    _fields_ = [
        ('translation', Vector3),
        ('rotation', Quaternion),
        ('scale', Vector3),
    ]

    def __init__(self, translation: Vector3, rotation: Quaternion, scale: Vector3):
        super().__init__(translation, rotation, scale)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.translation}, {self.rotation}, {self.scale})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.translation}, {self.rotation}, {self.scale})"

    # endregion


class BoneInfo(Structure):
    _fields_ = [
        ('name', c_char * 32),
        ('parent', c_int),
    ]

    def __init__(self, name: str, parent: int):
        n = len(name)
        if n > 32:
            raise ValueError(f"name argument is more than 32 characters long ({n}).")
        super().__init__(_str_in(name), parent)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.name}, {self.parent})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.name}, {self.parent})"

    # endregion


class Model(Structure):
    _fields_ = [
        ('transform', Transform),

        ('meshCount', c_int),
        ('materialCount', c_int),
        ('meshes', POINTER(Mesh)),
        ('materials', POINTER(Material)),
        ('meshMaterial', POINTER(c_int)),

        ('boneCount', c_int),
        ('bones', POINTER(BoneInfo)),
        ('bindPose', POINTER(Transform)),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Model':
        """Load model from files (meshes and materials)"""
        return _rl.LoadModel(_str_in(file_name))

    @staticmethod
    def load_from_mesh(mesh: Mesh) -> 'Model':
        """Load model from generated mesh (default material)"""
        return _rl.LoadModelFromMesh(mesh)

    # endregion (classmethods)

    def __init__(self, transform: Transform, mesh_count: int, material_count: int, meshes: Sequence[Mesh],
                 materials: Sequence[Material], mesh_material: Sequence[int], bone_count: int,
                 bones: Sequence[BoneInfo], bind_pose: Sequence[Transform], keep_meshes: bool = False):
        mesh_array = Mesh * len(meshes)
        material_array = Material * len(materials)
        mesh_material_array = c_int * len(mesh_material)
        bone_array = BoneInfo * len(bones)
        transform_array = Transform * len(bind_pose)
        super().__init__(transform, mesh_count, material_count, mesh_array(*meshes), material_array(*materials),
                         mesh_material_array(*mesh_material), bone_count, bone_array(*bones),
                         transform_array(bind_pose))
        self.keep_meshes: bool = keep_meshes

    def __del__(self):
        if self.keep_meshes:
            _rl.UnloadModelKeepMeshes(self)
        else:
            _rl.UnloadModel(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.transform}, {self.materialCount}, {self.bones}, {self.framePoses})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.transform}, {self.materialCount}, {self.bones}, {self.framePoses})"

    # endregion

    # region METHODS

    def set_model_mesh_material(self, mesh_id: int, material_id: int) -> None:
        """Set material for a mesh"""
        return _rl.SetModelMeshMaterial(byref(self), int(mesh_id), int(material_id))

    @staticmethod
    def load_model_animations(file_name: str) -> Tuple['ModelAnimationPtr', int]:
        """Load model animations from file"""
        anims_count = IntPtr(0)
        model_anim = _rl.LoadModelAnimations(_str_in(file_name), anims_count)
        return model_anim, anims_count.contents

    def update_model_animation(self, anim: 'ModelAnimation', frame: int) -> None:
        """Update model animation pose"""
        return _rl.UpdateModelAnimation(self, anim, int(frame))

    @staticmethod
    def unload_model_animation(anim: 'ModelAnimation') -> None:
        """Unload animation data"""
        return _rl.UnloadModelAnimation(anim)

    @staticmethod
    def unload_model_animations(animations: 'ModelAnimation', count: int) -> None:
        """Unload animation array data"""
        return _rl.UnloadModelAnimations(byref(animations), int(count))

    def is_model_animation_valid(self, anim: 'ModelAnimation') -> bool:
        """Check model animation skeleton match"""
        return _rl.IsModelAnimationValid(self, anim)

    # endregion (methods)


ModelPtr = POINTER(Model)


class ModelAnimation(Structure):
    _fields_ = [
        ('boneCount', c_int),
        ('frameCount', c_int),
        ('bones', POINTER(BoneInfo)),
        ('framePoses', POINTER(POINTER(Transform))),
    ]

    def __init__(self, bone_count: Vector3, frame_count: Vector3, bones: Sequence[BoneInfo],
                 frame_poses: Sequence[Sequence[Transform]]):
        bone_array = BoneInfo * len(bones)
        transform_array = Transform * len(frame_poses[0])
        array_array = transform_array * len(frame_poses)
        super().__init__(bone_count, frame_count, bone_array(*bones), array_array(*frame_poses))

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.boneCount}, {self.frameCount}, {self.bones}, {self.framePoses})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.boneCount}, {self.frameCount}, {self.bones}, {self.framePoses})"

    # endregion


ModelAnimationPtr = POINTER(ModelAnimation)


class Ray(Structure):
    _fields_ = [
        ('position', Vector3),
        ('direction', Vector3),
    ]

    def __init__(self, position: Optional[Vector3] = None, direction: [Vector3] = None):
        super().__init__(position if position else Vector3(), direction if position else Vector3())

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.position}, {self.direction})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.position}, {self.direction})"

    # endregion

    # region METHODS

    # endregion (methods


class RayHitInfo(Structure):
    _fields_ = [
        ('hit', c_bool),
        ('distance', c_float),
        ('position', Vector3),
        ('normal', Vector3),
    ]


RayHitInfoPtr = POINTER(RayHitInfo)


class BoundingBox(Structure):
    _fields_ = [
        ('min', Vector3),
        ('max', Vector3),
    ]

    def __init__(self, min: Vector3, max: Vector3):
        super().__init__(min, max)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.min}, {self.max})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.min}, {self.max})"

    # endregion


class Wave(Structure):
    _fields_ = [
        ('sampleCount', c_uint),
        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
        ('data', c_void_p),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Wave':
        """Load wave data from file"""
        return _rl.LoadWave(_str_in(file_name))

    @staticmethod
    def load_from_memory(file_type: str, file_data: bytes, data_size: int) -> 'Wave':
        """Load wave from memory buffer, fileType refers to extension: i.e. ".wav"."""
        return _rl.LoadWaveFromMemory(_str_in(file_type), file_data, int(data_size))

    # endregion (classmethods)

    def __init__(self, sample_count: int, sample_rate: int, sample_size: int, channels: int, data: IntPtr):
        super().__init__(sample_count, sample_rate, sample_size, channels, data)

    def __del__(self):
        _rl.UnloadWave(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.sampleCount}, {self.sampleRate}, {self.SampleSize}, {self.channels})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.sampleCount}, {self.sampleRate}, {self.SampleSize}, {self.channels})"

    # endregion

    # region METHODS

    def format(self, sample_rate: int, sample_size: int, channels: int) -> None:
        """Convert wave data to desired format"""
        return _rl.WaveFormat(self, int(sample_rate), int(sample_size), int(channels))

    def copy(self) -> 'Wave':
        """Copy a wave to a new wave"""
        return _rl.WaveCopy(self)

    def crop(self, init_sample: int, final_sample: int) -> None:
        """Crop a wave to defined samples range"""
        return _rl.WaveCrop(self, int(init_sample), int(final_sample))

    def export_wave(self, file_name: str) -> bool:
        """Export wave data to file, returns true on success"""
        return _rl.ExportWave(self, _str_in(file_name))

    def export_wave_as_code(self, file_name: str) -> bool:
        """Export wave sample data to code (.h), returns true on success"""
        return _rl.ExportWaveAsCode(self, _str_in(file_name))

    # endregion (methods)


WavePtr = POINTER(Wave)


class rAudioBuffer(Structure):
    pass


rAudioBufferPtr = POINTER(rAudioBuffer)


class AudioStream(Structure):
    _fields_ = [
        ('buffer', POINTER(rAudioBuffer)),

        ('sampleRate', c_uint),
        ('SampleSize', c_uint),
        ('channels', c_uint),
    ]

    # region CLASSMETHODS

    @staticmethod
    def init_audio_stream(sample_rate: int, sample_size: int, channels: int) -> 'AudioStream':
        """Init audio stream (to stream raw audio pcm data)"""
        return _rl.InitAudioStream(int(sample_rate), int(sample_size), int(channels))

    @staticmethod
    def set_buffer_size_default(size: int) -> None:
        """Default size for new audio streams"""
        return _rl.SetAudioStreamBufferSizeDefault(int(size))

    # endregion (classmethods)

    def __init__(self, buffer: rAudioBufferPtr, sample_rate: int, sample_size: int, channels: int):
        super().__init__(buffer, sample_rate, sample_size, channels)

    def __del__(self):
        _rl.CloseAudioStream(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.sampleRate}, {self.SampleSize}, {self.channels})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.sampleRate}, {self.SampleSize}, {self.channels})"

    # endregion

    # region PROPERTIES

    @property
    def is_processed(self) -> bool:
        """Check if any audio stream buffers requires refill"""
        return _rl.IsAudioStreamProcessed(self)

    @property
    def is_playing(self) -> bool:
        """Check if audio stream is playing"""
        return _rl.IsAudioStreamPlaying(self)

    # endregion (properties)

    # region METHODS

    def update(self, data: bytes, samples_count: int) -> None:
        """Update audio stream buffers with data"""
        return _rl.UpdateAudioStream(self, data, int(samples_count))

    def play(self) -> None:
        """Play audio stream"""
        return _rl.PlayAudioStream(self)

    def pause(self) -> None:
        """Pause audio stream"""
        return _rl.PauseAudioStream(self)

    def resume(self) -> None:
        """Resume audio stream"""
        return _rl.ResumeAudioStream(self)

    def stop(self) -> None:
        """Stop audio stream"""
        return _rl.StopAudioStream(self)

    def set_volume(self, volume: float) -> None:
        """Set volume for audio stream (1.0 is max level)"""
        return _rl.SetAudioStreamVolume(self, float(volume))

    def set_pitch(self, pitch: float) -> None:
        """Set pitch for audio stream (1.0 is base level)"""
        return _rl.SetAudioStreamPitch(self, float(pitch))

    # endregion (methods)


class Sound(Structure):
    _fields_ = [
        ('stream', AudioStream),
        ('sampleCount', c_uint),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load(file_name: str) -> 'Sound':
        """Load sound from file"""
        return _rl.LoadSound(_str_in(file_name))

    @staticmethod
    def load_from_wave(wave: Wave) -> 'Sound':
        """Load sound from wave data"""
        return _rl.LoadSoundFromWave(wave)

    # endregion (classmethods)

    def __init__(self, stream: AudioStream, sample_count: int):
        super().__init__(stream, sample_count)

    def __del__(self):
        _rl.UnloadWave(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.stream}, {self.sampleCount})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.stream}, {self.sampleCount})"

    # endregion

    # region PROPERTIES

    @property
    def is_playing(self) -> bool:
        """Check if a sound is currently playing"""
        return _rl.IsSoundPlaying(self)

    @property
    def get_sounds_playing(self) -> int:
        """Get number of sounds playing in the multichannel"""
        return _rl.GetSoundsPlaying()

    # endregion (properties)

    # region METHODS

    def play(self) -> None:
        """Play a sound"""
        return _rl.PlaySound(self)

    def stop(self) -> None:
        """Stop playing a sound"""
        return _rl.StopSound(self)

    def pause(self) -> None:
        """Pause a sound"""
        return _rl.PauseSound(self)

    def resume(self) -> None:
        """Resume a paused sound"""
        return _rl.ResumeSound(self)

    def update(self, data: bytes, samples_count: int) -> None:
        """Update sound buffer with new data"""
        return _rl.UpdateSound(self, data, int(samples_count))

    def play_multi(self) -> None:
        """Play a sound (using multichannel buffer pool)"""
        return _rl.PlaySoundMulti(self)

    @staticmethod
    def stop_multi() -> None:
        """Stop any sound playing (using multichannel buffer pool)"""
        return _rl.StopSoundMulti()

    def set_volume(self, volume: float) -> None:
        """Set volume for a sound (1.0 is max level)"""
        return _rl.SetSoundVolume(self, float(volume))

    def set_pitch(self, pitch: float) -> None:
        """Set pitch for a sound (1.0 is base level)"""
        return _rl.SetSoundPitch(self, float(pitch))

    @staticmethod
    def load_samples(wave: Wave) -> Sequence[float]:
        """Load samples data from wave as a floats array"""
        return _rl.LoadWaveSamples(wave)

    @staticmethod
    def unload_samples(samples: Sequence[float]) -> None:
        """Unload samples data loaded with LoadWaveSamples()"""
        return _rl.UnloadWaveSamples(_arr(Float, samples))

    # endregion (methods)


class Music(Structure):
    _fields_ = [
        ('stream', AudioStream),
        ('sampleCount', c_uint),
        ('looping', c_bool),

        ('ctxType', c_int),
        ('ctxData', c_void_p),
    ]

    # region CLASSMETHODS

    @staticmethod
    def load_stream(file_name: str) -> 'Music':
        """Load music stream from file"""
        return _rl.LoadMusicStream(_str_in(file_name))

    @staticmethod
    def load_stream_from_memory(file_type: str, data: bytes, data_size: int) -> 'Music':
        """Load music stream from data"""
        return _rl.LoadMusicStreamFromMemory(_str_in(file_type), data, int(data_size))

    # endregion (classmethods)

    def __init__(self, stream: AudioStream, sample_count: int, looping: bool, ctx_type: int, ctx_data: IntPtr):
        super().__init__(stream, sample_count, looping, ctx_type, ctx_data)

    def __del__(self):
        _rl.UnloadMusicStream(self)

    # region REPRESENTATION

    def __str__(self) -> str:
        return f"({self.stream}, {self.sampleCount}, {self.looping}, {self.ctxType})"

    def __repr__(self) -> str:
        return f"{_clsname(self)}({self.stream}, {self.sampleCount}, {self.looping}, {self.ctxType})"

    # endregion

    # region PROPERTIES

    @property
    def time_length(self) -> float:
        """Get music time length (in seconds)"""
        return _rl.GetMusicTimeLength(self)

    @property
    def time_played(self) -> float:
        """Get current music time played (in seconds)"""
        return _rl.GetMusicTimePlayed(self)

    # endregion (properties)

    # region METHODS

    def play_stream(self) -> None:
        """Start music playing"""
        return _rl.PlayMusicStream(self)

    def is_playing(self) -> bool:
        """Check if music is playing"""
        return _rl.IsMusicPlaying(self)

    def update_stream(self) -> None:
        """Updates buffers for music streaming"""
        return _rl.UpdateMusicStream(self)

    def stop_stream(self) -> None:
        """Stop music playing"""
        return _rl.StopMusicStream(self)

    def pause_stream(self) -> None:
        """Pause music playing"""
        return _rl.PauseMusicStream(self)

    def resume_stream(self) -> None:
        """Resume playing paused music"""
        return _rl.ResumeMusicStream(self)

    def set_volume(self, volume: float) -> None:
        """Set volume for music (1.0 is max level)"""
        return _rl.SetMusicVolume(self, float(volume))

    def set_pitch(self, pitch: float) -> None:
        """Set pitch for a music (1.0 is base level)"""
        return _rl.SetMusicPitch(self, float(pitch))

    # endregion (methods)


MusicData = POINTER(Music)


class VrDeviceInfo(Structure):
    _fields_ = [
        ('hResolution', c_int),
        ('vResolution', c_int),
        ('hScreenSize', c_float),
        ('vScreenSize', c_float),
        ('vScreenCenter', c_float),
        ('eyeToScreenDistance', c_float),
        ('lensSeparationDistance', c_float),
        ('interpupillaryDistance', c_float),
        ('lensDistortionValues', c_float * 4),
        ('chromaAbCorrection', c_float * 4),
    ]

    def __init__(self, h_resolution: int, v_resolution: int, h_screen_size: float, v_screen_size: float,
                 v_screen_center: float, eye_to_screen_distance: float, lens_separation_distance: float,
                 interpupillary_distance: float, lens_distortion_values: Sequence[float],
                 chroma_ab_correction: Sequence[float]):
        super().__init__(h_resolution, v_resolution, h_screen_size, v_screen_size, v_screen_center,
                         eye_to_screen_distance, lens_separation_distance, interpupillary_distance,
                         _arr(Float, lens_distortion_values), _arr(Float, chroma_ab_correction))

    # region REPRESENTATION

    def __str__(self) -> str:
        return (f"({self.hResolution}, {self.vResolution}, {self.hScreenSize}, {self.vScreenSize},"
                f" {self.vScreenCenter}, {self.eyeToScreenDistance}, {self.lensSeparationDistance},"
                f" {self.interpupillaryDistance}, {self.lensDistortionValues}, {self.chromaAbCorrection})")

    def __repr__(self) -> str:
        return (f"{_clsname(self)}({self.hResolution}, {self.vResolution}, {self.hScreenSize}, {self.vScreenSize},"
                f" {self.vScreenCenter}, {self.eyeToScreenDistance}, {self.lensSeparationDistance},"
                f" {self.interpupillaryDistance}, {self.lensDistortionValues}, {self.chromaAbCorrection})")

    # endregion (representation)

    # region METHODS

    def load(self) -> 'VrStereoConfig':
        """Load VR stereo config for VR simulator device parameters"""
        return _rl.LoadVrStereoConfig(self)

    # endregion (methods)


class VrStereoConfig(Structure):
    _fields_ = [
        ('projection', Matrix * 2),
        ('viewOffset', Matrix * 2),
        ('leftLensCenter', c_float * 2),
        ('rightLensCenter', c_float * 2),
        ('leftScreenCenter', c_float * 2),
        ('rightScreenCenter', c_float * 2),
        ('scale', c_float * 2),
        ('scaleIn', c_float * 2),
    ]

    def __init__(self, projection: Sequence[Matrix], view_offset: Sequence[Matrix],
                 left_lens_center: Sequence[float], right_lens_center: Sequence[float],
                 left_screen_center: Sequence[float], right_screen_center: Sequence[float],
                 scale: Sequence[float], scale_in: Sequence[float]):
        super().__init__(self, _arr(Matrix, projection), _arr(Matrix, view_offset),
                         _arr(Float, left_lens_center), _arr(Float, right_lens_center),
                         _arr(Float, left_screen_center), _arr(Float, right_screen_center),
                         _arr(Float, scale), _arr(Float, scale_in))

    # region REPRESENTATION

    def __str__(self) -> str:
        return (f"({self.projection}, {self.viewOffset}, {self.leftLensCenter},"
                f" {self.rightLensCenter}, {self.leftScreenCenter},"
                f" {self.rightScreenCenter}, {self.scale}, {self.scaleIn})")

    def __repr__(self) -> str:
        return (f"({_clsname(self)}{self.projection}, {self.viewOffset}, {self.leftLensCenter},"
                f" {self.rightLensCenter}, {self.leftScreenCenter},"
                f" {self.rightScreenCenter}, {self.scale}, {self.scaleIn})")

    # endregion (representation)

    # region METHODS

    def unload(self) -> None:
        """Unload VR stereo config"""
        return _rl.UnloadVrStereoConfig(self)

    # endregion (methods)

# endregion (classes)
# ---------------------------------------------------------
