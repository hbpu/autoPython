class Settings:
    """存储游戏设置的类"""

    def __init__(self):
        """初始化"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (148, 193, 232)
        self.ship_speed = 1.5

        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)



