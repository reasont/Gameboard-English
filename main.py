import flet as ft
import traceback

def main(page: ft.Page):
    page.title = "Diagnóstico de Error"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#1e1e1e"

    error_text = ft.Text("Cargando aplicación...", color="white", size=14)

    page.add(
        ft.Text("Consola de Depuración", size=20, weight="bold", color="yellow"),
        error_text
    )

    try:
        # Verificamos que el entorno responda correctamente
        error_text.value = "¡Inicialización exitosa! El motor de Python y Flet funcionan correctamente."
        page.update()
        
    except Exception as ex:
        tb_str = traceback.format_exc()
        error_text.value = f"ERROR DETECTADO:\n{tb_str}"
        error_text.color = "red"
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
