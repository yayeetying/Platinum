# Bokemon Blatinum by CornInCantonesePlusNuts

## Description
Team CornInCantonesePlusNuts brings the classic Pokemon Platinum game into a bootleg Pygame version.

## Overview
Bokemon Blatinum is a heavily Object Oriented app. I wanted to focus specifically on making reproducable code and avoiding hard coding. What I mean by my first point is that I didn't want to make new scenarios for every new Pokemon / Move / Tile that I had (ie. an 'if' statement for if the starter Pokemon was Chimchar, another 'if' statement for if the starter Pokemon was Piplup, etc.) I thought using Objects was a pretty good way that avoid this. I also tried to avoid including "magic" numbers in my code, and instead replacing them with variables when applicable.

## Explaining the Elements
### main.py
Main.py has the main loop and some helper functions. In my main loop, I basically want to populate certain variables, like the rival trainer and GAME_STATE, before going onto a forever loop until the game is quit. In that forever loop, I first check for user interaction, like mouse clicks and arrow key presses. I then look at the global variable GAME_STATE, which importantly dictates what "phase" of the game the user is on (are they choosing their starter Pokemon? Are they roaming the map? Are they battling their rival?), and call helper functions that help set up those phases. Helper functions like draw_choice() helps draw the choosing a starter Pokemon, draw_map() the drawing of the map, etc. map_state() and battle_state() basically deal with the interactivity of these phases; they animate the player according to the arrows pressed during the map phase, and keep track of moves dealt by Pokemon during the battle phase.

### tile.py
This Tile class keeps track of the x,y coordinates of the tile and the character it represents. For example, '#' represents a dark tree tile, '@' a light tree tile, '.' a grass tile, 's' a flower tile, and '3' a water tile. It also contains a collision function to detect if the player is touching the Tile.

### map.py
This Map class keeps track of a 2d array of Tile objects (I intended Map to be a class so that multiple maps could be made with more time). The Map class has a function that reads a txt file containing '#' '.' '@' etc. characters and converts these characters into Tiles, then storing all the Tiles in a grid. Map also has a function that "gives" the Tiles special properties (ie. if the Tile is a '#', or tree Tile, then don't allow the player to pass through it, etc.)

### pokemon.py
This file describes the Pokemon class. Every Pokemon has a name (str), types (array), stats (dict), moveset (array), image (str, path to image), and a level (int).

### battle_pokemon.py
This Battle_Pokemon class describes more specifically a Pokemon in the battle phase, so not only does it need the Pokemon it represents, it needs the x,y cords it stands at, and the width and length of the image to be drawn onto the screen.

### move.py
This Move class describes the moves that the Battle Pokemon can have. A Move object keeps track of the name of the move, the type of move it is (Attacking move? Self Buffing move? Opponent Debuffing move?), the attack power / buff factor of the move, the stat the buff or attack uses, and the Pokemon type of the move (Normal, Psychic, Water, Fire, Grass, etc. type). When the move executes itself, the calculates the damage done (taking into account the player's Pokemon's stats, the opponent's Pokemon's stats, the power of the move, and just some luck) and inflicts it on the opposing Pokemon.

### player.py
The Player class keeps track of the cartoon character's dimensions, walking speed, animation frames, x,y coordinates, and Pokemon they have. When the character moves (according to the arrow key presses), not only are the x,y coordinates updating, the animating frames are also cycling through. <br>
- Here's how the animation works:
The program keeps track of different frames of the character walking up, down, left, or right. When the user presses the 'up' arrow for example, the Player object remembers that direction and cycles through the frames for the 'walking up' animation motion. These frames are really just pictures that when looked at all together consecutively, look like an animation. The same process is done for the rest of the arrow keys.

### trainer.py
This Trainer class keeps track of the NPC trainers, including our rival Barry. I meant for this to be a class because I wanted more than 1 rival, but I unfortunately did not have enough time to get there. Much like the player, the Trainer NPC keeps track of their dimenseions, x,y cords, and Pokemon that they have. 