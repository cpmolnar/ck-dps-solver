# Requirements
You need Python.  
When installing it, make sure you check "add to PATH".

To install Python dependencies, go to terminal navigate to  
project folder, and type: `pip install -r requirements.txt`

# Setup
I may improve this part if anyone finds interest in the code.
## Character Stats
Edit `dps_solver.py` with your editor software. Near the  
top, you can update with your skill levels and perk trees.  
You can also edit whether to search range or melee combat.

## Character DPS Settings
Edit `objects/Character.py`. Near the top, there is a  
settings block. Update with settings to your preference  
for DPS calculation. BIG ONE IS "PYRDRA DEFEATED", make  
note of this setting for non-lategame users.

## Items
Edit `items.py` to add or remove items to search.  
There are a lot of item examples in there, you need to copy  
the template. Obviously, new set bonuses need to be programmed  
by you.

# Run
Type `python dps_solver.py` in your terminal to run it
