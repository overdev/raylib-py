from ctypes import byref
from raylibpy._types import *
from raylibpy.core import *
from raylibpy import _rl

__all__ = [
    'clamp',
    'lerp',
    'normalize',
    'remap',
    'vector2_zero',
    'vector2_one',
    'vector2_add',
    'vector2_add_value',
    'vector2_subtract',
    'vector2_subtract_value',
    'vector2_length',
    'vector2_length_sqr',
    'vector2_dot_product',
    'vector2_distance',
    'vector2_angle',
    'vector2_scale',
    'vector2_multiply',
    'vector2_negate',
    'vector2_divide',
    'vector2_normalize',
    'vector2_lerp',
    'vector2_reflect',
    'vector2_rotate',
    'vector2_move_towards',
    'vector3_zero',
    'vector3_one',
    'vector3_add',
    'vector3_add_value',
    'vector3_subtract',
    'vector3_subtract_value',
    'vector3_scale',
    'vector3_multiply',
    'vector3_cross_product',
    'vector3_perpendicular',
    'vector3_length',
    'vector3_lengths_qr',
    'vector3_dot_product',
    'vector3_distance',
    'vector3_negate',
    'vector3_divide',
    'vector3_normalize',
    'vector3_ortho_normalize',
    'vector3_transform',
    'vector3_rotate_by_quaternion',
    'vector3_lerp',
    'vector3_reflect',
    'vector3_min',
    'vector3_max',
    'vector3_barycenter',
    'vector3_to_float_v',
    'matrix_determinant',
    'matrix_trace',
    'matrix_transpose',
    'matrix_invert',
    'matrix_normalize',
    'matrix_identity',
    'matrix_add',
    'matrix_subtract',
    'matrix_multiply',
    'matrix_translate',
    'matrix_rotate',
    'matrix_rotate_x',
    'matrix_rotate_y',
    'matrix_rotate_z',
    'matrix_rotate_xyz',
    'matrix_rotate_zyx',
    'matrix_scale',
    'matrix_frustum',
    'matrix_perspective',
    'matrix_ortho',
    'matrix_look_at',
    'matrix_to_float_v',
    'quaternion_add',
    'quaternion_add_value',
    'quaternion_subtract',
    'quaternion_subtract_value',
    'quaternion_identity',
    'quaternion_length',
    'quaternion_normalize',
    'quaternion_invert',
    'quaternion_multiply',
    'quaternion_scale',
    'quaternion_divide',
    'quaternion_lerp',
    'quaternion_nlerp',
    'quaternion_slerp',
    'quaternion_from_vector3_to_vector3',
    'quaternion_from_matrix',
    'quaternion_to_matrix',
    'quaternion_from_axis_angle',
    'quaternion_to_axis_angle',
    'quaternion_from_euler',
    'quaternion_to_euler',
    'quaternion_transform',
    'vector3_unproject',
]


# ----------------------------------------------------------------------------------
#  Module Functions Definition - Utils math
# ----------------------------------------------------------------------------------


def clamp(value: float, min_: float, max_: float) -> float:
    """Clamp float value"""
    return _rl.Clamp(value, min_, max_)


def lerp(start: float, end: float, amount: float) -> float:
    """Calculate linear interpolation between two floats"""
    return _rl.Lerp(start, end, amount)


def normalize(value: float, start: float, end: float) -> float:
    """Normalize input value within input range"""
    return _rl.Normalize(value, start, end)


def remap(value: float, input_start: float, input_end: float, output_start: float, output_end: float) -> float:
    """Remap input value within input range to output range"""
    return _rl.Remap(value, input_start, input_end, output_start, output_end)


# ----------------------------------------------------------------------------------
#  Module Functions Definition - Vector2 math
# ----------------------------------------------------------------------------------


def vector2_zero() -> Vector2:
    """Vector with components value 0.0f"""
    return _rl.Vector2Zero()


def vector2_one() -> Vector2:
    """Vector with components value 1.0f"""
    return _rl.Vector2One()


