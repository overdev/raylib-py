from library import rl as _rl
from structures import *
from ctypes import byref
from typing import Tuple


__all__ = [
    # Basic shapes drawing functions
    'draw_pixel',
    'draw_pixel_v',
    'draw_line',
    'draw_line_v',
    'draw_line_ex',
    'draw_line_bezier',
    'draw_circle',
    'draw_circle_gradient',
    'draw_circle_v',
    'draw_circle_lines',
    'draw_rectangle',
    'draw_rectangle_v',
    'draw_rectangle_rec',
    'draw_rectangle_pro',
    'draw_rectangle_gradient_v',
    'draw_rectangle_gradient_h',
    'draw_rectangle_gradient_ex',
    'draw_rectangle_lines',
    'draw_rectangle_lines_ex',
    'draw_triangle',
    'draw_triangle_lines',
    'draw_poly',
    'draw_poly_ex',
    'draw_poly_ex_lines',
    # Basic shapes collision detection functions
    'check_collision_recs',
    'check_collision_circles',
    'check_collision_circle_rec',
    'get_collision_rec',
    'check_collision_point_rec',
    'check_collision_point_circle',
    'check_collision_point_triangle',

    'byref',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Basic Shapes Drawing Functions (Module: shapes)
# -----------------------------------------------------------------------------------

# Basic shapes drawing functions
_rl.DrawPixel.argtypes = [Int, Int, Color]
_rl.DrawPixel.restype = None
def draw_pixel(pos_x: int, pos_y: int, color: Color) -> None:
    '''Draw a pixel'''
    return _rl.DrawPixel(pos_x, pos_y, color)


_rl.DrawPixelV.argtypes = [Vector2, Color]
_rl.DrawPixelV.restype = None
def draw_pixel_v(position: Vector2, color: Color) -> None:
    '''Draw a pixel (Vector version)'''
    return _rl.DrawPixelV(position, color)


_rl.DrawLine.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawLine.restype = None
def draw_line(startPos_x: int, startPos_y: int, endPos_x: int, endPos_y: int, color: Color) -> None:
    '''Draw a line'''
    return _rl.DrawLine(startPos_x, startPos_y, endPos_x, endPos_y, color)


_rl.DrawLineV.argtypes = [Vector2, Vector2, Color]
_rl.DrawLineV.restype = None
def draw_line_v(start_pos: Vector2, end_pos: Vector2, color: Color) -> None:
    '''Draw a line (Vector version)'''
    return _rl.DrawLineV(start_pos, end_pos, color)


_rl.DrawLineEx.argtypes = [Vector2, Vector2, Float, Color]
_rl.DrawLineEx.restype = None
def draw_line_ex(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None:
    '''Draw a line defining thickness'''
    return _rl.DrawLineEx(start_pos, end_pos, thick, color)


_rl.DrawLineBezier.argtypes = [Vector2, Vector2, Float, Color]
_rl.DrawLineBezier.restype = None
def draw_line_bezier(start_pos: Vector2, end_pos: Vector2, thick: float, color: Color) -> None:
    '''Draw a line using cubic-bezier curves in-out'''
    return _rl.DrawLineBezier(start_pos, end_pos, thick, color)


_rl.DrawCircle.argtypes = [Int, Int, Float, Color]
_rl.DrawCircle.restype = None
def draw_circle(center_x: int, center_y: int, radius: float, color: Color) -> None:
    '''Draw a color-filled circle'''
    return _rl.DrawCircle(center_x, center_y, radius, color)


_rl.DrawCircleGradient.argtypes = [Int, Int, Float, Color, Color]
_rl.DrawCircleGradient.restype = None
def draw_circle_gradient(center_x: int, center_y: int, radius: float, color1: Color, color2: Color) -> None:
    '''Draw a gradient-filled circle'''
    return _rl.DrawCircleGradient(center_x, center_y, radius, color1, color2)


_rl.DrawCircleV.argtypes = [Vector2, Float, Color]
_rl.DrawCircleV.restype = None
def draw_circle_v(center: Vector2, radius: float, color: Color) -> None:
    '''Draw a color-filled circle (Vector version)'''
    return _rl.DrawCircleV(center, radius, color)


_rl.DrawCircleLines.argtypes = [Int, Int, Float, Color]
_rl.DrawCircleLines.restype = None
def draw_circle_lines(center_x: int, center_y: int, radius: float, color: Color) -> None:
    '''Draw circle outline'''
    return _rl.DrawCircleLines(center_x, center_y, radius, color)


_rl.DrawRectangle.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawRectangle.restype = None
def draw_rectangle(posX: int, posY: int, width: int, height: int, color: Color) -> None:
    '''Draw a color-filled rectangle'''
    return _rl.DrawRectangle(posX, posY, width, height, color)


_rl.DrawRectangleV.argtypes = [Vector2, Vector2, Color]
_rl.DrawRectangleV.restype = None
def draw_rectangle_v(position: Vector2, size: Vector2, color: Color) -> None:
    '''Draw a color-filled rectangle (Vector version)'''
    return _rl.DrawRectangleV(position, size, color)


_rl.DrawRectangleRec.argtypes = [Rectangle, Color]
_rl.DrawRectangleRec.restype = None
def draw_rectangle_rec(rec: Rectangle, color: Color) -> None:
    '''Draw a color-filled rectangle'''
    return _rl.DrawRectangleRec(rec, color)


_rl.DrawRectanglePro.argtypes = [Rectangle, Vector2, Float, Color]
_rl.DrawRectanglePro.restype = None
def draw_rectangle_pro(rec: Rectangle, origin: Vector2, rotation: float, color: Color) -> None:
    '''Draw a color-filled rectangle with pro parameters'''
    return _rl.DrawRectanglePro(rec, origin, rotation, color)


_rl.DrawRectangleGradientV.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.DrawRectangleGradientV.restype = None
def draw_rectangle_gradient_v(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
    '''Draw a vertical-gradient-filled rectangle'''
    return _rl.DrawRectangleGradientV(posX, posY, width, height, color1, color2)


_rl.DrawRectangleGradientH.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.DrawRectangleGradientH.restype = None
def draw_rectangle_gradient_h(posX: int, posY: int, width: int, height: int, color1: Color, color2: Color) -> None:
    '''Draw a horizontal-gradient-filled rectangle'''
    return _rl.DrawRectangleGradientH(posX, posY, width, height, color1, color2)


_rl.DrawRectangleGradientEx.argtypes = [Rectangle, Color, Color, Color, Color]
_rl.DrawRectangleGradientEx.restype = None
def draw_rectangle_gradient_ex(rec: Rectangle, col1: Color, col2: Color, col3: Color, col4: Color) -> None:
    '''Draw a gradient-filled rectangle with custom vertex colors'''
    return _rl.DrawRectangleGradientEx(rec, col1, col2, col3, col4)


_rl.DrawRectangleLines.argtypes = [Int, Int, Int, Int, Color]
_rl.DrawRectangleLines.restype = None
def draw_rectangle_lines(posX: int, posY: int, width: int, height: int, color: Color) -> None:
    '''Draw rectangle outline'''
    return _rl.DrawRectangleLines(posX, posY, width, height, color)


_rl.DrawRectangleLinesEx.argtypes = [Rectangle, Int, Color]
_rl.DrawRectangleLinesEx.restype = None
def draw_rectangle_lines_ex(rec: Rectangle, line_thick: int, color: Color) -> None:
    '''Draw rectangle outline with extended parameters'''
    return _rl.DrawRectangleLinesEx(rec, line_thick, color)


_rl.DrawTriangle.argtypes = [Vector2, Vector2, Vector2, Color]
_rl.DrawTriangle.restype = None
def draw_triangle(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
    '''Draw a color-filled triangle'''
    return _rl.DrawTriangle(v1, v2, v3, color)


_rl.DrawTriangleLines.argtypes = [Vector2, Vector2, Vector2, Color]
_rl.DrawTriangleLines.restype = None
def draw_triangle_lines(v1: Vector2, v2: Vector2, v3: Vector2, color: Color) -> None:
    '''Draw triangle outline'''
    return _rl.DrawTriangleLines(v1, v2, v3, color)


_rl.DrawPoly.argtypes = [Vector2, Int, Float, Float, Color]
_rl.DrawPoly.restype = None
def draw_poly(center: Vector2, sides: int, radius: float, rotation: float, color: Color) -> None:
    '''Draw a regular polygon (Vector version)'''
    return _rl.DrawPoly(center, sides, radius, rotation, color)


_rl.DrawPolyEx.argtypes = [Vector2Ptr, Int, Color]
_rl.DrawPolyEx.restype = None
def draw_poly_ex(points: Vector2Ptr, num_points: int, color: Color) -> None:
    '''Draw a closed polygon defined by points'''
    return _rl.DrawPolyEx(points, num_points, color)


_rl.DrawPolyExLines.argtypes = [Vector2Ptr, Int, Color]
_rl.DrawPolyExLines.restype = None
def draw_poly_ex_lines(points: Vector2Ptr, num_points: int, color: Color) -> None:
    '''Draw polygon lines'''
    return _rl.DrawPolyExLines(points, num_points, color)


# Basic shapes collision detection functions
_rl.CheckCollisionRecs.argtypes = [Rectangle, Rectangle]
_rl.CheckCollisionRecs.restype = Bool
def check_collision_recs(rec1: Rectangle, rec2: Rectangle) -> bool:
    '''Check collision between two rectangles'''
    return _rl.CheckCollisionRecs(rec1, rec2)


_rl.CheckCollisionCircles.argtypes = [Vector2, Float, Vector2, Float]
_rl.CheckCollisionCircles.restype = Bool
def check_collision_circles(center1: Vector2, radius1: float, center2: Vector2, radius2: float) -> bool:
    '''Check collision between two circles'''
    return _rl.CheckCollisionCircles(center1, radius1, center2, radius2)


_rl.CheckCollisionCircleRec.argtypes = [Vector2, Float, Rectangle]
_rl.CheckCollisionCircleRec.restype = Bool
def check_collision_circle_rec(center: Vector2, radius: float, rec: Rectangle) -> bool:
    '''Check collision between circle and rectangle'''
    return _rl.CheckCollisionCircleRec(center, radius, rec)


_rl.GetCollisionRec.argtypes = [Rectangle, Rectangle]
_rl.GetCollisionRec.restype = Rectangle
def get_collision_rec(rec1: Rectangle, rec2: Rectangle):
    '''Get collision rectangle for two rectangles collision'''
    return _rl.GetCollisionRec(rec1, rec2)


_rl.CheckCollisionPointRec.argtypes = [Vector2, Rectangle]
_rl.CheckCollisionPointRec.restype = Bool
def check_collision_point_rec(point: Vector2, rec: Rectangle) -> bool:
    '''Check if point is inside rectangle'''
    return _rl.CheckCollisionPointRec(point, rec)


_rl.CheckCollisionPointCircle.argtypes = [Vector2, Vector2, Float]
_rl.CheckCollisionPointCircle.restype = Bool
def check_collision_point_circle(point: Vector2, center: Vector2, radius: Float) -> bool:
    '''Check if point is inside circle'''
    return _rl.CheckCollisionPointCircle(point, center, radius)


_rl.CheckCollisionPointTriangle.argtypes = [Vector2, Vector2, Vector2, Vector2]
_rl.CheckCollisionPointTriangle.restype = Bool
def check_collision_point_triangle(point: Vector2, p1: Vector2, p2: Vector2, p3: Vector2) -> bool:
    '''Check if point is inside a triangle'''
    return _rl.CheckCollisionPointTriangle(point, p1, p2, p3)
