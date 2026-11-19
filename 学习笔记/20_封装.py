# 封装就是把数据（属性）和操作数据的函数（方法）捆绑在一起，形成一个独立的单元（类），并隐藏内部的实现细节，之对外暴露不要动功能（方法）
# 你在打游戏的时候，不必关心这个游戏是如何实现的，只需要通过UI进行操作就能游玩
# 我们使用的UI就是游戏对外暴露出的功能，而游戏的具体实现是对玩家隐藏起来了的

# 需要隐藏的内部实现细节应该设置为私有属性、私有方法
# 需要暴露给外部调用功能应该设置为公共属性、公共方法

# 私有/公共
# 与java或c#不同，python没有public与private，而是使用下划线对私有进行标识
# 当然，python中没有真正的私有机制，也就是说，我们所说的“私有”只是约定。
# Java和Python开了情侣房，没想到墙是玻璃做的，完全没有私人空间
# Java愤怒地要求把整个房间设为private，而Python说：亲爱的，我们不妨在前面加上下划线，假装它是私有的

class Character:
    def __init__(self, c_name, c_hp, c_hobby, c_secret):
        self.name = c_name
        self.hp = c_hp
        self.hobby = c_hobby
        #私有属性：角色的秘密
        self.__secret = c_secret

    def __str__(self):
        return f"角色名称：{self.name}, 角色生命值：{self.hp}, 角色爱好：{self.hobby}"

    # 私有方法：角色谈论他们的秘密
    def __talk_secret(self):
        print(f"角色的秘密是：{self.__secret}")

    # 当然，私有属性和方法可以在内部进行访问
    def talk_with_alice(self):
        print("marisa, what is your secret?")
        print(marisa.__secret)
        marisa.__talk_secret()

# 现在我们来创建实例
marisa = Character("marisa", 100, "magic", "I love Alice")

# 共有属性和方法可以被访问
print(marisa.name)
print(marisa.hp)
print(marisa.hobby)
print(marisa.__str__())

# 而私有属性是无法访问的
# print(marisa.__secret)
# print(marisa.__talk_secret())

# 通过内部访问私有属性、私有方法
marisa.talk_with_alice()

# 当然，这只是约定，如果你想无视风险，强行访问也是完全没问题的……
# 事实上，所谓私有不过是改变了属性或方法的名称，从原来的__属性/方法名称改为了_类__属性/方法名称，让你通过原有名称访问不到而已……