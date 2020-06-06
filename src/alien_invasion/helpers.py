import os
import pygame


def load_image(image_file_name):
    current_dir = os.path.dirname(__file__)
    images_dir = f'{current_dir}/../images'
    image_path = os.path.join(images_dir, image_file_name)
    return pygame.image.load(image_path)
