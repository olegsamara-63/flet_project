# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
#     # Стилизация поля ввода: добавляем белый цвет текста и рамки
#     name_input = ft.TextField(
#         label=" Давайте познакомимся! Напишите Ваше имя", 
#         width=300,
#         color="#FFFFFF",
#         label_style=ft.TextStyle(color="#AAAAAA"),
#         focused_border_color="#007BFF"
#     )
    
#     # Белый цвет для текста результата
#     result_text = ft.Text("", size=14, color="#FFFFFF")
    
#     def on_click(e):
#         if name_input.value:
#             result_text.value = f"Привет, {name_input.value}! Рады нашему знакомству!"
#         else:
#             result_text.value = "Пожалуйста, введите имя"
#         page.update()
    
#     page.add(
#         # Белый цвет для главного заголовка
#         ft.Text("Компания Web Testers Company приветствует Вас!", size=18, weight="bold", color="#FFFFFF"),
#         name_input,
#         # Стилизация кнопки: синий фон и белый текст
#         ft.ElevatedButton(
#             "Сказать привет", 
#             on_click=on_click,
#             style=ft.ButtonStyle(
#                 color="#FFFFFF",
#                 bgcolor="#007BFF"
#             )
#         ),
#         result_text
#     )

# ft.app(target=main)

# 
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     # Общий стиль для кнопок (белый текст, синий фон)
#     btn_style = ft.ButtonStyle(
#         color="#FFFFFF",
#         bgcolor="#007BFF"
#     )

#     # Функция смены экранов (маршрутизация)
#     def route_change(e): # Исправлено: добавлен аргумент события 'e'
#         page.views.clear()
        
#         # ГЛАВНЫЙ ЭКРАН
#         if page.route == "/":
#             page.views.append(
#                 ft.View(
#                     route="/",
#                     controls=[
#                         # Новый главный заголовок
#                         ft.Text(
#                             "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF",
#                             text_align=ft.TextAlign.CENTER
#                         ),
#                         # 5 кнопок переходов
#                         ft.ElevatedButton("1-ый экран", on_click=lambda _: page.go("/screen1"), style=btn_style),
#                         ft.ElevatedButton("2-ой экран", on_click=lambda _: page.go("/screen2"), style=btn_style),
#                         ft.ElevatedButton("3-ий экран", on_click=lambda _: page.go("/screen3"), style=btn_style),
#                         ft.ElevatedButton("4-ый экран", on_click=lambda _: page.go("/screen4"), style=btn_style),
#                         ft.ElevatedButton("5-ый экран", on_click=lambda _: page.go("/screen5"), style=btn_style),
#                         # Текст внизу (размер в два раза меньше главного заголовка: 18 / 2 = 9)
#                         ft.Text(
#                             "Адрес сайта Компании https://h1n.ru", 
#                             size=9, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
        
#         # 5 НОВЫХ ЭКРАНОВ
#         elif page.route in ["/screen1", "/screen2", "/screen3", "/screen4", "/screen5"]:
#             # Определяем номер экрана из маршрута для текста
#             screen_num = page.route[-1]
            
#             page.views.append(
#                 ft.View(
#                     route=page.route,
#                     controls=[
#                         # Надпись (стиль, цвет и размер 18 как у главного заголовка)
#                         ft.Text(
#                             f"Экран номер {screen_num}", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         ),
#                         # Кнопка возврата (стиль как у главных кнопок)
#                         ft.ElevatedButton(
#                             "На главный экран", 
#                             on_click=lambda _: page.go("/"), 
#                             style=btn_style
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor # Такой же цвет фона
#                 )
#             )
            
#         page.update()

#     # Регистрация обработчика маршрутов
#     page.on_route_change = route_change
    
#     # ИСПРАВЛЕНИЕ: Запуск через текущий маршрут страницы 
#     # Это заставит flet run корректно обработать стартовый экран
#     page.go(page.route) 

# ft.app(target=main)

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     # Общий стиль для кнопок (белый текст, синий фон)
#     btn_style = ft.ButtonStyle(
#         color="#FFFFFF",
#         bgcolor="#007BFF"
#     )

#     # Функция смены экранов (маршрутизация)
#     def route_change(e):
#         page.views.clear()
        
