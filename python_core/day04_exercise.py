"""
    技能系统
"""

class SkillImpactEffect:
    """
        技能影响效果
    """
    def impact(self):
        raise NotImplementedError
    
class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """
    def __init__(self, value):
        self.value = value
        
    def impact(self):
        print("减血%d"%self.value)

class LowerDefenseEffect(SkillImpactEffect):
    """
        降低防御力
    """
    def __init__(self, value, time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低防御力%d,持续%d"%(self.value, self.time))

class DizzinessEffect(SkillImpactEffect):
    """
        眩晕
    """
    def __init__(self, time):
        # self.value = value
        self.time = time

    def impact(self):
        print("眩晕持续%d"%(self.time))

class SkillDeployer:
    """
        技能释放器
        1.加载配置文件
        2.创建效果对象
        3,生成技能,执行效果
    """
    def __init__(self, name):
        self.name = name
        self.__skill_config = self.__load_config_file()
        self.__effect_object = self.__creat_effect_object()

    def __load_config_file(self):

        #加载配置文件后返回技能效果配置文件.一定数据结构
        return {
            "降龙十八掌":["DamageEffect(200)", "LowerDefenseEffect(-20, 5)", "DizzinessEffect(10)"],
            "六脉神剑":["DamageEffect(100)", "DizzinessEffect(8)"]

        }

    def __creat_effect_object(self):
        list_effect_name = self.__skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object = eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object
 
    def generate_skill(self):
        print(self.name, "释放了")
        for item in self.__effect_object:
            item.impact()

xlsbz = SkillDeployer("降龙十八掌")
xlsbz.generate_skill()