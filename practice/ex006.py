"""
一个孩子正在玩一个高层建筑物n楼上的球。该地板的高度h是已知的。
他把球扔出窗外。球反弹。（例如，达到其高度的三分之二，则反弹bounce为0.66）。

他的母亲从离地面1.5米的窗户向外望去。

母亲会看到多少次球从她的窗户前经过（包括坠落和弹跳时）？

有效的实验必须满足三个条件：
以米为单位的浮点参数"h"必须大于0
浮动参数"bounce"必须大于0且小于1
浮动参数"window"必须小于h。
如果满足以上所有三个条件，则返回正整数，否则返回-1。

注意：
仅当反弹球的高度严格大于window参数时，才能看到该球。
"""


def bouncing_ball(h, bounce, window):
    if 0 < window < h and 0 < bounce < 1:
        times = 0
        while h > window:
            times += 2
            h *= bounce
        return times - 1
    else:
        return -1


if __name__ == '__main__':
    print(bouncing_ball(3, 0.66, 1.5) == 3)
    print(bouncing_ball(30, 0.66, 1.5) == 15)
    print(bouncing_ball(2, 0.5, 1) == 1)
    print(bouncing_ball(30, 0.75, 1.5) == 21)
    print(bouncing_ball(30, 0.4, 10) == 3)
    print(bouncing_ball(40, 1, 10) == -1)
    print(bouncing_ball(-5, 0.66, 1.5) == -1)

