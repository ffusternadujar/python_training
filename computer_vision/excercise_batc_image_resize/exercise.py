"""
EJERCICIO: REDIMENSIONADO DE IMÁGENES POR LOTES
===============================================

Este script redimensiona todas las imágenes .jpg de una carpeta especificada
a una resolución de 100x100 píxeles.

OBJETIVOS:
- Practicar el uso de OpenCV para procesamiento de imágenes.
- Utilizar glob para listar archivos.
- Manejar rutas de sistema de archivos.
EJECUCIÓN:
- Asegúrate de tener OpenCV instalado (`pip install opencv-python`).
- Coloca tus imágenes .jpg en la carpeta `sample_images`.
- Ejecuta el script y verifica que las imágenes redimensionadas se guarden.
"""
import os
import glob
import cv2


def resize_images_in_folder(folder_path):
    """Resizes all images in the specified folder to 100x100 pixels and saves them with a new name.

    Args:
        folder_path (str): The path to the folder containing the images to be resized.

    """

    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return

    images = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not images:
        print("Folder is empty.")
        return

    for image in images:
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        resized_img = cv2.resize(img, (100,100))
        cv2.imwrite(os.path.join(folder_path, f"resized2_{os.path.basename(image)}"), resized_img)


if __name__ == "__main__":
    SAMPLE_IMAGES_PATH = "sample_images"
    resize_images_in_folder(SAMPLE_IMAGES_PATH)
