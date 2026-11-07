import flet as ft

def main(page: ft.Page):
    page.title = "Gameboard English"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#282828"

    txt_info = ft.Text("¡Aplicación lista y funcionando!", size=18, color="white")

    def click_boton(e):
        txt_info.value = "¡Botón presionado correctamente!"
        page.update()

    btn = ft.ElevatedButton("Probar interacción", on_click=click_boton)

    page.add(
        ft.Text("Estudio de Inglés", size=24, weight="bold", color="white"),
        txt_info,
        btn
    )

if name == "main":
    ft.app(target=main)
