import pyautogui as pg
import time
from datetime import datetime


# Функция определяющая разрешение экрана для вычисления его составных частей
def region_getter():
    x, y = pg.size()
    screen = x, y
    
    return screen

# Функция, переводящая получаемые координаты в кортеж для клика
def coords_converter(coords):
    coords_tuple = (int(coords[0]), 
                    int(coords[1]), 
                    int(coords[2]), 
                    int(coords[3]))
    
    return coords_tuple


screen = region_getter()                                                                        # Разрешение экрана
left_half = (int(0), int(0), int(screen[0] / 2), int(screen[1]))                                # Левая половина
right_half = (int(screen[0] / 2), int(0), int(screen[0] / 2), int(screen[1]))                   # Правая половина
upper_half = (int(0), int(0), int(screen[0]), int(screen[1] / 2))                               # Верхняя половина
lower_half = (int(0), int(screen[1] / 2), int(screen[0]), int(screen[1] / 2))                   # Нижняя половина
quarter_1 = (int(screen[0] / 2), int(0), int(screen[0] / 2), int(screen[1] / 2))                # Первая четверть
quarter_2 = (int(0), int(0), int(screen[0] / 2), int(screen[1] / 2))                            # Вторая четверть
quarter_3 = (int(0), int(screen[1] / 2), int(screen[0] / 2), int(screen[1]))                    # Третья четверть
quarter_4 = (int(screen[0] / 2), int(screen[1] / 2), int(screen[0] / 2), int(screen[1] / 2))    # Четвертая четверть


# Функция переопределяющая библиотечный клик для работы по заданным параметрам
def my_click(image, confidence=0.5, action='left', region=None):
    image_coords_raw = pg.locateOnScreen(f'./images/{image}', confidence=confidence, region=region)
    pg.PAUSE = 2
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


