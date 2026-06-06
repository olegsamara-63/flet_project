import flet as ft
import os
from pygame import mixer  # ИСПРАВЛЕНИЕ: Используем надежный фоновый микшер Python

def main(page: ft.Page):
    page.title = "Web Testers Company 2026"
    page.bgcolor = "#222222"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Стиль для кнопок (белый текст, синий фон)
    btn_style = ft.ButtonStyle(
        color="#FFFFFF",
        bgcolor="#007BFF"
    )

    # Инициализируем аудиомикшер внутри Python процесса
    mixer.init()
    audio_path = os.path.abspath("voda.mp3")

    # Состояние аудио (играет / остановлено)
    is_playing = False

    # Синхронная функция управления аудиозаписью внутри процесса приложения
    def toggle_audio(e):
        nonlocal is_playing
        if not is_playing:
            try:
                mixer.music.load(audio_path)
                mixer.music.play()  # Воспроизведение звука внутри приложения
                e.control.text = "Остановить"
                is_playing = True
            except Exception as ex:
                print(f"Ошибка воспроизведения файла: {ex}")
        else:
            mixer.music.stop()  # Остановка звука внутри приложения
            e.control.text = "Слушать волны"
            is_playing = False
        page.update()

    # Синхронная функция отрисовки ГЛАВНОГО ЭКРАНА
    def show_main_screen(e=None):
        nonlocal is_playing
        # Если музыка играет, глушим её при возврате на главную страницу
        if is_playing:
            mixer.music.stop()
            is_playing = False 
            
        page.controls.clear()
        page.controls.extend([
            ft.Text(
                "Компания Web Testers Company выполняет тестирование сайтов, web-приложений, приложений для ПК и другой ПО.", 
                size=18, 
                weight="bold", 
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER
            ),
            ft.FilledButton("1-ый экран", on_click=lambda _: show_sub_screen(1), style=btn_style),
            ft.FilledButton("2-ой экран", on_click=lambda _: show_sub_screen(2), style=btn_style),
            ft.FilledButton("3-ий экран", on_click=lambda _: show_sub_screen(3), style=btn_style),
            ft.FilledButton("4-ый экран", on_click=lambda _: show_sub_screen(4), style=btn_style),
            ft.FilledButton("5-ый экран", on_click=lambda _: show_sub_screen(5), style=btn_style),
            ft.Text(
                "Адрес сайта Компании https://h1n.ru", 
                size=9, 
                weight="bold", 
                color="#FFFFFF"
            )
        ])
        page.update()

    # Синхронная функция отрисовки ДОПОЛНИТЕЛЬНЫХ ЭКРАНОВ
    def show_sub_screen(screen_num):
        page.controls.clear()
        
        screen_controls = [
            ft.Text(
                f"Экран номер {screen_num}", 
                size=18, 
                weight="bold", 
                color="#FFFFFF"
            ),
            ft.FilledButton(
                "На главный экран", 
                on_click=lambda _: show_main_screen(), 
                style=btn_style
            )
        ]
        
        if screen_num == 1:
            current_text = "Остановить" if is_playing else "Слушать волны"
            audio_button = ft.FilledButton(
                current_text,
                on_click=toggle_audio,
                style=btn_style
            )
            screen_controls.insert(1, audio_button)
            
        page.controls.extend(screen_controls)
        page.update()

    # Стартовый запуск главного экрана
    show_main_screen()

# ИСПРАВЛЕНИЕ: Используем ft.run(main) вместо устаревшего ft.app
ft.run(main)







