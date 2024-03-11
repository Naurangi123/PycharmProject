import pygame
from pygame import mixer
pygame.init()

# Adjusted screen dimensions for a smaller screen
WIDTH = 800
HEIGHT = 600

# Adjusted button sizes
BUTTON_WIDTH = 120
BUTTON_HEIGHT = 50

# Adjusted font sizes
LABEL_FONT_SIZE = 20
MEDIUM_FONT_SIZE = 16

# Adjusted positions of elements
PLAY_PAUSE_POS = (20, HEIGHT - 100)
BPM_POS = (200, HEIGHT - 100)
# Adjust other elements accordingly

# Adjusted font paths
LABEL_FONT_PATH = 'Roboto-Bold'
MEDIUM_FONT_PATH = 'Roboto-Bold'

# Adjusted colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
DARK_GRAY = (50, 50, 50)
LIGHT_GRAY = (170, 170, 170)
BLUE = (0, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GOLD = (212, 175, 55)

# Adjusted sounds path
HI_HAT_SOUND_PATH = 'sounds/hi hat.wav'
SNARE_SOUND_PATH = 'sounds/snare.wav'
KICK_SOUND_PATH = 'sounds/kick.wav'
CRASH_SOUND_PATH = 'sounds/crash.wav'
CLAP_SOUND_PATH = 'sounds/clap.wav'
TOM_SOUND_PATH = 'sounds/tom.wav'

# Adjusted grid parameters
NUM_BEATS = 8
NUM_INSTRUMENTS = 6

# Initialize Pygame window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('The Beat Maker')

# Adjust font sizes
label_font = pygame.font.Font(LABEL_FONT_PATH, LABEL_FONT_SIZE)
medium_font = pygame.font.Font(MEDIUM_FONT_PATH, MEDIUM_FONT_SIZE)

# Adjusted button positions
play_pause = pygame.Rect(PLAY_PAUSE_POS[0], PLAY_PAUSE_POS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
bpm_rect = pygame.Rect(BPM_POS[0], BPM_POS[1], BUTTON_WIDTH, BUTTON_HEIGHT)
# Adjust other button positions accordingly

# Adjust other elements such as instrument rectangles, colors, etc.

# Rest of the code remains the same
pygame.display()