def vector2_add(v1: Vector2, v2: Vector2) -> Vector2:
    """Add two vectors (v1 + v2)"""
    return _rl.Vector2Add(v1, v2)


def vector2_add_value(v: Vector2, add: float) -> Vector2:
    """Add vector and float value"""
    return _rl.Vector2AddValue(v, add)


def vector2_subtract(v1: Vector2, v2: Vector2) -> Vector2:
    """Subtract two vectors (v1 - v2)"""
    return _rl.Vector2Subtract(v1, v2)


def vector2_subtract_value(v: Vector2, sub: float) -> Vector2:
    """Subtract vector by float value"""
    return _rl.Vector2SubtractValue(v, sub)


def vector2_length(v: Vector2) -> float:
    """Calculate vector length"""
    return _rl.Vector2Length(v)


def vector2_length_sqr(v: Vector2) -> float:
    """Calculate vector square length"""
    return _rl.Vector2LengthSqr(v)


def vector2_dot_product(v1: Vector2, v2: Vector2) -> float:
    """Calculate two vectors dot product"""
    return _rl.Vector2DotProduct(v1, v2)


def vector2_distance(v1: Vector2, v2: Vector2) -> float:
    """Calculate distance between two vectors"""
    return _rl.Vector2Distance(v1, v2)


def vector2_angle(v1: Vector2, v2: Vector2) -> float:
    """Calculate angle from two vectors in X-axis"""
    return _rl.Vector2Angle(v1, v2)


def vector2_scale(v: Vector2, scale: float) -> Vector2:
    """Scale vector (value: multiply)"""
    return _rl.Vector2Scale(v, scale)


def vector2_multiply(v1: Vector2, v2: Vector2) -> Vector2:
    """Multiply vector by vector"""
    return _rl.Vector2Multiply(v1, v2)


def vector2_negate(v: Vector2) -> Vector2:
    """Negate vector"""
    return _rl.Vector2Negate(v)


def vector2_divide(v1: Vector2, v2: Vector2) -> Vector2:
    """Divide vector by vector"""
    return _rl.Vector2Divide(v1, v2)


def vector2_normalize(v: Vector2) -> Vector2:
    """Normalize provided vector"""
    return _rl.Vector2Normalize(v)


def vector2_lerp(v1: Vector2, v2: Vector2, amount: float) -> Vector2:
    """Calculate linear interpolation between two vectors"""
    return _rl.Vector2Lerp(v1, v2, amount)


def vector2_reflect(v: Vector2, normal: Vector2) -> Vector2:
    """Calculate reflected vector to normal"""
    return _rl.Vector2Reflect(v, normal)


def vector2_rotate(v: Vector2, degs: float) -> Vector2:
    """Rotate Vector by float in Degrees."""
    return _rl.Vector2Rotate(v, degs)


def vector2_move_towards(v: Vector2, target: Vector2, max_distance: float) -> Vector2:
    """Move Vector towards target"""
    return _rl.Vector2MoveTowards(v, target, max_distance)


# ----------------------------------------------------------------------------------
#  Module Functions Definition - Vector3 math
# ----------------------------------------------------------------------------------

def vector3_zero() -> Vector3:
    """Vector with components value 0.0f"""
    return _rl.Vector3Zero()


def vector3_one() -> Vector3:
    """Vector with components value 1.0f"""
    return _rl.Vector3One()


def vector3_add(v1: Vector3, v2: Vector3) -> Vector3:
    """Add two vectors"""
    return _rl.Vector3Add(v1, v2)


def vector3_add_value(v: Vector3, add: float) -> Vector3:
    """Add vector and float value"""
    return _rl.Vector3AddValue(v, add)


def vector3_subtract(v1: Vector3, v2: Vector3) -> Vector3:
    """Subtract two vectors"""
    return _rl.Vector3Subtract(v1, v2)


def vector3_subtract_value(v: Vector3, sub: float) -> Vector3:
    """Subtract vector by float value"""
    return _rl.Vector3SubtractValue(v, sub)


