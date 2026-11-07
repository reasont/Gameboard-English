import flet as ft

def main(page: ft.Page):
    page.title = "Gameboard Mobile"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#282828"

    txt_display = ft.Text("Presiona el botón para cargar oraciones", size=18, color="white")
    audio_player = ft.Audio()
    page.overlay.append(audio_player)

    def procesar_archivo(e: ft.FilePickerResultEvent):
        if e.files and e.files[0].path:
            try:
                with open(e.files[0].path, "r", encoding="utf-8") as f:
                    contenido = f.read()
                txt_display.value = f"Archivo cargado:\n{contenido[:200]}..."
            except Exception as ex:
                txt_display.value = "Error al leer el archivo"
            page.update()

    file_picker = ft.FilePicker(on_result=procesar_archivo)
    page.overlay.append(file_picker)

    def hablar_texto(e):
        texto = "Hello, welcome to your English study app."
        url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={texto.replace(' ', '%20')}&tl=en&client=tw-ob"
        audio_player.src = url
        audio_player.play()

    btn_cargar = ft.ElevatedButton("📂 Cargar TXT", on_click=lambda _: file_picker.pick_files(allowed_extensions=["txt"]))
    btn_hablar = ft.ElevatedButton("🔊 Escuchar", on_click=hablar_texto)

    page.add(
        ft.Text("Estudio de Inglés", size=24, weight="bold", color="white"),
        txt_display,
        btn_cargar,
        btn_hablar
    )

if name == "main":
    ft.app(target=main)