#         # ГЛАВНЫЙ ЭКРАН
#         if page.route == "/":
#             page.views.append(
#                 ft.View(
#                     route="/",
#                     controls=[
#                         # Новый главный заголовок
#                         ft.Text(
#                             "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF",
#                             text_align=ft.TextAlign.CENTER
#                         ),
#                         # 5 кнопок переходов
#                         ft.ElevatedButton("1-ый экран", on_click=lambda _: page.go("/screen1"), style=btn_style),
#                         ft.ElevatedButton("2-ой экран", on_click=lambda _: page.go("/screen2"), style=btn_style),
#                         ft.ElevatedButton("3-ий экран", on_click=lambda _: page.go("/screen3"), style=btn_style),
#                         ft.ElevatedButton("4-ый экран", on_click=lambda _: page.go("/screen4"), style=btn_style),
#                         ft.ElevatedButton("5-ый экран", on_click=lambda _: page.go("/screen5"), style=btn_style),
#                         # Текст внизу (размер в два раза меньше главного заголовка: 18 / 2 = 9)
#                         ft.Text(
#                             "Адрес сайта Компании https://h1n.ru", 
#                             size=9, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
        
#         # 5 НОВЫХ ЭКРАНОВ
#         elif page.route in ["/screen1", "/screen2", "/screen3", "/screen4", "/screen5"]:
#             # Определяем номер экрана из маршрута для текста
#             screen_num = page.route[-1]
            
#             page.views.append(
#                 ft.View(
#                     route=page.route,
#                     controls=[
#                         # Надпись (стиль, цвет и размер 18 как у главного заголовка)
#                         ft.Text(
#                             f"Экран номер {screen_num}", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         ),
#                         # Кнопка возврата (стиль как у главных кнопок)
#                         ft.ElevatedButton(
#                             "На главный экран", 
#                             on_click=lambda _: page.go("/"), 
#                             style=btn_style
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor # Такой же цвет фона
#                 )
#             )
            
#         page.update()

#     # Обязательная функция для корректной работы системной кнопки "Назад" (например, в Android)
#     def view_pop(e):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)

#     # Регистрация обработчиков
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
    
#     # ИСПРАВЛЕНИЕ ДЛЯ flet run: 
#     # Сначала жестко принудительно очищаем и устанавливаем стартовый маршрут
#     page.route = "/" 
#     # Вызываем функцию отрисовки напрямую, передавая None вместо события
#     route_change(None) 

# ft.app(target=main)

# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     # Общий стиль для кнопок (белый текст, синий фон)
#     btn_style = ft.ButtonStyle(
#         color="#FFFFFF",
#         bgcolor="#007BFF"
#     )

#     # Функция смены экранов (маршрутизация)
#     def route_change(e):
#         page.views.clear()
        
#         # ГЛАВНЫЙ ЭКРАН (обрабатываем и "/" и пустой маршрут для надежности flet run)
#         if page.route == "/" or page.route == "":
#             page.views.append(
#                 ft.View(
#                     route="/",
#                     controls=[
#                         # Новый главный заголовок
#                         ft.Text(
#                             "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF",
#                             text_align=ft.TextAlign.CENTER
#                         ),
#                         # 5 кнопок переходов
#                         ft.ElevatedButton("1-ый экран", on_click=lambda _: page.go("/screen1"), style=btn_style),
#                         ft.ElevatedButton("2-ой экран", on_click=lambda _: page.go("/screen2"), style=btn_style),
#                         ft.ElevatedButton("3-ий экран", on_click=lambda _: page.go("/screen3"), style=btn_style),
#                         ft.ElevatedButton("4-ый экран", on_click=lambda _: page.go("/screen4"), style=btn_style),
#                         ft.ElevatedButton("5-ый экран", on_click=lambda _: page.go("/screen5"), style=btn_style),
#                         # Текст внизу (размер в два раза меньше главного заголовка: 18 / 2 = 9)
#                         ft.Text(
#                             "Адрес сайта Компании https://h1n.ru", 
#                             size=9, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
        
#         # 5 НОВЫХ ЭКРАНОВ
#         elif page.route in ["/screen1", "/screen2", "/screen3", "/screen4", "/screen5"]:
#             # Определяем номер экрана из маршрута для текста
#             screen_num = page.route[-1]
            
#             page.views.append(
#                 ft.View(
#                     route=page.route,
#                     controls=[
#                         # Надпись (стиль, цвет и размер 18 как у главного заголовка)
#                         ft.Text(
#                             f"Экран номер {screen_num}", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         ),
#                         # Кнопка возврата (стиль как у главных кнопок)
#                         ft.ElevatedButton(
#                             "На главный экран", 
#                             on_click=lambda _: page.go("/"), 
#                             style=btn_style
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
            
#         page.update()

