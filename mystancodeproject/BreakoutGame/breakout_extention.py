"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gimage import GImage
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmousemoved, onmouseclicked
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10  # 100 frames per second
NUM_LIVES = 5  # Number of attempts

graphics = BreakoutGraphics()

def main():




    dx = 0
    dy = 0

    while True:

        if dx == 0 and dy == 0:

            dx = graphics.get_ball_dx()
            dy = graphics.get_ball_dy()

            pause(FRAME_RATE)

        else:

            graphics.ball.move(dx, dy)

            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                dx = -dx
            if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
                dy = -dy

            size = graphics.ball.width

            ball_hit = graphics.window.get_object_at(graphics.ball.x - 1, graphics.ball.y - 1) \
                       or graphics.window.get_object_at(graphics.ball.x + size + 1, graphics.ball.y - 1) \
                       or graphics.window.get_object_at(graphics.ball.x - 1, graphics.ball.y + size + 1) \
                       or graphics.window.get_object_at(graphics.ball.x + size + 1, graphics.ball.y + size + 1)

            if ball_hit is not None:

                if ball_hit is not graphics.img:

                    if ball_hit is not graphics.paddle:

                        graphics.window.remove(ball_hit)
                        dy = -dy

                    else:

                        dy = -dy

            else:

                dy = dy

            pause(FRAME_RATE)

    # Add the animation loop here!


if __name__ == '__main__':
    main()
