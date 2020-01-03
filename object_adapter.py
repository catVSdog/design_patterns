"""
适配器模式
使原本接口不兼容,无法一起工作的类,变得兼容起来,可以一起工作.
主要目的是复用一些现存的类,但它又和现在的接口不一致,所以做一些兼容

对象适配器模式
"""


class Computer:
    def play_video(self, video):
        video.play()


class Movi:
    def play(self):
        print("播放电影中..请礼貌观影..")


class GIF:
    def play_mul(self):
        print("偷录自一个电影的多个GIF图联播中...凑活看吧...")


class TransGif(Movi):
    def __init__(self, gif):
        self.gif = gif

    def play(self):  # 对象适配器模式采用委托的方式实现
        self.gif.play_mul()


if __name__ == '__main__':
    cp = Computer()
    print("+++ 看高清电影 +++")
    mv = Movi()
    cp.play_video(mv)

    print("++ 看盗版电影 ++")
    gif = GIF()
    tr_gif = TransGif(gif)
    cp.play_video(tr_gif)
