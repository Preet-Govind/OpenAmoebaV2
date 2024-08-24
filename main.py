import pygame
from environment import AmoebaEnvironment

def run_simulation():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Amoeba Simulation")

    env = AmoebaEnvironment()
    env.generate_data()

    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))  # Clear the screen

        # The amoeba chooses an action based on the state
        env.amoeba.update(env.food_items, env.obstacles, env.toxic_zones)

        env.draw(screen)  # Draw everything in the environment

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

    # After the simulation, train the model
    env.train_model()

if __name__ == "__main__":
    run_simulation()