# Пункты проверки согласно ПМИ
'''
def punkt_6_1():
    pointer = ''

    print('[+] 6.1 Проверка автоматической загрузки ПО Модуль "Отчет".', datetime.now())
    print('[+] 6.1.1 Запустить ПО "Графический терминал".', datetime.now())
    print('\t[debug] Поиск логотипа "КОМПАКС 7"')
                
    try:
        my_click('6_1.Logo_COMPACS.png', confidence=0.8)
        time.sleep(1.5)
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.1.1 пройден успешно!', datetime.now())
    except:
        print('\t\t[error] Не найдено!')
        print('[+] Пункт 6.1.1 не пройден!', datetime.now())
        pointer += ' 6.1.1'
        
    finally:
        time.sleep(5)
 
    print('[+] 6.1.2 В главном меню выбрать "Справка -> О модулях...".', datetime.now())
    print('\t[debug] Поиск кнопки "Справка"')
    p612 = 0

    try:
        my_click('6_1.Knopka_Spravka.png', confidence=0.8)
        time.sleep(1.5)
        print('\t\t[info] Успешно!')
        p612 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.2'
    finally:
        time.sleep(5)
    
    print('\t[debug] Поиск пункта КМ "О модулях...".')
      
    try:
        my_click('6_1.KM_Spravka.Knopka_O_Modulyakh.png', confidence=0.5)
        time.sleep(1.5)
        print('\t\t[info] Успешно!')
        p612 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.2'
    finally:
        time.sleep(5)

    if p612 == 2:
        print('[+] Пункт 6.1.2 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.1.2 не пройден!', datetime.now())

    print('[+] 6.1.3 В появившемся окне найти и выбрать модуль с именем: "КОМПАКС 7 модуль отчет на базе HTML 5 (reporthtml)".', datetime.now())
    print('\t[debug] Поиск окна "О модулях...".')
    p613 = 0

    try:
        my_click('6_1.W_O_Modulyakh.png')
        time.sleep(1.5)
        print('\t\t[info] Успешно!')
        p613 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.3'
    finally:
        time.sleep(5)

    print('\t[debug] Поиск модуля "КОМПАКС 7 модуль отчет на базе HTML 5 (reporthtml)".')
        
    try:
        my_click('6_1.Report_HTML.png', confidence=0.7)
        time.sleep(1.5)
        print('\t\t[info] Успешно!')
        p613 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.1.3'
    finally:
        time.sleep(5)

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
        time.sleep(5)
        
    print('[+] 6.1.5 ПО Модуль «Отчет» считается выдержавшим испытания, если на панели выбора режимов отобразилась кнопка «Отчет», был отображен диалог с информацией о версии, состояние модуля было отмечено серой опцией.', datetime.now())
    if pointer:
        print(f'[+] Пункт 6.1 не соответствует ПМИ! Ошибка в подпунктах: {pointer}', datetime.now())
    else:
        print('[+] Пункт 6.1 соответствует ПМИ!', datetime.now())

    time.sleep(5)


def punkt_6_2():
    pointer = ''

    print('[+] 6.2 Проверка устойчивости при нажатиях клавиш клавиатуры, перемещениях указателя, выбора шаблонов отчетов в ПО Модуль "Отчет".', datetime.now())
    
    print('[+] 6.2.1 Перейти в экран "ОТЧЕТ".', datetime.now())
    print('\t[debug] Поиск кнопки "ОТЧЕТ"')
    try:
        my_click('6_2.Knopka_Otchet.png')
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.2.1 пройден успешно!', datetime.now()) 
    except:
        print('\t\t[error] Не найдено!')
        print('[+] Пункт 6.2.1 не пройден!', datetime.now())
        pointer += ' 6.2.1'
    finally:
        time.sleep(5)

    print('[+] 6.2.2 Последовательно нажимать все клавиши клавиатуры, перемещать указатель "мыши".', datetime.now())
    try:
        pg.write('asdfjkl', interval=0.5)
        time.sleep(1.5)
        pg.press('down')
        time.sleep(1.5)
        pg.press('up')
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.2.2 пройден успешно!', datetime.now())
    except:
        print('\t\t[error] Не удалось!')
        print('[+] Пункт 6.2.2 не пройден!', datetime.now())
        pointer += ' 6.2.2'
    finally:
        time.sleep(5)
    
    print('[+] 6.2.3 Последовательно выбирать все имеющиеся шаблоны отчетов.', datetime.now())
    print('[+] Поиск шаблонов отчетов: "Объекты, требующие ремонта", "Состояние объектов", "Детальное состояние объектов", "Объекты в определенном состоянии", "Состояние объектов за месяц", "Состояние диагностических признаков", "События", "История ремонтов", "Проверка конфигурации", "История измерений диагностических признаков", "матрица слышимости".', datetime.now())
    try:
        my_click('6_2.Shablon_Obyecty_trebuyushchie_remonta.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Sostoyanie_obyectov.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Detalnoe_sostoyanie_obyectov.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Obyecty_v_opredelennom_sostoyanii.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Sostoyanie_obyectov_za_mesyac.png', confidence=0.9)
        time.sleep(3)
        my_click('6_2.Shablon_Sostoyanie_diagnosticheskikh_priznakov.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Sobytiya.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Istoriya_remontov.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Proverka_konfiguracii.png', confidence=0.8)
        time.sleep(3)
        pg.scroll(-300)
        my_click('6_2.Shablon_Istoriya_izmereniy_diagnostocheskikh_priznakov.png', confidence=0.8)
        time.sleep(3)
        my_click('6_2.Shablon_Matritsa_slyshimosti.png', confidence=0.8)
        time.sleep(2)
        pg.scroll(300)
        print('\t\t[info] Успешно!')
        print('[+] Пункт 6.2.3 пройден успешно!', datetime.now())
    except:
        print('\t\t[error] Состав шаблонов отчетов не соответствует!')
        print('[+] Пункт 6.2.3 не пройден!', datetime.now())
        pointer += ' 6.2.3'
    finally:
        time.sleep(5)
        my_click('Monitor.png')

    print('[+] 6.2.4 ПО Модуль "Отчет" считается выдержавшим испытание, если не произошло зависания, искажения изображения на экране и формы отчетов соответствовали формам, приведенным в приложении 1. .', datetime.now())
    if pointer:
        print(f'[+] Пункт 6.2 не соответствует ПМИ! Ошибка в подпунктах: {pointer}', datetime.now())
    else:
        print('[+] Пункт 6.2 соответствует ПМИ!', datetime.now())

    time.sleep(5)


def punkt_6_3():
    pointer = ''

    print('[+] 6.3 Проверка формирования и отображения отчетов по требованию оператора .', datetime.now())
    print('[+] 6.3.1 Выбрать шаблон отчета "Состояние объектов установки"', datetime.now())
    print('\t[debug] Поиск кнопки "ОТЧЕТ".')
    p631 = 0

    try:
        my_click('6_2.Knopka_Otchet.png')
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p631 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.3.1'
    finally:
        time.sleep(5)
        
    print('\t[debug] Поиск шаблона отчета "Состояние объектов установки".')
    try:
        my_click('6_2.Shablon_Sostoyanie_obyectov.png', confidence=0.8, region=upper_half)
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p631 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.3.1'
    finally:
        time.sleep(5)

    if p631 == 2:
        print('[+] Пункт 6.3.1 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.3.1 не пройден!', datetime.now())

    print('[+] 6.3.2 Нажать на кнопку "Выбрать все", для выбора всех объектов и  нажать на кнопку "Сформировать".', datetime.now())
    print('\t[debug] Поиск кнопки "Выбрать все".')
    p632 = 0
    try:
        my_click('6_3.Knopka_Vybrat_vse.png')
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p632 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.3.2'
    finally:
        time.sleep(5)

    print('\t[debug] Поиск кнопки "Сформировать".')
    try:
        my_click('6_3.Knopka_Sformirovat.png', confidence=0.8, region=lower_half)
        time.sleep(30)
        print('\t\t[info] Успешно!')
        p632 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.3.2'
    finally:
        time.sleep(5)

    if p632 == 2:
        print('[+] Пункт 6.3.2 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.3.2 не пройден!', datetime.now())

    print('[+] 6.3.3 Дождаться окончания формирования отчета.')
    print('\t[debug] Поиск заголовка сформированного отчета.')
    try:
        my_click('6_3.Otchet_Sostoyanie_obyectov.png')
        time.sleep(5)
        print('\t\t[info] Успешно!')
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.3.3'
    finally:
        time.sleep(5)
        my_click('Monitor.png')

    print('[+] 6.3.4 ПО Модуль «Отчет» считается выдержавшим испытания, если после нажатия на кнопку «Сформировать» отобразился диалог с прогрессом формирования отчета и при достижении значения прогресса 100 %, отобразился сформированный отчет.', datetime.now())
    if pointer:
        print(f'[+] Пункт 6.3 не соответствует ПМИ! Ошибка в подпунктах: {pointer}', datetime.now())
    else:
        print('[+] Пункт 6.3 соответствует ПМИ!', datetime.now())

    time.sleep(5)
'''

