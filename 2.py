import os
import sys
import requests
import pygame

from PyQt6 import uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow
from io import BytesIO

os.chdir(os.path.dirname(__file__))
API_KEY_STATIC = 'dbcb1a72-711c-454c-8aad-1732cd8bda67'

server_address = 'https://static-maps.yandex.ru/v1?'
ll_spn = 'll=37.530887,55.703118&spn=0.002,0.002'


def get_map(ll, map_zoom):
    screen.fill("black")
    map_params = {
        "ll": ",".join(map(str, ll)),
        'z': map_zoom,
        'apikey': API_KEY_STATIC,
    }

    response = requests.get('https://static-maps.yandex.ru/v1',
                            params=map_params)
    map_file = BytesIO(response.content)
    screen.blit(pygame.image.load(map_file), (0, 0))


pygame.init()
screen = pygame.display.set_mode((600, 450))
ll = [45.711434, 43.326383]
map_zoom = 15
get_map(ll, map_zoom)
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                print(map_zoom)
                map_zoom += 1
                get_map(ll, map_zoom)
            elif event.key == pygame.K_PAGEDOWN:
                print(map_zoom)
                map_zoom -= 1
                get_map(ll, map_zoom)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
