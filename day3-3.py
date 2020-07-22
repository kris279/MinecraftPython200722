# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 11:01:38 2020

@author: user
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    hits=mc.events.pollProjectileHits()
    print(hits)
    if len(hits) > 0 :
        hit = hits[0]
        x,y,z =hit.pos.x,hit.pos.y,hit.pos.z
        block =mc.getBlock(x,y,z)
        mc.createExplosion(x,y,z,power=10)