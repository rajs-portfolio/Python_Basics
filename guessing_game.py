import pygame, random

pygame.init()  # Initialize Pygame
screen = pygame.display.set_mode((600, 400))  # Create a window of 600x400 pixels
pygame.display.set_caption("Guess the Number")  # Set the window title

font = pygame.font.SysFont('Arial', 24)  # Set up font for text

def display_text(text, x, y):
    screen.blit(font.render(text, True, (255, 255, 255)), (x, y))  # Display white text

def guessing_game():
    number_to_guess = random.randint(1, 100)  # Random number to guess
    input_text = ""  # Store user's input as text
    feedback = ""  # Store feedback (Too low, Too high, etc.)
    attempts = 0  # Track the number of attempts
    game_over = False  # Flag to end the game

    while not game_over:
        screen.fill((0, 0, 0))  # Fill screen with black
        for event in pygame.event.get():  # Check for events like key presses
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Press enter to submit guess
                    try:
                        guess = int(input_text)  # Convert input text to an integer
                        attempts += 1
                        if guess == number_to_guess:
                            feedback = f"Correct! {attempts} attempts."
                            display_text(feedback, 200, 150)  # Show final feedback
                            pygame.display.update()  # Update the screen
                            pygame.time.wait(2000)  # Wait for 2 seconds to display the message
                            game_over = True
                        elif guess < number_to_guess:
                            feedback = "Too low!"
                        else:
                            feedback = "Too high!"
                        input_text = ""  # Clear input for a new guess
                    except ValueError:
                        feedback = "Enter a valid number."  # Error message for invalid input
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]  # Remove last character
                else:
                    input_text += event.unicode  # Append typed character

        # Display the game instructions and feedback
        display_text("Guess the number (1-100):", 200, 50)
        display_text(f"Your guess: {input_text}", 200, 100)
        display_text(feedback, 200, 150)  # Show feedback (Too low, Too high, etc.)
        pygame.display.update()  # Update the screen

guessing_game()  # Start the game
pygame.quit()  # Close Pygame
