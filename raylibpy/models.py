from library import rl as _rl
from structures import *
from ctypes import byref


__all__ = [
    'draw_line3_d',
    'draw_circle3_d',
    'draw_cube',
    'draw_cube_v',
    'draw_cube_wires',
    'draw_cube_texture',
    'draw_sphere',
    'draw_sphere_ex',
    'draw_sphere_wires',
    'draw_cylinder',
    'draw_cylinder_wires',
    'draw_plane',
    'draw_ray',
    'draw_grid',
    'draw_gizmo',
    'load_model',
    'load_model_from_mesh',
    'unload_model',
    'load_mesh',
    'unload_mesh',
    'export_mesh',
    'mesh_bounding_box',
    'mesh_tangents',
    'mesh_binormals',
    'gen_mesh_plane',
    'gen_mesh_cube',
    'gen_mesh_sphere',
    'gen_mesh_hemi_sphere',
    'gen_mesh_cylinder',
    'gen_mesh_torus',
    'gen_mesh_knot',
    'gen_mesh_heightmap',
    'gen_mesh_cubicmap',
    'load_material',
    'load_material_default',
    'unload_material',
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
    'get_collision_ray_model',
    'get_collision_ray_triangle',
    'get_collision_ray_ground',

    'byref',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Basic 3d Shapes Drawing Functions (Module: models)
# -----------------------------------------------------------------------------------

# Basic geometric 3D shapes drawing functions
_rl.DrawLine3D.argtypes = [Vector3, Vector3, Color]
_rl.DrawLine3D.restype = None
def draw_line3_d(startPos: Vector3, endPos: Vector3, color: Color) -> None:
    '''Draw a line in 3D world space'''
    return _rl.DrawLine3D(startPos, endPos, color)


_rl.DrawCircle3D.argtypes = [Vector3, Float, Vector3, Float, Color]
_rl.DrawCircle3D.restype = None
def draw_circle3_d(center: Vector3, radius: float, rotationAxis: Vector3, rotationAngle: float, color: Color) -> None:
    '''Draw a circle in 3D world space'''
    return _rl.DrawCircle3D(center, radius, rotationAxis, rotationAngle, color)


_rl.DrawCube.argtypes = [Vector3, Float, Float, Float, Color]
_rl.DrawCube.restype = None
def draw_cube(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
    '''Draw cube'''
    return _rl.DrawCube(position, width, height, length, color)


_rl.DrawCubeV.argtypes = [Vector3, Vector3, Color]
_rl.DrawCubeV.restype = None
def draw_cube_v(position: Vector3, size: Vector3, color: Color) -> None:
    '''Draw cube (Vector version)'''
    return _rl.DrawCubeV(position, size, color)


_rl.DrawCubeWires.argtypes = [Vector3, Float, Float, Float, Color]
_rl.DrawCubeWires.restype = None
def draw_cube_wires(position: Vector3, width: float, height: float, length: float, color: Color) -> None:
    '''Draw cube wires'''
    return _rl.DrawCubeWires(position, width, height, length, color)


_rl.DrawCubeTexture.argtypes = [Texture2D, Vector3, Float, Float, Float, Color]
_rl.DrawCubeTexture.restype = None
def draw_cube_texture(texture: Texture2D, position: Vector3, width: float, height: float, length: float, color: Color) -> None:
    '''Draw cube textured'''
    return _rl.DrawCubeTexture(texture, position, width, height, length, color)


_rl.DrawSphere.argtypes = [Vector3, Float, Color]
_rl.DrawSphere.restype = None
def draw_sphere(centerPos: Vector3, radius: float, color: Color) -> None:
    '''Draw sphere'''
    return _rl.DrawSphere(centerPos, radius, color)


_rl.DrawSphereEx.argtypes = [Vector3, Float, Int, Int, Color]
_rl.DrawSphereEx.restype = None
def draw_sphere_ex(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
    '''Draw sphere with extended parameters'''
    return _rl.DrawSphereEx(centerPos, radius, rings, slices, color)


_rl.DrawSphereWires.argtypes = [Vector3, Float, Int, Int, Color]
_rl.DrawSphereWires.restype = None
def draw_sphere_wires(centerPos: Vector3, radius: float, rings: int, slices: int, color: Color) -> None:
    '''Draw sphere wires'''
    return _rl.DrawSphereWires(centerPos, radius, rings, slices, color)


_rl.DrawCylinder.argtypes = [Vector3, Float, Float, Float, Int, Color]
_rl.DrawCylinder.restype = None
def draw_cylinder(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
    '''Draw a cylinder/cone'''
    return _rl.DrawCylinder(position, radiusTop, radiusBottom, height, slices, color)


_rl.DrawCylinderWires.argtypes = [Vector3, Float, Float, Float, Int, Color]
_rl.DrawCylinderWires.restype = None
def draw_cylinder_wires(position: Vector3, radiusTop: float, radiusBottom: float, height: float, slices: int, color: Color) -> None:
    '''Draw a cylinder/cone wires'''
    return _rl.DrawCylinderWires(position, radiusTop, radiusBottom, height, slices, color)


_rl.DrawPlane.argtypes = [Vector3, Vector2, Color]
_rl.DrawPlane.restype = None
def draw_plane(centerPos: Vector3, size: Vector2, color: Color) -> None:
    '''Draw a plane XZ'''
    return _rl.DrawPlane(centerPos, size, color)


_rl.DrawRay.argtypes = [Ray, Color]
_rl.DrawRay.restype = None
def draw_ray(ray: Ray, color: Color) -> None:
    '''Draw a ray line'''
    return _rl.DrawRay(ray, color)


_rl.DrawGrid.argtypes = [Int, Float]
_rl.DrawGrid.restype = None
def draw_grid(slices: int, spacing: float) -> None:
    '''Draw a grid (centered at (0, 0, 0))'''
    return _rl.DrawGrid(slices, spacing)


_rl.DrawGizmo.argtypes = [Vector3]
_rl.DrawGizmo.restype = None
def draw_gizmo(position: Vector3) -> None:
    '''Draw simple gizmo'''
    return _rl.DrawGizmo(position)


# -----------------------------------------------------------------------------------
# Model 3d Loading and Drawing Functions (Module: models)
# -----------------------------------------------------------------------------------

# Model loading/unloading functions
_rl.LoadModel.argtypes = [CharPtr]
_rl.LoadModel.restype = Model
def load_model(fileName: bytes) -> Mesh:
    '''Load model from files (mesh and material)'''
    return _rl.LoadModel(fileName)


_rl.LoadModelFromMesh.argtypes = [Mesh]
_rl.LoadModelFromMesh.restype = Model
def load_model_from_mesh(mesh: Mesh) -> Mesh:
    '''Load model from generated mesh'''
    return _rl.LoadModelFromMesh(mesh)


_rl.UnloadModel.argtypes = [Model]
_rl.UnloadModel.restype = None
def unload_model(model: Model) -> None:
    '''Unload model from memory (RAM and/or VRAM)'''
    return _rl.UnloadModel(model)


# Mesh loading/unloading functions
_rl.LoadMesh.argtypes = [CharPtr]
_rl.LoadMesh.restype = Mesh
def load_mesh(fileName: bytes) -> Mesh:
    '''Load mesh from file'''
    return _rl.LoadMesh(fileName)


_rl.UnloadMesh.argtypes = [MeshPtr]
_rl.UnloadMesh.restype = None
def unload_mesh(mesh: Mesh) -> None:
    '''Unload mesh from memory (RAM and/or VRAM)'''
    return _rl.UnloadMesh(mesh)


_rl.ExportMesh.argtypes = [CharPtr, Mesh]
_rl.ExportMesh.restype = None
def export_mesh(fileName: bytes, mesh: Mesh) -> None:
    '''Export mesh as an OBJ file'''
    return _rl.ExportMesh(fileName, mesh)


# Mesh manipulation functions
_rl.MeshBoundingBox.argtypes = [Mesh]
_rl.MeshBoundingBox.restype = BoundingBox
def mesh_bounding_box(mesh: Mesh) -> BoundingBox:
    '''Compute mesh bounding box limits'''
    return _rl.MeshBoundingBox(mesh)


_rl.MeshTangents.argtypes = [MeshPtr]
_rl.MeshTangents.restype = None
def mesh_tangents(mesh: MeshPtr) -> None:
    '''Compute mesh tangents'''
    return _rl.MeshTangents(mesh)


_rl.MeshBinormals.argtypes = [MeshPtr]
_rl.MeshBinormals.restype = None
def mesh_binormals(mesh: MeshPtr) -> None:
    '''Compute mesh binormals'''
    return _rl.MeshBinormals(mesh)


# Mesh generation functions
_rl.GenMeshPlane.argtypes = [Float, Float, Int, Int]
_rl.GenMeshPlane.restype = Mesh
def gen_mesh_plane(width: float, length: float, resX: int, resZ: int) -> Mesh:
    '''Generate plane mesh (with subdivisions)'''
    return _rl.GenMeshPlane(width, length, resX, resZ)


_rl.GenMeshCube.argtypes = [Float, Float, Float]
_rl.GenMeshCube.restype = Mesh
def gen_mesh_cube(width: float, height: float, length: float) -> Mesh:
    '''Generate cuboid mesh'''
    return _rl.GenMeshCube(width, height, length)


_rl.GenMeshSphere.argtypes = [Float, Int, Int]
_rl.GenMeshSphere.restype = Mesh
def gen_mesh_sphere(radius: float, rings: int, slices: int) -> Mesh:
    '''Generate sphere mesh (standard sphere)'''
    return _rl.GenMeshSphere(radius, rings, slices)


_rl.GenMeshHemiSphere.argtypes = [Float, Int, Int]
_rl.GenMeshHemiSphere.restype = Mesh
def gen_mesh_hemi_sphere(radius: float, rings: int, slices: int) -> Mesh:
    '''Generate half-sphere mesh (no bottom cap)'''
    return _rl.GenMeshHemiSphere(radius, rings, slices)


_rl.GenMeshCylinder.argtypes = [Float, Float, Int]
_rl.GenMeshCylinder.restype = Mesh
def gen_mesh_cylinder(radius: float, height: float, slices: int) -> Mesh:
    '''Generate cylinder mesh'''
    return _rl.GenMeshCylinder(radius, height, slices)


_rl.GenMeshTorus.argtypes = [Float, Float, Int, Int]
_rl.GenMeshTorus.restype = Mesh
def gen_mesh_torus(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
    '''Generate torus mesh'''
    return _rl.GenMeshTorus(radius, size, radSeg, sides)


_rl.GenMeshKnot.argtypes = [Float, Float, Int, Int]
_rl.GenMeshKnot.restype = Mesh
def gen_mesh_knot(radius: float, size: float, radSeg: int, sides: int) -> Mesh:
    '''Generate trefoil knot mesh'''
    return _rl.GenMeshKnot(radius, size, radSeg, sides)


_rl.GenMeshHeightmap.argtypes = [Image, Vector3]
_rl.GenMeshHeightmap.restype = Mesh
def gen_mesh_heightmap(heightmap: Image, size: Vector3) -> Mesh:
    '''Generate heightmap mesh from image data'''
    return _rl.GenMeshHeightmap(heightmap, size)


_rl.GenMeshCubicmap.argtypes = [Image, Vector3]
_rl.GenMeshCubicmap.restype = Mesh
def gen_mesh_cubicmap(cubicmap: Image, cubeSize: Vector3) -> Mesh:
    '''Generate cubes-based map mesh from image data'''
    return _rl.GenMeshCubicmap(cubicmap, cubeSize)


# Material loading/unloading functions
_rl.LoadMaterial.argtypes = [CharPtr]
_rl.LoadMaterial.restype = Material
def load_material(fileName: bytes) -> Material:
    '''Load material from file'''
    return _rl.LoadMaterial(fileName)


_rl.LoadMaterialDefault.argtypes = _NOARGS
_rl.LoadMaterialDefault.restype = Material
def load_material_default() -> Material:
    '''Load default material (Supports: DIFFUSE, SPECULAR, NORMAL maps)'''
    return _rl.LoadMaterialDefault()


_rl.UnloadMaterial.argtypes = [Material]
_rl.UnloadMaterial.restype = None
def unload_material(material: Material) -> None:
    '''Unload material from GPU memory (VRAM)'''
    return _rl.UnloadMaterial(material)


# Model drawing functions
_rl.DrawModel.argtypes = [Model, Vector3, Float, Color]
_rl.DrawModel.restype = None
def draw_model(model: Model, position: Vector3, scale: float, tint: Color) -> None:
    '''Draw a model (with texture if set)'''
    return _rl.DrawModel(model, position, scale, tint)


_rl.DrawModelEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
_rl.DrawModelEx.restype = None
def draw_model_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
    '''Draw a model with extended parameters'''
    return _rl.DrawModelEx(model, position, rotationAxis, rotationAngle, scale, tint)


_rl.DrawModelWires.argtypes = [Model, Vector3, Float, Color]
_rl.DrawModelWires.restype = None
def draw_model_wires(model: Model, position: Vector3, scale: float, tint: Color) -> None:
    '''Draw a model wires (with texture if set)'''
    return _rl.DrawModelWires(model, position, scale, tint)


_rl.DrawModelWiresEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
_rl.DrawModelWiresEx.restype = None
def draw_model_wires_ex(model: Model, position: Vector3, rotationAxis: Vector3, rotationAngle: float, scale: Vector3, tint: Color) -> None:
    '''Draw a model wires (with texture if set) with extended parameters'''
    return _rl.DrawModelWiresEx(model, position, rotationAxis, rotationAngle, scale, tint)


_rl.DrawBoundingBox.argtypes = [BoundingBox, Color]
_rl.DrawBoundingBox.restype = None
def draw_bounding_box(box: BoundingBox, color: Color) -> None:
    '''Draw bounding box (wires)'''
    return _rl.DrawBoundingBox(box, color)


_rl.DrawBillboard.argtypes = [Camera, Texture2D, Vector3, Float, Color]
_rl.DrawBillboard.restype = None
def draw_billboard(camera: Camera, texture: Texture2D, center: Vector3, size: float, tint: Color) -> None:
    '''Draw a billboard texture'''
    return _rl.DrawBillboard(camera, texture, center, size, tint)


_rl.DrawBillboardRec.argtypes = [Camera, Texture2D, Rectangle, Vector3, Float, Color]
_rl.DrawBillboardRec.restype = None
def draw_billboard_rec(camera: Camera, texture: Texture2D, sourceRec: Rectangle, center: Vector3, size: float, tint: Color) -> None:
    '''Draw a billboard texture defined by sourceRec'''
    return _rl.DrawBillboardRec(camera, texture, sourceRec, center, size, tint)


# Collision detection functions
_rl.CheckCollisionSpheres.argtypes = [Vector3, Float, Vector3, Float]
_rl.CheckCollisionSpheres.restype = Bool
def check_collision_spheres(centerA: Vector3, radiusA: float, centerB: Vector3, radiusB: float) -> bool:
    '''Detect collision between two spheres'''
    return _rl.CheckCollisionSpheres(centerA, radiusA, centerB, radiusB)


_rl.CheckCollisionBoxes.argtypes = [BoundingBox, BoundingBox]
_rl.CheckCollisionBoxes.restype = Bool
def check_collision_boxes(box1: BoundingBox, box2: BoundingBox) -> bool:
    '''Detect collision between two bounding boxes'''
    return _rl.CheckCollisionBoxes(box1, box2)


_rl.CheckCollisionBoxSphere.argtypes = [BoundingBox, Vector3, Float]
_rl.CheckCollisionBoxSphere.restype = Bool
def check_collision_box_sphere(box: BoundingBox, centerSphere: Vector3, radiusSphere: float) -> bool:
    '''Detect collision between box and sphere'''
    return _rl.CheckCollisionBoxSphere(box, centerSphere, radiusSphere)


_rl.CheckCollisionRaySphere.argtypes = [Ray, Vector3, Float]
_rl.CheckCollisionRaySphere.restype = Bool
def check_collision_ray_sphere(ray: Ray, spherePosition: Vector3, sphereRadius: float) -> bool:
    '''Detect collision between ray and sphere'''
    return _rl.CheckCollisionRaySphere(ray, spherePosition, sphereRadius)


_rl.CheckCollisionRaySphereEx.argtypes = [Ray, Vector3, Float, Vector3Ptr]
_rl.CheckCollisionRaySphereEx.restype = Bool
def check_collision_ray_sphere_ex(ray: Ray, spherePosition: Vector3, sphereRadius: float, collisionPoint: Vector3Ptr) -> bool:
    '''Detect collision between ray and sphere, returns collision point'''
    return _rl.CheckCollisionRaySphereEx(ray, spherePosition, sphereRadius, collisionPoint)


_rl.CheckCollisionRayBox.argtypes = [Ray, BoundingBox]
_rl.CheckCollisionRayBox.restype = Bool
def check_collision_ray_box(ray: Ray, box: BoundingBox) -> bool:
    '''Detect collision between ray and box'''
    return _rl.CheckCollisionRayBox(ray, box)


_rl.GetCollisionRayModel.argtypes = [Ray, ModelPtr]
_rl.GetCollisionRayModel.restype = RayHitInfo
def get_collision_ray_model(ray: Ray, model: ModelPtr) -> RayHitInfo:
    '''Get collision info between ray and model'''
    return _rl.GetCollisionRayModel(ray, model)


_rl.GetCollisionRayTriangle.argtypes = [Ray, Vector3, Vector3, Vector3]
_rl.GetCollisionRayTriangle.restype = RayHitInfo
def get_collision_ray_triangle(ray: Ray, p1: Vector3, p2: Vector3, p3: Vector3) -> RayHitInfo:
    '''Get collision info between ray and triangle'''
    return _rl.GetCollisionRayTriangle(ray, p1, p2, p3)


_rl.GetCollisionRayGround.argtypes = [Ray, Float]
_rl.GetCollisionRayGround.restype = RayHitInfo
def get_collision_ray_ground(ray: Ray, groundHeight: float) -> RayHitInfo:
    '''Get collision info between ray and ground plane (Y-normal plane)'''
    return _rl.GetCollisionRayGround(ray, groundHeight)
