from library import rl as _rl
from structures import *
from ctypes import byref


__all__ = [
    'load_text',
    'load_shader',
    'load_shader_code',
    'unload_shader',
    'get_shader_default',
    'get_texture_default',
    'get_shader_location',
    'set_shader_value',
    'set_shader_valuei',
    'set_shader_value_matrix',
    'set_matrix_projection',
    'set_matrix_modelview',
    'get_matrix_modelview',
    'gen_texture_cubemap',
    'gen_texture_irradiance',
    'gen_texture_prefilter',
    'gen_texture_brdf',
    'begin_shader_mode',
    'end_shader_mode',
    'begin_blend_mode',
    'end_blend_mode',
    'get_vr_device_info',
    'init_vr_simulator',
    'close_vr_simulator',
    'is_vr_simulator_ready',
    'set_vr_distortion_shader',
    'update_vr_tracking',
    'toggle_vr_mode',
    'begin_vr_drawing',
    'end_vr_drawing',

    'byref',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Shaders System Functions (Module: rlgl)
# NOTE: This functions are useless when using OpenGL 1.1
# -----------------------------------------------------------------------------------

# Shader loading/unloading functions
_rl.LoadText.argtypes = [CharPtr]
_rl.LoadText.restype = CharPtr
def load_text(fileName: bytes) -> bytes:
    '''Load bytess array from text file'''
    return _rl.LoadText(fileName)


_rl.LoadShader.argtypes = [CharPtr, CharPtr]
_rl.LoadShader.restype = Shader
def load_shader(vsFileName: bytes, fsFileName: bytes) -> Shader:
    '''Load shader from files and bind default locations'''
    return _rl.LoadShader(vsFileName, fsFileName)


_rl.LoadShaderCode.argtypes = [CharPtr, CharPtr]
_rl.LoadShaderCode.restype = Shader
def load_shader_code(vsCode: bytes, fsCode: bytes) -> Shader:
    '''Load shader from code strings and bind default locations'''
    return _rl.LoadShaderCode(vsCode, fsCode)


_rl.UnloadShader.argtypes = [Shader]
_rl.UnloadShader.restype = None
def unload_shader(shader: Shader) -> None:
    '''Unload shader from GPU memory (VRAM)'''
    return _rl.UnloadShader(shader)


_rl.GetShaderDefault.argtypes = _NOARGS
_rl.GetShaderDefault.restype = Shader
def get_shader_default() -> Shader:
    '''Get default shader'''
    return _rl.GetShaderDefault()


_rl.GetTextureDefault.argtypes = _NOARGS
_rl.GetTextureDefault.restype = Texture2D
def get_texture_default() -> Texture2D:
    '''Get default texture'''
    return _rl.GetTextureDefault()


# Shader configuration functions
_rl.GetShaderLocation.argtypes = [Shader, CharPtr]
_rl.GetShaderLocation.restype = Int
def get_shader_location(shader: Shader, uniformName: bytes) -> int:
    '''Get shader uniform location'''
    return _rl.GetShaderLocation(shader, uniformName)


_rl.SetShaderValue.argtypes = [Shader, Int, FloatPtr, Int]
_rl.SetShaderValue.restype = None
def set_shader_value(shader: Shader, uniformLoc: int, value: FloatPtr, size: int) -> None:
    '''Set shader uniform value (float)'''
    return _rl.SetShaderValue(shader, uniformLoc, value, size)


_rl.SetShaderValuei.argtypes = [Shader, Int, IntPtr, Int]
_rl.SetShaderValuei.restype = None
def set_shader_valuei(shader: Shader, uniformLoc: int, value: IntPtr, size: int) -> None:
    '''Set shader uniform value (int)'''
    return _rl.SetShaderValuei(shader, uniformLoc, value, size)


_rl.SetShaderValueMatrix.argtypes = [Shader, Int, Matrix]
_rl.SetShaderValueMatrix.restype = None
def set_shader_value_matrix(shader: Shader, uniformLoc: Int, mat: Matrix) -> None:
    '''Set shader uniform value (matrix 4x4)'''
    return _rl.SetShaderValueMatrix(shader, uniformLoc, mat)


_rl.SetMatrixProjection.argtypes = [Matrix]
_rl.SetMatrixProjection.restype = None
def set_matrix_projection(proj: Matrix) -> None:
    '''Set a custom projection matrix (replaces internal projection matrix)'''
    return _rl.SetMatrixProjection(proj)


_rl.SetMatrixModelview.argtypes = [Matrix]
_rl.SetMatrixModelview.restype = None
def set_matrix_modelview(view: Matrix) -> None:
    '''Set a custom modelview matrix (replaces internal modelview matrix)'''
    return _rl.SetMatrixModelview(view)


_rl.GetMatrixModelview.argtypes = _NOARGS
_rl.GetMatrixModelview.restype = Matrix
def get_matrix_modelview() -> Matrix:
    '''Get internal modelview matrix'''
    return _rl.GetMatrixModelview()


# Texture maps generation (PBR)
# NOTE: Required shaders should be provided
_rl.GenTextureCubemap.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureCubemap.restype = Texture2D
def gen_texture_cubemap(shader: Shader, skyHDR: Texture2D, size: int) -> Texture2D:
    '''Generate cubemap texture from HDR texture'''
    return _rl.GenTextureCubemap(shader, skyHDR, size)


_rl.GenTextureIrradiance.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureIrradiance.restype = Texture2D
def gen_texture_irradiance(shader: Shader, cubemap: Texture2D, size: Int) -> Texture2D:
    '''Generate irradiance texture using cubemap data'''
    return _rl.GenTextureIrradiance(shader, cubemap, size)


_rl.GenTexturePrefilter.argtypes = [Shader, Texture2D, Int]
_rl.GenTexturePrefilter.restype = Texture2D
def gen_texture_prefilter(shader: Shader, cubemap: Texture2D, size: int) -> Texture2D:
    '''Generate prefilter texture using cubemap data'''
    return _rl.GenTexturePrefilter(shader, cubemap, size)


_rl.GenTextureBRDF.argtypes = [Shader, Texture2D, Int]
_rl.GenTextureBRDF.restype = Texture2D
def gen_texture_brdf(shader: Shader, cubemap: Texture2D, size: int) -> Texture2D:
    '''Generate BRDF texture using cubemap data'''
    return _rl.GenTextureBRDF(shader, cubemap, size)


# Shading begin/end functions
_rl.BeginShaderMode.argtypes = [Shader]
_rl.BeginShaderMode.restype = None
def begin_shader_mode(shader: Shader) -> None:
    '''Begin custom shader drawing'''
    return _rl.BeginShaderMode(shader)


_rl.EndShaderMode.argtypes = _NOARGS
_rl.EndShaderMode.restype = None
def end_shader_mode() -> None:
    '''End custom shader drawing (use default shader)'''
    return _rl.EndShaderMode()


_rl.BeginBlendMode.argtypes = [Int]
_rl.BeginBlendMode.restype = None
def begin_blend_mode(mode: int) -> None:
    '''Begin blending mode (alpha, additive, multiplied)'''
    return _rl.BeginBlendMode(mode)


_rl.EndBlendMode.argtypes = _NOARGS
_rl.EndBlendMode.restype = None
def end_blend_mode() -> None:
    '''End blending mode (reset to default: alpha blending)'''
    return _rl.EndBlendMode()


# VR control functions
_rl.GetVrDeviceInfo.argtypes = [Int]
_rl.GetVrDeviceInfo.restype = VrDeviceInfo
def get_vr_device_info(vrDeviceType: int):
    '''Get VR device information for some standard devices'''
    return _rl.GetVrDeviceInfo(vrDeviceType)


_rl.InitVrSimulator.argtypes = [VrDeviceInfo]
_rl.InitVrSimulator.restype = None
def init_vr_simulator(info: VrDeviceInfo) -> None:
    '''Init VR simulator for selected device parameters'''
    return _rl.InitVrSimulator(info)


_rl.CloseVrSimulator.argtypes = _NOARGS
_rl.CloseVrSimulator.restype = None
def close_vr_simulator() -> None:
    '''Close VR simulator for current device'''
    return _rl.CloseVrSimulator()


_rl.IsVrSimulatorReady.argtypes = _NOARGS
_rl.IsVrSimulatorReady.restype = bool
def is_vr_simulator_ready():
    '''Detect if VR simulator is ready'''
    return _rl.IsVrSimulatorReady()


_rl.SetVrDistortionShader.argtypes = [Shader]
_rl.SetVrDistortionShader.restype = None
def set_vr_distortion_shader(shader: Shader) -> None:
    '''Set VR distortion shader for stereoscopic rendering'''
    return _rl.SetVrDistortionShader(shader)


_rl.UpdateVrTracking.argtypes = [CameraPtr]
_rl.UpdateVrTracking.restype = None
def update_vr_tracking(camera: CameraPtr) -> None:
    '''Update VR tracking (position and orientation) and camera'''
    return _rl.UpdateVrTracking(camera)


_rl.ToggleVrMode.argtypes = _NOARGS
_rl.ToggleVrMode.restype = None
def toggle_vr_mode() -> None:
    '''Enable/Disable VR experience'''
    return _rl.ToggleVrMode()


_rl.BeginVrDrawing.argtypes = _NOARGS
_rl.BeginVrDrawing.restype = None
def begin_vr_drawing() -> None:
    '''Begin VR simulator stereo rendering'''
    return _rl.BeginVrDrawing()


_rl.EndVrDrawing.argtypes = _NOARGS
_rl.EndVrDrawing.restype = None
def end_vr_drawing() -> None:
    '''End VR simulator stereo rendering'''
    return _rl.EndVrDrawing()