def punkt_6_4():
    pointer = ''

    print('[+] 6.4 Проверка формирования типовых шаблонов отчетов.', datetime.now())
    print('[+] 6.4.1 Перейти во вкладку "Новые отчеты".', datetime.now())
    print('\t[debug] Поиск кнопки "ОТЧЕТ".')
    

    try:
        my_click('6_2.Knopka_Otchet.png')
        time.sleep(5)
        print('\t\t[info] Успешно!')
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.4.1'
    finally:
        time.sleep(5)

    print('[+] 6.4.2 Последовательно выбирать форму отчета и проверять ее соответствие форме отчета, приведенной в приложении 1.')
    p642 = 0

    print('\t[debug] Поиск шаблона "Объекты, требующие ремонта", формирование шаблона, проверка шаблона на соответствие.')
    
    try:
        my_click('6_2.Shablon_Obyecty_trebuyushchie_remonta.png', region=left_half)
        time.sleep(5)
        my_click('6_3.Knopka_Sformirovat.png', region=lower_half)
        time.sleep(30)
        my_click('6_4.Zagolovok_Obyecty_trebuyushchie_remonta.png', region=upper_half)
        time.sleep(5)
        my_click('6_4.Vkladka_Obyecty_trebuyushchie_remonta.png', region=quarter_3)
        time.sleep(5)
        my_click('6_4.Knopka_zakryt_vkladku.png', region=quarter_3)
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p642 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.4.2'
    finally:
        time.sleep(5)

    print('\t[debug] Поиск шаблона "Состояние объектов", формирование шаблона, проверка шаблона на соответствие.')
    
    try:
        my_click('6_2.Shablon_Sostoyanie_obyectov.png', region=left_half)
        time.sleep(5)
        my_click('6_4.Checkbox_Sostoyanie_obyectov.png', region=upper_half)
        time.sleep(5)
        my_click('6_3.Knopka_Sformirovat.png', region=lower_half)
        time.sleep(30)
        my_click('6_4.Zagolovok_Sostoyanie_obyectov.png', region=upper_half)
        time.sleep(5)
        my_click('6_4.Vkladka_Sostoyanie_obyectov.png', confidence=0.8, region=quarter_3)
        time.sleep(5)
        my_click('6_4.Knopka_zakryt_vkladku.png', region=quarter_3)
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p642 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.4.2'
    finally:
        time.sleep(5)

    print('\t[debug] Поиск шаблона "Детальное остояние объектов", формирование шаблона, проверка шаблона на соответствие.')
    
    try:
        my_click('6_2.Shablon_Detalnoe_sostoyanie_obyectov.png', confidence=0.8, region=left_half)
        time.sleep(5)
        my_click('6_4.Checkbox_Sostoyanie_obyectov.png', region=upper_half)
        time.sleep(5)
        my_click('6_3.Knopka_Sformirovat.png', region=lower_half)
        time.sleep(30)
        my_click('6_4.Zagolovok_Detalnoe_sostoyanie_obyectov.png', region=upper_half)
        time.sleep(5)
        my_click('6_4.Vkladka_Detalnoe_sostoyanie_obyectov.png', confidence=0.8, region=quarter_3)
        time.sleep(5)
        my_click('6_4.Knopka_zakryt_vkladku.png', region=quarter_3)
        time.sleep(5)
        print('\t\t[info] Успешно!')
        p642 += 1
    except:
        print('\t\t[error] Не найдено!')
        pointer += ' 6.4.2'
    finally:
        time.sleep(5)

    if p642 == 3:
        print('[+] Пункт 6.4.2 пройден успешно!', datetime.now())
    else:
        print('[+] Пункт 6.4.2 не пройден!', datetime.now())

def main():
    start = datetime.now()
    print('[start] Начинается проверка модуля "Отчет".')

    #punkt_6_1()
    #punkt_6_2()
    #punkt_6_3()
    punkt_6_4()

    end = datetime.now()
    print(f'[finish] Проверка модуля "Отчет" заняла - {end - start}.')


main()
input()