# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 10:37:13 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random,time

pos =mc.player.getPos()
while True:
    x=pos.x+random.uniform(-20,20)
    y=pos.y+30
    z=pos.z+random.uniform(-20,20)
    mc.spawnEntity(x,y,z,264)
    time.sleep(0.2)

