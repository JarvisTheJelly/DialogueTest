#!/usr/bin/env python

"""A test in creating a dialogue engine.

In order to take a step towards creating more story driven games,
I have to create a system for dialogue. Inspired by old games
like Advance Wars for the GBA. The system will be able to take in a
string and format it properly so it fits the speech bubble. Even splitting
up the string if too long (although I think it would be better to
not make the strings that long in the first place).
"""

import pygame
import Handler
import DemoHandler

__author__ = "Nick Jarvis"
__copyright__ = "Nick Jarvis 2015"

#Will McGugan for creating vector2.py and util.py found in gametools
__credits__ = ["Nick Jarvis", "Will McGugan"]

__license__ = "GNU General Public License (GPL)"
__version__ = "0.0.0"
__maintainer__ = "Nick Jarvis"
__email__ = "najarvis2016@gmail.com"
__status__ = "Prototype"

def run():
    """The main function for the program.

    When called it will initialize the screen, as well as the main handler.
    The main loop will run from in here, and the main handler will update
    itself and everything else.
    TL;DR - main function that starts the program.
    """

    #Initialize the needed modules (Obviously font will be needed).
    pygame.init()
    pygame.font.init()

    #Initialize the screen and create a variable for the screen_size.
    screen_size = (800, 640)
    screen = pygame.display.set_mode(screen_size)

    #Initialize the game engine
    game_engine = Handler.Handler()

    #Initialize the demo handler
    demo_handler = DemoHandler.DemoHandler(game_engine)

    #Set up the demo
    demo_handler.set_up_demo()

    #A boolean value to handle the main game loop.
    done = False
    while not done:

        #Update the world below here but above rendering
        done = game_engine.update()

        #Render everything below here
        screen.fill((0, 0, 0))
        game_engine.render(screen)

        pygame.display.flip()

    #de-initialize everything below here
    game_engine.destroy()
    pygame.quit()

if __name__ == "__main__":
    run()
