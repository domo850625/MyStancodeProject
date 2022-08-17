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
from campy.gui.events.mouse import onmouseclicked, onmousemoved
from campy.gui.events.timer import pause
import random

BRICK_SPACING = 5  # 磚塊與磚塊之間的距離。
BRICK_WIDTH = 40  # 一個磚塊的寬。
BRICK_HEIGHT = 15  # 一個磚塊的高。
BRICK_ROWS = 10  # 磚塊的總列數。 #10
BRICK_COLS = 10  # 磚塊的總行數。
BRICK_OFFSET = 50  # 第一列磚塊頂部與視窗頂部邊界的距離。
BALL_RADIUS = 10  # 球的半徑。
PADDLE_WIDTH = 475  # 板子的寬。 #75
PADDLE_HEIGHT = 15  # 板子的高。
PADDLE_OFFSET = 50  # 板子底部與視窗底部邊界的距離。
INITIAL_Y_SPEED = 7  # 球在Y方向移動的初始速度。
MAX_X_SPEED = 5  # 球在X方向移動的最大速度。

loading_key = False
start_key = False
loading_finish = False
game_over_key = False
score_counter = 0


class BreakoutGraphics:
    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # first page of game
        self.img = GImage('background.gif')
        self.window.add(self.img, x=0, y=0)

        self.game_start_word = GLabel('Welcome to the StanBall')
        self.game_start_word.font = 'Verdana-20-bold-italic'
        self.window.add(self.game_start_word, x=(self.window.width - self.game_start_word.width) / 2,
                        y=(self.window.height - self.game_start_word.height) / 2 - 60)

        self.game_word = GLabel('---- click to continue ----')
        self.game_word.font = 'Verdana-10-bold-italic'
        self.window.add(self.game_word, x=(self.window.width - self.game_word.width) / 2,
                        y=(self.window.height - self.game_word.height) / 2 + 70)
        self.game_start_click_word = GLabel('---- click to start the Game ----')

        # bricks
        self.brick_rows = BRICK_ROWS
        self.brick_cols = BRICK_COLS

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.paddle.fill_color = 'white'
        self.paddle.color = 'white'

        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.ball.filled = True
        self.ball.fill_color = 'black'
        self.ball.color = 'black'

        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)
        onmouseclicked(self.ball_move)

        # life_word & score_word
        self.life_counter = 3

        self.life_word = GLabel('life X '+str(self.life_counter))
        self.life_word.font = 'Verdana-10-bold-italic'
        self.score_word = GLabel('Score : ' + str(score_counter))
        self.score_word.font = 'Verdana-10-bold-italic'



        # game over word
        self.game_over_word = GLabel('Game Over !!!')
        self.game_over_word.font = 'Verdana-40-bold-italic'

        self.game_over_fighting_word = GLabel(
            'Keep fighting, Keep pushing !!!\n\n                       But..\n\n          U have no chance !!!\n\n              See u next time~')
        self.game_over_fighting_word.font = 'Verdana-10-bold-italic'

        # the word of winning the game
        self.win_the_game_word = GLabel('U Winnn !')
        self.win_the_game_word.font = 'Verdana-40-bold-italic'

        self.win_the_game_word_1 = GLabel('Congratulations !!!')
        self.win_the_game_word_1.font = 'Verdana-10-bold-italic'

        self.win_the_game_word_2 = GLabel('U\'re a super Genius of StanBall !!!')
        self.win_the_game_word_2.font = 'Verdana-10-bold-italic'

    # extension:等待畫面。
    def loading_page(self):
        global loading_key, loading_finish
        loading_key = True
        self.window.remove(self.game_word)
        self.game_wait_word = GLabel('Please wait a minute!!')
        self.game_wait_word.font = 'Verdana-10-bold-italic'
        self.window.add(self.game_wait_word, x=(self.window.width - self.game_wait_word.width) / 2,
                        y=(self.window.height - self.game_wait_word.height) / 2 - 10)

        self.loading_page_animation()
        loading_finish = True

    # 遊戲開始的處理器，清除一切雜物、列出磚塊、球、板子、計分板、生命板。
    def game_start(self):

        global start_key

        # remove item
        self.window.remove(self.game_start_word)
        self.window.remove(self.game_wait_word)
        for i in range(9):
            self.window.remove(self.loading_box_list[i])
        self.window.remove(self.game_start_click_word)
        start_key = True

        # make the paddle and ball and score
        self.window.add(self.paddle, x=(self.window.width - PADDLE_WIDTH) / 2, y=self.window.height - PADDLE_OFFSET)
        self.window.add(self.ball, x=self.window.width / 2 - BALL_RADIUS, y=self.window.height / 2 - BALL_RADIUS)
        self.window.add(self.life_word, self.window.width-self.life_word.width - 10,y=self.window.height - 10)
        self.window.add(self.score_word, x=0, y=self.window.height - 10)

        # Draw bricks
        color_list = ['darkblue', 'royalblue', 'cornflowerblue', 'dodgerblue', 'lightskyblue', 'skyblue',
                      'powderblue', 'lightcyan', 'azure', 'white', 'white', 'azure', 'lightcyan', 'powderblue',
                      'skyblue', 'lightskyblue', 'dodgerblue', 'cornflowerblue', 'royalblue', 'darkblue']

        self.brick_list = []
        self.brick_list_col = []
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                brick_word = str('brick' + str(i) + '_' + str(j))
                self.brick_list_col += [brick_word]
            self.brick_list.insert(i, self.brick_list_col)
            self.brick_list_col = []

        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick_list[i][j] = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick_list[i][j].filled = True
                self.brick_list[i][j].fill_color = color_list[i % len(color_list)]
                self.brick_list[i][j].color = color_list[i % len(color_list)]
                self.window.add(self.brick_list[i][j], x=(BRICK_WIDTH + BRICK_SPACING) * j,
                                y=(BRICK_HEIGHT + BRICK_SPACING) * i + BRICK_HEIGHT * 2)

    # 球板定義。
    def paddle_move(self, event):
        self.paddle.x = event.x - PADDLE_WIDTH / 2
        if self.paddle.x <= 0:
            self.paddle.x = 0
        elif self.paddle.x >= self.window.width - PADDLE_WIDTH:
            self.paddle.x = self.window.width - PADDLE_WIDTH

    # 球速定義(在第二個elif)，順便加入首頁、等待頁面的判定。
    def ball_move(self, event):
        if loading_key is False:
            self.loading_page()

        elif start_key is False and loading_key is True and loading_finish is True:
            self.game_start()

        elif start_key is True and loading_key is True and loading_finish is True and game_over_key is False:
            if self.__dx == 0 and self.__dy == 0:
                self.__dx = random.randint(1, MAX_X_SPEED)
                self.__dy = INITIAL_Y_SPEED
                if random.random() > 0.5:
                    self.__dx = -self.__dx

    # 回傳x軸速度。
    def get_ball_dx(self):
        return self.__dx

    # 回傳y軸速度。
    def get_ball_dy(self):
        return self.__dy

    # extension:等待畫面動效。
    def loading_page_animation(self):

        loading_counter = 0

        self.loading_box_list = ['loading1', 'loading2', 'loading3', 'loading4', 'loading5', 'loading6', 'loading7',
                                 'loading8', 'loading9']

        for i in range(9):
            self.loading_box_list[i] = GRect(10, 20)
            self.loading_box_list[i].filled = True
            self.loading_box_list[i].fill_color = 'darkgrey'
            self.loading_box_list[i].color = 'darkgrey'
            self.window.add(self.loading_box_list[i], x=(self.window.width - 120) / 2 + (i - 1) * 20,
                            y=(self.window.height / 2 + 20))
        while True:

            loading_counter += 1

            for i in range(9):
                self.loading_box_list[i].fill_color = 'darkgrey'
                self.loading_box_list[i].color = 'darkgrey'

            self.loading_box_list[loading_counter % 9 - 1].fill_color = 'darkorange'
            self.loading_box_list[loading_counter % 9 - 1].color = 'darkorange'
            self.loading_box_list[loading_counter % 9].fill_color = 'darkorange'
            self.loading_box_list[loading_counter % 9].color = 'darkorange'
            self.loading_box_list[loading_counter % 9 - 2].fill_color = 'darkorange'
            self.loading_box_list[loading_counter % 9 - 2].color = 'darkorange'

            if loading_counter >= 15:
                break

            pause(500)

        for i in range(9):
            self.loading_box_list[i].fill_color = 'darkorange'
            self.loading_box_list[i].color = 'darkorange'

        self.game_start_click_word.font = 'Verdana-10-bold-italic'
        self.window.add(self.game_start_click_word, x=(self.window.width - self.game_start_click_word.width) / 2,
                        y=(self.window.height - self.game_start_click_word.height) / 2 + 130)

    # 清除作業。
    def clear_all(self):

        # clear brick
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.window.remove(self.brick_list[i][j])

        # clear paddle
        self.window.remove(self.paddle)

        # clear ball
        self.window.remove(self.ball)

        # clear game over page
        self.window.remove(self.game_over_word)
        self.window.remove(self.game_over_fighting_word)
        self.window.remove(self.img)

    # 使用完三條命且沒消滅完磚塊，進入的「結束頁面」。
    def game_over(self):
        global game_over_key
        game_over_key = True
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.window.remove(self.brick_list[i][j])
        self.window.remove(self.paddle)
        self.window.remove(self.ball)
        self.window.add(self.game_over_word, x=(self.window.width - self.game_over_word.width) / 2,
                        y=(self.window.height - self.game_over_word.height) / 2 - 20)
        self.window.add(self.game_over_fighting_word,
                        x=-(self.window.width - self.game_over_fighting_word.width) / 2 - 30,
                        y=self.game_over_word.y + self.game_over_word.height * 3)

    # extension:背景動起來。
    def back_ground_move(self):
        if self.img.y + self.img.height > self.window.height:
            self.img.y -= 0.2

    # 3條命的限制 (涵蓋extension:紀錄餘剩的生命。)
    def game_continues(self):
        if self.life_counter > 0:

            self.window.add(self.ball, x=self.window.width / 2 - BALL_RADIUS, y=self.window.height / 2 - BALL_RADIUS)
            self.__dx = 0
            self.__dy = 0

        elif self.life_counter <= 0:

            self.game_over()

    # 消滅完全部的磚塊，進入的「勝利頁面」。
    def win_the_game(self):
        self.window.remove(self.paddle)
        self.window.remove(self.ball)
        self.window.add(self.win_the_game_word, x=(self.window.width - self.win_the_game_word.width) / 2,
                        y=(self.window.height - self.win_the_game_word.height) / 2 - 20)
        self.window.add(self.win_the_game_word_1,
                        x=(self.window.width - self.win_the_game_word_1.width) / 2,
                        y=self.win_the_game_word.y + self.win_the_game_word.height)
        self.window.add(self.win_the_game_word_2,
                        x=(self.window.width - self.win_the_game_word_2.width) / 2,
                        y=self.win_the_game_word_1.y + self.win_the_game_word_1.height * 3)

    # extension：計算分數的function，打前50%的磚+5分，第50~70%的磚+10分，第70~80%的磚+15分，第80~90%的磚+20分，第90~100%的磚+50分。
    def score_get(self, count):
        global score_counter
        all_bricks = self.brick_cols * self.brick_rows
        if all_bricks > count >= all_bricks*0.5:
            score_counter += 5
        elif all_bricks*0.5 > count >= all_bricks*0.3:
            score_counter += 10
        elif all_bricks*0.3 > count >= all_bricks*0.2:
            score_counter += 15
        elif all_bricks*0.2 > count >= all_bricks*0.1:
            score_counter += 20
        elif all_bricks*0.1 > count:
            score_counter += 50

        score_counter_box = score_counter
        score_word_print = 'Score : ' + str(score_counter_box)
        self.window.remove(self.score_word)
        self.score_word = GLabel(score_word_print)
        self.score_word.font = 'Verdana-10-bold-italic'
        self.window.add(self.score_word, x=0, y=self.window.height - 10)

    def life_get(self):
        life_counter_box = self.life_counter
        life_word_print = 'life X ' + str(life_counter_box)
        if self.life_counter >= 0:
            self.window.remove(self.life_word)
            self.life_word = GLabel(life_word_print)
            self.life_word.font = 'Verdana-10-bold-italic'
            self.window.add(self.life_word, self.window.width - self.life_word.width - 10, y=self.window.height - 10)
        else:
            self.window.remove(self.life_word)
