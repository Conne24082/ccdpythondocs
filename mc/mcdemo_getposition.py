
'''
load the minecraft modules
get the player's position and store to a varible
say variable in MC chat
'''

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat(pos)
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
mc.postToChat(pos)
mc.postToChat("Your X position is: " + str(pos.x))
mc.postToChat("Your Y position is: " + str(pos.y))
mc.postToChat("Your Z position is: " + str(pos.z))