# mypack/games/contra.py

def play():
    print("正在玩魂斗罗....")


def gameover():
    # 想在游戏调用结束之后调用菜单 show_menu
    # 1. 用绝对导入
    # from mypack.menu import show_menu
    # show_menu()

    # 2. 使用相对导入
    from ..menu import show_menu
    show_menu()
    # 想在此处调用 tanks.py里的play
    # from .tanks import play  # 当前一级
    # from ..games.tanks import play
    from ...mypack.games.tanks import play  # 出错超出包的范围
    play() 


print("魂斗罗模块被加载!")

