# --- Manejador para examinar archivos del teléfono ---
    def procesar_archivo_seleccionado(e: ft.FilePickerResultEvent):
        if e.files:
            file_path = e.files[0].path
            try:
                nuevas_oraciones = []
                tema_actual = "General"
                with open(file_path, "r", encoding="utf-8") as f:
                    for linea in f:
                        linea = linea.strip()
                        if not linea: continue
                        if linea.startswith('===') and linea.endswith('==='):
                            tema_actual = linea.strip('= ').strip()
                        else:
                            nuevas_oraciones.append({'tema': tema_actual, 'texto': linea})
                
                if nuevas_oraciones:
                    nonlocal oraciones_data
                    oraciones_data = nuevas_oraciones
                    estado["indice"] = 0
                    cargar_oracion_actual()
                    lbl_mensaje.value = "¡Archivo cargado con éxito! 📂"
                    lbl_mensaje.color = "#4ECDC4"
                    page.update()
            except Exception as ex:
                lbl_mensaje.value = f"Error al leer archivo"
                lbl_mensaje.color = "#FF6B6B"
                page.update()

    file_picker = ft.FilePicker(on_result=procesar_archivo_seleccionado)
    page.overlay.append(file_picker)

    # Layout general
    page.add(
        ft.Row([lbl_titulo, lbl_contador], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
        lbl_tiempo,
        ft.Container(content=lbl_estructura, bgcolor="#1A237E", padding=10, border_radius=8),
        container_display,
        ft.Center(content=lbl_mensaje),
        grid_palabras,
        ft.Divider(height=15, color="transparent"),
        ft.Row([
            ft.ElevatedButton("📂 Abrir TXT", bgcolor="#5CB85C", color="white", on_click=lambda _: file_picker.pick_files(allowed_extensions=["txt"])),
            ft.ElevatedButton("🔊 Escuchar", bgcolor="#45B7D1", color="white", on_click=lambda _: hablar_oracion(estado["oracion_actual"]))
        ], alignment=ft.MainAxisAlignment.SPACE_AROUND),
        ft.Divider(height=10, color="transparent"),
        ft.Row([
            ft.ElevatedButton("Borrar", icon=ft.icons.BACKSPACE, bgcolor="#D9534F", color="white", on_click=borrar_ultima),
            ft.ElevatedButton("Siguiente →", bgcolor="#4ECDC4", color="#282828", on_click=siguiente_oracion)
        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN)
    )

    cargar_oracion_actual()

if name == "main":
    ft.app(target=main)
