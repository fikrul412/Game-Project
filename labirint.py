from pygame import *

back = (255, 255, 255)
layar = display.set_mode((500, 500))
display.set_caption('Game labirin')
jam = time.Clock()

background = transform.scale(image.load('background.jpg'), (500,500))
class GameSprite(sprite.Sprite):

    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = x_cor
        self.rect.y = y_cor

    def reset(self):
        layar.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

class Musuh(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

class Dinding(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

class Koin(GameSprite):
    def __init__(self, sprite_image, x_cor, y_cor, size_x, size_y):
        GameSprite.__init__(self, sprite_image, x_cor, y_cor,size_x, size_y)

player1 = Player('player.png', 50, 50, 75, 75)
musuh1 = Musuh('musuh.png', 300, 200, 75, 75)
koin1 = Koin('coin.png', 400, 400, 75, 75)
dinding1 = Dinding('dinding.jpg', 250, 250, 50, 340)

run = True
while run:
    layar.fill(back)
    layar.blit(background, (0,0))
    jam.tick(40)
    player1.reset()
    musuh1.reset()
    dinding1.reset()
    koin1.reset()
    for kejadian in event.get():
        if kejadian.type == QUIT:
            run = False

    display.update()



