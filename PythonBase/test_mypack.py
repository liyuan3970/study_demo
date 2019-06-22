# test_mypack.py

# 玩魂斗罗
# 1. 用import 语句导入
import mypack.games.contra
mypack.games.contra.play()
import mypack.games.contra as con  # 为mypack.games.contra 取别名为con
con.play()  
# 2. 用from import 语句导入
from mypack.games.contra import play
play()  # 魂斗罗里的play()

# 3. 用 from  import *语句导入
from mypack.games.supermario import *
play()  # 超级玛丽里的play()