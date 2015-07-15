"""Class for loading images quickly"""

import pygame


class ImageLoader(object):
    """Class for loading a single image or multiple images quickly.

    Class for loading images quickly and cleanly.
    """

    def __init__(self):
        """Does nothing"""

        pass

    def load_image(self, image_name, colorkey=(255, 0, 255)):
        """Loads a single image from the image name.

        Arguments:
            image_name - the filename of the image (without res or extension)
            colorkey - the color used to colorkey the image

        Surrounds image_name in "res/" and ".png" and loads it.

        Automatically colorkey's.

        Returns the loaded image.
        """

        filename = "res/" + image_name + ".png"
        return_image = pygame.image.load(filename).convert()
        return_image.set_colorkey(colorkey)

        return return_image

    def load_images(self, image_names, colorkey=(255, 0, 255)):
        """Loads and returns multiple images in a list.

        Arguments:
            image_names - list of filenames of images
            colorkey - the color used to colorkey images

        uses the load_image function multiple times and returns list of images
        """

        return_images = []
        for name in image_names:
            return_images.append(self.load_image(name, colorkey))

        return return_images
