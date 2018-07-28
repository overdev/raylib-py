# core_basic_window.py
import raylibpy as rl


def main():

    rl.init_window(800, 450, b"raylib [core] example - basic window")

    rl.set_target_fps(60)

    while not rl.window_should_close():

        rl.begin_drawing()
        rl.clear_background(rl.RAYWHITE)
        rl.draw_text(b"Congrats! You created your first window!", 190, 200, 20, rl.LIGHTGRAY)
        rl.end_drawing()

    rl.close_window()


if __name__ == '__main__':
    main()