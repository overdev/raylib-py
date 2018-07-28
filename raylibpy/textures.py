from library import rl as _rl
from structures import *
from ctypes import byref
from typing import Tuple


__all__ = [
    'load_image',
    'load_image_ex',
    'load_image_pro',
    'load_image_raw',
    'export_image',
    'load_texture',
    'load_texture_from_image',
    'load_render_texture',
    'unload_image',
    'unload_texture',
    'unload_render_texture',
    'get_image_data',
    'get_image_data_normalized',
    'get_pixel_data_size',
    'get_texture_data',
    'update_texture',
    'image_copy',
    'image_to_pot',
    'image_format',
    'image_alpha_mask',
    'image_alpha_clear',
    'image_alpha_crop',
    'image_alpha_premultiply',
    'image_crop',
    'image_resize',
    'image_resize_nn',
    'image_resize_canvas',
    'image_mipmaps',
    'image_dither',
    'image_text',
    'image_text_ex',
    'image_draw',
    'image_draw_rectangle',
    'image_draw_text',
    'image_draw_text_ex',
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
    'gen_image_color',
    'gen_image_gradient_v',
    'gen_image_gradient_h',
    'gen_image_gradient_radial',
    'gen_image_checked',
    'gen_image_white_noise',
    'gen_image_perlin_noise',
    'gen_image_cellular',
    'gen_texture_mipmaps',
    'set_texture_filter',
    'set_texture_wrap',
    'draw_texture',
    'draw_texture_v',
    'draw_texture_ex',
    'draw_texture_rec',
    'draw_texture_pro',
]

_NOARGS = []


# -----------------------------------------------------------------------------------
# Texture Loading and Drawing Functions (Module: textures)
# -----------------------------------------------------------------------------------

# Image/Texture2D data loading/unloading/saving functions
_rl.LoadImage.argtypes = [CharPtr]
_rl.LoadImage.restype = Image
def load_image(file_name: bytes) -> Image:
    '''Load image from file into CPU memory (RAM)'''
    return _rl.LoadImage(file_name)


_rl.LoadImageEx.argtypes = [ColorPtr, Int, Int]
_rl.LoadImageEx.restype = Image
def load_image_ex(pixels: ColorPtr, width: int, height: int) -> Image:
    '''Load image from Color array data (RGBA - 32bit)'''
    return _rl.LoadImageEx(pixels, width, height)


_rl.LoadImagePro.argtypes = [VoidPtr, Int, Int, Int]
_rl.LoadImagePro.restype = Image
def load_image_pro(data: VoidPtr, width: int, height: int, format: int) -> Image:
    '''Load image from raw data with parameters'''
    return _rl.LoadImagePro(data, width, height, format)


_rl.LoadImageRaw.argtypes = [CharPtr, Int, Int, Int, Int]
_rl.LoadImageRaw.restype = Image
def load_image_raw(fileName: bytes, width: int, height: int, format: int, headerSize: int) -> Image:
    '''Load image from RAW file data'''
    return _rl.LoadImageRaw(fileName, width, height, format, headerSize)


_rl.ExportImage.argtypes = [CharPtr, Image]
_rl.ExportImage.restype = None
def export_image(fileName: bytes, image: Image) -> None:
    '''Export image as a PNG file'''
    return _rl.ExportImage(fileName, image)


_rl.LoadTexture.argtypes = [CharPtr]
_rl.LoadTexture.restype = Texture2D
def load_texture(fileName: bytes) -> Texture2D:
    '''Load texture from file into GPU memory (VRAM)'''
    return _rl.LoadTexture(fileName)


_rl.LoadTextureFromImage.argtypes = [Image]
_rl.LoadTextureFromImage.restype = Texture2D
def load_texture_from_image(image: Image) -> Texture2D:
    '''Load texture from image data'''
    return _rl.LoadTextureFromImage(image)


_rl.LoadRenderTexture.argtypes = [Int, Int]
_rl.LoadRenderTexture.restype = RenderTexture2D
def load_render_texture(width: int, height: int) -> RenderTexture2D:
    '''Load texture for rendering (framebuffer)'''
    return _rl.LoadRenderTexture(width, height)