def vector3_scale(v: Vector3, scalar: float) -> Vector3:
    """Multiply vector by scalar"""
    return _rl.Vector3Scale(v, scalar)


def vector3_multiply(v1: Vector3, v2: Vector3) -> Vector3:
    """Multiply vector by vector"""
    return _rl.Vector3Multiply(v1, v2)


def vector3_cross_product(v1: Vector3, v2: Vector3) -> Vector3:
    """Calculate two vectors cross product"""
    return _rl.Vector3CrossProduct(v1, v2)


def vector3_perpendicular(v: Vector3) -> Vector3:
    """Calculate one vector perpendicular vector"""
    return _rl.Vector3Perpendicular(v)


def vector3_length(v: Vector3) -> float:
    """Calculate vector length"""
    return _rl.Vector3Length(v)


def vector3_lengths_qr(v: Vector3) -> float:
    """Calculate vector square length"""
    return _rl.Vector3LengthSqr(v)


def vector3_dot_product(v1: Vector3, v2: Vector3) -> float:
    """Calculate two vectors dot product"""
    return _rl.Vector3DotProduct(v1, v2)


def vector3_distance(v1: Vector3, v2: Vector3) -> float:
    """Calculate distance between two vectors"""
    return _rl.Vector3Distance(v1, v2)


def vector3_negate(v: Vector3) -> Vector3:
    """Negate provided vector (direction: invert)"""
    return _rl.Vector3Negate(v)


def vector3_divide(v1: Vector3, v2: Vector3) -> Vector3:
    """Divide vector by vector"""
    return _rl.Vector3Divide(v1, v2)


def vector3_normalize(v: Vector3) -> Vector3:
    """Normalize provided vector"""
    return _rl.Vector3Normalize(v)


def vector3_ortho_normalize(v1: Vector3, v2: Vector3) -> None:
    """Orthonormalize provided vectors

    Makes vectors normalized and orthogonal to each other
    Gram-Schmidt function implementation
    """
    return _rl.Vector3OrthoNormalize(byref(v1), byref(v2))


def vector3_transform(v: Vector3, mat: Matrix) -> Vector3:
    """Transforms a Vector3 by a given Matrix"""
    return _rl.Vector3Transform(v, mat)


def vector3_rotate_by_quaternion(v: Vector3, q: Quaternion) -> Vector3:
    """Transform a vector by quaternion rotation"""
    return _rl.Vector3RotateByQuaternion(v, q)


def vector3_lerp(v1: Vector3, v2: Vector3, amount: float) -> Vector3:
    """Calculate linear interpolation between two vectors"""
    return _rl.Vector3Lerp(v1, v2, amount)


def vector3_reflect(v: Vector3, normal: Vector3) -> Vector3:
    """Calculate reflected vector to normal"""
    return _rl.Vector3Reflect(v, normal)


def vector3_min(v1: Vector3, v2: Vector3) -> Vector3:
    """Return min value for each pair of components"""
    return _rl.Vector3Min(v1, v2)


def vector3_max(v1: Vector3, v2: Vector3) -> Vector3:
    """Return max value for each pair of components"""
    return _rl.Vector3Max(v1, v2)


def vector3_barycenter(p: Vector3, a: Vector3, b: Vector3, c: Vector3) -> Vector3:
    """Compute barycenter coordinates (u, v, w) for point p with respect to triangle (a, b, c)

    NOTE: Assumes P is on the plane of the triangle
    """
    return _rl.Vector3Barycenter(p, a, b, c)


def vector3_to_float_v(v: Vector3) -> AnyVec3:
    """Returns Vector3 as float array"""
    result = _rl.Vector3ToFloatV(v)
    return tuple(result.contents[i] for i in (0, 1, 2))


# ----------------------------------------------------------------------------------
#  Module Functions Definition - Matrix math
# ----------------------------------------------------------------------------------

def matrix_determinant(mat: Matrix) -> float:
    """Compute matrix determinant"""
    return _rl.MatrixDeterminant(mat)


