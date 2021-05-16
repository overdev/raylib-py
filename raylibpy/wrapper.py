from raylibpy._types import *
from raylibpy.core import *
from raylibpy import _rl

__all__ = [
    '_init',
]

# ---------------------------------------------------------
# region HEADERS

_initialized: bool = False


def _init():
    global _initialized

    if _initialized:
        return

    # region RAYLIB

    _rl.InitWindow.argtypes = [Int, Int, CharPtr]
    _rl.InitWindow.restype = None

    _rl.WindowShouldClose.argtypes = []
    _rl.WindowShouldClose.restype = Bool

    _rl.CloseWindow.argtypes = []
    _rl.CloseWindow.restype = None

    _rl.IsWindowReady.argtypes = []
    _rl.IsWindowReady.restype = Bool

    _rl.IsWindowFullscreen.argtypes = []
    _rl.IsWindowFullscreen.restype = Bool

    _rl.IsWindowHidden.argtypes = []
    _rl.IsWindowHidden.restype = Bool

    _rl.IsWindowMinimized.argtypes = []
    _rl.IsWindowMinimized.restype = Bool

    _rl.IsWindowMaximized.argtypes = []
    _rl.IsWindowMaximized.restype = Bool

    _rl.IsWindowFocused.argtypes = []
    _rl.IsWindowFocused.restype = Bool

    _rl.IsWindowResized.argtypes = []
    _rl.IsWindowResized.restype = Bool

    _rl.IsWindowState.argtypes = [UInt]
    _rl.IsWindowState.restype = Bool

    _rl.SetWindowState.argtypes = [UInt]
    _rl.SetWindowState.restype = None

    _rl.ClearWindowState.argtypes = [UInt]
    _rl.ClearWindowState.restype = None

    _rl.ToggleFullscreen.argtypes = []
    _rl.ToggleFullscreen.restype = None

    _rl.MaximizeWindow.argtypes = []
    _rl.MaximizeWindow.restype = None

    _rl.MinimizeWindow.argtypes = []
    _rl.MinimizeWindow.restype = None

    _rl.RestoreWindow.argtypes = []
    _rl.RestoreWindow.restype = None

    _rl.SetWindowIcon.argtypes = [Image]
    _rl.SetWindowIcon.restype = None

    _rl.SetWindowTitle.argtypes = [CharPtr]
    _rl.SetWindowTitle.restype = None

    _rl.SetWindowPosition.argtypes = [Int, Int]
    _rl.SetWindowPosition.restype = None

    _rl.SetWindowMonitor.argtypes = [Int]
    _rl.SetWindowMonitor.restype = None

    _rl.SetWindowMinSize.argtypes = [Int, Int]
    _rl.SetWindowMinSize.restype = None

    _rl.SetWindowSize.argtypes = [Int, Int]
    _rl.SetWindowSize.restype = None

    _rl.GetWindowHandle.argtypes = []
    _rl.GetWindowHandle.restype = VoidPtr

    _rl.GetScreenWidth.argtypes = []
    _rl.GetScreenWidth.restype = Int

    _rl.GetScreenHeight.argtypes = []
    _rl.GetScreenHeight.restype = Int

    _rl.GetMonitorCount.argtypes = []
    _rl.GetMonitorCount.restype = Int

    _rl.GetCurrentMonitor.argtypes = []
    _rl.GetCurrentMonitor.restype = Int

    _rl.GetMonitorPosition.argtypes = [Int]
    _rl.GetMonitorPosition.restype = Vector2

    _rl.GetMonitorWidth.argtypes = [Int]
    _rl.GetMonitorWidth.restype = Int

    _rl.GetMonitorHeight.argtypes = [Int]
    _rl.GetMonitorHeight.restype = Int

    _rl.GetMonitorPhysicalWidth.argtypes = [Int]
    _rl.GetMonitorPhysicalWidth.restype = Int

    _rl.GetMonitorPhysicalHeight.argtypes = [Int]
    _rl.GetMonitorPhysicalHeight.restype = Int

    _rl.GetMonitorRefreshRate.argtypes = [Int]
    _rl.GetMonitorRefreshRate.restype = Int

    _rl.GetWindowPosition.argtypes = []
    _rl.GetWindowPosition.restype = Vector2

    _rl.GetWindowScaleDPI.argtypes = []
    _rl.GetWindowScaleDPI.restype = Vector2

    _rl.GetMonitorName.argtypes = [Int]
    _rl.GetMonitorName.restype = CharPtr

    _rl.SetClipboardText.argtypes = [CharPtr]
    _rl.SetClipboardText.restype = None

    _rl.GetClipboardText.argtypes = []
    _rl.GetClipboardText.restype = CharPtr

    _rl.ShowCursor.argtypes = []
    _rl.ShowCursor.restype = None

    _rl.HideCursor.argtypes = []
    _rl.HideCursor.restype = None

    _rl.IsCursorHidden.argtypes = []
    _rl.IsCursorHidden.restype = Bool

    _rl.EnableCursor.argtypes = []
    _rl.EnableCursor.restype = None

    _rl.DisableCursor.argtypes = []
    _rl.DisableCursor.restype = None

    _rl.IsCursorOnScreen.argtypes = []
    _rl.IsCursorOnScreen.restype = Bool

    _rl.ClearBackground.argtypes = [Color]
    _rl.ClearBackground.restype = None

    _rl.BeginDrawing.argtypes = []
    _rl.BeginDrawing.restype = None

    _rl.EndDrawing.argtypes = []
    _rl.EndDrawing.restype = None

    _rl.BeginMode2D.argtypes = [Camera2D]
    _rl.BeginMode2D.restype = None

    _rl.EndMode2D.argtypes = []
    _rl.EndMode2D.restype = None

    _rl.BeginMode3D.argtypes = [Camera3D]
    _rl.BeginMode3D.restype = None

    _rl.EndMode3D.argtypes = []
    _rl.EndMode3D.restype = None

    _rl.BeginTextureMode.argtypes = [RenderTexture2D]
    _rl.BeginTextureMode.restype = None

    _rl.EndTextureMode.argtypes = []
    _rl.EndTextureMode.restype = None

    _rl.BeginShaderMode.argtypes = [Shader]
    _rl.BeginShaderMode.restype = None

    _rl.EndShaderMode.argtypes = []
    _rl.EndShaderMode.restype = None

    _rl.BeginBlendMode.argtypes = [Int]
    _rl.BeginBlendMode.restype = None

    _rl.EndBlendMode.argtypes = []
    _rl.EndBlendMode.restype = None

    _rl.BeginScissorMode.argtypes = [Int, Int, Int, Int]
    _rl.BeginScissorMode.restype = None

    _rl.EndScissorMode.argtypes = []
    _rl.EndScissorMode.restype = None

    _rl.BeginVrStereoMode.argtypes = [VrStereoConfig]
    _rl.BeginVrStereoMode.restype = None

    _rl.EndVrStereoMode.argtypes = []
    _rl.EndVrStereoMode.restype = None

    _rl.LoadVrStereoConfig.argtypes = [VrDeviceInfo]
    _rl.LoadVrStereoConfig.restype = VrStereoConfig

    _rl.UnloadVrStereoConfig.argtypes = [VrStereoConfig]
    _rl.UnloadVrStereoConfig.restype = None

    _rl.LoadShader.argtypes = [CharPtr, CharPtr]
    _rl.LoadShader.restype = Shader

    _rl.LoadShaderFromMemory.argtypes = [CharPtr, CharPtr]
    _rl.LoadShaderFromMemory.restype = Shader

    _rl.GetShaderLocation.argtypes = [Shader, CharPtr]
    _rl.GetShaderLocation.restype = Int

    _rl.GetShaderLocationAttrib.argtypes = [Shader, CharPtr]
    _rl.GetShaderLocationAttrib.restype = Int

    _rl.SetShaderValue.argtypes = [Shader, Int, VoidPtr, Int]
    _rl.SetShaderValue.restype = None

    _rl.SetShaderValueV.argtypes = [Shader, Int, VoidPtr, Int, Int]
    _rl.SetShaderValueV.restype = None

    _rl.SetShaderValueMatrix.argtypes = [Shader, Int, Matrix]
    _rl.SetShaderValueMatrix.restype = None

    _rl.SetShaderValueTexture.argtypes = [Shader, Int, Texture2D]
    _rl.SetShaderValueTexture.restype = None

    _rl.UnloadShader.argtypes = [Shader]
    _rl.UnloadShader.restype = None

    _rl.GetMouseRay.argtypes = [Vector2, Camera]
    _rl.GetMouseRay.restype = Ray

    _rl.GetCameraMatrix.argtypes = [Camera]
    _rl.GetCameraMatrix.restype = Matrix

    _rl.GetCameraMatrix2D.argtypes = [Camera2D]
    _rl.GetCameraMatrix2D.restype = Matrix

    _rl.GetWorldToScreen.argtypes = [Vector3, Camera]
    _rl.GetWorldToScreen.restype = Vector2

    _rl.GetWorldToScreenEx.argtypes = [Vector3, Camera, Int, Int]
    _rl.GetWorldToScreenEx.restype = Vector2

    _rl.GetWorldToScreen2D.argtypes = [Vector2, Camera2D]
    _rl.GetWorldToScreen2D.restype = Vector2

    _rl.GetScreenToWorld2D.argtypes = [Vector2, Camera2D]
    _rl.GetScreenToWorld2D.restype = Vector2

    _rl.SetTargetFPS.argtypes = [Int]
    _rl.SetTargetFPS.restype = None

    _rl.GetFPS.argtypes = []
    _rl.GetFPS.restype = Int

    _rl.GetFrameTime.argtypes = []
    _rl.GetFrameTime.restype = Float

    _rl.GetTime.argtypes = []
    _rl.GetTime.restype = Double

    _rl.GetRandomValue.argtypes = [Int, Int]
    _rl.GetRandomValue.restype = Int

    _rl.TakeScreenshot.argtypes = [CharPtr]
    _rl.TakeScreenshot.restype = None

    _rl.SetConfigFlags.argtypes = [UInt]
    _rl.SetConfigFlags.restype = None

    _rl.TraceLog.argtypes = [Int, CharPtr]
    _rl.TraceLog.restype = None

    _rl.SetTraceLogLevel.argtypes = [Int]
    _rl.SetTraceLogLevel.restype = None

    _rl.MemAlloc.argtypes = [Int]
    _rl.MemAlloc.restype = VoidPtr

    _rl.MemRealloc.argtypes = [VoidPtr, Int]
    _rl.MemRealloc.restype = VoidPtr

    _rl.MemFree.argtypes = [VoidPtr]
    _rl.MemFree.restype = None

    _rl.SetTraceLogCallback.argtypes = [TraceLogCallback]
    _rl.SetTraceLogCallback.restype = None

    _rl.SetLoadFileDataCallback.argtypes = [LoadFileDataCallback]
    _rl.SetLoadFileDataCallback.restype = None

    _rl.SetSaveFileDataCallback.argtypes = [SaveFileDataCallback]
    _rl.SetSaveFileDataCallback.restype = None

    _rl.SetLoadFileTextCallback.argtypes = [LoadFileTextCallback]
    _rl.SetLoadFileTextCallback.restype = None

    _rl.SetSaveFileTextCallback.argtypes = [SaveFileTextCallback]
    _rl.SetSaveFileTextCallback.restype = None

    _rl.LoadFileData.argtypes = [CharPtr, UIntPtr]
    _rl.LoadFileData.restype = UCharPtr

    _rl.UnloadFileData.argtypes = [UCharPtr]
    _rl.UnloadFileData.restype = None

    _rl.SaveFileData.argtypes = [CharPtr, VoidPtr, UInt]
    _rl.SaveFileData.restype = Bool

    _rl.LoadFileText.argtypes = [CharPtr]
    _rl.LoadFileText.restype = CharPtr

    _rl.UnloadFileText.argtypes = [UCharPtr]
    _rl.UnloadFileText.restype = None

    _rl.SaveFileText.argtypes = [CharPtr, CharPtr]
    _rl.SaveFileText.restype = Bool

    _rl.FileExists.argtypes = [CharPtr]
    _rl.FileExists.restype = Bool

    _rl.DirectoryExists.argtypes = [CharPtr]
    _rl.DirectoryExists.restype = Bool

    _rl.IsFileExtension.argtypes = [CharPtr, CharPtr]
    _rl.IsFileExtension.restype = Bool

    _rl.GetFileExtension.argtypes = [CharPtr]
    _rl.GetFileExtension.restype = CharPtr

    _rl.GetFileName.argtypes = [CharPtr]
    _rl.GetFileName.restype = CharPtr

    _rl.GetFileNameWithoutExt.argtypes = [CharPtr]
    _rl.GetFileNameWithoutExt.restype = CharPtr

    _rl.GetDirectoryPath.argtypes = [CharPtr]
    _rl.GetDirectoryPath.restype = CharPtr

    _rl.GetPrevDirectoryPath.argtypes = [CharPtr]
    _rl.GetPrevDirectoryPath.restype = CharPtr

    _rl.GetWorkingDirectory.argtypes = []
    _rl.GetWorkingDirectory.restype = CharPtr

    _rl.GetDirectoryFiles.argtypes = [CharPtr, IntPtr]
    _rl.GetDirectoryFiles.restype = CharPtrPtr

    _rl.ClearDirectoryFiles.argtypes = []
    _rl.ClearDirectoryFiles.restype = None

    _rl.ChangeDirectory.argtypes = [CharPtr]
    _rl.ChangeDirectory.restype = Bool

    _rl.IsFileDropped.argtypes = []
    _rl.IsFileDropped.restype = Bool

    _rl.GetDroppedFiles.argtypes = [IntPtr]
    _rl.GetDroppedFiles.restype = CharPtrPtr

    _rl.ClearDroppedFiles.argtypes = []
    _rl.ClearDroppedFiles.restype = None

    _rl.GetFileModTime.argtypes = [CharPtr]
    _rl.GetFileModTime.restype = Long

    _rl.CompressData.argtypes = [UCharPtr, Int, IntPtr]
    _rl.CompressData.restype = UCharPtr

    _rl.DecompressData.argtypes = [UCharPtr, Int, IntPtr]
    _rl.DecompressData.restype = UCharPtr

    _rl.SaveStorageValue.argtypes = [UInt, Int]
    _rl.SaveStorageValue.restype = Bool

    _rl.LoadStorageValue.argtypes = [UInt]
    _rl.LoadStorageValue.restype = Int

    _rl.OpenURL.argtypes = [CharPtr]
    _rl.OpenURL.restype = None

    _rl.IsKeyPressed.argtypes = [Int]
    _rl.IsKeyPressed.restype = Bool

    _rl.IsKeyDown.argtypes = [Int]
    _rl.IsKeyDown.restype = Bool

    _rl.IsKeyReleased.argtypes = [Int]
    _rl.IsKeyReleased.restype = Bool

    _rl.IsKeyUp.argtypes = [Int]
    _rl.IsKeyUp.restype = Bool

    _rl.SetExitKey.argtypes = [Int]
    _rl.SetExitKey.restype = None

    _rl.GetKeyPressed.argtypes = []
    _rl.GetKeyPressed.restype = Int

    _rl.GetCharPressed.argtypes = []
    _rl.GetCharPressed.restype = Int

    _rl.IsGamepadAvailable.argtypes = [Int]
    _rl.IsGamepadAvailable.restype = Bool

    _rl.IsGamepadName.argtypes = [Int, CharPtr]
    _rl.IsGamepadName.restype = Bool

    _rl.GetGamepadName.argtypes = [Int]
    _rl.GetGamepadName.restype = CharPtr

    _rl.IsGamepadButtonPressed.argtypes = [Int, Int]
    _rl.IsGamepadButtonPressed.restype = Bool

    _rl.IsGamepadButtonDown.argtypes = [Int, Int]
    _rl.IsGamepadButtonDown.restype = Bool

    _rl.IsGamepadButtonReleased.argtypes = [Int, Int]
    _rl.IsGamepadButtonReleased.restype = Bool

    _rl.IsGamepadButtonUp.argtypes = [Int, Int]
    _rl.IsGamepadButtonUp.restype = Bool

    _rl.GetGamepadButtonPressed.argtypes = []
    _rl.GetGamepadButtonPressed.restype = Int

    _rl.GetGamepadAxisCount.argtypes = [Int]
    _rl.GetGamepadAxisCount.restype = Int

    _rl.GetGamepadAxisMovement.argtypes = [Int, Int]
    _rl.GetGamepadAxisMovement.restype = Float

    _rl.SetGamepadMappings.argtypes = [CharPtr]
    _rl.SetGamepadMappings.restype = Int

    _rl.IsMouseButtonPressed.argtypes = [Int]
    _rl.IsMouseButtonPressed.restype = Bool

    _rl.IsMouseButtonDown.argtypes = [Int]
    _rl.IsMouseButtonDown.restype = Bool

    _rl.IsMouseButtonReleased.argtypes = [Int]
    _rl.IsMouseButtonReleased.restype = Bool

    _rl.IsMouseButtonUp.argtypes = [Int]
    _rl.IsMouseButtonUp.restype = Bool

    _rl.GetMouseX.argtypes = []
    _rl.GetMouseX.restype = Int

    _rl.GetMouseY.argtypes = []
    _rl.GetMouseY.restype = Int

    _rl.GetMousePosition.argtypes = []
    _rl.GetMousePosition.restype = Vector2

    _rl.SetMousePosition.argtypes = [Int, Int]
    _rl.SetMousePosition.restype = None

    _rl.SetMouseOffset.argtypes = [Int, Int]
    _rl.SetMouseOffset.restype = None

    _rl.SetMouseScale.argtypes = [Float, Float]
    _rl.SetMouseScale.restype = None

    _rl.GetMouseWheelMove.argtypes = []
    _rl.GetMouseWheelMove.restype = Float

    _rl.SetMouseCursor.argtypes = [Int]
    _rl.SetMouseCursor.restype = None

    _rl.GetTouchX.argtypes = []
    _rl.GetTouchX.restype = Int

    _rl.GetTouchY.argtypes = []
    _rl.GetTouchY.restype = Int

    _rl.GetTouchPosition.argtypes = [Int]
    _rl.GetTouchPosition.restype = Vector2

    _rl.SetGesturesEnabled.argtypes = [UInt]
    _rl.SetGesturesEnabled.restype = None

    _rl.IsGestureDetected.argtypes = [Int]
    _rl.IsGestureDetected.restype = Bool

    _rl.GetGestureDetected.argtypes = []
    _rl.GetGestureDetected.restype = Int

    _rl.GetTouchPointsCount.argtypes = []
    _rl.GetTouchPointsCount.restype = Int

    _rl.GetGestureHoldDuration.argtypes = []
    _rl.GetGestureHoldDuration.restype = Float

    _rl.GetGestureDragVector.argtypes = []
    _rl.GetGestureDragVector.restype = Vector2

    _rl.GetGestureDragAngle.argtypes = []
    _rl.GetGestureDragAngle.restype = Float

    _rl.GetGesturePinchVector.argtypes = []
    _rl.GetGesturePinchVector.restype = Vector2

    _rl.GetGesturePinchAngle.argtypes = []
    _rl.GetGesturePinchAngle.restype = Float

    _rl.SetCameraMode.argtypes = [Camera, Int]
    _rl.SetCameraMode.restype = None

    _rl.UpdateCamera.argtypes = [CameraPtr]
    _rl.UpdateCamera.restype = None

    _rl.SetCameraPanControl.argtypes = [Int]
    _rl.SetCameraPanControl.restype = None

    _rl.SetCameraAltControl.argtypes = [Int]
    _rl.SetCameraAltControl.restype = None

    _rl.SetCameraSmoothZoomControl.argtypes = [Int]
    _rl.SetCameraSmoothZoomControl.restype = None

    _rl.SetCameraMoveControls.argtypes = [Int, Int, Int, Int, Int, Int]
    _rl.SetCameraMoveControls.restype = None

    _rl.DrawPixel.argtypes = [Int, Int, Color]
    _rl.DrawPixel.restype = None

    _rl.DrawPixelV.argtypes = [Vector2, Color]
    _rl.DrawPixelV.restype = None

    _rl.DrawLine.argtypes = [Int, Int, Int, Int, Color]
    _rl.DrawLine.restype = None

    _rl.DrawLineV.argtypes = [Vector2, Vector2, Color]
    _rl.DrawLineV.restype = None

    _rl.DrawLineEx.argtypes = [Vector2, Vector2, Float, Color]
    _rl.DrawLineEx.restype = None

    _rl.DrawLineBezier.argtypes = [Vector2, Vector2, Float, Color]
    _rl.DrawLineBezier.restype = None

    _rl.DrawLineBezierQuad.argtypes = [Vector2, Vector2, Vector2, Float, Color]
    _rl.DrawLineBezierQuad.restype = None

    _rl.DrawLineStrip.argtypes = [Vector2Ptr, Int, Color]
    _rl.DrawLineStrip.restype = None

    _rl.DrawCircle.argtypes = [Int, Int, Float, Color]
    _rl.DrawCircle.restype = None

    _rl.DrawCircleSector.argtypes = [Vector2, Float, Float, Float, Int, Color]
    _rl.DrawCircleSector.restype = None

    _rl.DrawCircleSectorLines.argtypes = [Vector2, Float, Float, Float, Int, Color]
    _rl.DrawCircleSectorLines.restype = None

    _rl.DrawCircleGradient.argtypes = [Int, Int, Float, Color, Color]
    _rl.DrawCircleGradient.restype = None

    _rl.DrawCircleV.argtypes = [Vector2, Float, Color]
    _rl.DrawCircleV.restype = None

    _rl.DrawCircleLines.argtypes = [Int, Int, Float, Color]
    _rl.DrawCircleLines.restype = None

    _rl.DrawEllipse.argtypes = [Int, Int, Float, Float, Color]
    _rl.DrawEllipse.restype = None

    _rl.DrawEllipseLines.argtypes = [Int, Int, Float, Float, Color]
    _rl.DrawEllipseLines.restype = None

    _rl.DrawRing.argtypes = [Vector2, Float, Float, Float, Float, Int, Color]
    _rl.DrawRing.restype = None

    _rl.DrawRingLines.argtypes = [Vector2, Float, Float, Float, Float, Int, Color]
    _rl.DrawRingLines.restype = None

    _rl.DrawRectangle.argtypes = [Int, Int, Int, Int, Color]
    _rl.DrawRectangle.restype = None

    _rl.DrawRectangleV.argtypes = [Vector2, Vector2, Color]
    _rl.DrawRectangleV.restype = None

    _rl.DrawRectangleRec.argtypes = [Rectangle, Color]
    _rl.DrawRectangleRec.restype = None

    _rl.DrawRectanglePro.argtypes = [Rectangle, Vector2, Float, Color]
    _rl.DrawRectanglePro.restype = None

    _rl.DrawRectangleGradientV.argtypes = [Int, Int, Int, Int, Color, Color]
    _rl.DrawRectangleGradientV.restype = None

    _rl.DrawRectangleGradientH.argtypes = [Int, Int, Int, Int, Color, Color]
    _rl.DrawRectangleGradientH.restype = None

    _rl.DrawRectangleGradientEx.argtypes = [Rectangle, Color, Color, Color, Color]
    _rl.DrawRectangleGradientEx.restype = None

    _rl.DrawRectangleLines.argtypes = [Int, Int, Int, Int, Color]
    _rl.DrawRectangleLines.restype = None

    _rl.DrawRectangleLinesEx.argtypes = [Rectangle, Int, Color]
    _rl.DrawRectangleLinesEx.restype = None

    _rl.DrawRectangleRounded.argtypes = [Rectangle, Float, Int, Color]
    _rl.DrawRectangleRounded.restype = None

    _rl.DrawRectangleRoundedLines.argtypes = [Rectangle, Float, Int, Int, Color]
    _rl.DrawRectangleRoundedLines.restype = None

    _rl.DrawTriangle.argtypes = [Vector2, Vector2, Vector2, Color]
    _rl.DrawTriangle.restype = None

    _rl.DrawTriangleLines.argtypes = [Vector2, Vector2, Vector2, Color]
    _rl.DrawTriangleLines.restype = None

    _rl.DrawTriangleFan.argtypes = [Vector2Ptr, Int, Color]
    _rl.DrawTriangleFan.restype = None

    _rl.DrawTriangleStrip.argtypes = [Vector2Ptr, Int, Color]
    _rl.DrawTriangleStrip.restype = None

    _rl.DrawPoly.argtypes = [Vector2, Int, Float, Float, Color]
    _rl.DrawPoly.restype = None

    _rl.DrawPolyLines.argtypes = [Vector2, Int, Float, Float, Color]
    _rl.DrawPolyLines.restype = None

    _rl.CheckCollisionRecs.argtypes = [Rectangle, Rectangle]
    _rl.CheckCollisionRecs.restype = Bool

    _rl.CheckCollisionCircles.argtypes = [Vector2, Float, Vector2, Float]
    _rl.CheckCollisionCircles.restype = Bool

    _rl.CheckCollisionCircleRec.argtypes = [Vector2, Float, Rectangle]
    _rl.CheckCollisionCircleRec.restype = Bool

    _rl.CheckCollisionPointRec.argtypes = [Vector2, Rectangle]
    _rl.CheckCollisionPointRec.restype = Bool

    _rl.CheckCollisionPointCircle.argtypes = [Vector2, Vector2, Float]
    _rl.CheckCollisionPointCircle.restype = Bool

    _rl.CheckCollisionPointTriangle.argtypes = [Vector2, Vector2, Vector2, Vector2]
    _rl.CheckCollisionPointTriangle.restype = Bool

    _rl.CheckCollisionLines.argtypes = [Vector2, Vector2, Vector2, Vector2, Vector2Ptr]
    _rl.CheckCollisionLines.restype = Bool

    _rl.GetCollisionRec.argtypes = [Rectangle, Rectangle]
    _rl.GetCollisionRec.restype = Rectangle

    _rl.LoadImage.argtypes = [CharPtr]
    _rl.LoadImage.restype = Image

    _rl.LoadImageRaw.argtypes = [CharPtr, Int, Int, Int, Int]
    _rl.LoadImageRaw.restype = Image

    _rl.LoadImageAnim.argtypes = [CharPtr, IntPtr]
    _rl.LoadImageAnim.restype = Image

    _rl.LoadImageFromMemory.argtypes = [CharPtr, UCharPtr, Int]
    _rl.LoadImageFromMemory.restype = Image

    _rl.UnloadImage.argtypes = [Image]
    _rl.UnloadImage.restype = None

    _rl.ExportImage.argtypes = [Image, CharPtr]
    _rl.ExportImage.restype = Bool

    _rl.ExportImageAsCode.argtypes = [Image, CharPtr]
    _rl.ExportImageAsCode.restype = Bool

    _rl.GenImageColor.argtypes = [Int, Int, Color]
    _rl.GenImageColor.restype = Image

    _rl.GenImageGradientV.argtypes = [Int, Int, Color, Color]
    _rl.GenImageGradientV.restype = Image

    _rl.GenImageGradientH.argtypes = [Int, Int, Color, Color]
    _rl.GenImageGradientH.restype = Image

    _rl.GenImageGradientRadial.argtypes = [Int, Int, Float, Color, Color]
    _rl.GenImageGradientRadial.restype = Image

    _rl.GenImageChecked.argtypes = [Int, Int, Int, Int, Color, Color]
    _rl.GenImageChecked.restype = Image

    _rl.GenImageWhiteNoise.argtypes = [Int, Int, Float]
    _rl.GenImageWhiteNoise.restype = Image

    _rl.GenImagePerlinNoise.argtypes = [Int, Int, Int, Int, Float]
    _rl.GenImagePerlinNoise.restype = Image

    _rl.GenImageCellular.argtypes = [Int, Int, Int]
    _rl.GenImageCellular.restype = Image

    _rl.ImageCopy.argtypes = [Image]
    _rl.ImageCopy.restype = Image

    _rl.ImageFromImage.argtypes = [Image, Rectangle]
    _rl.ImageFromImage.restype = Image

    _rl.ImageText.argtypes = [CharPtr, Int, Color]
    _rl.ImageText.restype = Image

    _rl.ImageTextEx.argtypes = [Font, CharPtr, Float, Float, Color]
    _rl.ImageTextEx.restype = Image

    _rl.ImageFormat.argtypes = [ImagePtr, Int]
    _rl.ImageFormat.restype = None

    _rl.ImageToPOT.argtypes = [ImagePtr, Color]
    _rl.ImageToPOT.restype = None

    _rl.ImageCrop.argtypes = [ImagePtr, Rectangle]
    _rl.ImageCrop.restype = None

    _rl.ImageAlphaCrop.argtypes = [ImagePtr, Float]
    _rl.ImageAlphaCrop.restype = None

    _rl.ImageAlphaClear.argtypes = [ImagePtr, Color, Float]
    _rl.ImageAlphaClear.restype = None

    _rl.ImageAlphaMask.argtypes = [ImagePtr, Image]
    _rl.ImageAlphaMask.restype = None

    _rl.ImageAlphaPremultiply.argtypes = [ImagePtr]
    _rl.ImageAlphaPremultiply.restype = None

    _rl.ImageResize.argtypes = [ImagePtr, Int, Int]
    _rl.ImageResize.restype = None

    _rl.ImageResizeNN.argtypes = [ImagePtr, Int, Int]
    _rl.ImageResizeNN.restype = None

    _rl.ImageResizeCanvas.argtypes = [ImagePtr, Int, Int, Int, Int, Color]
    _rl.ImageResizeCanvas.restype = None

    _rl.ImageMipmaps.argtypes = [ImagePtr]
    _rl.ImageMipmaps.restype = None

    _rl.ImageDither.argtypes = [ImagePtr, Int, Int, Int, Int]
    _rl.ImageDither.restype = None

    _rl.ImageFlipVertical.argtypes = [ImagePtr]
    _rl.ImageFlipVertical.restype = None

    _rl.ImageFlipHorizontal.argtypes = [ImagePtr]
    _rl.ImageFlipHorizontal.restype = None

    _rl.ImageRotateCW.argtypes = [ImagePtr]
    _rl.ImageRotateCW.restype = None

    _rl.ImageRotateCCW.argtypes = [ImagePtr]
    _rl.ImageRotateCCW.restype = None

    _rl.ImageColorTint.argtypes = [ImagePtr, Color]
    _rl.ImageColorTint.restype = None

    _rl.ImageColorInvert.argtypes = [ImagePtr]
    _rl.ImageColorInvert.restype = None

    _rl.ImageColorGrayscale.argtypes = [ImagePtr]
    _rl.ImageColorGrayscale.restype = None

    _rl.ImageColorContrast.argtypes = [ImagePtr, Float]
    _rl.ImageColorContrast.restype = None

    _rl.ImageColorBrightness.argtypes = [ImagePtr, Int]
    _rl.ImageColorBrightness.restype = None

    _rl.ImageColorReplace.argtypes = [ImagePtr, Color, Color]
    _rl.ImageColorReplace.restype = None

    _rl.LoadImageColors.argtypes = [Image]
    _rl.LoadImageColors.restype = ColorPtr

    _rl.LoadImagePalette.argtypes = [Image, Int, IntPtr]
    _rl.LoadImagePalette.restype = ColorPtr

    _rl.UnloadImageColors.argtypes = [ColorPtr]
    _rl.UnloadImageColors.restype = None

    _rl.UnloadImagePalette.argtypes = [ColorPtr]
    _rl.UnloadImagePalette.restype = None

    _rl.GetImageAlphaBorder.argtypes = [Image, Float]
    _rl.GetImageAlphaBorder.restype = Rectangle

    _rl.ImageClearBackground.argtypes = [ImagePtr, Color]
    _rl.ImageClearBackground.restype = None

    _rl.ImageDrawPixel.argtypes = [ImagePtr, Int, Int, Color]
    _rl.ImageDrawPixel.restype = None

    _rl.ImageDrawPixelV.argtypes = [ImagePtr, Vector2, Color]
    _rl.ImageDrawPixelV.restype = None

    _rl.ImageDrawLine.argtypes = [ImagePtr, Int, Int, Int, Int, Color]
    _rl.ImageDrawLine.restype = None

    _rl.ImageDrawLineV.argtypes = [ImagePtr, Vector2, Vector2, Color]
    _rl.ImageDrawLineV.restype = None

    _rl.ImageDrawCircle.argtypes = [ImagePtr, Int, Int, Int, Color]
    _rl.ImageDrawCircle.restype = None

    _rl.ImageDrawCircleV.argtypes = [ImagePtr, Vector2, Int, Color]
    _rl.ImageDrawCircleV.restype = None

    _rl.ImageDrawRectangle.argtypes = [ImagePtr, Int, Int, Int, Int, Color]
    _rl.ImageDrawRectangle.restype = None

    _rl.ImageDrawRectangleV.argtypes = [ImagePtr, Vector2, Vector2, Color]
    _rl.ImageDrawRectangleV.restype = None

    _rl.ImageDrawRectangleRec.argtypes = [ImagePtr, Rectangle, Color]
    _rl.ImageDrawRectangleRec.restype = None

    _rl.ImageDrawRectangleLines.argtypes = [ImagePtr, Rectangle, Int, Color]
    _rl.ImageDrawRectangleLines.restype = None

    _rl.ImageDraw.argtypes = [ImagePtr, Image, Rectangle, Rectangle, Color]
    _rl.ImageDraw.restype = None

    _rl.ImageDrawText.argtypes = [ImagePtr, CharPtr, Int, Int, Int, Color]
    _rl.ImageDrawText.restype = None

    _rl.ImageDrawTextEx.argtypes = [ImagePtr, Font, CharPtr, Vector2, Float, Float, Color]
    _rl.ImageDrawTextEx.restype = None

    _rl.LoadTexture.argtypes = [CharPtr]
    _rl.LoadTexture.restype = Texture2D

    _rl.LoadTextureFromImage.argtypes = [Image]
    _rl.LoadTextureFromImage.restype = Texture2D

    _rl.LoadTextureCubemap.argtypes = [Image, Int]
    _rl.LoadTextureCubemap.restype = TextureCubemap

    _rl.LoadRenderTexture.argtypes = [Int, Int]
    _rl.LoadRenderTexture.restype = RenderTexture2D

    _rl.UnloadTexture.argtypes = [Texture2D]
    _rl.UnloadTexture.restype = None

    _rl.UnloadRenderTexture.argtypes = [RenderTexture2D]
    _rl.UnloadRenderTexture.restype = None

    _rl.UpdateTexture.argtypes = [Texture2D, VoidPtr]
    _rl.UpdateTexture.restype = None

    _rl.UpdateTextureRec.argtypes = [Texture2D, Rectangle, VoidPtr]
    _rl.UpdateTextureRec.restype = None

    _rl.GetTextureData.argtypes = [Texture2D]
    _rl.GetTextureData.restype = Image

    _rl.GetScreenData.argtypes = []
    _rl.GetScreenData.restype = Image

    _rl.GenTextureMipmaps.argtypes = [Texture2DPtr]
    _rl.GenTextureMipmaps.restype = None

    _rl.SetTextureFilter.argtypes = [Texture2D, Int]
    _rl.SetTextureFilter.restype = None

    _rl.SetTextureWrap.argtypes = [Texture2D, Int]
    _rl.SetTextureWrap.restype = None

    _rl.DrawTexture.argtypes = [Texture2D, Int, Int, Color]
    _rl.DrawTexture.restype = None

    _rl.DrawTextureV.argtypes = [Texture2D, Vector2, Color]
    _rl.DrawTextureV.restype = None

    _rl.DrawTextureEx.argtypes = [Texture2D, Vector2, Float, Float, Color]
    _rl.DrawTextureEx.restype = None

    _rl.DrawTextureRec.argtypes = [Texture2D, Rectangle, Vector2, Color]
    _rl.DrawTextureRec.restype = None

    _rl.DrawTextureQuad.argtypes = [Texture2D, Vector2, Vector2, Rectangle, Color]
    _rl.DrawTextureQuad.restype = None

    _rl.DrawTextureTiled.argtypes = [Texture2D, Rectangle, Rectangle, Vector2, Float, Float, Color]
    _rl.DrawTextureTiled.restype = None

    _rl.DrawTexturePro.argtypes = [Texture2D, Rectangle, Rectangle, Vector2, Float, Color]
    _rl.DrawTexturePro.restype = None

    _rl.DrawTextureNPatch.argtypes = [Texture2D, NPatchInfo, Rectangle, Vector2, Float, Color]
    _rl.DrawTextureNPatch.restype = None

    _rl.DrawTexturePoly.argtypes = [Texture2D, Vector2, Vector2Ptr, Vector2Ptr, Int, Color]
    _rl.DrawTexturePoly.restype = None

    _rl.Fade.argtypes = [Color, Float]
    _rl.Fade.restype = Color

    _rl.ColorToInt.argtypes = [Color]
    _rl.ColorToInt.restype = Int

    _rl.ColorNormalize.argtypes = [Color]
    _rl.ColorNormalize.restype = Vector4

    _rl.ColorFromNormalized.argtypes = [Vector4]
    _rl.ColorFromNormalized.restype = Color

    _rl.ColorToHSV.argtypes = [Color]
    _rl.ColorToHSV.restype = Vector3

    _rl.ColorFromHSV.argtypes = [Float, Float, Float]
    _rl.ColorFromHSV.restype = Color

    _rl.ColorAlpha.argtypes = [Color, Float]
    _rl.ColorAlpha.restype = Color

    _rl.ColorAlphaBlend.argtypes = [Color, Color, Color]
    _rl.ColorAlphaBlend.restype = Color

    _rl.GetColor.argtypes = [Int]
    _rl.GetColor.restype = Color

    _rl.GetPixelColor.argtypes = [VoidPtr, Int]
    _rl.GetPixelColor.restype = Color

    _rl.SetPixelColor.argtypes = [VoidPtr, Color, Int]
    _rl.SetPixelColor.restype = None

    _rl.GetPixelDataSize.argtypes = [Int, Int, Int]
    _rl.GetPixelDataSize.restype = Int

    _rl.GetFontDefault.argtypes = []
    _rl.GetFontDefault.restype = Font

    _rl.LoadFont.argtypes = [CharPtr]
    _rl.LoadFont.restype = Font

    _rl.LoadFontEx.argtypes = [CharPtr, Int, IntPtr, Int]
    _rl.LoadFontEx.restype = Font

    _rl.LoadFontFromImage.argtypes = [Image, Color, Int]
    _rl.LoadFontFromImage.restype = Font

    _rl.LoadFontFromMemory.argtypes = [CharPtr, UCharPtr, Int, Int, IntPtr, Int]
    _rl.LoadFontFromMemory.restype = Font

    _rl.LoadFontData.argtypes = [UCharPtr, Int, Int, IntPtr, Int, Int]
    _rl.LoadFontData.restype = CharInfoPtr

    _rl.GenImageFontAtlas.argtypes = [CharInfoPtr, RectanglePtrPtr, Int, Int, Int, Int]
    _rl.GenImageFontAtlas.restype = Image

    _rl.UnloadFontData.argtypes = [CharInfoPtr, Int]
    _rl.UnloadFontData.restype = None

    _rl.UnloadFont.argtypes = [Font]
    _rl.UnloadFont.restype = None

    _rl.DrawFPS.argtypes = [Int, Int]
    _rl.DrawFPS.restype = None

    _rl.DrawText.argtypes = [CharPtr, Int, Int, Int, Color]
    _rl.DrawText.restype = None

    _rl.DrawTextEx.argtypes = [Font, CharPtr, Vector2, Float, Float, Color]
    _rl.DrawTextEx.restype = None

    _rl.DrawTextRec.argtypes = [Font, CharPtr, Rectangle, Float, Float, Bool, Color]
    _rl.DrawTextRec.restype = None

    _rl.DrawTextRecEx.argtypes = [Font, CharPtr, Rectangle, Float, Float, Bool, Color, Int, Int, Color, Color]
    _rl.DrawTextRecEx.restype = None

    _rl.DrawTextCodepoint.argtypes = [Font, Int, Vector2, Float, Color]
    _rl.DrawTextCodepoint.restype = None

    _rl.MeasureText.argtypes = [CharPtr, Int]
    _rl.MeasureText.restype = Int

    _rl.MeasureTextEx.argtypes = [Font, CharPtr, Float, Float]
    _rl.MeasureTextEx.restype = Vector2

    _rl.GetGlyphIndex.argtypes = [Font, Int]
    _rl.GetGlyphIndex.restype = Int

    _rl.TextCopy.argtypes = [CharPtr, CharPtr]
    _rl.TextCopy.restype = Int

    _rl.TextIsEqual.argtypes = [CharPtr, CharPtr]
    _rl.TextIsEqual.restype = Bool

    _rl.TextLength.argtypes = [CharPtr]
    _rl.TextLength.restype = UInt

    _rl.TextFormat.argtypes = [CharPtr]
    _rl.TextFormat.restype = CharPtr

    _rl.TextSubtext.argtypes = [CharPtr, Int, Int]
    _rl.TextSubtext.restype = CharPtr

    _rl.TextReplace.argtypes = [CharPtr, CharPtr, CharPtr]
    _rl.TextReplace.restype = CharPtr

    _rl.TextInsert.argtypes = [CharPtr, CharPtr, Int]
    _rl.TextInsert.restype = CharPtr

    _rl.TextJoin.argtypes = [CharPtrPtr, Int, CharPtr]
    _rl.TextJoin.restype = CharPtr

    _rl.TextSplit.argtypes = [CharPtr, Char, IntPtr]
    _rl.TextSplit.restype = CharPtrPtr

    _rl.TextAppend.argtypes = [CharPtr, CharPtr, IntPtr]
    _rl.TextAppend.restype = None

    _rl.TextFindIndex.argtypes = [CharPtr, CharPtr]
    _rl.TextFindIndex.restype = Int

    _rl.TextToUpper.argtypes = [CharPtr]
    _rl.TextToUpper.restype = CharPtr

    _rl.TextToLower.argtypes = [CharPtr]
    _rl.TextToLower.restype = CharPtr

    _rl.TextToPascal.argtypes = [CharPtr]
    _rl.TextToPascal.restype = CharPtr

    _rl.TextToInteger.argtypes = [CharPtr]
    _rl.TextToInteger.restype = Int

    _rl.TextToUtf8.argtypes = [IntPtr, Int]
    _rl.TextToUtf8.restype = CharPtr

    _rl.GetCodepoints.argtypes = [CharPtr, IntPtr]
    _rl.GetCodepoints.restype = IntPtr

    _rl.GetCodepointsCount.argtypes = [CharPtr]
    _rl.GetCodepointsCount.restype = Int

    _rl.GetNextCodepoint.argtypes = [CharPtr, IntPtr]
    _rl.GetNextCodepoint.restype = Int

    _rl.CodepointToUtf8.argtypes = [Int, IntPtr]
    _rl.CodepointToUtf8.restype = CharPtr

    _rl.DrawLine3D.argtypes = [Vector3, Vector3, Color]
    _rl.DrawLine3D.restype = None

    _rl.DrawPoint3D.argtypes = [Vector3, Color]
    _rl.DrawPoint3D.restype = None

    _rl.DrawCircle3D.argtypes = [Vector3, Float, Vector3, Float, Color]
    _rl.DrawCircle3D.restype = None

    _rl.DrawTriangle3D.argtypes = [Vector3, Vector3, Vector3, Color]
    _rl.DrawTriangle3D.restype = None

    _rl.DrawTriangleStrip3D.argtypes = [Vector3Ptr, Int, Color]
    _rl.DrawTriangleStrip3D.restype = None

    _rl.DrawCube.argtypes = [Vector3, Float, Float, Float, Color]
    _rl.DrawCube.restype = None

    _rl.DrawCubeV.argtypes = [Vector3, Vector3, Color]
    _rl.DrawCubeV.restype = None

    _rl.DrawCubeWires.argtypes = [Vector3, Float, Float, Float, Color]
    _rl.DrawCubeWires.restype = None

    _rl.DrawCubeWiresV.argtypes = [Vector3, Vector3, Color]
    _rl.DrawCubeWiresV.restype = None

    _rl.DrawCubeTexture.argtypes = [Texture2D, Vector3, Float, Float, Float, Color]
    _rl.DrawCubeTexture.restype = None

    _rl.DrawSphere.argtypes = [Vector3, Float, Color]
    _rl.DrawSphere.restype = None

    _rl.DrawSphereEx.argtypes = [Vector3, Float, Int, Int, Color]
    _rl.DrawSphereEx.restype = None

    _rl.DrawSphereWires.argtypes = [Vector3, Float, Int, Int, Color]
    _rl.DrawSphereWires.restype = None

    _rl.DrawCylinder.argtypes = [Vector3, Float, Float, Float, Int, Color]
    _rl.DrawCylinder.restype = None

    _rl.DrawCylinderWires.argtypes = [Vector3, Float, Float, Float, Int, Color]
    _rl.DrawCylinderWires.restype = None

    _rl.DrawPlane.argtypes = [Vector3, Vector2, Color]
    _rl.DrawPlane.restype = None

    _rl.DrawRay.argtypes = [Ray, Color]
    _rl.DrawRay.restype = None

    _rl.DrawGrid.argtypes = [Int, Float]
    _rl.DrawGrid.restype = None

    _rl.LoadModel.argtypes = [CharPtr]
    _rl.LoadModel.restype = Model

    _rl.LoadModelFromMesh.argtypes = [Mesh]
    _rl.LoadModelFromMesh.restype = Model

    _rl.UnloadModel.argtypes = [Model]
    _rl.UnloadModel.restype = None

    _rl.UnloadModelKeepMeshes.argtypes = [Model]
    _rl.UnloadModelKeepMeshes.restype = None

    _rl.UploadMesh.argtypes = [MeshPtr, Bool]
    _rl.UploadMesh.restype = None

    _rl.UpdateMeshBuffer.argtypes = [Mesh, Int, VoidPtr, Int, Int]
    _rl.UpdateMeshBuffer.restype = None

    _rl.DrawMesh.argtypes = [Mesh, Material, Matrix]
    _rl.DrawMesh.restype = None

    _rl.DrawMeshInstanced.argtypes = [Mesh, Material, MatrixPtr, Int]
    _rl.DrawMeshInstanced.restype = None

    _rl.UnloadMesh.argtypes = [Mesh]
    _rl.UnloadMesh.restype = None

    _rl.ExportMesh.argtypes = [Mesh, CharPtr]
    _rl.ExportMesh.restype = Bool

    _rl.LoadMaterials.argtypes = [CharPtr, IntPtr]
    _rl.LoadMaterials.restype = MaterialPtr

    _rl.LoadMaterialDefault.argtypes = []
    _rl.LoadMaterialDefault.restype = Material

    _rl.UnloadMaterial.argtypes = [Material]
    _rl.UnloadMaterial.restype = None

    _rl.SetMaterialTexture.argtypes = [MaterialPtr, Int, Texture2D]
    _rl.SetMaterialTexture.restype = None

    _rl.SetModelMeshMaterial.argtypes = [ModelPtr, Int, Int]
    _rl.SetModelMeshMaterial.restype = None

    _rl.LoadModelAnimations.argtypes = [CharPtr, IntPtr]
    _rl.LoadModelAnimations.restype = ModelAnimationPtr

    _rl.UpdateModelAnimation.argtypes = [Model, ModelAnimation, Int]
    _rl.UpdateModelAnimation.restype = None

    _rl.UnloadModelAnimation.argtypes = [ModelAnimation]
    _rl.UnloadModelAnimation.restype = None

    _rl.UnloadModelAnimations.argtypes = [ModelAnimationPtr, UInt]
    _rl.UnloadModelAnimations.restype = None

    _rl.IsModelAnimationValid.argtypes = [Model, ModelAnimation]
    _rl.IsModelAnimationValid.restype = Bool

    _rl.GenMeshPoly.argtypes = [Int, Float]
    _rl.GenMeshPoly.restype = Mesh

    _rl.GenMeshPlane.argtypes = [Float, Float, Int, Int]
    _rl.GenMeshPlane.restype = Mesh

    _rl.GenMeshCube.argtypes = [Float, Float, Float]
    _rl.GenMeshCube.restype = Mesh

    _rl.GenMeshSphere.argtypes = [Float, Int, Int]
    _rl.GenMeshSphere.restype = Mesh

    _rl.GenMeshHemiSphere.argtypes = [Float, Int, Int]
    _rl.GenMeshHemiSphere.restype = Mesh

    _rl.GenMeshCylinder.argtypes = [Float, Float, Int]
    _rl.GenMeshCylinder.restype = Mesh

    _rl.GenMeshTorus.argtypes = [Float, Float, Int, Int]
    _rl.GenMeshTorus.restype = Mesh

    _rl.GenMeshKnot.argtypes = [Float, Float, Int, Int]
    _rl.GenMeshKnot.restype = Mesh

    _rl.GenMeshHeightmap.argtypes = [Image, Vector3]
    _rl.GenMeshHeightmap.restype = Mesh

    _rl.GenMeshCubicmap.argtypes = [Image, Vector3]
    _rl.GenMeshCubicmap.restype = Mesh

    _rl.MeshBoundingBox.argtypes = [Mesh]
    _rl.MeshBoundingBox.restype = BoundingBox

    _rl.MeshTangents.argtypes = [MeshPtr]
    _rl.MeshTangents.restype = None

    _rl.MeshBinormals.argtypes = [MeshPtr]
    _rl.MeshBinormals.restype = None

    _rl.DrawModel.argtypes = [Model, Vector3, Float, Color]
    _rl.DrawModel.restype = None

    _rl.DrawModelEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
    _rl.DrawModelEx.restype = None

    _rl.DrawModelWires.argtypes = [Model, Vector3, Float, Color]
    _rl.DrawModelWires.restype = None

    _rl.DrawModelWiresEx.argtypes = [Model, Vector3, Vector3, Float, Vector3, Color]
    _rl.DrawModelWiresEx.restype = None

    _rl.DrawBoundingBox.argtypes = [BoundingBox, Color]
    _rl.DrawBoundingBox.restype = None

    _rl.DrawBillboard.argtypes = [Camera, Texture2D, Vector3, Float, Color]
    _rl.DrawBillboard.restype = None

    _rl.DrawBillboardRec.argtypes = [Camera, Texture2D, Rectangle, Vector3, Float, Color]
    _rl.DrawBillboardRec.restype = None

    _rl.CheckCollisionSpheres.argtypes = [Vector3, Float, Vector3, Float]
    _rl.CheckCollisionSpheres.restype = Bool

    _rl.CheckCollisionBoxes.argtypes = [BoundingBox, BoundingBox]
    _rl.CheckCollisionBoxes.restype = Bool

    _rl.CheckCollisionBoxSphere.argtypes = [BoundingBox, Vector3, Float]
    _rl.CheckCollisionBoxSphere.restype = Bool

    _rl.CheckCollisionRaySphere.argtypes = [Ray, Vector3, Float]
    _rl.CheckCollisionRaySphere.restype = Bool

    _rl.CheckCollisionRaySphereEx.argtypes = [Ray, Vector3, Float, Vector3Ptr]
    _rl.CheckCollisionRaySphereEx.restype = Bool

    _rl.CheckCollisionRayBox.argtypes = [Ray, BoundingBox]
    _rl.CheckCollisionRayBox.restype = Bool

    _rl.GetCollisionRayMesh.argtypes = [Ray, Mesh, Matrix]
    _rl.GetCollisionRayMesh.restype = RayHitInfo

    _rl.GetCollisionRayModel.argtypes = [Ray, Model]
    _rl.GetCollisionRayModel.restype = RayHitInfo

    _rl.GetCollisionRayTriangle.argtypes = [Ray, Vector3, Vector3, Vector3]
    _rl.GetCollisionRayTriangle.restype = RayHitInfo

    _rl.GetCollisionRayGround.argtypes = [Ray, Float]
    _rl.GetCollisionRayGround.restype = RayHitInfo

    _rl.InitAudioDevice.argtypes = []
    _rl.InitAudioDevice.restype = None

    _rl.CloseAudioDevice.argtypes = []
    _rl.CloseAudioDevice.restype = None

    _rl.IsAudioDeviceReady.argtypes = []
    _rl.IsAudioDeviceReady.restype = Bool

    _rl.SetMasterVolume.argtypes = [Float]
    _rl.SetMasterVolume.restype = None

    _rl.LoadWave.argtypes = [CharPtr]
    _rl.LoadWave.restype = Wave

    _rl.LoadWaveFromMemory.argtypes = [CharPtr, UCharPtr, Int]
    _rl.LoadWaveFromMemory.restype = Wave

    _rl.LoadSound.argtypes = [CharPtr]
    _rl.LoadSound.restype = Sound

    _rl.LoadSoundFromWave.argtypes = [Wave]
    _rl.LoadSoundFromWave.restype = Sound

    _rl.UpdateSound.argtypes = [Sound, VoidPtr, Int]
    _rl.UpdateSound.restype = None

    _rl.UnloadWave.argtypes = [Wave]
    _rl.UnloadWave.restype = None

    _rl.UnloadSound.argtypes = [Sound]
    _rl.UnloadSound.restype = None

    _rl.ExportWave.argtypes = [Wave, CharPtr]
    _rl.ExportWave.restype = Bool

    _rl.ExportWaveAsCode.argtypes = [Wave, CharPtr]
    _rl.ExportWaveAsCode.restype = Bool

    _rl.PlaySound.argtypes = [Sound]
    _rl.PlaySound.restype = None

    _rl.StopSound.argtypes = [Sound]
    _rl.StopSound.restype = None

    _rl.PauseSound.argtypes = [Sound]
    _rl.PauseSound.restype = None

    _rl.ResumeSound.argtypes = [Sound]
    _rl.ResumeSound.restype = None

    _rl.PlaySoundMulti.argtypes = [Sound]
    _rl.PlaySoundMulti.restype = None

    _rl.StopSoundMulti.argtypes = []
    _rl.StopSoundMulti.restype = None

    _rl.GetSoundsPlaying.argtypes = []
    _rl.GetSoundsPlaying.restype = Int

    _rl.IsSoundPlaying.argtypes = [Sound]
    _rl.IsSoundPlaying.restype = Bool

    _rl.SetSoundVolume.argtypes = [Sound, Float]
    _rl.SetSoundVolume.restype = None

    _rl.SetSoundPitch.argtypes = [Sound, Float]
    _rl.SetSoundPitch.restype = None

    _rl.WaveFormat.argtypes = [WavePtr, Int, Int, Int]
    _rl.WaveFormat.restype = None

    _rl.WaveCopy.argtypes = [Wave]
    _rl.WaveCopy.restype = Wave

    _rl.WaveCrop.argtypes = [WavePtr, Int, Int]
    _rl.WaveCrop.restype = None

    _rl.LoadWaveSamples.argtypes = [Wave]
    _rl.LoadWaveSamples.restype = FloatPtr

    _rl.UnloadWaveSamples.argtypes = [FloatPtr]
    _rl.UnloadWaveSamples.restype = None

    _rl.LoadMusicStream.argtypes = [CharPtr]
    _rl.LoadMusicStream.restype = Music

    _rl.LoadMusicStreamFromMemory.argtypes = [CharPtr, UCharPtr, Int]
    _rl.LoadMusicStreamFromMemory.restype = Music

    _rl.UnloadMusicStream.argtypes = [Music]
    _rl.UnloadMusicStream.restype = None

    _rl.PlayMusicStream.argtypes = [Music]
    _rl.PlayMusicStream.restype = None

    _rl.IsMusicPlaying.argtypes = [Music]
    _rl.IsMusicPlaying.restype = Bool

    _rl.UpdateMusicStream.argtypes = [Music]
    _rl.UpdateMusicStream.restype = None

    _rl.StopMusicStream.argtypes = [Music]
    _rl.StopMusicStream.restype = None

    _rl.PauseMusicStream.argtypes = [Music]
    _rl.PauseMusicStream.restype = None

    _rl.ResumeMusicStream.argtypes = [Music]
    _rl.ResumeMusicStream.restype = None

    _rl.SetMusicVolume.argtypes = [Music, Float]
    _rl.SetMusicVolume.restype = None

    _rl.SetMusicPitch.argtypes = [Music, Float]
    _rl.SetMusicPitch.restype = None

    _rl.GetMusicTimeLength.argtypes = [Music]
    _rl.GetMusicTimeLength.restype = Float

    _rl.GetMusicTimePlayed.argtypes = [Music]
    _rl.GetMusicTimePlayed.restype = Float

    _rl.InitAudioStream.argtypes = [UInt, UInt, UInt]
    _rl.InitAudioStream.restype = AudioStream

    _rl.UpdateAudioStream.argtypes = [AudioStream, VoidPtr, Int]
    _rl.UpdateAudioStream.restype = None

    _rl.CloseAudioStream.argtypes = [AudioStream]
    _rl.CloseAudioStream.restype = None

    _rl.IsAudioStreamProcessed.argtypes = [AudioStream]
    _rl.IsAudioStreamProcessed.restype = Bool

    _rl.PlayAudioStream.argtypes = [AudioStream]
    _rl.PlayAudioStream.restype = None

    _rl.PauseAudioStream.argtypes = [AudioStream]
    _rl.PauseAudioStream.restype = None

    _rl.ResumeAudioStream.argtypes = [AudioStream]
    _rl.ResumeAudioStream.restype = None

    _rl.IsAudioStreamPlaying.argtypes = [AudioStream]
    _rl.IsAudioStreamPlaying.restype = Bool

    _rl.StopAudioStream.argtypes = [AudioStream]
    _rl.StopAudioStream.restype = None

    _rl.SetAudioStreamVolume.argtypes = [AudioStream, Float]
    _rl.SetAudioStreamVolume.restype = None

    _rl.SetAudioStreamPitch.argtypes = [AudioStream, Float]
    _rl.SetAudioStreamPitch.restype = None

    _rl.SetAudioStreamBufferSizeDefault.argtypes = [Int]
    _rl.SetAudioStreamBufferSizeDefault.restype = None

    # endregion (raylib)

    # region RAYMATH

    _rl.Clamp.argtypes = (Float, Float, Float)
    _rl.Clamp.restype = Float

    _rl.Lerp.argtypes = (Float, Float, Float)
    _rl.Lerp.restype = Float

    _rl.Normalize.argtypes = (Float, Float, Float)
    _rl.Normalize.restype = Float

    _rl.Remap.argtypes = (Float, Float, Float, Float, Float)
    _rl.Remap.restype = Float

    _rl.Vector2Zero.argtypes = ()
    _rl.Vector2Zero.restype = Vector2

    _rl.Vector2One.argtypes = ()
    _rl.Vector2One.restype = Vector2

    _rl.Vector2Add.argtypes = (Vector2, Vector2)
    _rl.Vector2Add.restype = Vector2

    _rl.Vector2AddValue.argtypes = (Vector2, Float)
    _rl.Vector2AddValue.restype = Vector2

    _rl.Vector2Subtract.argtypes = (Vector2, Vector2)
    _rl.Vector2Subtract.restype = Vector2

    _rl.Vector2SubtractValue.argtypes = (Vector2, Float)
    _rl.Vector2SubtractValue.restype = Vector2

    _rl.Vector2Length.argtypes = (Vector2,)
    _rl.Vector2Length.restype = Float

    _rl.Vector2LengthSqr.argtypes = (Vector2,)
    _rl.Vector2LengthSqr.restype = Float

    _rl.Vector2DotProduct.argtypes = (Vector2, Vector2)
    _rl.Vector2DotProduct.restype = Float

    _rl.Vector2Distance.argtypes = (Vector2, Vector2)
    _rl.Vector2Distance.restype = Float

    _rl.Vector2Angle.argtypes = (Vector2, Vector2)
    _rl.Vector2Angle.restype = Float

    _rl.Vector2Scale.argtypes = (Vector2, Float)
    _rl.Vector2Scale.restype = Vector2

    _rl.Vector2Multiply.argtypes = (Vector2, Vector2)
    _rl.Vector2Multiply.restype = Vector2

    _rl.Vector2Negate.argtypes = (Vector2,)
    _rl.Vector2Negate.restype = Vector2

    _rl.Vector2Divide.argtypes = (Vector2, Vector2)
    _rl.Vector2Divide.restype = Vector2

    _rl.Vector2Normalize.argtypes = (Vector2,)
    _rl.Vector2Normalize.restype = Vector2

    _rl.Vector2Lerp.argtypes = (Vector2, Vector2, Float)
    _rl.Vector2Lerp.restype = Vector2

    _rl.Vector2Reflect.argtypes = (Vector2, Vector2)
    _rl.Vector2Reflect.restype = Vector2

    _rl.Vector2Rotate.argtypes = (Vector2, Float)
    _rl.Vector2Rotate.restype = Vector2

    _rl.Vector2MoveTowards.argtypes = (Vector2, Vector2, Float)
    _rl.Vector2MoveTowards.restype = Vector2

    _rl.Vector3Zero.argtypes = ()
    _rl.Vector3Zero.restype = Vector3

    _rl.Vector3One.argtypes = ()
    _rl.Vector3One.restype = Vector3

    _rl.Vector3Add.argtypes = (Vector3, Vector3)
    _rl.Vector3Add.restype = Vector3

    _rl.Vector3AddValue.argtypes = (Vector3, Float)
    _rl.Vector3AddValue.restype = Vector3

    _rl.Vector3Subtract.argtypes = (Vector3, Vector3)
    _rl.Vector3Subtract.restype = Vector3

    _rl.Vector3SubtractValue.argtypes = (Vector3, Float)
    _rl.Vector3SubtractValue.restype = Vector3

    _rl.Vector3Scale.argtypes = (Vector3, Float)
    _rl.Vector3Scale.restype = Vector3

    _rl.Vector3Multiply.argtypes = (Vector3, Vector3)
    _rl.Vector3Multiply.restype = Vector3

    _rl.Vector3CrossProduct.argtypes = (Vector3, Vector3)
    _rl.Vector3CrossProduct.restype = Vector3

    _rl.Vector3Perpendicular.argtypes = (Vector3,)
    _rl.Vector3Perpendicular.restype = Vector3

    _rl.Vector3Length.argtypes = (Vector3,)
    _rl.Vector3Length.restype = Float

    _rl.Vector3LengthSqr.argtypes = (Vector3,)
    _rl.Vector3LengthSqr.restype = Float

    _rl.Vector3DotProduct.argtypes = (Vector3, Vector3)
    _rl.Vector3DotProduct.restype = Float

    _rl.Vector3Distance.argtypes = (Vector3, Vector3)
    _rl.Vector3Distance.restype = Float

    _rl.Vector3Negate.argtypes = (Vector3,)
    _rl.Vector3Negate.restype = Vector3

    _rl.Vector3Divide.argtypes = (Vector3, Vector3)
    _rl.Vector3Divide.restype = Vector3

    _rl.Vector3Normalize.argtypes = (Vector3,)
    _rl.Vector3Normalize.restype = Vector3

    _rl.Vector3OrthoNormalize.argtypes = (Vector3, Vector3)
    _rl.Vector3OrthoNormalize.restype = None

    _rl.Vector3Transform.argtypes = (Vector3, Matrix)
    _rl.Vector3Transform.restype = Vector3

    _rl.Vector3RotateByQuaternion.argtypes = (Vector3, Quaternion)
    _rl.Vector3RotateByQuaternion.restype = Vector3

    _rl.Vector3Lerp.argtypes = (Vector3, Vector3, Float)
    _rl.Vector3Lerp.restype = Vector3

    _rl.Vector3Reflect.argtypes = (Vector3, Vector3)
    _rl.Vector3Reflect.restype = Vector3

    _rl.Vector3Min.argtypes = (Vector3, Vector3)
    _rl.Vector3Min.restype = Vector3

    _rl.Vector3Max.argtypes = (Vector3, Vector3)
    _rl.Vector3Max.restype = Vector3

    _rl.Vector3Barycenter.argtypes = (Vector3, Vector3, Vector3, Vector3)
    _rl.Vector3Barycenter.restype = Vector3

    _rl.Vector3ToFloatV.argtypes = (Vector3,)
    _rl.Vector3ToFloatV.restype = FloatPtr

    _rl.MatrixDeterminant.argtypes = (Matrix,)
    _rl.MatrixDeterminant.restype = Float

    _rl.MatrixTrace.argtypes = (Matrix,)
    _rl.MatrixTrace.restype = Float

    _rl.MatrixTranspose.argtypes = (Matrix,)
    _rl.MatrixTranspose.restype = Matrix

    _rl.MatrixInvert.argtypes = (Matrix,)
    _rl.MatrixInvert.restype = Matrix

    _rl.MatrixNormalize.argtypes = (Matrix,)
    _rl.MatrixNormalize.restype = Matrix

    _rl.MatrixIdentity.argtypes = ()
    _rl.MatrixIdentity.restype = Matrix

    _rl.MatrixAdd.argtypes = (Matrix, Matrix)
    _rl.MatrixAdd.restype = Matrix

    _rl.MatrixSubtract.argtypes = (Matrix, Matrix)
    _rl.MatrixSubtract.restype = Matrix

    _rl.MatrixMultiply.argtypes = (Matrix, Matrix)
    _rl.MatrixMultiply.restype = Matrix

    _rl.MatrixTranslate.argtypes = (Float, Float, Float)
    _rl.MatrixTranslate.restype = Matrix

    _rl.MatrixRotate.argtypes = (Vector3, Float)
    _rl.MatrixRotate.restype = Matrix

    _rl.MatrixRotateX.argtypes = (Float,)
    _rl.MatrixRotateX.restype = Matrix

    _rl.MatrixRotateY.argtypes = (Float,)
    _rl.MatrixRotateY.restype = Matrix

    _rl.MatrixRotateZ.argtypes = (Float,)
    _rl.MatrixRotateZ.restype = Matrix

    _rl.MatrixRotateXYZ.argtypes = (Vector3,)
    _rl.MatrixRotateXYZ.restype = Matrix

    _rl.MatrixRotateZYX.argtypes = (Vector3,)
    _rl.MatrixRotateZYX.restype = Matrix

    _rl.MatrixScale.argtypes = (Float, Float, Float)
    _rl.MatrixScale.restype = Matrix

    _rl.MatrixFrustum.argtypes = (Double, Double, Double, Double, Double, Double)
    _rl.MatrixFrustum.restype = Matrix

    _rl.MatrixPerspective.argtypes = (Double, Double, Double, Double)
    _rl.MatrixPerspective.restype = Matrix

    _rl.MatrixOrtho.argtypes = (Double, Double, Double, Double, Double, Double)
    _rl.MatrixOrtho.restype = Matrix

    _rl.MatrixLookAt.argtypes = (Vector3, Vector3, Vector3)
    _rl.MatrixLookAt.restype = Matrix

    _rl.MatrixToFloatV.argtypes = (Matrix,)
    _rl.MatrixToFloatV.restype = FloatPtr

    _rl.QuaternionAdd.argtypes = (Quaternion, Quaternion)
    _rl.QuaternionAdd.restype = Quaternion

    _rl.QuaternionAddValue.argtypes = (Quaternion, Float)
    _rl.QuaternionAddValue.restype = Quaternion

    _rl.QuaternionSubtract.argtypes = (Quaternion, Quaternion)
    _rl.QuaternionSubtract.restype = Quaternion

    _rl.QuaternionSubtractValue.argtypes = (Quaternion, Float)
    _rl.QuaternionSubtractValue.restype = Quaternion

    _rl.QuaternionIdentity.argtypes = ()
    _rl.QuaternionIdentity.restype = Quaternion

    _rl.QuaternionLength.argtypes = (Quaternion,)
    _rl.QuaternionLength.restype = Float

    _rl.QuaternionNormalize.argtypes = (Quaternion,)
    _rl.QuaternionNormalize.restype = Quaternion

    _rl.QuaternionInvert.argtypes = (Quaternion,)
    _rl.QuaternionInvert.restype = Quaternion

    _rl.QuaternionMultiply.argtypes = (Quaternion, Quaternion)
    _rl.QuaternionMultiply.restype = Quaternion

    _rl.QuaternionScale.argtypes = (Quaternion, Float)
    _rl.QuaternionScale.restype = Quaternion

    _rl.QuaternionDivide.argtypes = (Quaternion, Quaternion)
    _rl.QuaternionDivide.restype = Quaternion

    _rl.QuaternionLerp.argtypes = (Quaternion, Quaternion, Float)
    _rl.QuaternionLerp.restype = Quaternion

    _rl.QuaternionNlerp.argtypes = (Quaternion, Quaternion, Float)
    _rl.QuaternionNlerp.restype = Quaternion

    _rl.QuaternionSlerp.argtypes = (Quaternion, Quaternion, Float)
    _rl.QuaternionSlerp.restype = Quaternion

    _rl.QuaternionFromVector3ToVector3.argtypes = (Vector3, Vector3)
    _rl.QuaternionFromVector3ToVector3.restype = Quaternion

    _rl.QuaternionFromMatrix.argtypes = (Matrix,)
    _rl.QuaternionFromMatrix.restype = Quaternion

    _rl.QuaternionToMatrix.argtypes = (Quaternion,)
    _rl.QuaternionToMatrix.restype = Matrix

    _rl.QuaternionFromAxisAngle.argtypes = (Vector3, Float)
    _rl.QuaternionFromAxisAngle.restype = Quaternion

    _rl.QuaternionToAxisAngle.argtypes = (Quaternion, Vector3, Float)
    _rl.QuaternionToAxisAngle.restype = None

    _rl.QuaternionFromEuler.argtypes = (Float, Float, Float)
    _rl.QuaternionFromEuler.restype = Quaternion

    _rl.QuaternionToEuler.argtypes = (Quaternion,)
    _rl.QuaternionToEuler.restype = Vector3

    _rl.QuaternionTransform.argtypes = (Quaternion, Matrix)
    _rl.QuaternionTransform.restype = Quaternion

    _rl.Vector3Unproject.argtypes = (Vector3, Matrix, Matrix)
    _rl.Vector3Unproject.restype = Vector3

    # endregion (raymath)

    _initialized = True

# endregion (headers)
# ---------------------------------------------------------