_rl.UnloadImage.argtypes = [Image]
_rl.UnloadImage.restype = None
def unload_image(image: Image) -> None:
    '''Unload image from CPU memory (RAM)'''
    return _rl.UnloadImage(image)


_rl.UnloadTexture.argtypes = [Texture2D]
_rl.UnloadTexture.restype = None
def unload_texture(texture: Texture2D) -> None:
    '''Unload texture from GPU memory (VRAM)'''
    return _rl.UnloadTexture(texture)


_rl.UnloadRenderTexture.argtypes = [RenderTexture2D]
_rl.UnloadRenderTexture.restype = None
def unload_render_texture(target: RenderTexture2D) -> None:
    '''Unload render texture from GPU memory (VRAM)'''
    return _rl.UnloadRenderTexture(target)


_rl.GetImageData.argtypes = [Image]
_rl.GetImageData.restype = ColorPtr
def get_image_data(image: Image) -> ColorPtr:
    '''Get pixel data from image as a Color struct array'''
    return _rl.GetImageData(image)


_rl.GetImageDataNormalized.argtypes = [Image]
_rl.GetImageDataNormalized.restype = Vector4Ptr
def get_image_data_normalized(image: Image) -> Vector4Ptr:
    '''Get pixel data from image as Vector4 array (float normalized)'''
    return _rl.GetImageDataNormalized(image)


_rl.GetPixelDataSize.argtypes = [Int, Int, Int]
_rl.GetPixelDataSize.restype = Int
def get_pixel_data_size(width: int, height: int, format: int) -> int:
    '''Get pixel data size in bytes (image or texture)'''
    return _rl.GetPixelDataSize(width, height, format)


_rl.GetTextureData.argtypes = [Texture2D]
_rl.GetTextureData.restype = Image
def get_texture_data(texture: Texture2D) -> Image:
    '''Get pixel data from GPU texture and return an Image'''
    return _rl.GetTextureData(texture)


_rl.UpdateTexture.argtypes = [Texture2D, VoidPtr]
_rl.UpdateTexture.restype = None
def update_texture(texture: Texture2D, pixels: bytes) -> None:
    '''Update GPU texture with new data'''
    return _rl.UpdateTexture(texture, pixels)


# Image manipulation functions
_rl.ImageCopy.argtypes = [Image]
_rl.ImageCopy.restype = Image
def image_copy(image: Image):
    '''Create an image duplicate (useful for transformations)'''
    return _rl.ImageCopy(image)


_rl.ImageToPOT.argtypes = [ImagePtr, Color]
_rl.ImageToPOT.restype = None
def image_to_pot(image: Image, fillColor: Color) -> None:
    '''Convert image to POT (power-of-two)'''
    return _rl.ImageToPOT(image, fillColor)


_rl.ImageFormat.argtypes = [ImagePtr, Int]
_rl.ImageFormat.restype = None
def image_format(image: Image, newFormat: int) -> None:
    '''Convert image data to desired format'''
    return _rl.ImageFormat(image, newFormat)


_rl.ImageAlphaMask.argtypes = [ImagePtr, Image]
_rl.ImageAlphaMask.restype = None
def image_alpha_mask(image: Image, alphaMask: Image) -> None:
    '''Apply alpha mask to image'''
    return _rl.ImageAlphaMask(image, alphaMask)


_rl.ImageAlphaClear.argtypes = [ImagePtr, Color, Float]
_rl.ImageAlphaClear.restype = None
def image_alpha_clear(image: Image, color: Color, threshold: float) -> None:
    '''Clear alpha channel to desired color'''
    return _rl.ImageAlphaClear(image, color, threshold)


_rl.ImageAlphaCrop.argtypes = [ImagePtr, Float]
_rl.ImageAlphaCrop.restype = None
def image_alpha_crop(image: Image, threshold: float) -> None:
    '''Crop image depending on alpha value'''
    return _rl.ImageAlphaCrop(image, threshold)


_rl.ImageAlphaPremultiply.argtypes = [ImagePtr]
_rl.ImageAlphaPremultiply.restype = None
def image_alpha_premultiply(image: Image) -> None:
    '''Premultiply alpha channel'''
    return _rl.ImageAlphaPremultiply(image)


