# Bokemon Blatinum by CornInCantonesePlusNuts

## Roles
- Yaying Liang Li: Frontend, Backend

## Demo
Youtube Link: [Bokemon Blatinum](https://www.youtube.com/watch?v=4aOc4HC5nK8&ab_channel=YayaLiangLi)

## Description
&nbsp; Wanting to play a Pokemon adventure game but too broke to buy a DS? Thinking that the newer Pokemon games have lost their classic charm? Thinking that Sinnoh is the best region? (The _only_ correct opinion) <br>
    
&nbsp; Well, introducing Bokemon Blatinum! Team CornInCantonesePlusNuts brings the classic Pokemon Platinum game into a bootleg Pygame version. Experience choosing your very own starter Pokemon (Chimchar, Piplup, and Turtwig) and having your rival choose his Pokemon according to your choice. Roam the bushy, wild Sinnoh grass, and avoid getting glitched out of the cage of trees. Stop and admire the flowers (but not for too long, or else your rival's Pokemon will come after you). Beat your rival's Pokemon to a pulp for trying to ambush you. <br>
    
&nbsp; Our world knows no bounds (except for the trees). Come join us for a world of fun and adventure!

## Launch Code
- Clone the Repository <br>
```$ git clone https://github.com/yayeetying/Platinum.git``` <br>
- Move into Repository <br>
```$ cd Platinum/``` <br>
- Run the app <br>
```$ python3 main.py``` <br>

## Alternative Launch Code
- Clone the Repository <br>
```$ git clone https://github.com/yayeetying/Platinum.git``` <br>
- Move into Repository <br>
```$ cd Platinum/``` <br>
- Open main file
```$ code main.py``` <br>
- Run ```main.py``` by clicking on the triangle on the top-right corner of VSCode

## How to Play
After launching the game, you will be prompted to "Choose a Starter Pokemon!" Choose any of the three Pokemon (Chimchar, Piplup, Turtwig) by **mouse clicking** within the respective buttons. After initially playing the game, you may want to restart and click a different Starter Pokemon to see the changes. <br>

The next screen you will see is a screen of a grassy map. There are light and dark green trees (can't walk through those), dark and light water patches (also can't walk through those), and grass patches and flower patches (can walk through those). To move the player, use the **arrow keys**, which also triggers the player's walking animation. Walking through or standing on top of grass patches may trigger a Pokemon battle with your rival, Barry. <br>

Going into the **rival battle**, Barry will always choose a Pokemon that has a type super-effective against yours (ie. if you chose Chimchar, a fire type, Barry will choose Piplup, a water type). To engage in battle, choose one of the two moves your starter Pokemon knows by **mouse clicking** on the button. There are two types of moves: attacking moves (the first move) and debuffing moves (the second one). Attack moves lower the opponent's HP, or health points, and debuff moves lower a stat of the opposing Pokemon (ie. Attack or Defense). After clicking a move, it may seem like nothing has happened, but the program (and the terminal) keeps track of both sides' Pokemon HPs (along with other stats). Look in the terminal to see these stats ("Player" refers to the user, and "Opponent" refers to Barry.)
The player and Barry will exchange hits with their Pokemon until either Pokemon faints (HP drops to or below 0), in which case the user will be prompted back to the map area again. The winner of the battle can be determined by the statements printed in the terminal -- if Player's HP is less than or equal to 0, then the player has lost. <br>

Regardless of the outcome of the battle, the player is now sent back to the map area. This time, the player can freely roam the map and explore the fields (and glitches) without being ambushed by wild Pokemon. <br>

To quit the game (and perhaps try out a new Pokemon starter!), click the 'x' button on the top left corner of the app.

## Q & A
- Q: Oops! Looks like I ended up outside of the map/tree cage. What can I do? <br>
A: Not much. Either quit the program and restart, or try to glitch your way back into the map. If there's a hole out, there has to be a hole in. <br> <br>
- Q: Life is so hard when you're as popular as me. How can I stop having these Pokemon ambush me so quickly? <br>
A: As soon as you load into the game, try to run into a flower patch. Pokemon don't spawn there.<br><br>
- Q: I know it's winter, but I'm quirky so I like to swim in the water. Is there any way to do so? <br>
A: No, it's winter. <br><br>
- Q: I keep losing the rival battle!! How do I stop? <br>
A: ~~Get better.~~ Try different starter Pokemon. <br> <br>
- Q: Is there any way to level up our Pokemon? <br>
A: Not at the moment. <br>

