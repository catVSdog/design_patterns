"""
适配器模式:
使原本接口不兼容,无法一起工作的类,变得兼容起来,可以一起工作.
主要目的是复用一些现存的类,但它又和现在的接口不一致,所以做一些兼容

类适配器模式
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


class Trans(Movi, GIF):  # 类适配器采用多重继承的方式实现
    def play(self):
        self.play_mul()


if __name__ == '__main__':
    cp = Computer()
    print("+++ 看高清电影 +++")
    mv = Movi()
    cp.play_video(mv)

    print("++ 看盗版电影 ++")
    tr_gif = Trans()
    cp.play_video(tr_gif)
