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
$ cd src
$ python3 -m venv .venv
$ source .venv/bin/activate
# Recent versions of Mac OS X requires PyGame 2
$ (.venv) pip install -r requirements.txt
$ (.venv) python alien_invasion/app.py
```

## Tests and Cod
```sh
$ (.venv) python -m unittest discover ./src
```

To run the tests with code coverage report, execute the following commands
```sh
$ (.venv) pip install coverage
$ (.venv) coverage run --source=./src/alien_invasion -m unittest discover ./src
$ (.venv) coverage html
```
And open `./htmlcov/index.html` on browser to see the code coverage report

## TODO
- [ ] Difficulty levels: let the player choose the difficulty level, change game tempo and scoring based on that