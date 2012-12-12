#!/usr/bin/python -u
# -*- coding: utf-8 -*-

"""
A print function, which prints (notifies) using notify-osd linux daemon
"""

__author__ = 'पुष्पक दगड़े (Pushpak Dagade) <guanidene@gmail.com>'
__date__ = 'Fri Oct 19 12:15:37 2012'
__version__ = '1.0.0'

from subprocess import check_output, CalledProcessError

def print_notify(title, message):
    try:
        check_output(['notify-send', title, message, '-i info'])
    except CalledProcessError as ex:
        check_output(['notify-send', '[notify-send] Failed to send output',
                      ex.output, '-i','error'])