def matrix_trace(mat: Matrix) -> float:
    """Returns the trace of the matrix (sum of the values along diagonal: the)"""
    return _rl.MatrixTrace(mat)


def matrix_transpose(mat: Matrix) -> Matrix:
    """Transposes provided matrix"""
    return _rl.MatrixTranspose(mat)


def matrix_invert(mat: Matrix) -> Matrix:
    """Invert provided matrix"""
    return _rl.MatrixInvert(mat)


def matrix_normalize(mat: Matrix) -> Matrix:
    """Normalize provided matrix"""
    return _rl.MatrixNormalize(mat)


def matrix_identity() -> Matrix:
    """Returns identity matrix"""
    return _rl.MatrixIdentity()


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    """Add two matrices"""
    return _rl.MatrixAdd(left, right)


def matrix_subtract(left: Matrix, right: Matrix) -> Matrix:
    """Subtract two matrices (left - right)"""
    return _rl.MatrixSubtract(left, right)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    """Returns two matrix multiplication

    NOTE: When multiplying matrices... the order matters!
    """
    return _rl.MatrixMultiply(left, right)


def matrix_translate(x: float, y: float, z: float) -> Matrix:
    """Returns translation matrix"""
    return _rl.MatrixTranslate(x, y, z)


def matrix_rotate(axis: Vector3, angle: float) -> Matrix:
    """Create rotation matrix from axis and angle

    NOTE: Angle should be provided in radians
    """
    return _rl.MatrixRotate(axis, angle)


def matrix_rotate_x(angle: float) -> Matrix:
    """Returns x-rotation matrix (angle radians: in)"""
    return _rl.MatrixRotateX(angle)


def matrix_rotate_y(angle: float) -> Matrix:
    """Returns y-rotation matrix (angle radians: in)"""
    return _rl.MatrixRotateY(angle)


def matrix_rotate_z(angle: float) -> Matrix:
    """Returns z-rotation matrix (angle radians: in)"""
    return _rl.MatrixRotateZ(angle)


def matrix_rotate_xyz(ang: Vector3) -> Matrix:
    """Returns xyz-rotation matrix (angles radians: in)"""
    return _rl.MatrixRotateXYZ(ang)


def matrix_rotate_zyx(ang: Vector3) -> Matrix:
    """Returns zyx-rotation matrix (angles radians: in)"""
    return _rl.MatrixRotateZYX(ang)


def matrix_scale(x: float, y: float, z: float) -> Matrix:
    """Returns scaling matrix"""
    return _rl.MatrixScale(x, y, z)


