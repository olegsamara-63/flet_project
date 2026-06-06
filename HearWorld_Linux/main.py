import flet as ft
import os
import sys
from pygame import mixer  # Используем надежный фоновый микшер Python

def main(page: ft.Page):
    page.title = "Ты слышишь? Да!"
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

    # Состояние аудио (играет / остановлено)
    is_playing = False
    
    # Переменная для хранения номера текущего активного экрана со звуком
    current_active_screen = None

    # Карта настроек для каждого экрана: (Имя файла, Текст кнопки старта, Текст заголовка экрана, Зациклить?)
    screen_audio_configs = {
        1: ("voda.mp3", "Слушать волны", "Море, всегда звучит прекрасно!", True),
        2: ("les_audio.mp3", "Услышать Лес", "Лес всегда выглядит и звучит прекрасно!", True),
        3: ("Gorod.mp3", "Твой Город", "Город всегда живой!", True),
        4: ("koster_nicht.mp3", "Твои Ночь и Костёр", "Ночь и Костёр для Вас!", True),
        5: ("meditaciya.mp3", "Медитация", "Вам не о чем беспокоиться!", True)
    }

    # Универсальная функция управления аудиозаписью
    def toggle_audio(e, screen_num):
        nonlocal is_playing, current_active_screen
        config = screen_audio_configs.get(screen_num)
        if not config:
            return

        file_name, default_text, _, loop = config
        
        # Динамически определяем путь к assets рядом с файлом запуска main.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        audio_path = os.path.join(base_dir, "assets", file_name)

        if not is_playing:
            try:
                mixer.music.load(audio_path)
                
                if loop:
                    mixer.music.play(loops=-1)  # Бесконечный повтор файла
                else:
                    mixer.music.play()          # Обычное одиночное воспроизведение
                    
                e.control.text = "Остановить"
                is_playing = True
                current_active_screen = screen_num
            except Exception as ex:
                print(f"Ошибка воспроизведения файла {file_name}: {ex}")
        else:
            mixer.music.stop()  # Остановка звука внутри приложения
            e.control.text = default_text
            is_playing = False
            current_active_screen = None
        page.update()  # ИСПРАВЛЕНИЕ: Синхронный вызов, БЕЗ await

    # Синхронная функция отрисовки ГЛАВНОГО ЭКРАНА
    def show_main_screen(e=None):
        nonlocal is_playing, current_active_screen
        if is_playing:
            mixer.music.stop()
            is_playing = False 
            current_active_screen = None
            
        page.controls.clear()
        page.controls.extend([
            ft.Text(
                "Окружающий Мир рядом, даже если нет доступа к интернету!", 
                size=18, 
                weight="bold", 
                color="#FFFFFF",
                text_align=ft.TextAlign.CENTER
            ),
            ft.FilledButton("Волны Моря", on_click=lambda _: show_sub_screen(1), style=btn_style),
            ft.FilledButton("Лес", on_click=lambda _: show_sub_screen(2), style=btn_style),
            ft.FilledButton("Город", on_click=lambda _: show_sub_screen(3), style=btn_style),
            ft.FilledButton("Костёр ночью ", on_click=lambda _: show_sub_screen(4), style=btn_style),
            ft.FilledButton("Медитация", on_click=lambda _: show_sub_screen(5), style=btn_style),
            ft.Text(
                "Разработчик: company WebtestersCompany - https://profitest.h1n.ru", 
                size=9, 
                weight="bold", 
                color="#FFFFFF"
            )
        ])
        page.update()  # ИСПРАВЛЕНИЕ: Синхронный вызов, БЕЗ await

    # Синхронная функция отрисовки ДОПОЛНИТЕЛЬНЫХ ЭКРАНОВ
    def show_sub_screen(screen_num):
        nonlocal is_playing, current_active_screen
        page.controls.clear()
        
        if is_playing and current_active_screen != screen_num:
            mixer.music.stop()
            is_playing = False
            current_active_screen = None

        config = screen_audio_configs.get(screen_num)
        if config:
            _, _, screen_title, _ = config
        else:
            screen_title = f"Экран номер {screen_num}"
        
        screen_controls = [
            ft.Text(screen_title, size=18, weight="bold", color="#FFFFFF"),
            ft.FilledButton("На главный экран", on_click=lambda _: show_main_screen(), style=btn_style)
        ]
        
        if screen_num in screen_audio_configs:
            file_name, default_text, _, _ = screen_audio_configs[screen_num]
            current_btn_text = "Остановить" if (is_playing and current_active_screen == screen_num) else default_text
            
            audio_button = ft.FilledButton(
                current_btn_text,
                on_click=lambda e: toggle_audio(e, screen_num),
                style=btn_style
            )
            screen_controls.insert(1, audio_button)
            
        page.controls.extend(screen_controls)
        page.update()  # ИСПРАВЛЕНИЕ: Синхронный вызов, БЕЗ await

    show_main_screen()

# Используем классический запуск
ft.app(target=main)
