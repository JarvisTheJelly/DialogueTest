"""Main game handler / the engine. Description in the class Doctring."""

import pygame


class Handler(object):
    """The big and most important class. Handles everything.

    This class will handle everything. Entities moving, updating, rendering,
    initialization, and destruction. The game clock, dialogue, game states.
    Basically this class is the game engine.
    """

    def __init__(self):
        """Initializes the game handler.

        Initializes the handler (engine) and all of the variables. Will
        not specifically create entities, as this needs to be as open and
        reusable as possible.
        """

        self.clock = pygame.time.Clock()
        self.game_fps = 60.0

        self.entities = []
        self.to_remove = []

    def update(self):
        """Updates the engine and everything in it.

        Loops through and updates every entity, as well as the game clock.
        """

        self.clock.tick(self.game_fps)

        for entity in self.entities:
            entity.update()

    def render(self, surface):
        """Renders everything

        Renders everyting in the engine to the provided surface. In most
        cases it should be the main python screen.
        """

        for entity in self.entities:
            entity.render(surface)

    def add_entity(self, entity):
        """appends the entity to the entity list."""

        self.entities.append(entity)

    def remove_entity(self, entity):
        """Adds an entity to the 'to remove' list which is dumped
        every update
        """

        self.to_remove.append(entity)

    def destroy(self):
        """De-initializes all the variables and entities

        Never written someting like this, not sure if it is redundant
        and handled automatically but I figured I would write one anyways.
        """

        del self.entities[:]
        del self #Not sure if this works.
