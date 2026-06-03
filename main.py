import flet as ft

def main(page: ft.Page):
    page.title = "Web Testers Company 2026"
    page.bgcolor = "#222222"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    
    # Стилизация поля ввода: добавляем белый цвет текста и рамки
    name_input = ft.TextField(
        label=" Давайте познакомимся! Напишите Ваше имя", 
        width=300,
        color="#FFFFFF",
        label_style=ft.TextStyle(color="#AAAAAA"),
        focused_border_color="#007BFF"
    )
    
    # Белый цвет для текста результата
    result_text = ft.Text("", size=14, color="#FFFFFF")
    
    def on_click(e):
        if name_input.value:
            result_text.value = f"Привет, {name_input.value}! Рады нашему знакомству!"
        else:
            result_text.value = "Пожалуйста, введите имя"
        page.update()
    
    page.add(
        # Белый цвет для главного заголовка
        ft.Text("Компания Web Testers Company приветствует Вас!", size=18, weight="bold", color="#FFFFFF"),
        name_input,
        # Стилизация кнопки: синий фон и белый текст
        ft.ElevatedButton(
            "Сказать привет", 
            on_click=on_click,
            style=ft.ButtonStyle(
                color="#FFFFFF",
                bgcolor="#007BFF"
            )
        ),
        result_text
    )

ft.app(target=main)
