import pygame
import sys

# 初始化 Pygame
pygame.init()

# 遊戲畫面尺寸
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("貪食蛇")

# 顏色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 遊戲主迴圈
def game_loop():
    game_over = False
    game_exit = False

    while not game_exit:
        while game_over:
            # 遊戲結束畫面 (待實作)
            screen.fill(white)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("你輸了！ 按 C 重新開始或 Q 離開", True, red)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop() # 重新開始遊戲

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            # 玩家控制 (待實作)

        # 遊戲邏輯 (待實作)

        # 畫面更新
        screen.fill(black)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    game_loop()