_rl.ImageCrop.argtypes = [ImagePtr, Rectangle]
_rl.ImageCrop.restype = None
def image_crop(image: Image, crop: Rectangle) -> None:
    '''Crop an image to a defined rectangle'''
    return _rl.ImageCrop(image, crop)


_rl.ImageResize.argtypes = [ImagePtr, Int, Int]
_rl.ImageResize.restype = None
def image_resize(image: Image, newWidth: int, newHeight: int) -> None:
    '''Resize image (bilinear filtering)'''
    return _rl.ImageResize(image, newWidth, newHeight)


_rl.ImageResizeNN.argtypes = [ImagePtr, Int, Int]
_rl.ImageResizeNN.restype = None
def image_resize_nn(image: Image, newWidth: int, newHeight: int) -> None:
    '''Resize image (Nearest-Neighbor scaling algorithm)'''
    return _rl.ImageResizeNN(image, newWidth, newHeight)


_rl.ImageResizeCanvas.argtypes = [ImagePtr, Int, Int, Int, Int, Color]
_rl.ImageResizeCanvas.restype = None
def image_resize_canvas(image: Image, newWidth: int, newHeight: int, offsetX: int, offsetY: int, color: Color) -> None:
    '''Resize canvas and fill with color'''
    return _rl.ImageResizeCanvas(image, newWidth, newHeight, offsetX, offsetY, color)


_rl.ImageMipmaps.argtypes = [ImagePtr]
_rl.ImageMipmaps.restype = None
def image_mipmaps(image: Image) -> None:
    '''Generate all mipmap levels for a provided image'''
    return _rl.ImageMipmaps(image)


_rl.ImageDither.argtypes = [ImagePtr, Int, Int, Int, Int]
_rl.ImageDither.restype = None
def image_dither(image: Image, rBpp: int, gBpp: int, bBpp: int, aBpp: int) -> None:
    '''Dither image data to 16bpp or lower (Floyd-Steinberg dithering)'''
    return _rl.ImageDither(image, rBpp, gBpp, bBpp, aBpp)


_rl.ImageText.argtypes = [CharPtr, Int, Color]
_rl.ImageText.restype = Image
def image_text(text: bytes, fontSize: int, color: Color) -> Image:
    '''Create an image from text (default font)'''
    return _rl.ImageText(text, fontSize, color)


_rl.ImageTextEx.argtypes = [Font, CharPtr, Float, Float, Color]
_rl.ImageTextEx.restype = Image
def image_text_ex(font: Font, text: bytes, fontSize: float, spacing: float, tint: Color) -> Image:
    '''Create an image from text (custom sprite font)'''
    return _rl.ImageTextEx(font, text, fontSize, spacing, tint)


_rl.ImageDraw.argtypes = [ImagePtr, Image, Rectangle, Rectangle]
_rl.ImageDraw.restype = None
def image_draw(dst: Image, src: Image, srcRec: Rectangle, dstRec: Rectangle) -> None:
    '''Draw a source image within a destination image'''
    return _rl.ImageDraw(dst, src, srcRec, dstRec)


_rl.ImageDrawRectangle.argtypes = [ImagePtr, Vector2, Rectangle, Color]
_rl.ImageDrawRectangle.restype = None
def image_draw_rectangle(dst: Image, position: Vector2, rec: Rectangle, color: Color) -> None:
    '''Draw rectangle within an image'''
    return _rl.ImageDrawRectangle(dst, position, rec, color)


_rl.ImageDrawText.argtypes = [ImagePtr, Vector2, CharPtr, Int, Color]
_rl.ImageDrawText.restype = None
def image_draw_text(dst: Image, position: Vector2, text: bytes, fontSize: int, color: Color) -> None:
    '''Draw text (default font) within an image (destination)'''
    return _rl.ImageDrawText(dst, position, text, fontSize, color)


_rl.ImageDrawTextEx.argtypes = [ImagePtr, Vector2, Font, CharPtr, Float, Float, Color]
_rl.ImageDrawTextEx.restype = None
def image_draw_text_ex(dst: Image, position: Vector2, font: Font, text: bytes, fontSize: float, spacing: float, color: Color) -> None:
    '''Draw text (custom sprite font) within an image (destination)'''
    return _rl.ImageDrawTextEx(dst, position, font, text, fontSize, spacing, color)


