# Thomas Marshall
# fallGreeting.py
# I certify that this lab is entirely my own work.

# Allows graphic use and math symbols
from math import *
from graphics import *
import time

def fallGreeting():

    # Creates window
    width = 600
    height = 600
    win = GraphWin("Greeting Card", width, height)
    win.setBackground("gray5")

    # Greeting
    greeting = Text(Point(width/2, 30), "")
    greeting.setText("Happy Fall!")
    greeting.setSize(20)
    greeting.setStyle("italic")
    greeting.setFill("yellow")
    greeting.draw(win)

    # The sky
    cPt1 = Point(0, 247.5)
    cPt2 = Point(width, height/2 + 30)
    cloud1 = Rectangle(cPt1, cPt2)
    cloud1.setFill("gray20")
    cloud1.setOutline("gray20")
    cloud1.draw(win)
    cloud2 = Rectangle(Point(0, 165), Point(width, 247.5))
    cloud2.setFill("gray15")
    cloud2.setOutline("gray15")
    cloud2.draw(win)
    cloud3 = Rectangle(Point(0, 82.5), Point(width, 165))
    cloud3.setFill("gray10")
    cloud3.setOutline("gray10")
    cloud3.draw(win)

    # the ground
    gPt1 = Point(0, height/2 + 30)
    gPt2 = Point(width, height)
    ground = Rectangle(gPt1, gPt2)
    ground.setFill("#8b4513")
    ground.setOutline("#8b4513")
    ground.draw(win)

    # The tree
    tree = Polygon(Point(196, 331), Point(204, 319), Point(204, 163), Point(207,180),
                   Point(216, 155), Point(216, 319), Point(230, 332), Point(218, 335),
                   Point(214, 346), Point(207, 328), Point(202, 331))
    tree.setFill("#a0522d")
    tree.draw(win)

    leaves1 = Circle(Point(225, 171), 25)
    leaves2 = Circle(Point(203, 178), 25)
    leaves3 = Circle(Point(210, 132), 25)
    leaves4 = Circle(Point(234, 145), 25)
    leaves5 = Circle(Point(183, 161), 25)
    leaves1.setFill("green")
    leaves2.setFill("green")
    leaves3.setFill("green")
    leaves4.setFill("green")
    leaves5.setFill("green")
    leaves1.draw(win)
    leaves2.draw(win)
    leaves3.draw(win)
    leaves4.draw(win)
    leaves5.draw(win)

    # The lightning
    lightning = Polygon(Point(191,0), Point(196,60), Point(189,60), Point(201,120),
                        Point(199,120), Point(206, 173), Point(203,150), Point(197,150),
                        Point(198,100), Point(193,100))
    lightning.setFill("yellow")
    
    # jack o lanterns 10 in all
    jack = Polygon(Point(280, 221), Point(290, 220), Point(292, 247), Point(315, 243),
                   Point(334, 242), Point(349, 251), Point(360, 265), Point(366, 283),
                   Point(367, 306), Point(362, 328), Point(348, 336), Point(330, 340),
                   Point(318, 338), Point(304, 338), Point(292, 343), Point(277, 343),
                   Point(265, 338), Point(258, 332), Point(252, 321), Point(243, 307),
                   Point(241, 290), Point(238, 270), Point(242, 255), Point(250, 245),
                   Point(259, 241), Point(264, 241), Point(270, 243), Point(275, 247),
                   Point(281, 251), Point(287, 247))
    jack.setFill("orange")
    jack.draw(win)

    stem = Polygon(Point(280, 221), Point(290, 220), Point(292, 247), Point(287, 247))
    stem.setFill("#a0522d")
    stem.draw(win)

    eyeR = Polygon(Point(317, 269), Point(341, 262), Point(320, 286))
    eyeR.setFill("black")
    eyeR.draw(win)

    eyeL = Polygon(Point(294, 269), Point(260, 262), Point(273, 286))
    eyeL.setFill("black")
    eyeL.draw(win)

    mouth = Polygon(Point(272, 301), Point(282, 309), Point(293, 303), Point(301, 312),
                    Point(311, 304), Point(321, 315), Point(332, 304), Point(324, 329),
                    Point(315, 321), Point(305, 329), Point(292, 322), Point(283, 330))
    mouth.setFill("black")
    mouth.draw(win)

    jack2 = Polygon(Point(80, 221), Point(90, 220), Point(92, 247), Point(115, 243),
                   Point(134, 242), Point(149, 251), Point(160, 265), Point(166, 283),
                   Point(167, 306), Point(162, 328), Point(148, 336), Point(130, 340),
                   Point(118, 338), Point(104, 338), Point(92, 343), Point(77, 343),
                   Point(65, 338), Point(58, 332), Point(52, 321), Point(43, 307),
                   Point(41, 290), Point(38, 270), Point(42, 255), Point(50, 245),
                   Point(59, 241), Point(64, 241), Point(70, 243), Point(75, 247),
                   Point(81, 251), Point(87, 247))

    jack2.setFill("orange")
    jack2.draw(win)

    stem2 = Polygon(Point(80, 221), Point(90, 220), Point(92, 247), Point(87, 247))
    stem2.setFill("#a0522d")
    stem2.draw(win)

    eyeR2 = Polygon(Point(117, 269), Point(141, 262), Point(120, 286))
    eyeR2.setFill("black")
    eyeR2.draw(win)

    eyeL2 = Polygon(Point(94, 269), Point(60, 262), Point(73, 286))
    eyeL2.setFill("black")
    eyeL2.draw(win)

    mouth2 = Polygon(Point(72, 301), Point(82, 309), Point(93, 303), Point(101, 312),
                    Point(111, 304), Point(121, 315), Point(132, 304), Point(124, 329),
                    Point(115, 321), Point(105, 329), Point(92, 322), Point(83, 330))
    mouth2.setFill("black")
    mouth2.draw(win)
    
    jack3 = Polygon(Point(480, 221), Point(490, 220), Point(492, 247), Point(515, 243),
                   Point(534, 242), Point(549, 251), Point(560, 265), Point(566, 283),
                   Point(567, 306), Point(562, 328), Point(548, 336), Point(530, 340),
                   Point(518, 338), Point(504, 338), Point(492, 343), Point(477, 343),
                   Point(465, 338), Point(458, 332), Point(452, 321), Point(443, 307),
                   Point(441, 290), Point(438, 270), Point(442, 255), Point(450, 245),
                   Point(459, 241), Point(464, 241), Point(470, 243), Point(475, 247),
                   Point(481, 251), Point(487, 247))
    jack3.setFill("orange")
    jack3.draw(win)

    stem3 = Polygon(Point(480, 221), Point(490, 220), Point(492, 247), Point(487, 247))
    stem3.setFill("#a0522d")
    stem3.draw(win)

    eyeR3 = Polygon(Point(517, 269), Point(541, 262), Point(520, 286))
    eyeR3.setFill("black")
    eyeR3.draw(win)

    eyeL3 = Polygon(Point(494, 269), Point(460, 262), Point(473, 286))
    eyeL3.setFill("black")
    eyeL3.draw(win)

    mouth3 = Polygon(Point(472, 301), Point(482, 309), Point(493, 303), Point(501, 312),
                    Point(511, 304), Point(521, 315), Point(532, 304), Point(524, 329),
                    Point(515, 321), Point(505, 329), Point(492, 322), Point(483, 330))
    mouth3.setFill("black")
    mouth3.draw(win)

    jack4 = Polygon(Point(180, 321), Point(190, 320), Point(192, 347), Point(215, 343),
                   Point(234, 342), Point(249, 351), Point(260, 365), Point(266, 383),
                   Point(267, 406), Point(262, 428), Point(248, 436), Point(230, 440),
                   Point(218, 438), Point(204, 438), Point(192, 443), Point(177, 443),
                   Point(165, 438), Point(158, 432), Point(152, 421), Point(143, 407),
                   Point(141, 390), Point(138, 370), Point(142, 355), Point(150, 345),
                   Point(159, 341), Point(164, 341), Point(170, 343), Point(175, 347),
                   Point(181, 351), Point(187, 347))
    jack4.setFill("orange")
    jack4.draw(win)

    stem4 = Polygon(Point(180, 321), Point(190, 320), Point(192, 347), Point(187, 347))
    stem4.setFill("#a0522d")
    stem4.draw(win)

    eyeR4 = Polygon(Point(217, 369), Point(241, 362), Point(220, 386))
    eyeR4.setFill("black")
    eyeR4.draw(win)

    eyeL4 = Polygon(Point(194, 369), Point(160, 362), Point(173, 386))
    eyeL4.setFill("black")
    eyeL4.draw(win)

    mouth4 = Polygon(Point(172, 401), Point(182, 409), Point(193, 403), Point(201, 412),
                    Point(211, 404), Point(221, 415), Point(232, 404), Point(224, 429),
                    Point(215, 421), Point(205, 429), Point(192, 422), Point(183, 430))
    mouth4.setFill("black")
    mouth4.draw(win)

    jack5 = Polygon(Point(-20, 321), Point(-10, 320), Point(-8, 347), Point(15, 343),
                   Point(34, 342), Point(49, 351), Point(60, 365), Point(66, 383),
                   Point(67, 406), Point(62, 428), Point(48, 436), Point(30, 440),
                   Point(18, 438), Point(4, 438), Point(-8, 443), Point(-23, 443),
                   Point(-41, 438), Point(-42, 432), Point(-48, 421), Point(-57, 407),
                   Point(-59, 390), Point(-62, 370), Point(-58, 355), Point(-50, 345),
                   Point(-41, 341), Point(-36, 341), Point(-30, 343), Point(-25, 347),
                   Point(-19, 351), Point(-13, 347))
    jack5.setFill("orange")
    jack5.draw(win)

    stem5 = Polygon(Point(-20, 321), Point(-10, 320), Point(-8, 347), Point(-13, 347))
    stem5.setFill("#a0522d")
    stem5.draw(win)

    eyeR5 = Polygon(Point(17, 369), Point(41, 362), Point(20, 386))
    eyeR5.setFill("black")
    eyeR5.draw(win)

    eyeL5 = Polygon(Point(-6, 369), Point(-40, 362), Point(-27, 386))
    eyeL5.setFill("black")
    eyeL5.draw(win)

    mouth5 = Polygon(Point(-28, 401), Point(-18, 409), Point(-7, 403), Point(1, 412),
                    Point(11, 404), Point(21, 415), Point(32, 404), Point(24, 429),
                    Point(15, 421), Point(5, 429), Point(-8, 422), Point(-17, 430))
    mouth5.setFill("black")
    mouth5.draw(win)
    
    jack6 = Polygon(Point(380, 321), Point(390, 320), Point(392, 347), Point(415, 343),
                   Point(434, 342), Point(449, 351), Point(460, 365), Point(466, 383),
                   Point(467, 406), Point(462, 428), Point(448, 436), Point(430, 440),
                   Point(418, 438), Point(404, 438), Point(392, 443), Point(377, 443),
                   Point(365, 438), Point(358, 432), Point(352, 421), Point(343, 407),
                   Point(341, 390), Point(338, 370), Point(342, 355), Point(350, 345),
                   Point(359, 341), Point(364, 341), Point(370, 343), Point(375, 347),
                   Point(381, 351), Point(387, 347))
    jack6.setFill("orange")
    jack6.draw(win)

    stem6 = Polygon(Point(380, 321), Point(390, 320), Point(392, 347), Point(387, 347))
    stem6.setFill("#a0522d")
    stem6.draw(win)

    eyeR6 = Polygon(Point(417, 369), Point(441, 362), Point(420, 386))
    eyeR6.setFill("black")
    eyeR6.draw(win)

    eyeL6 = Polygon(Point(394, 369), Point(360, 362), Point(373, 386))
    eyeL6.setFill("black")
    eyeL6.draw(win)

    mouth6 = Polygon(Point(372, 401), Point(382, 409), Point(393, 403), Point(401, 412),
                    Point(411, 404), Point(421, 415), Point(432, 404), Point(424, 429),
                    Point(415, 421), Point(405, 429), Point(392, 422), Point(383, 430))
    mouth6.setFill("black")
    mouth6.draw(win)

    jack7 = Polygon(Point(580, 321), Point(590, 320), Point(592, 347), Point(615, 343),
                   Point(634, 342), Point(649, 351), Point(660, 365), Point(666, 383),
                   Point(667, 406), Point(662, 428), Point(648, 436), Point(630, 440),
                   Point(618, 438), Point(604, 438), Point(592, 443), Point(577, 443),
                   Point(565, 438), Point(558, 432), Point(552, 421), Point(543, 407),
                   Point(541, 390), Point(538, 370), Point(542, 355), Point(550, 345),
                   Point(559, 341), Point(564, 341), Point(570, 343), Point(575, 347),
                   Point(581, 351), Point(587, 347))
    jack7.setFill("orange")
    jack7.draw(win)

    stem7 = Polygon(Point(580, 321), Point(590, 320), Point(592, 347), Point(587, 347))
    stem7.setFill("#a0522d")
    stem7.draw(win)

    eyeR7 = Polygon(Point(617, 369), Point(641, 362), Point(620, 386))
    eyeR7.setFill("black")
    eyeR7.draw(win)

    eyeL7 = Polygon(Point(594, 369), Point(560, 362), Point(573, 386))
    eyeL7.setFill("black")
    eyeL7.draw(win)

    mouth7 = Polygon(Point(572, 401), Point(582, 409), Point(593, 403), Point(601, 412),
                    Point(611, 404), Point(621, 415), Point(632, 404), Point(624, 429),
                    Point(615, 421), Point(605, 429), Point(592, 422), Point(583, 430))
    mouth7.setFill("black")
    mouth7.draw(win)

    jack8 = Polygon(Point(280, 421), Point(290, 420), Point(292, 447), Point(315, 443),
                   Point(334, 442), Point(349, 451), Point(360, 465), Point(366, 483),
                   Point(367, 506), Point(362, 528), Point(348, 536), Point(330, 540),
                   Point(318, 538), Point(304, 538), Point(292, 543), Point(277, 543),
                   Point(265, 538), Point(258, 532), Point(252, 521), Point(243, 507),
                   Point(241, 490), Point(238, 470), Point(242, 455), Point(250, 445),
                   Point(259, 441), Point(264, 441), Point(270, 443), Point(275, 447),
                   Point(281, 451), Point(287, 447))
    jack8.setFill("orange")
    jack8.draw(win)

    stem8 = Polygon(Point(280, 421), Point(290, 420), Point(292, 447), Point(287, 447))
    stem8.setFill("#a0522d")
    stem8.draw(win)

    eyeR8 = Polygon(Point(317, 469), Point(341, 462), Point(320, 486))
    eyeR8.setFill("black")
    eyeR8.draw(win)

    eyeL8 = Polygon(Point(294, 469), Point(260, 462), Point(273, 486))
    eyeL8.setFill("black")
    eyeL8.draw(win)

    mouth8 = Polygon(Point(272, 501), Point(282, 509), Point(293, 503), Point(301, 512),
                    Point(311, 504), Point(321, 515), Point(332, 504), Point(324, 529),
                    Point(315, 521), Point(305, 529), Point(292, 522), Point(283, 530))
    mouth8.setFill("black")
    mouth8.draw(win)

    jack9 = Polygon(Point(80, 421), Point(90, 420), Point(92, 447), Point(115, 443),
                   Point(134, 442), Point(149, 451), Point(160, 465), Point(166, 483),
                   Point(167, 506), Point(162, 528), Point(148, 536), Point(130, 540),
                   Point(118, 538), Point(104, 538), Point(92, 543), Point(77, 543),
                   Point(65, 538), Point(58, 532), Point(52, 521), Point(43, 507),
                   Point(41, 490), Point(38, 470), Point(42, 455), Point(50, 445),
                   Point(59, 441), Point(64, 441), Point(70, 443), Point(75, 447),
                   Point(81, 451), Point(87, 447))

    jack9.setFill("orange")
    jack9.draw(win)

    stem9 = Polygon(Point(80, 421), Point(90, 420), Point(92, 447), Point(87, 447))
    stem9.setFill("#a0522d")
    stem9.draw(win)

    eyeR9 = Polygon(Point(117, 469), Point(141, 462), Point(120, 486))
    eyeR9.setFill("black")
    eyeR9.draw(win)

    eyeL9 = Polygon(Point(94, 469), Point(60, 462), Point(73, 486))
    eyeL9.setFill("black")
    eyeL9.draw(win)

    mouth9 = Polygon(Point(72, 501), Point(82, 509), Point(93, 503), Point(101, 512),
                    Point(111, 504), Point(121, 515), Point(132, 504), Point(124, 529),
                    Point(115, 521), Point(105, 529), Point(92, 522), Point(83, 530))
    mouth9.setFill("black")
    mouth9.draw(win)
    
    jack0 = Polygon(Point(480, 421), Point(490, 420), Point(492, 447), Point(515, 443),
                   Point(534, 442), Point(549, 451), Point(560, 465), Point(566, 483),
                   Point(567, 506), Point(562, 528), Point(548, 536), Point(530, 540),
                   Point(518, 538), Point(504, 538), Point(492, 543), Point(477, 543),
                   Point(465, 538), Point(458, 532), Point(452, 521), Point(443, 507),
                   Point(441, 490), Point(438, 470), Point(442, 455), Point(450, 445),
                   Point(459, 441), Point(464, 441), Point(470, 443), Point(475, 447),
                   Point(481, 451), Point(487, 447))
    jack0.setFill("orange")
    jack0.draw(win)

    stem0 = Polygon(Point(480, 421), Point(490, 420), Point(492, 447), Point(487, 447))
    stem0.setFill("#a0522d")
    stem0.draw(win)

    eyeR0 = Polygon(Point(517, 469), Point(541, 462), Point(520, 486))
    eyeR0.setFill("black")
    eyeR0.draw(win)

    eyeL0 = Polygon(Point(494, 469), Point(460, 462), Point(473, 486))
    eyeL0.setFill("black")
    eyeL0.draw(win)

    mouth0 = Polygon(Point(472, 501), Point(482, 509), Point(493, 503), Point(501, 512),
                    Point(511, 504), Point(521, 515), Point(532, 504), Point(524, 529),
                    Point(515, 521), Point(505, 529), Point(492, 522), Point(483, 530))
    mouth0.setFill("black")
    mouth0.draw(win)

    # The bat
    bat = Polygon(Point(49, 72), Point(52, 63), Point(55, 68), Point(56, 65),
                  Point(63, 65), Point(69, 64), Point(68, 66), Point(72, 60),
                  Point(74, 73), Point(74, 74), Point(75, 81), Point(71, 90),
                  Point(63, 94), Point(53, 93), Point(48, 88), Point(42, 83),
                  Point(44, 77), Point(48, 72), Point(53, 69), Point(54, 95),
                  Point(55, 103), Point(48, 109), Point(40, 114), Point(31, 117),
                  Point(20, 117), Point(16, 113), Point(16, 101), Point(26, 95),
                  Point(34, 89))
    
    bat.setFill("black")
    bat.draw(win)

    # First frame of bat wings
    batWing1 = Polygon(Point(54, 104), Point(67, 109), Point(82, 111), Point(88, 111),
                       Point(84, 129), Point(80, 125), Point(73, 128), Point(65, 123),
                       Point(56, 127), Point(48, 110))
    batWing1.setFill("black")
    batWing1.draw(win)

    batWing2 = Polygon(Point(28, 95), Point(16, 114), Point(12, 118), Point(7, 118),
                       Point(10, 130), Point(17, 128), Point(27, 127), Point(29, 119),
                       Point(32, 111), Point(36, 105))
    batWing2.setFill("black")
    batWing2.draw(win)

    # Second frame of bat wings
    batWing3 = Polygon(Point(80, 99), Point(94, 98), Point(106, 94), Point(119, 87),
                       Point(123, 80), Point(129, 96), Point(121, 99), Point(113, 111),
                       Point(91, 110), Point(74, 111))
    batWing3.setFill("black")

    batWing4 = Polygon(Point(56, 94), Point(46, 83), Point(40, 72), Point(33, 63),
                       Point(36, 59), Point(22, 69), Point(25, 79), Point(32, 83),
                       Point(34, 95), Point(47, 99))
    batWing4.setFill("black")

    bEyeL = Polygon(Point(56, 77), Point(65, 77), Point(56, 73))
    bEyeL.setFill("red")
    bEyeL.draw(win)

    bEyeR = Polygon(Point(68, 77), Point(74, 77), Point(65, 73))
    bEyeR.setFill("red")
    bEyeR.draw(win)

    # Moves the bat across the screen and changes wing frames
    for i in range(12):
        time.sleep(0.2)
        bEyeL.move(25, 0)
        bEyeR.move(25, 0)
        bat.move(25, 0)
        batWing1.undraw()
        batWing2.undraw()
        batWing1.move(50, 0)
        batWing2.move(50, 0)
        batWing3.draw(win)
        batWing4.draw(win)
        time.sleep(0.2)
        bat.move(25, 0)
        bEyeL.move(25, 0)
        bEyeR.move(25, 0)
        batWing3.undraw()
        batWing4.undraw()
        batWing3.move(50, 0)
        batWing4.move(50, 0)
        batWing1.draw(win)
        batWing2.draw(win)

    # Creates the lightning and flash and despawns lightning, bat, flash, and leaves on te tree.
    lightning.draw(win)
    time.sleep(.03)
    fPt1 = Point(0, 0)
    fPt2 = Point(width, height)
    flash = Rectangle(fPt1, fPt2)
    flash.setFill("white")
    flash.setOutline("white")
    flash.draw(win)
    bat.undraw()
    batWing1.undraw()
    batWing2.undraw()
    leaves1.undraw()
    leaves2.undraw()
    leaves3.undraw()
    leaves4.undraw()
    leaves5.undraw()
    lightning.undraw()
    # Simulates a lightning struck tree
    tree.setFill("black")
    time.sleep(.05)
    flash.undraw()

    # Makes the jack-o-lanterns flash        
    colors = ["yellow", "black"]        
    for i in range(50):
        for color in colors:
            time.sleep(.4)
            eyeR.setFill(color)
            eyeL.setFill(color)
            mouth.setFill(color)
            eyeR2.setFill(color)
            eyeL2.setFill(color)
            mouth2.setFill(color)
            eyeR3.setFill(color)
            eyeL3.setFill(color)
            mouth3.setFill(color)
            eyeR4.setFill(color)
            eyeL4.setFill(color)
            mouth4.setFill(color)
            eyeR5.setFill(color)
            eyeL5.setFill(color)
            mouth5.setFill(color)
            eyeR6.setFill(color)
            eyeL6.setFill(color)
            mouth6.setFill(color)
            eyeR7.setFill(color)
            eyeL7.setFill(color)
            mouth7.setFill(color)
            eyeR8.setFill(color)
            eyeL8.setFill(color)
            mouth8.setFill(color)
            eyeR9.setFill(color)
            eyeL9.setFill(color)
            mouth9.setFill(color)
            eyeR0.setFill(color)
            eyeL0.setFill(color)
            mouth0.setFill(color)
            
    # Closes window
    close = Text(Point(width/2, height - 30), "")
    close.setText("Click anywhere to close")
    close.setStyle("italic")
    close.setFill("yellow")
    close.draw(win)
    end = win.getMouse()
    win.close()

fallGreeting()
