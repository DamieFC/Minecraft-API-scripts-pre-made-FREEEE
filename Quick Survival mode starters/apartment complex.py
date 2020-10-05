#this python script will build an apartment complex
from mcpi import minecraft
mc.Minecraft.createWorld()                        #I think that's how you do it?
mc.postToChat("Creating basic structure...")
mc.setBlocks(-4, -4, -4, 4, 4, 4, block.STONE.id)
mc.postToChat("Creating air inside so you don't have to carve it out from PURE STONE...")
mc.setBlocks(-2, -2, -2, 2, 2, 2, block.AIR.id)
mc.postToChat("Creating basic structure...")
mc.setBlocks(-4, -4, -4, 4, 4, 4, block.STONE.id)
mc.postToChat("Creating air inside so you don't have to carve it out from PURE STONE...")
mc.setBlocks(-2, -2, -2, 2, 2, 2, block.AIR.id)
mc.postToChat("All Done!")
mc.postToChat("All you have to do is carve out windows and doors")
#I think this script will make 2 houses on top of each other, or in the same place, and may freeze your computer/game. I would be careful of this, and if you can, please fix it. this is being done in a little time that I found, so I don't have time to look up a gazillion YouTube videos. Thanks!
#Credits to Mojang and Python.