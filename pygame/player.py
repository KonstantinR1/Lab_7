import pygame
import os

pygame.init()

# Set up the screen
screen = pygame.display.set_mode((400, 200))
pygame.display.set_caption("Music Player")

# Set up the clock
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Load some sample music files
music_folder = "music"  # Create a folder named "music" and place some music files inside
music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

# Initialize the music player
pygame.mixer.init()
current_track = 0
pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))

# Font for displaying track information
font = pygame.font.Font(None, 36)

# Main loop
running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play/Pause
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            elif event.key == pygame.K_s:  # Stop
                pygame.mixer.music.stop()
                paused = False
            elif event.key == pygame.K_n:  # Next track
                current_track = (current_track + 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:  # Previous track
                current_track = (current_track - 1) % len(music_files)
                pygame.mixer.music.load(os.path.join(music_folder, music_files[current_track]))
                pygame.mixer.music.play()

    # Display current track information
    track_info = f"Track: {music_files[current_track]}"
    text = font.render(track_info, True, BLACK)
    
    screen.fill(WHITE)
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()