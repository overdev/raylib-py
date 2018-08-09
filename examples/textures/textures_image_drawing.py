# textures_image_drawing.py

from raylibpy import *

NORMAL = 0
HOVERED = 1
PRESSED = 2
DISABLED = 3


def gui_button(rec: Rectangle, text: str, enabled: bool = True) -> bool:
    global state

    clicked: bool = False

    size = 10
    text_width: int = measure_text(text, size)
    text_height: int = size
    
    if rec.width < text_width:
        rec.width = text_width
    if rec.height < text_height:
        rec.height = text_height

    if enabled:
        # Update control
        # -------------------------------------------------------------------
        if (state != DISABLED):
            mouse_point: Vector2 = get_mouse_position()

            # Check button state
            if check_collision_point_rec(mouse_point, rec):
                state = HOVERED
                if is_mouse_button_down(MOUSE_LEFT_BUTTON):
                    state = PRESSED
                elif is_mouse_button_released(MOUSE_LEFT_BUTTON):
                    clicked = True
                    state = HOVERED
            else:
                state = NORMAL
            # -------------------------------------------------------------------

            # Draw control
            # -------------------------------------------------------------------
            draw_npatch(button_states[state], rec, False, (0, 0), 0., WHITE)
            draw_text(text, rec.x + (rec.width / 2) - (text_width / 2), rec.y + (rec.height / 2) - (text_height / 2), size, BLACK)
    else:
        draw_npatch(button_states[DISABLED], rec, False, (0, 0), 0., WHITE)
        draw_text(text, rec.x + (rec.width / 2) - (text_width / 2), rec.y + (rec.height / 2) - (text_height / 2), size, DARKGRAY)
        # -----------------------------------------------------------------

    return clicked


def main() -> int:
    global state, button_states

    screen_width: int = 800
    screen_height: int = 450

    init_window(screen_width, screen_height, "raylib [textures] example - nine patch drawing")

    # NOTE: Textures MUST be loaded after Window initialization (OpenGL context is required)
    npatch_button: Texture2D = load_texture("resources/ninepatch_button.png")

    btn_normal: NPatch = NPatch()
    btn_normal.texture = npatch_button
    btn_normal.sourceRec = Rectangle(0, 0, 64, 64)
    btn_normal.minSize = Vector2(0, 0)
    btn_normal.set_border_width(8, 8, 8, 8)
    btn_normal.set_padding(8, 8, 8, 8)
    btn_normal.type = NPT_9PATCH

    btn_hovered: NPatch = NPatch()
    btn_hovered.texture = npatch_button
    btn_hovered.sourceRec = Rectangle(0, 64, 64, 64)
    btn_hovered.minSize = Vector2(0, 0)
    btn_hovered.set_border_width(8, 8, 8, 8)
    btn_hovered.set_padding(8, 8, 8, 8)
    btn_hovered.type = NPT_9PATCH

    btn_pressed: NPatch = NPatch()
    btn_pressed.texture = npatch_button
    btn_pressed.sourceRec = Rectangle(0, 128, 64, 64)
    btn_pressed.minSize = Vector2(0, 0)
    btn_pressed.set_border_width(8, 8, 8, 8)
    btn_pressed.set_padding(8, 8, 8, 8)
    btn_pressed.type = NPT_9PATCH

    btn_disabled: NPatch = NPatch()
    btn_disabled.texture = npatch_button
    btn_disabled.sourceRec = Rectangle(0, 192, 64, 64)
    btn_disabled.minSize = Vector2(0, 0)
    btn_disabled.set_border_width(8, 8, 8, 8)
    btn_disabled.set_padding(8, 8, 8, 8)
    btn_disabled.type = NPT_9PATCH

    use_padding: bool = True
    state = NORMAL
    button_states = [
        btn_normal,
        btn_hovered,
        btn_pressed,
        btn_disabled,
    ]

    button: Rectangle = Rectangle(200, 175, 175, 100)
    toggle_button: Rectangle = Rectangle(425, 175, 175, 100)
    enabled: bool = False

    set_target_fps(60)

    # Main game loop
    # ----------------------------------------------------------------------
    while not window_should_close():
        # Update
        # ------------------------------------------------------------------
        if gui_button(button, "Enabler/Disabler Button"):
            enabled = not enabled
        if gui_button(toggle_button, "Click Me", enabled):
            print("Clicked!")

        # Draw
        # ------------------------------------------------------------------
        begin_drawing()
        clear_background(RAYWHITE)

        draw_rectangle( 10, 10, 250, 93, fade(SKYBLUE, 0.5))
        draw_rectangle_lines( 10, 10, 250, 93, BLUE)

        draw_text("NPatch example (emulating a button)", 20, 20, 10, BLACK)
        draw_text("  Click the button at the left", 40, 40, 10, DARKGRAY)
        draw_text("  to enable/disable the button", 40, 60, 10, DARKGRAY)
        draw_text("  at the right.", 40, 80, 10, DARKGRAY)

        end_drawing()

    unload_texture(npatch_button)

    close_window()

    return 0


if __name__ == '__main__':
    main()