def matrix_frustum(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix:
    """Returns perspective projection matrix"""
    return _rl.MatrixFrustum(left, right, bottom, top, near, far)


def matrix_perspective(fovy: float, aspect: float, near: float, far: float) -> Matrix:
    """Returns perspective projection matrix

    NOTE: Angle should be provided in radians
    """
    return _rl.MatrixPerspective(fovy, aspect, near, far)


def matrix_ortho(left: float, right: float, bottom: float, top: float, near: float, far: float) -> Matrix:
    """Returns orthographic projection matrix"""
    return _rl.MatrixOrtho(left, right, bottom, top, near, far)


def matrix_look_at(eye: Vector3, target: Vector3, up: Vector3) -> Matrix:
    """Returns camera look-at matrix (matrix: view)"""
    return _rl.MatrixLookAt(eye, target, up)


def matrix_to_float_v(mat: Matrix) -> Seq:
    """Returns float array of matrix data"""
    return _rl.MatrixToFloatV(mat)


# ----------------------------------------------------------------------------------
#  Module Functions Definition - Quaternion math
# ----------------------------------------------------------------------------------

def quaternion_add(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """Add two quaternions"""
    return _rl.QuaternionAdd(q1, q2)


def quaternion_add_value(q: Quaternion, add: float) -> Quaternion:
    """Add quaternion and float value"""
    return _rl.QuaternionAddValue(q, add)


def quaternion_subtract(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """Subtract two quaternions"""
    return _rl.QuaternionSubtract(q1, q2)


def quaternion_subtract_value(q: Quaternion, sub: float) -> Quaternion:
    """Subtract quaternion and float value"""
    return _rl.QuaternionSubtractValue(q, sub)


def quaternion_identity() -> Quaternion:
    """Returns identity quaternion"""
    return _rl.QuaternionIdentity()


def quaternion_length(q: Quaternion) -> float:
    """Computes the length of a quaternion"""
    return _rl.QuaternionLength(q)


def quaternion_normalize(q: Quaternion) -> Quaternion:
    """Normalize provided quaternion"""
    return _rl.QuaternionNormalize(q)


def quaternion_invert(q: Quaternion) -> Quaternion:
    """Invert provided quaternion"""
    return _rl.QuaternionInvert(q)


def quaternion_multiply(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """Calculate two quaternion multiplication"""
    return _rl.QuaternionMultiply(q1, q2)


def quaternion_scale(q: Quaternion, mul: float) -> Quaternion:
    """Scale quaternion by float value"""
    return _rl.QuaternionScale(q, mul)


def quaternion_divide(q1: Quaternion, q2: Quaternion) -> Quaternion:
    """Divide two quaternions"""
    return _rl.QuaternionDivide(q1, q2)


def quaternion_lerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
    """Calculate linear interpolation between two quaternions"""
    return _rl.QuaternionLerp(q1, q2, amount)


def quaternion_nlerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
    """Calculate slerp-optimized interpolation between two quaternions"""
    return _rl.QuaternionNlerp(q1, q2, amount)


def quaternion_slerp(q1: Quaternion, q2: Quaternion, amount: float) -> Quaternion:
    """Calculates spherical linear interpolation between two quaternions"""
    return _rl.QuaternionSlerp(q1, q2, amount)


def quaternion_from_vector3_to_vector3(from_: Vector3, to: Vector3) -> Quaternion:
    """Calculate quaternion based on the rotation from one vector to another"""
    return _rl.QuaternionFromVector3ToVector3(from_, to)


def quaternion_from_matrix(mat: Matrix) -> Quaternion:
    """Returns a quaternion for a given rotation matrix"""
    return _rl.QuaternionFromMatrix(mat)


def quaternion_to_matrix(q: Quaternion) -> Matrix:
    """Returns a matrix for a given quaternion"""
    return _rl.QuaternionToMatrix(q)


def quaternion_from_axis_angle(axis: Vector3, angle: float) -> Quaternion:
    """Returns rotation quaternion for an angle and axis

    NOTE: angle must be provided in radians
    """
    return _rl.QuaternionFromAxisAngle(axis, angle)


def quaternion_to_axis_angle(q: Quaternion, out_axis: Vector3, out_angle: float) -> float:
    """Returns the rotation angle and axis for a given quaternion"""
    ptr = FloatPtr(out_angle)
    _rl.QuaternionToAxisAngle(q, byref(out_axis), ptr)
    return ptr.contents[0]


def quaternion_from_euler(pitch: float, yaw: float, roll: float) -> Quaternion:
    """Returns the quaternion equivalent to Euler angles

    NOTE: Rotation order is ZYX
    """
    return _rl.QuaternionFromEuler(pitch, yaw, roll)


def quaternion_to_euler(q: Quaternion) -> Vector3:
    """Return the Euler angles equivalent to quaternion (roll, pitch, yaw)

    NOTE: Angles are returned in a Vector3 struct in degrees
    """
    return _rl.QuaternionToEuler(q)


def quaternion_transform(q: Quaternion, mat: Matrix) -> Quaternion:
    """Transform a quaternion given a transformation matrix"""
    return _rl.QuaternionTransform(q, mat)


def vector3_unproject(source: Vector3, projection: Matrix, view: Matrix) -> Vector3:
    """Projects a Vector3 from screen space into object space"""
    return _rl.Vector3Unproject(source, projection, view)
