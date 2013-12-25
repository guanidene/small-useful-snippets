#!/usr/bin/python -u
# -*- coding: utf-8 -*-

"""
A simple pythonic interface to the commandline utility 'notify-send'.
"""

__author__ = 'पुष्पक दगड़े (Pushpak Dagade) <guanidene@gmail.com>'
__date__ = 'Fri Oct 19 12:15:37 2012'
__version__ = '1.0.0'

from os.path import basename
from subprocess import check_output, CalledProcessError


def notify(message='', title=basename(__file__), icon='info'):
    """
    title: Title of notification
    message: Message of notification
    icon: icon to be used (ex: info, error, dialog-warning, etc.).
          It can be name of any icon file present in /usr/share/icons.
          Best place to find icons: /usr/share/icons/Faenza/

    For exact usage of the cmdline utility 'notify-send', refer to its man page
    """
    try:
        check_output(['notify-send', title, message, '-i', icon])
    except CalledProcessError as ex:
        check_output(['notify-send', '[notify.py] Failed to send output',
                      ex.output, '-i', 'error'])

if __name__ == '__main__':
    notify('sadad', 'erqwe', 'info')
    notify('sadad', 'erqwe', 'dialog-info')
    notify('sadad', 'erqwe', 'error')
    notify('sadad', 'erqwe', 'dialog-error')
    notify('sadad', 'erqwe', 'dialog-warning')
    notify('sadad', 'erqwe', 'warning')
