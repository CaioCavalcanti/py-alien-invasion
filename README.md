# Alien Invasion
Alien Invasion is a 2D game inspired on the classic game Space Invaders and developed using Python and [PyGame](https://www.pygame.org/news).

This is one of the projects from the book [Python Crash Course: A Hands-On, Project-Based Introduction to Programming](https://www.amazon.com/Python-Crash-Course-Hands-Project-Based/dp/1593276036), by Eric Matthes ([@ehmatthes](https://twitter.com/ehmatthes/))

## How it works
- In Alien Invasion, the player controls a rocket ship that appears at the bottom center of the screen.
- The player can move the ship right and left using the arrow keys and shoot bullets using the spacebar.
- When the game begins, a fleet of aliens fills the sky and moves accross and down the screen.
- The player shoots and destroys the aliens.
- If the player shoots all the aliens, a new fleet appears that moves faster than the previous fleet.
- If any alien hits the player's ship or reaches the bottom of the screen, the player loses a ship.
- If the player loses three ships, the game ends.

## Running
```sh
# Recent versions of Mac OS X requires PyGame 2
$ python3 -m pip install -U pygame==2.0.0.dev6 --user
$ python3 src/alien_invasion/app.py
```

## Tests
```sh
$ python3 -m unittest discover ./src
```