import sys
import pygame


from settings import Settings
from ship import Ship

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logging.info('start')

class AlienInvasion:
    # 管理游戏资源和行为的类

    def __init__(self):
        # 初始化游戏并创建游戏资源
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 在屏幕绘制完成后生成飞船
        self.ship = Ship(self)

        # 设置背景颜色
        self.bg_color = self.settings.bg_color



    def run_game(self):
        # 开始游戏的主循环
        while True:
            self._check_events()
            self.ship.update()
            self._updata_screen()



    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('esc')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    logging.info('已按键')
                    # 向右移动飞船
                    self.ship.moving_right = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False

                #     self.ship.rect.x += 1
                # if event.key == pygame.K_LEFT:
                #     # 向左移动飞船
                #     self.ship.rect.x -= 1
                # if event.key == pygame.K_UP:
                #     # 向上移动飞船
                #     self.ship.rect.y -= 1
                # if event.key == pygame.K_DOWN:
                #     # 向下移动飞船
                #     self.ship.rect.y += 1


    def _updata_screen(self):
        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

if __name__ == '__main__':
    # 创建实例并运行
    ai = AlienInvasion()
    ai.run_game()
