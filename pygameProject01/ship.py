import pygame


class Ship:
    """飞船类"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load('img/ship01.png')
        self.rect = self.image.get_rect()

        # 初始化的飞船都放在底部中间位置
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
