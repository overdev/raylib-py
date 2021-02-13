from raylibpy import *


def main():
    screen_width = 800
    mouse_scale_mark_size = 12
    screen_height = 450
    init_window(screen_width, screen_height, "raylib [shapes] example - rectangle scaling mouse")
    rec = Rectangle(100, 100, 200, 80)
    mouse_scale_ready = False
    mouse_scale_mode = False

    set_target_fps(60)

    while not window_should_close():
        mouse_position = get_mouse_position()
        if check_collision_point_rec(mouse_position, rec) and check_collision_point_rec(mouse_position,
                                                                                        Rectangle(
                                                                                            rec.x + rec.width - mouse_scale_mark_size,
                                                                                            rec.y + rec.height - mouse_scale_mark_size,
                                                                                            mouse_scale_mark_size,
                                                                                            mouse_scale_mark_size)):
            mouse_scale_ready = True
            if is_mouse_button_pressed(MOUSE_LEFT_BUTTON):
                mouse_scale_mode = True
        else:
            mouse_scale_ready = False

        if mouse_scale_mode:
            mouse_scale_ready = True
            rec.width = (mouse_position.x - rec.x)
            rec.height = (mouse_position.y - rec.y)
            if rec.width < mouse_scale_mark_size:
                rec.width = mouse_scale_mark_size
            if rec.height < mouse_scale_mark_size:
                rec.height = mouse_scale_mark_size
            if is_mouse_button_released(MOUSE_LEFT_BUTTON):
                mouse_scale_mode = False

        begin_drawing()
        clear_background(RAYWHITE)
        draw_text("Scale rectangle dragging from bottom-right corner!", 10, 10, 20, GRAY)
        draw_rectangle_rec(rec, fade(GREEN, 0.5))

        if mouse_scale_ready:
            draw_rectangle_lines_ex(rec, 1, RED)
            draw_triangle(Vector2(rec.x + rec.width - mouse_scale_mark_size, rec.y + rec.height),
                          Vector2(rec.x + rec.width, rec.y + rec.height),
                          Vector2(rec.x + rec.width, rec.y + rec.height - mouse_scale_mark_size),
                          RED)

        end_drawing()

    close_window()


if __name__ == '__main__':
    main()
