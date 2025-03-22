import pygame
import os


def load_image(filename):
    """
    Carga una hoja de sprites desde la carpeta assets/images.
    :param filename: Nombre del archivo de la hoja de sprites
    (ejemplo: "main.png")
    :return: Surface con la imagen cargada
    """
    # Construir ruta absoluta desde la raíz del proyecto
    base_path = os.path.abspath(os.path.join(__file__, "../../.."))
    image_path = os.path.join(base_path, "assets", "images", filename)

    # Intentar cargar la hoja de sprites
    try:
        sprite_sheet = pygame.image.load(image_path)
        print(f"✅ Hoja de sprites '{filename}' cargada correctamente.")
        return sprite_sheet
    except FileNotFoundError:
        print(f"❌ No se encontró la hoja de sprites en: {image_path}")
        return None


# Extrae los frames de la hoja de sprites
def get_frames(sheet: pygame.Surface, frame_width, frame_height):
    frames = []
    for i in range(sheet.get_width() // frame_width):
        frame = sheet.subsurface((i * frame_width,
                                  0,
                                  frame_width,
                                  frame_height))
        frames.append(frame)
    return frames