_rl.ImageFlipVertical.argtypes = [ImagePtr]
_rl.ImageFlipVertical.restype = None
def image_flip_vertical(image: Image) -> None:
    '''Flip image vertically'''
    return _rl.ImageFlipVertical(image)


_rl.ImageFlipHorizontal.argtypes = [ImagePtr]
_rl.ImageFlipHorizontal.restype = None
def image_flip_horizontal(image: Image) -> None:
    '''Flip image horizontally'''
    return _rl.ImageFlipHorizontal(image)


_rl.ImageRotateCW.argtypes = [ImagePtr]
_rl.ImageRotateCW.restype = None
def image_rotate_cw(image: Image) -> None:
    '''Rotate image clockwise 90deg'''
    return _rl.ImageRotateCW(image)


_rl.ImageRotateCCW.argtypes = [ImagePtr]
_rl.ImageRotateCCW.restype = None
def image_rotate_ccw(image: Image) -> None:
    '''Rotate image counter-clockwise 90deg'''
    return _rl.ImageRotateCCW(image)


_rl.ImageColorTint.argtypes = [ImagePtr, Color]
_rl.ImageColorTint.restype = None
def image_color_tint(image: Image, color: Color) -> None:
    '''Modify image color: tint'''
    return _rl.ImageColorTint(image, color)


_rl.ImageColorInvert.argtypes = [ImagePtr]
_rl.ImageColorInvert.restype = None
def image_color_invert(image: Image) -> None:
    '''Modify image color: invert'''
    return _rl.ImageColorInvert(image)


_rl.ImageColorGrayscale.argtypes = [ImagePtr]
_rl.ImageColorGrayscale.restype = None
def image_color_grayscale(image: Image) -> None:
    '''Modify image color: grayscale'''
    return _rl.ImageColorGrayscale(image)


_rl.ImageColorContrast.argtypes = [ImagePtr, Float]
_rl.ImageColorContrast.restype = None
def image_color_contrast(image: Image, contrast: float) -> None:
    '''Modify image color: contrast (-100 to 100)'''
    return _rl.ImageColorContrast(image, contrast)


_rl.ImageColorBrightness.argtypes = [ImagePtr, Int]
_rl.ImageColorBrightness.restype = None
def image_color_brightness(image: Image, brightness: int) -> None:
    '''Modify image color: brightness (-255 to 255)'''
    return _rl.ImageColorBrightness(image, brightness)


_rl.ImageColorReplace.argtypes = [ImagePtr, Color, Color]
_rl.ImageColorReplace.restype = None
def image_color_replace(image: Image, color: Color, replace: Color) -> None:
    '''Modify image color: replace color'''
    return _rl.ImageColorReplace(image, color, replace)


_rl.GenImageColor.argtypes = [Int, Int, Color]
_rl.GenImageColor.restype = Image
def gen_image_color(width: int, height: int, color: Color) -> Image:
    '''Generate image: plain color'''
    return _rl.GenImageColor(width, height, color)


_rl.GenImageGradientV.argtypes = [Int, Int, Color, Color]
_rl.GenImageGradientV.restype = Image
def gen_image_gradient_v(width: int, height: int, top: Color, bottom: Color) -> Image:
    '''Generate image: vertical gradient'''
    return _rl.GenImageGradientV(width, height, top, bottom)


_rl.GenImageGradientH.argtypes = [Int, Int, Color, Color]
_rl.GenImageGradientH.restype = Image
def gen_image_gradient_h(width: int, height: int, left: Color, right: Color) -> Image:
    '''Generate image: horizontal gradient'''
    return _rl.GenImageGradientH(width, height, left, right)


_rl.GenImageGradientRadial.argtypes = [Int, Int, Float, Color, Color]
_rl.GenImageGradientRadial.restype = Image
def gen_image_gradient_radial(width: int, height: int, density: float, inner: Color, outer: Color) -> Image:
    '''Generate image: radial gradient'''
    return _rl.GenImageGradientRadial(width, height, density, inner, outer)


