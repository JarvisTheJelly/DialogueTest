"""Creates stuff in the world to keep other files clean"""

import pygame
import Entity
import ImageLoader

class DemoHandler(object):
    """Class for creating and running the demo.
    
    Instead of manually calling and creating the entities in one of
    the other files, I want to keep those as open as possible. This
    will allow the game to be set up in a separate file and keep those
    clean.
    """

    def __init__(self, engine):
        """just initializes the demo handler, doesn't set up anything."""

        self.engine = engine
        self.image_loader = ImageLoader.ImageLoader()

    def set_up_demo(self):
        """Here is where the actual demo will be set up. 
        
        Scripting a specific level can all go in here, but in the future
        I want levels to be created in separate files (xml, txt, etc), 
        then loaded in to this function.
        """

        tank_image = self.image_loader.load_image("TankImage")
        tank_entity = Entity.Entity(self.engine, (20, 20), tank_image)
        self.engine.add_entity(tank_entity)
