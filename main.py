import pygame

# стартуем в файле модули пайгейм
pygame.init()

# размеры для окна игры
display_width = 800  # высота
display_height = 600  # ширина

# отрисовка окна игры
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Don't crush my car, dude!")  # название игры

# цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# модуль для времени, чтобы мониторить кадры в секунду
clock = pygame.time.Clock()
crashed = False  # авария (нужно для остановки игры)
carImg = pygame.image.load('images/car.png')  # картинка для игрока
carImg = pygame.transform.scale(carImg, (70, 80))  # задаем размер картинки, если большая
car_width = 73


# функция для отрисовки машины, параметры = позиция
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


x_change = 0  # позиция
car_speed = 0  # скорость


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            # управление
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # смена позиции
        x += x_change

        # фон
        gameDisplay.fill(white)
        # создаем машину
        car(x, y)

        if x > display_width - car_width or x < 0:
            gameExit = True


        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


game_loop()
pygame.quit()
quit()