# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 19:42:44 2012

@author: Pushpak Dagade
"""

# making cal graphs using pycallgraphs
from sys import path
from pycallgraph import start_trace, stop_trace, make_dot_graph

# append the module paths to be used
path.append('../omap_autogen')
path.append('../omap_autogen/omap4430/2.0')
path.append('../omap_autogen/omap4430/2.0/registers')

start_trace()
__import__('gen_all')
stop_trace()
make_dot_graph("callgraph_clean.png")