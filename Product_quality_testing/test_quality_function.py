#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 23:58:28 2018

@author: hannaholdorf
"""

#%%

from quality_function import recalculate_quality, Product
    
def test_recalculate_potato():
    yucon = Product("potato",7)
    recalculate_quality(yucon)
    assert yucon.quality == 6.5
    
def test_recalculate_cheese():
    camembert = Product("cheese",5)
    recalculate_quality(camembert)
    assert camembert.quality == 3
    
def test_recalculate_veggie():
    cucumber = Product("veggie",1)
    recalculate_quality(cucumber)
    assert cucumber.quality == -2
    
def test_recalculate_meat():
    beef = Product("meat",1.5)
    recalculate_quality(beef)
    assert beef.quality == -1.5