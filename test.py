import pyautogui as pg
from datetime import datetime


def region_getter():
    x, y = pg.size()
    screen = x, y
    
    return screen

screen = region_getter()
left_half = (int(0), int(0), int(screen[0] / 2), int(screen[1]))
right_half = (int(screen[0] / 2), int(0), int(screen[0] / 2), int(screen[1]))
upper_half = (int(0), int(0), int(screen[0]), int(screen[1] / 2))
lower_half = (int(0), int(screen[1] / 2), int(screen[0]), int(screen[1] / 2))



# Функция, переводящая получаемые координаты в кортеж для клика
def coords_converter(coords):
    coords_tuple = (int(coords[0]), 
                    int(coords[1]), 
                    int(coords[2]), 
                    int(coords[3]))
    
    return coords_tuple


# Функция переопределяющая библиотечный клик для работы по заданным параметрам
def my_click(image, confidence=0.5, action='left', region=None):
    image_coords_raw = pg.locateOnScreen(f'./images/{image}', confidence=confidence, region=region)
    image_coords = coords_converter(image_coords_raw)
    x = image_coords[0] + (image_coords[2] / 2)
    y = image_coords[1] + (image_coords[3] / 2)
    pg.moveTo(x, y)
    
    if action == 'left':
        pg.click()
    elif action == 'right':
        pg.rightClick()
    elif action == 'double':
        pg.doubleClick()


start = datetime.now()
my_click('6_2.Knopka_Otchet.png', region=left_half)
end = datetime.now()
print(end - start)
