import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen)

    bg_color = (230, 230, 230)

    while True:
        for event in pygame.event.get():    #监视键盘机鼠标事件
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        ship.blitme()
        pygame.display.flip()   #让最近绘制的屏幕可见


run_game()
