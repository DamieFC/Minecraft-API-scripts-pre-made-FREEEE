from mcpi import minecraft
mc.Minecraft.createWorld() #I think that's how you do it?
mc.postToChat("Creating cube...")
mc.setBlocks(-4, -4, -4, 4, 4, 4, block.STONE.id)
mc.postToChat("Creating air...")
mc.setBlocks(-2, -2, -2, 2, 2, 2, block.AIR.id)