#     # Обязательная функция для корректной работы системной кнопки "Назад"
#     def view_pop(e):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)

#     # Регистрация обработчиков
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
    
#     # ИСПРАВЛЕНИЕ: устанавливаем начальное состояние приложения напрямую в корневую вьюшку
#     page.views.append(
#         ft.View(
#             route="/",
#             controls=[
#                 ft.Text(
#                     "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                     size=18, 
#                     weight="bold", 
#                     color="#FFFFFF",
#                     text_align=ft.TextAlign.CENTER
#                 ),
#                 ft.ElevatedButton("1-ый экран", on_click=lambda _: page.go("/screen1"), style=btn_style),
#                 ft.ElevatedButton("2-ой экран", on_click=lambda _: page.go("/screen2"), style=btn_style),
#                 ft.ElevatedButton("3-ий экран", on_click=lambda _: page.go("/screen3"), style=btn_style),
#                 ft.ElevatedButton("4-ый экран", on_click=lambda _: page.go("/screen4"), style=btn_style),
#                 ft.ElevatedButton("5-ый экран", on_click=lambda _: page.go("/screen5"), style=btn_style),
#                 ft.Text(
#                     "Адрес сайта Компании https://h1n.ru", 
#                     size=9, 
#                     weight="bold", 
#                     color="#FFFFFF"
#                 )
#             ],
#             horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#             vertical_alignment=ft.MainAxisAlignment.CENTER,
#             bgcolor=page.bgcolor
#         )
#     )
    
#     # Задаем базовый маршрут и обновляем страницу
#     page.route = "/"
#     page.update()

# ft.app(target=main)
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     # Общий стиль для кнопок (белый текст, синий фон)
#     btn_style = ft.ButtonStyle(
#         color="#FFFFFF",
#         bgcolor="#007BFF"
#     )

#     # Функция смены экранов (маршрутизация)
#     def route_change(e):
#         # ИСПРАВЛЕНИЕ: берем точный маршрут из события перехода e.route
#         current_route = e.route if e and e.route else page.route
        
#         page.views.clear()
        
#         # ГЛАВНЫЙ ЭКРАН
#         if current_route == "/" or current_route == "":
#             page.views.append(
#                 ft.View(
#                     route="/",
#                     controls=[
#                         ft.Text(
#                             "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF",
#                             text_align=ft.TextAlign.CENTER
#                         ),
#                         ft.ElevatedButton("1-ый экран", on_click=lambda _: page.go("/screen1"), style=btn_style),
#                         ft.ElevatedButton("2-ой экран", on_click=lambda _: page.go("/screen2"), style=btn_style),
#                         ft.ElevatedButton("3-ий экран", on_click=lambda _: page.go("/screen3"), style=btn_style),
#                         ft.ElevatedButton("4-ый экран", on_click=lambda _: page.go("/screen4"), style=btn_style),
#                         ft.ElevatedButton("5-ый экран", on_click=lambda _: page.go("/screen5"), style=btn_style),
#                         ft.Text(
#                             "Адрес сайта Компании https://h1n.ru", 
#                             size=9, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
        
#         # 5 НОВЫХ ЭКРАНОВ
#         elif current_route in ["/screen1", "/screen2", "/screen3", "/screen4", "/screen5"]:
#             # Получаем номер экрана из текущего маршрута события
#             screen_num = current_route[-1]
            
#             page.views.append(
#                 ft.View(
#                     route=current_route,
#                     controls=[
#                         ft.Text(
#                             f"Экран номер {screen_num}", 
#                             size=18, 
#                             weight="bold", 
#                             color="#FFFFFF"
#                         ),
#                         ft.ElevatedButton(
#                             "На главный экран", 
#                             on_click=lambda _: page.go("/"), 
#                             style=btn_style
#                         )
#                     ],
#                     horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                     vertical_alignment=ft.MainAxisAlignment.CENTER,
#                     bgcolor=page.bgcolor
#                 )
#             )
            
#         page.update()

#     # Функция для корректной работы кнопки "Назад"
#     def view_pop(e):
#         page.views.pop()
#         top_view = page.views[-1]
#         page.go(top_view.route)

#     # Регистрация обработчиков
#     page.on_route_change = route_change
#     page.on_view_pop = view_pop
    
#     # Запускаем изначальное построение главного экрана
#     page.go("/")

# ft.app(target=main)
# import flet as ft

# def main(page: ft.Page):
#     page.title = "Web Testers Company 2026"
#     page.bgcolor = "#222222"
#     page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
#     page.vertical_alignment = ft.MainAxisAlignment.CENTER

