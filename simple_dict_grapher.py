# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 15:01:40 2012
@author: Pushpak Dagade

This can be added as a magin function in ipython to interactively plot
any dictionary object.
"""

###############################################################################

import networkx as nx
import matplotlib.pyplot as plt

def draw_dict(mydict, name='mydict'):
    def __draw_dict(_dict, parent):
        for k, v in _dict.iteritems():
            if isinstance(v, dict):
                G.add_edge(k, parent, weight=len(str(k)))
                __draw_dict(v, k)
            else:
                pass
                #G.add_edge('%s_%s:%s' %(parent, str(k),str(v)) , parent)

    G = nx.DiGraph()
    __draw_dict(mydict, name)
    nx.draw(G, pos=nx.spring_layout(G), node_size=5000, width=0.5,
                     alpha=0.5, node_shape='s', style='dotted',
                     font_color='g')
    plt.show()

###############################################################################

voltage_domains={
    'bandgap': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_core_m': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_iva_abb': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_iva_m': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_mpu_abb': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_mpu_m': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d8',
        'type': 'voltage_converter'},
    'ldo_wakeup': {
        'avs': False,
        'controlled': True,
        'parent': 'vdds_1d2',
        'type': 'voltage_converter'},
    'vdd_core_l': {
        'avs': True,
        'controlled': True,
        'parent': '',
        'type': 'external'},
    'vdd_dac': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdd_iva_l': {
        'avs': True,
        'controlled': True,
        'parent': '',
        'type': 'external'},
    'vdd_mpu_l': {
        'avs': True,
        'controlled': True,
        'parent': '',
        'type': 'external'},
    'vdd_pll': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_1d2': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_1d8': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_csi': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_ddr': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_dsi': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_mmc': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_sim': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'},
    'vdds_unipro': {
        'avs': False,
        'controlled': False,
        'parent': '',
        'type': 'external'}}

draw_dict(voltage_domains, name='voltage_domains')