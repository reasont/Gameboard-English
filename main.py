import flet as ft

def main(page: ft.Page):
    page.title = "Gameboard Mobile"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#282828"

    txt_display = ft.Text("Aplicación iniciada correctamente", size=16, color="white")
    
    def probar_click(e):
        txt_display.value = "¡Botón presionado con éxito!"
        page.update()

    btn_test = ft.ElevatedButton("Probar interacción", on_click=probar_click)

    page.add(
        ft.Text("Estudio de Inglés", size=22, weight="bold", color="white"),
        txt_display,
        btn_test
    )

if name == "main":
    ft.app(target=main)
