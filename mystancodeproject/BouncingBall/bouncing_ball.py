"""
File: bouncing_ball.py
Name:Jason Tsai (智翔)
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 2                                                                  # 球的水平速度。
DELAY = 10                                                              # 動畫停格多少毫秒。
GRAVITY = 1                                                             # 重力加速度；每一圈 while loop 垂直速度要加上的數值。
SIZE = 20                                                               # 球的直徑。
REDUCE = 0.9                                                            # 每一次反彈時，在垂直速度所剩之比例。
START_X = 30                                                            # 球的起始 x 座標。
START_Y = 40                                                            # 球的起始 y 座標。

window = GWindow(800, 500, title='bouncing_ball.py')                    # 全域變數window。
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)                          # 全域變數ball。
count_click = 0                                                         # 全域變數count_click。
key = True                                                              # 全域變數key。
work_times = GLabel('Work times => ' + str(count_click))                # 全域變數work_times。


def main():
    work_times.font = 'Verdana-10-bold-italic'                                            # 字體大小。
    window.add(work_times, x=0, y=work_times.height+5)                    # 字體影像顯示。
    ball.filled = True                                                  # 改變圓的色彩前置條件。
    ball.filled_color = 'black'                                         # 改變圓的色彩。
    window.add(ball)                                                    # 將圓圖像顯示。
    onmouseclicked(ball_jump)                                           # 觸發點擊開關。


def ball_jump(mouse):
    global key, ball, count_click, GRAVITY                              # 執行全域變數 key, ball, count_click, GRAVITY。
    if key is True:                                                     # 利用 key 來鎖定點擊時是否執行彈跳運動。
        key = False                                                     # key 轉為 False 狀態，避免在球體運動時，點及觸發。
        count_click += 1                                                # 計數「球超出右側視窗次數」。
        work_times.text = ('Work times => ' + str(count_click))         # 計數縣在是第幾 RUN。
        vy = 0                                                          # 定義初始的垂直速度為 0。
        if count_click <= 3:                                            # 當「球超出右側視窗次數不超過3次」時執行。
            i = 1                                                       # 設置讓球滾地的開關
            while True:                                                 # 球體運動迴圈：不斷重複執行迴圈。
                vy = vy + GRAVITY * i                                   # 讓垂直速度可以隨著迴圈次數遞增。
                ball.move(VX, vy)                                       # 球體開始依「水平VX」和「垂直vy」的速度移動。
                if ball.y + SIZE >= window.height:                      # 球體底部接觸地面時執行。
                    # print(vy)                                         # 僅檢視落地時速率。
                    if int(vy) == 1:                                    # 當落地時速率整數部分為 1 時執行。
                        vy = 0                                          # 垂直速度直接歸0，避免「球體沉入地面」。
                        i = 0                                           # 避免迴圈累加，讓球可以在地上滾到終點(VX為1可以看到)。
                    while vy > 0:                                       # 該迴圈主要保證球落地時能絕對反彈。
                        vy = -(vy+1) * REDUCE                           # 球體落地時以最終速度乘REDUCE做反向運動(變成負速率)。
                        # (vy+1)額外註記                                 # 若vy不加1，即使沒有REDUCE，每次迴圈也會遞減1。
                if ball.x + SIZE >= window.width:                       # 球體超出畫布寬度時執行。
                    window.remove(ball)                                 # 球體超出畫布寬度時，將該求移除。
                    ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)      # 定義位置和球的大小，重新放置新球。
                    ball.filled = True                                  # 改變圓的色彩前置條件。
                    ball.filled_color = 'black'                         # 改變圓的色彩。
                    window.add(ball)                                    # 將圓圖像顯示。
                    break                                               # 終止迴圈。
                pause(DELAY)                                            # 動畫停格 "DELAY" 毫秒。
            if count_click <= 2:                                        # 當「球超出右側視窗次數不超過3次」時執行。
                key = True                                              # 結束迴圈時，將點擊開關打開，以便後續點擊觸發彈跳運動。
            else:                                                       # 當「球超出右側視窗次數大於3次」時執行。
                key = False                                             # 將迴圈點擊開關關閉。
                work_times_out = GLabel('U have no chance to keep going XD !!!  See u next time~')
                work_times_out.font = 'Verdana-10-bold-italic'
                window.add(work_times_out, x=0, y=work_times.height + work_times_out.height+10)


if __name__ == "__main__":
    main()
