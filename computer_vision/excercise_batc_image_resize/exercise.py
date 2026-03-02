import os
import cv2
import glob


def resize_images_in_folder(folder_path):
    """Resizes all images in the specified folder to 100x100 pixels and saves them with a new name.

    Args:        folder_path (str): The path to the folder containing the images to be resized.
    Returns:        None
    """

    images = []
    if not os.path.exists(folder_path):
        print("Folder does not exist")
        return

    images = glob.glob(os.path.join(folder_path, "*.jpg"))
    if not images:
        print("Foldr is empty.")
        return

    for image in images:
        img = cv2.imread(image, cv2.IMREAD_UNCHANGED)
        resized_img = cv2.resize(img, (100,100))
        cv2.imwrite(os.path.join(folder_path, f"resized2_{os.path.basename(image)}.jpg"), resized_img)

    if __name__ == "__main__":
        folder_path = "sample_images"
        resize_images_in_folder(folder_path)