#     # Общий стиль для кнопок (белый текст, синий фон)
#     btn_style = ft.ButtonStyle(
#         color="#FFFFFF",
#         bgcolor="#007BFF"
#     )

#     # Функция отрисовки ГЛАВНОГО ЭКРАНА
#     def show_main_screen(e=None):
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 controls=[
#                     ft.Text(
#                         "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
#                         size=18, 
#                         weight="bold", 
#                         color="#FFFFFF",
#                         text_align=ft.TextAlign.CENTER
#                     ),
#                     ft.ElevatedButton("1-ый экран", on_click=lambda _: show_sub_screen(1), style=btn_style),
#                     ft.ElevatedButton("2-ой экран", on_click=lambda _: show_sub_screen(2), style=btn_style),
#                     ft.ElevatedButton("3-ий экран", on_click=lambda _: show_sub_screen(3), style=btn_style),
#                     ft.ElevatedButton("4-ый экран", on_click=lambda _: show_sub_screen(4), style=btn_style),
#                     ft.ElevatedButton("5-ый экран", on_click=lambda _: show_sub_screen(5), style=btn_style),
#                     ft.Text(
#                         "Адрес сайта Компании https://h1n.ru", 
#                         size=9, 
#                         weight="bold", 
#                         color="#FFFFFF"
#                     )
#                 ],
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 vertical_alignment=ft.MainAxisAlignment.CENTER,
#                 bgcolor=page.bgcolor
#             )
#         )
#         page.update()

#     # Функция отрисовки ДОПОЛНИТЕЛЬНЫХ ЭКРАНОВ
#     def show_sub_screen(screen_num):
#         page.views.clear()
#         page.views.append(
#             ft.View(
#                 controls=[
#                     ft.Text(
#                         f"Экран номер {screen_num}", 
#                         size=18, 
#                         weight="bold", 
#                         color="#FFFFFF"
#                     ),
#                     ft.ElevatedButton(
#                         "На главный экран", 
#                         on_click=show_main_screen, 
#                         style=btn_style
#                     )
#                 ],
#                 horizontal_alignment=ft.CrossAxisAlignment.CENTER,
#                 vertical_alignment=ft.MainAxisAlignment.CENTER,
#                 bgcolor=page.bgcolor
#             )
#         )
#         page.update()

#     # Сразу принудительно отрисовываем главный экран при старте приложения
#     show_main_screen()

# ft.app(target=main)
import flet as ft

def main(page: ft.Page):
    page.title = "Web Testers Company 2026"
    page.bgcolor = "#222222"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Общий стиль для кнопок (белый текст, синий фон)
    btn_style = ft.ButtonStyle(
        color="#FFFFFF",
        bgcolor="#007BFF"
    )

    # Функция отрисовки ГЛАВНОГО ЭКРАНА
    def show_main_screen(e=None):
        page.controls.clear()  # Безопасно очищаем только элементы, а не экран целиком
        page.controls.extend([
            ft.Text(
                "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другого ПО.", 
                size=18, 
                weight="bold", 
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER
            ),
            ft.ElevatedButton("1-ый экран", on_click=lambda _: show_sub_screen(1), style=btn_style),
            ft.ElevatedButton("2-ой экран", on_click=lambda _: show_sub_screen(2), style=btn_style),
            ft.ElevatedButton("3-ий экран", on_click=lambda _: show_sub_screen(3), style=btn_style),
            ft.ElevatedButton("4-ый экран", on_click=lambda _: show_sub_screen(4), style=btn_style),
            ft.ElevatedButton("5-ый экран", on_click=lambda _: show_sub_screen(5), style=btn_style),
            ft.Text(
                "Адрес сайта Компании https://profitest.h1n.ru", 
                size=9, 
                weight="bold", 
                color="#FFFFFF"
            )
        ])
        page.update()

    # Функция отрисовки ДОПОЛНИТЕЛЬНЫХ ЭКРАНОВ
    def show_sub_screen(screen_num):
        page.controls.clear()  # Безопасно очищаем элементы главного экрана
        page.controls.extend([
            ft.Text(
                f"Экран номер {screen_num}", 
                size=18, 
                weight="bold", 
                color="#FFFFFF"
            ),
            ft.ElevatedButton(
                "На главный экран", 
                on_click=show_main_screen, 
                style=btn_style
            )
        ])
        page.update()

    # Сразу принудительно отрисовываем главный экран при старте приложения
    show_main_screen()

ft.app(target=main)
