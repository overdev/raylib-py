from library import rl as _rl
from structures import *



__all__ = [
    'get_font_default',
    'load_font',
    'load_font_ex',
    'load_font_data',
    'gen_image_font_atlas',
    'unload_font',
    'draw_fps',
    'draw_text',
    'draw_text_ex',
    'measure_text',
    'measure_text_ex',
    'format_text',
    'sub_text',
    'get_glyph_index',
]

_NOARGS = []

# -----------------------------------------------------------------------------------
# Font Loading and Text Drawing Functions (Module: text)
# -----------------------------------------------------------------------------------

# Font loading/unloading functions
_rl.GetFontDefault.argtypes = []
_rl.GetFontDefault.restype = Font
def get_font_default() -> Font:
    '''Get the default Font'''
    return _rl.GetFontDefault()


_rl.LoadFont.argtypes = [CharPtr]
_rl.LoadFont.restype = Font
def load_font(fileName: bytes) -> Font:
    '''Load font from file into GPU memory (VRAM)'''
    return _rl.LoadFont(fileName)


_rl.LoadFontEx.argtypes = [CharPtr, Int, Int, IntPtr]
_rl.LoadFontEx.restype = Font
def load_font_ex(fileName: bytes, fontSize: int, charsCount: int, fontChars: int) -> Font:
    '''Load font from file with extended parameters'''
    return _rl.LoadFontEx(fileName, fontSize, charsCount, fontChars)


_rl.LoadFontData.argtypes = [CharPtr, Int, IntPtr, Int, Bool]
_rl.LoadFontData.restype = CharInfoPtr
def load_font_data(fileName: bytes, fontSize: int, fontChars: int, charsCount: int, sdf: bool) -> CharInfoPtr:
    '''Load font data for further use'''
    return _rl.LoadFontData(fileName, fontSize, fontChars, charsCount, sdf)


_rl.GenImageFontAtlas.argtypes = [CharInfoPtr, Int, Int, Int, Int]
_rl.GenImageFontAtlas.restype = Image
def gen_image_font_atlas(chars: CharInfoPtr, fontSize: int, charsCount: int, padding: int, packMethod: int) -> Image:
    '''Generate image font atlas using chars info'''
    return _rl.GenImageFontAtlas(chars, fontSize, charsCount, padding, packMethod)


_rl.UnloadFont.argtypes = [Font]
_rl.UnloadFont.restype = None
def unload_font(font: Font) -> None:
    '''Unload Font from GPU memory (VRAM)'''
    return _rl.UnloadFont(font)

# Text drawing functions
_rl.DrawFPS.argtypes = [Int, Int]
_rl.DrawFPS.restype = None
def draw_fps(posX: int, posY: int) -> None:
    '''Shows current FPS'''
    return _rl.DrawFPS(posX, posY)


_rl.DrawText.argtypes = [CharPtr, Int, Int, Int, Color]
_rl.DrawText.restype = None
def draw_text(text: bytes, posX: int, posY: int, fontSize: int, color: Color) -> None:
    '''Draw text (using default font)'''
    return _rl.DrawText(text, posX, posY, fontSize, color)


_rl.DrawTextEx.argtypes = [Font, CharPtr, Vector2, Float, Float, Color]
_rl.DrawTextEx.restype = None
def draw_text_ex(font: Font, text: bytes, position: Vector2, fontSize: float, spacing: float, tint: Color) -> None:
    '''Draw text using font and additional parameters'''
    return _rl.DrawTextEx(font, text, position, fontSize, spacing, tint)


# Text misc. functions
_rl.MeasureText.argtypes = [CharPtr, Int]
_rl.MeasureText.restype = Int
def measure_text(text: bytes, fontSize: int) -> int:
    '''Measure string width for default font'''
    return _rl.MeasureText(text, fontSize)


_rl.MeasureTextEx.argtypes = [Font, CharPtr, Float, Float]
_rl.MeasureTextEx.restype = Vector2
def measure_text_ex(font: Font, text: bytes, fontSize: float, spacing: float) -> Vector2:
    '''Measure string size for Font'''
    return _rl.MeasureTextEx(font, text, fontSize, spacing)


_rl.FormatText.argtypes = [CharPtr]
_rl.FormatText.restype = CharPtr
def format_text(text: bytes, *args) -> bytes:
    '''Formatting of text with variables to "embed"'''
    return _rl.FormatText(text, *args)


_rl.SubText.argtypes = [CharPtr, Int, Int]
_rl.SubText.restype = CharPtr
def sub_text(text: bytes, position: int, length: int) -> bytes:
    '''Get a piece of a text string'''
    return _rl.SubText(text, position, length)


_rl.GetGlyphIndex.argtypes = [Font, Int]
_rl.GetGlyphIndex.restype = Int
def get_glyph_index(font: Font, character: int) -> int:
    '''Get index position for a unicode character on font'''
    return _rl.GetGlyphIndex(font, character)
