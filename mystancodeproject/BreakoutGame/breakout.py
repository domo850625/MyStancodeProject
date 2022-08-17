"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
--------------------------------------
TODO:製作彈力球小遊戲，限制三條命，在三條命內打完磚通關，沒打完則失敗。
MEMO:助教之抱歉沒仔細看到 extension 需要另外開檔案寫，然後發現的時候都已經寫在一起沒時間改了...需要再麻煩您的火眼金睛...以及您的耐心...
     希望貌美如花的助教可以見諒不成材的學員...可以吧 Q_Q ?
"""
import random
from campy.graphics.gobjects import GRect
from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 15  # 100 frames per second
NUM_LIVES = 5  # Number of attempts

graphics = BreakoutGraphics()
bonus_red_box = GRect(10, 10)
bonus_purple_box = GRect(10, 10)


def main():
    dx = 0
    dy = 0
    destroy_counter = graphics.brick_rows * graphics.brick_cols
    while True:

        speed = random.randint(5, 10)
        graphics.back_ground_move()

        # 球體運動前的初始狀態。
        if dx == 0 and dy == 0:

            dx = graphics.get_ball_dx()
            dy = graphics.get_ball_dy()

            pause(FRAME_RATE)
            graphics.window.remove(bonus_red_box)
            graphics.window.remove(bonus_purple_box)

        # 球體運動後狀態。
        else:
            if graphics.life_counter > 0:
                graphics.ball.move(dx, dy)
                bonus_red_box.move(0, speed)
                bonus_purple_box.move(0, speed)

                # 左右兩側碰壁限制。
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = -dx

                # 上方碰壁限制。
                if graphics.ball.y <= 0:
                    dy = -dy

                # 下方墜落限制。
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.window.remove(graphics.ball)
                    life_reduce()
                    graphics.game_continues()
                    dx = 0
                    dy = 0
                size = graphics.ball.width

                ball_hit = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y ) \
                           or graphics.window.get_object_at(graphics.ball.x + size, graphics.ball.y) \
                           or graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + size) \
                           or graphics.window.get_object_at(graphics.ball.x + size, graphics.ball.y + size)

                # 球體觸碰其他物件限制。
                if ball_hit is not None and ball_hit is not graphics.img and ball_hit is not bonus_red_box and \
                        ball_hit is not graphics.score_word and ball_hit is not graphics.life_word and \
                        ball_hit is not bonus_purple_box:

                    # 當該點接觸的物件是磚塊的時候觸發。
                    if ball_hit is not graphics.paddle:
                        graphics.window.remove(ball_hit)
                        destroy_counter -= 1
                        graphics.score_get(destroy_counter)
                        angel_and_evil(ball_hit)
                        dy = -dy

                    # 當該點接觸是球板時觸發。
                    else:
                        if graphics.ball.y + graphics.ball.height > graphics.paddle.y:
                            dy = -dy

                # 當該點接觸不為球板、磚塊時觸發。
                else:
                    if graphics.ball.y + graphics.ball.height >= graphics.paddle.y:
                        dy = dy

                # 當球板接到補血方塊時觸發。
                if graphics.paddle.x < bonus_red_box.x < graphics.paddle.x + graphics.paddle.width and \
                        graphics.paddle.y + graphics.paddle.height / 2 >= bonus_red_box.y + bonus_red_box.height >= \
                        graphics.paddle.y:
                    graphics.window.remove(bonus_red_box)
                    life_add()

                # 當球板接到扣血方塊時觸發。
                if graphics.paddle.x < bonus_purple_box.x < graphics.paddle.x + graphics.paddle.width and \
                        graphics.paddle.y + graphics.paddle.height / 2 >= bonus_purple_box.y + bonus_purple_box.height >= \
                        graphics.paddle.y:
                    graphics.window.remove(bonus_purple_box)
                    life_reduce()

                # 觸發勝利的條件。
                if destroy_counter == 0:
                    graphics.window.remove(graphics.ball)
                    graphics.win_the_game()
                    break
                pause(FRAME_RATE)

            # 當性命不足時終結畫面
            else:
                graphics.game_over()


# extension 之來不及寫完整的 bonus
def angel_and_evil(position):
    bonus_red_box.filled = True
    bonus_purple_box.filled = True
    if random.random() < 0.1:
        bonus_red_box.fill_color = 'red'
        bonus_red_box.color = 'red'
        graphics.window.add(bonus_red_box, x=position.x, y=position.y)
    if random.random() < 0.4:
        bonus_purple_box.fill_color = 'purple'
        bonus_purple_box.color = 'purple'
        graphics.window.add(bonus_purple_box, x=position.x, y=position.y)


# 計算補血。
def life_add():
    graphics.life_counter += 1
    graphics.life_get()


# 計算扣血。
def life_reduce():
    graphics.life_counter -= 1
    graphics.life_get()


if __name__ == '__main__':
    main()
