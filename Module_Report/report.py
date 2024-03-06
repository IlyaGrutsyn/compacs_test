import pyautogui as pg
from datetime import datetime


# Блок определения программных функций # <

def coords_converter(coords):
    coords_tuple = (int(coords[0]), 
                    int(coords[1]), 
                    int(coords[2]), 
                    int(coords[3]))
    
    return coords_tuple


def my_click(image, confidence=0.5, action='left'):
    image_coords_raw = pg.locateOnScreen(f'../../images/{image}', confidence=confidence)
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

######################################## />


def punkt_6_1():
    pointer = ''

    print('[+] 6.1 Проверка автоматической загрузки ПО Модуль "Отчет".', datetime.now())
    print('[+] 6.1.1 Запустить ПО "Графический терминал".', datetime.now())
    print('\t[debug] Поиск логотипа "КОМПАКС 7"')
                
    try:
        my_click('6_1.Logo_COMPACS.png', confidence=0.8)
        pg.PAUSE = 1.5
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.1.1 пройден успешно!', datetime.now())
    except:
        print('\t\t[error] Не найдено!')
        print('[+] Пункт 6.1.1 не пройден!', datetime.now())
        pointer += ' 6.1.1'
        
    finally:
        pg.PAUSE = 1.5
 
    print('[+] 6.1.2 В главном меню выбрать "Справка -> О модулях...".', datetime.now())
    print('\t[debug] Поиск кнопки "Справка"')
    p612 = 0

    try:
        my_click('6_1.Knopka_Spravka.png', confidence=0.8)
        pg.PAUSE = 1.5
        print('\t\t[info] Успешно!')
        p612 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.2'
    finally:
        pg.PAUSE = 1.5
    
    print('\t[debug] Поиск пункта КМ "О модулях...".')
      
    try:
        my_click('6_1.KM_Spravka.Knopka_O_Modulyakh.png', confidence=0.5)
        pg.PAUSE = 1.5
        print('\t\t[info] Успешно!')
        p612 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.2'
    finally:
        pg.PAUSE = 1.5

    if p612 == 2:
        print('[+] Пункт 6.1.2 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.1.2 не пройден!', datetime.now())

    print('[+] 6.1.3 В появившемся окне найти и выбрать модуль с именем: "КОМПАКС 7 модуль отчет на базе HTML 5 (reporthtml)".', datetime.now())
    print('\t[debug] Поиск окна "О модулях...".')
    p613 = 0

    try:
        my_click('6_1.W_O_Modulyakh.png')
        pg.PAUSE = 1.5
        print('\t\t[info] Успешно!')
        p613 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.3'
    finally:
        pg.PAUSE = 1.5

    print('\t[debug] Поиск модуля "КОМПАКС 7 модуль отчет на базе HTML 5 (reporthtml)".')
        
    try:
        my_click('6_1.Report_HTML.png', confidence=0.7)
        pg.PAUSE = 1.5
        print('\t\t[info] Успешно!')
        p613 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.3'
    finally:
        pg.PAUSE = 1.5

    if p613 == 2:
        print('[+] Пункт 6.1.3 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.1.3 не пройден!', datetime.now())

    print('[+] 6.1.4 Закрыть все открывшиеся окна.', datetime.now())
    print('\t[debug] Поиск кнопки "Закрыть".')
        
    try:
        my_click('6_1.Knopka_Zakryt.png')
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.1.4 пройден успешно!', datetime.now())        
    except:
        print('\t\t[error] Не найдено!')
        print('[+] Пункт 6.1.4 не пройден!', datetime.now())
        pointer += ' 6.1.4'
    finally:
        pg.PAUSE = 1.5
        
    print('[+] 6.1.5 ПО Модуль «Отчет» считается выдержавшим испытания, если на панели выбора режимов отобразилась кнопка «Отчет», был отображен диалог с информацией о версии, состояние модуля было отмечено серой опцией.', datetime.now())
    if pointer:
        print(f'[+] Пункт 6.1 не соответствует ПМИ! Ошибка в подпунктах: {pointer}', datetime.now())
    else:
        print('[+] Пункт 6.1 соответствует ПМИ!', datetime.now())

    pg.PAUSE = 5

punkt_6_1()
input()