_rl.GenImageChecked.argtypes = [Int, Int, Int, Int, Color, Color]
_rl.GenImageChecked.restype = Image
def gen_image_checked(width: int, height: int, checksX: int, checksY: int, col1: Color, col2: Color) -> Image:
    '''Generate image: checked'''
    return _rl.GenImageChecked(width, height, checksX, checksY, col1, col2)


_rl.GenImageWhiteNoise.argtypes = [Int, Int, Float]
_rl.GenImageWhiteNoise.restype = Image
def gen_image_white_noise(width: int, height: int, factor: float) -> Image:
    '''Generate image: white noise'''
    return _rl.GenImageWhiteNoise(width, height, factor)


_rl.GenImagePerlinNoise.argtypes = [Int, Int, Int, Int, Float]
_rl.GenImagePerlinNoise.restype = Image
def gen_image_perlin_noise(width: int, height: int, offsetX: int, offsetY: int, scale: float) -> Image:
    '''Generate image: perlin noise'''
    return _rl.GenImagePerlinNoise(width, height, offsetX, offsetY, scale)


_rl.GenImageCellular.argtypes = [Int, Int, Int]
_rl.GenImageCellular.restype = Image
def gen_image_cellular(width: int, height: int, tileSize: int) -> Image:
    '''Generate image: cellular algorithm. Bigger tileSize means bigger cells'''
    return _rl.GenImageCellular(width, height, tileSize)


_rl.GenTextureMipmaps.argtypes = [Texture2DPtr]
_rl.GenTextureMipmaps.restype = None
def gen_texture_mipmaps(texture: Texture2DPtr) -> None:
    '''Generate GPU mipmaps for a texture'''
    return _rl.GenTextureMipmaps(texture)


_rl.SetTextureFilter.argtypes = [Texture2D, Int]
_rl.SetTextureFilter.restype = None
def set_texture_filter(texture: Texture2D, filterMode: int) -> None:
    '''Set texture scaling filter mode'''
    return _rl.SetTextureFilter(texture, filterMode)


_rl.SetTextureWrap.argtypes = [Texture2D, Int]
_rl.SetTextureWrap.restype = None
def set_texture_wrap(texture: Texture2D, wrapMode: int) -> None:
    '''Set texture wrapping mode'''
    return _rl.SetTextureWrap(texture, wrapMode)


_rl.DrawTexture.argtypes = [Texture2D, Int, Int, Color]
_rl.DrawTexture.restype = None
def draw_texture(texture: Texture2D, posX: int, posY: int, tint: Color) -> None:
    '''Draw a Texture2D'''
    return _rl.DrawTexture(texture, posX, posY, tint)


_rl.DrawTextureV.argtypes = [Texture2D, Vector2, Color]
_rl.DrawTextureV.restype = None
def draw_texture_v(texture: Texture2D, position: Vector2, tint: Color) -> None:
    '''Draw a Texture2D with position defined as Vector2'''
    return _rl.DrawTextureV(texture, position, tint)


_rl.DrawTextureEx.argtypes = [Texture2D, Vector2, Float, Float, Color]
_rl.DrawTextureEx.restype = None
def draw_texture_ex(texture: Texture2D, position: Vector2, rotation: float, scale: float, tint: Color) -> None:
    '''Draw a Texture2D with extended parameters'''
    return _rl.DrawTextureEx(texture, position, rotation, scale, tint)


_rl.DrawTextureRec.argtypes = [Texture2D, Rectangle, Vector2, Color]
_rl.DrawTextureRec.restype = None
def draw_texture_rec(texture: Texture2D, sourceRec: Rectangle, position: Vector2, tint: Color) -> None:
    '''Draw a part of a texture defined by a rectangle'''
    return _rl.DrawTextureRec(texture, sourceRec, position, tint)


_rl.DrawTexturePro.argtypes = [Texture2D, Rectangle, Rectangle, Vector2, Float, Color]
_rl.DrawTexturePro.restype = None
def draw_texture_pro(texture: Texture2D, sourceRec: Rectangle, destRec: Rectangle, origin: Vector2, rotation: float, tint: Color) -> None:
    '''Draw a part of a texture defined by a rectangle with 'pro' parameters'''
    return _rl.DrawTexturePro(texture, sourceRec, destRec, origin, rotation, tint)
