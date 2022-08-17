"""
File: 
Name:Jason Tsai (智翔)
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GPolygon, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    # title: SlamDunk feat stancode _ I wanna leaning code !!
    # 創作理念：致敬最經典的 SLAMDUNK 同時....JERRY....我好想學 CODE 阿阿阿阿阿阿阿!!!!!!
    """
    # 定義畫布「長」、「寬」、「名稱」。
    window = GWindow(width=1200, height=850, title='SlamDunk _ I wanna leaning code')

    # 畫布底色製作。
    windows = GRect(1200, 850)
    windows.filled = True
    windows.fill_color = 'indianred'
    window.add(windows)

    # 畫布底部「SLAMDUNK」、「STANCODE」的wording製作。
    for i in range(20):
        for j in range(6):
            word_dunk = GLabel('SLAMDUNK    STANCODE')
            word_dunk.font = 'Verdana-20-bold-italic'
            word_dunk.color = 'white'
            window.add(word_dunk, x=j * 400 + (-1) ** i * 50, y=i * 50)

    # 對話框製作。
    speak = GOval(600, 900)
    speak.filled = True
    speak.fill_color = 'white'
    window.add(speak, x=600, y=10)

    # 對話框文字編列。
    word = GLabel(' Jerry...\n\n我好想學 code \n  ....')
    word.font = 'Verdana-49-bold-italic'
    window.add(word, x=740, y=570)

    # 利用陣列收納座標，透過迴圈製作「脖子」圖像。
    neck_list = [(261, 742), (346, 811), (481, 692), (526, 850), (275, 850)]
    neck = GPolygon()
    for i in range(5):
        neck.add_vertex(neck_list[i])
    neck.filled = True
    neck.fill_color = 'oldlace'
    neck.color = 'oldlace'
    window.add(neck)

    # 利用陣列收納座標，透過迴圈製作「衣服」圖像。
    cloth_list = [(268, 809), (131, 850), (275, 850)]
    cloth = GPolygon()
    for i in range(3):
        cloth.add_vertex(cloth_list[i])
    cloth.filled = True
    cloth.fill_color = 'dimgray'
    cloth.color = 'dimgray'
    window.add(cloth)

    # 利用陣列收納座標，透過迴圈製作「臉」圖像。
    face = GPolygon()
    face_list = [(250, 670), (197, 550), (285, 135), (370, 130), (405, 145), (440, 135), (490, 145), (545, 435),
                 (494, 644), (328, 709)]
    for i in range(10):
        face.add_vertex(face_list[i])
    face.filled = True
    face.fill_color = 'oldlace'
    face.color = 'oldlace'
    window.add(face)

    # 利用陣列收納座標，透過迴圈製作「鼻子陰影」圖像。
    nose_shadow = GPolygon()
    nose_shadow_list = [(330, 290), (339, 325), (298, 378), (274, 453), (281, 470), (327, 435), (307, 437), (301, 425),
                        (304, 396), (346, 335), (347, 312)]
    for i in range(11):
        nose_shadow.add_vertex(nose_shadow_list[i])
    nose_shadow.filled = True
    nose_shadow.fill_color = 'wheat'
    nose_shadow.color = 'wheat'
    window.add(nose_shadow)

    # 利用陣列收納座標，透過迴圈製作「下八陰影」圖像。
    chin_shadow = GPolygon()
    chin_shadow_list = [(250, 672), (261, 742), (346, 811), (481, 694), (494, 644), (328, 709)]
    for i in range(6):
        chin_shadow.add_vertex(chin_shadow_list[i])
    chin_shadow.filled = True
    chin_shadow.fill_color = 'gainsboro'
    chin_shadow.color = 'gainsboro'
    window.add(chin_shadow)

    # 利用陣列收納座標，透過迴圈製作「頭髮」圖像。
    hair = GPolygon()
    hair_list = [(167, 80), (40, 745), (145, 840), (267, 810), (250, 670), (197, 550), (285, 135), (370, 130),
                 (405, 145), (440, 135), (490, 145), (545, 435), (455, 796), (520, 850), (715, 850), (750, 567),
                 (727, 239), (615, 95), (510, 22), (415, 21), (372, 37), (320, 18)]
    for i in range(22):
        hair.add_vertex(hair_list[i])
    hair.filled = True
    hair.fill_color = 'black'
    hair.color = 'black'
    window.add(hair)

    # 利用陣列收納座標，透過迴圈製作「嘴巴」圖像。
    mouth = GPolygon()
    mouth_list = [(274, 500), (287, 533), (262, 547), (286, 570), (391, 581), (423, 563), (435, 533), (421, 518),
                  (372, 487), (302, 487), (273, 500)]
    for i in range(11):
        mouth.add_vertex(mouth_list[i])
    mouth.filled = True
    mouth.fill_color = 'rosybrown'
    mouth.color = 'rosybrown'
    window.add(mouth)

    # 利用陣列收納座標，透過迴圈製作「上排牙齒」圖像。
    teeth_upper = GPolygon()
    teeth_upper_list = [(286, 503), (290, 517), (317, 513), (317, 505), (370, 505), (369, 522), (395, 527), (419, 548),
                        (416, 527), (372, 497)]
    for i in range(10):
        teeth_upper.add_vertex(teeth_upper_list[i])
    teeth_upper.filled = True
    teeth_upper.fill_color = 'white'
    teeth_upper.color = 'white'
    window.add(teeth_upper)

    # 利用陣列收納座標，透過迴圈製作「左眉毛」圖像。
    eye_brow_left = GPolygon()
    eye_brow_left_list = [(321, 265), (326, 283), (148, 311)]
    for i in range(3):
        eye_brow_left.add_vertex(eye_brow_left_list[i])
    eye_brow_left.filled = True
    eye_brow_left.fill_color = 'black'
    eye_brow_left.color = 'black'
    window.add(eye_brow_left)

    # 利用陣列收納座標，透過迴圈製作「右眉毛」圖像。
    eye_brow_right = GPolygon()
    eye_brow_right_list = [(360, 268), (355, 294), (534, 315)]
    for i in range(3):
        eye_brow_right.add_vertex(eye_brow_right_list[i])
    eye_brow_right.filled = True
    eye_brow_right.fill_color = 'black'
    eye_brow_right.color = 'black'
    window.add(eye_brow_right)

    # 利用陣列收納座標，透過迴圈製作「左眼眶」圖像。
    eye_left = GPolygon()
    eye_left_list = [(274, 346), (247, 338), (249, 312), (294, 300), (326, 327)]
    for i in range(5):
        eye_left.add_vertex(eye_left_list[i])
    eye_left.filled = True
    eye_left.fill_color = 'white'
    eye_left.color = 'black'
    window.add(eye_left)

    # 利用陣列收納座標，透過迴圈製作「左眼球」圖像。
    eye_ball_left = GPolygon()
    eye_ball_left_list = [(263, 340), (275, 344), (300, 334), (308, 322), (289, 315), (266, 328)]
    for i in range(6):
        eye_ball_left.add_vertex(eye_ball_left_list[i])
    eye_ball_left.filled = True
    eye_ball_left.fill_color = 'black'
    eye_ball_left.color = 'black'
    window.add(eye_ball_left)

    # 利用陣列收納座標，透過迴圈製作「右眼眶」圖像。
    eye_right: GPolygon = GPolygon()
    eye_right_list = [(494, 370), (521, 366), (506, 345), (449, 316), (416, 334)]
    for i in range(5):
        eye_right.add_vertex(eye_right_list[i])
    eye_right.filled = True
    eye_right.fill_color = 'white'
    eye_right.color = 'black'
    window.add(eye_right)

    # 利用陣列收納座標，透過迴圈製作「右眼球」圖像。
    eye_ball_right = GPolygon()
    eye_ball_right_list = [(455, 338), (460, 348), (489, 357), (500, 350), (485, 336), (458, 332)]
    for i in range(6):
        eye_ball_right.add_vertex(eye_ball_right_list[i])
    eye_ball_right.filled = True
    eye_ball_right.fill_color = 'black'
    eye_ball_right.color = 'black'
    window.add(eye_ball_right)

    # 利用陣列收納座標，透過迴圈製作「左眼淚」圖像。
    tear_left = GPolygon()
    tear_left_list = [(244, 335), (247, 354), (263, 369), (254, 410), (257, 433), (264, 424), (270, 402), (275, 366),
                      (312, 348), (321, 331), (276, 345)]
    for i in range(11):
        tear_left.add_vertex(tear_left_list[i])
    tear_left.filled = True
    tear_left.fill_color = 'lightblue'
    tear_left.color = 'lightblue'
    window.add(tear_left)

    # 利用陣列收納座標，透過迴圈製作「右眼淚」圖像。
    tear_right = GPolygon()
    tear_right_list = [(458, 349), (448, 365), (481, 379), (507, 399), (494, 437), (496, 501), (487, 584), (500, 590),
                       (498, 556), (504, 517), (513, 484), (507, 461), (516, 408), (528, 379), (520, 366)]
    for i in range(15):
        tear_right.add_vertex(tear_right_list[i])
    tear_right.filled = True
    tear_right.fill_color = 'lightblue'
    tear_right.color = 'lightblue'
    window.add(tear_right)

    # 利用陣列收納座標，透過迴圈製作「血」圖像。
    blood = GPolygon()
    blood_list = [(253, 538), (231, 565), (234, 598), (250, 610), (236, 631), (254, 671), (282, 685), (259, 649),
                  (267, 608), (287, 587), (356, 589), (363, 610), (363, 623), (352, 645), (388, 618), (387, 669),
                  (408, 677), (405, 622), (428, 611), (426, 555)]
    for i in range(20):
        blood.add_vertex(blood_list[i])
    blood.filled = True
    blood.fill_color = 'lightpink'
    blood.color = 'lightpink'
    window.add(blood)

    # 利用陣列收納座標，透過迴圈製作「下排牙齒」圖像。
    teeth_down_list = [(314, 530), (291, 546), (346, 547), (403, 563), (413, 553), (380, 531)]
    teeth_down = GPolygon()
    for i in range(6):
        teeth_down.add_vertex(teeth_down_list[i])
    teeth_down.filled = True
    teeth_down.fill_color = 'white'
    teeth_down.color = 'white'
    window.add(teeth_down)

    # 利用陣列收納座標，透過迴圈製作「頭髮反光1」圖像。
    white1 = GPolygon()
    white1_list = [(526, 122), (566, 295), (571, 243), (597, 318), (603, 309), (647, 294), (703, 360), (702, 279),
                   (713, 292), (689, 208), (686, 239), (658, 191), (647, 213), (613, 149), (620, 197)]
    for i in range(15):
        white1.add_vertex(white1_list[i])
    white1.filled = True
    white1.fill_color = 'gainsboro'
    white1.color = 'gainsboro'
    window.add(white1)

    # 利用陣列收納座標，透過迴圈製作「頭髮反光2」圖像。
    white2 = GPolygon()
    white2_list = [(562, 652), (590, 788), (594, 715), (610, 743), (641, 697), (629, 815), (660, 715), (654, 795),
                   (676, 724), (696, 760), (722, 722), (695, 725), (654, 643), (626, 704), (612, 653), (605, 687)]
    for i in range(16):
        white2.add_vertex(white2_list[i])
    white2.filled = True
    white2.fill_color = 'gainsboro'
    white2.color = 'gainsboro'
    window.add(white2)

    # 製作「鼻子傷痕」圖像。
    hurt_nose1 = GLine(340, 456, 382, 439)
    hurt_nose1.color = 'darkgrey'
    window.add(hurt_nose1)

    # 透過迴圈製作「陰影」圖像。
    for i in range(2):
        hurt_nose2 = GLine(355, 454 + i * 4, 376, 445 + i * 4)
        hurt_nose2.color = 'darkgrey'
        window.add(hurt_nose2)

    # 透過迴圈製作「傷痕」圖像。
    for i in range(4):
        hurt = GLine(307, 182 + i * 4, 365, 174 + i * 4)
        hurt.color = 'indianred'
        window.add(hurt)

    # 透過迴圈製作「傷痕」圖像。
    for i in range(8):
        hurt1 = GLine(465, 219 + i * 3, 504, 246 + i * 3)
        hurt1.color = 'indianred'
        window.add(hurt1)

    # 透過迴圈製作「傷痕」圖像。
    for i in range(6):
        hurt2 = GLine(480 + i, 253 + i * 4.5, 504 - i, 270 + i * 3)
        hurt2.color = 'indianred'
        window.add(hurt2)

    hair1 = GArc(100, 2300, 0, 95)
    hair1.color = 'black'
    window.add(hair1, 383, 146)


if __name__ == '__main__':
    main()
