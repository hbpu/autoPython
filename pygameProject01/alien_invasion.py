import sys
import pygame


from settings import Settings
from ship import Ship
from bullet import Bullet

import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.disable()

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
        self.bullets = pygame.sprite.Group()

        # 设置背景颜色
        self.bg_color = self.settings.bg_color



    def run_game(self):
        # 开始游戏的主循环
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()





    def _check_events(self):
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                logging.info('esc')
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
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

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            logging.info('已按右键')
            # 向右移动飞船
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """创建一个新子弹，并加入编组"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):

        self.bullets.update()
        # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        logging.info(len(self.bullets))

    def _update_screen(self):
        # 每次循环都重绘屏幕
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

if __name__ == '__main__':
    # 创建实例并运行
    ai = AlienInvasion()
    ai.run_game()
