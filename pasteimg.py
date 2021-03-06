#!/usr/bin/python -u
# -*- coding: utf-8 -*-

# author: 'पुष्पक दगड़े (Pushpak Dagade) <guanidene@gmail.com>'
# date: 'Mon Jun 24 21:55:06 2013 (XXX. correct it)'
# version: '1.0.0 (XXX. correct it)'

"""
Easily save image in clipboard to file.

This code is originally copied from
https://github.com/cas--/PasteImg/blob/master/pasteimg

Some minor changes are done by me -
1. notifies user using notify-osd (ubuntu)
2. copies full path of saved file to clipboard, so that user can add it
   wherever req.
"""

import gtk
import os
import sys
import random
import argparse

from os.path import basename, join
from pynotify import notify
import pyperclip
default_img_save_folder_path = '/home/pushpak/Downloads'


class PasteImg:

    # Removed 'ico' from list until can catch size error
    imgTypeSet = ['png', 'bmp', 'jpg', 'jpeg', 'tiff']

    def __init__(self):

        parser = argparse.ArgumentParser(
            description='PasteImg: Output clipboard to file')
        parser.add_argument('filename', nargs='?', default='',
                            help='filename to use')
        parser.add_argument('-v', '--version', action='version',
                            version='%(prog)s 0.2')

        args = parser.parse_args()
        filename = args.filename

        clipb = gtk.clipboard_get()
        clipb.request_image(self.callback_img, filename)

    def callback_img(self, clipboard, pixbuf, filename):

        if filename == '':
            filename = ''.join(random.choice('0123456789abcdef')
                       for i in range(12))

         # Split filename suffix
        (shortname, extension) = os.path.splitext(filename)
        fileExt = extension.replace('.', '')

        # Default to png
        imgType = "png"

        if fileExt in self.imgTypeSet:
            # pixbuf only recongnises 'jpeg' as type
            if fileExt == 'jpg':
                fileExt = 'jpeg'
            imgType = fileExt
        elif fileExt == "":
            fileExt = imgType
        else:
            # Wrong extension
            notify("Error: Unknown file extension '%s'" % extension,
                   basename(__file__), 'error')
            sys.exit()

        # Save clipboard image to file
        if pixbuf is None:
            notify('No image in clipboard to save!',
                   basename(__file__), 'dialog-warning')
        else:
            try:
                fullpath = join(default_img_save_folder_path,
                                '%s.%s' % (filename, imgType))
                pixbuf.save(fullpath, imgType)
                notify(title='Saved clipboard image to file',
                       message='File name: %s.%s \nFolder: %s \n\n'
                               '[Path copied to clipboard]'
                       % (shortname, fileExt, default_img_save_folder_path),
                       icon='info')

                # copy full path of image saved to clipboard
                pyperclip.copy(fullpath)
            except Exception as ex:
                notify('Error occured while saving clipboard image to file: %s'
                       % ex, basename(__file__), 'error')

        self.exitPasteImg()

    def exitPasteImg(self):
        gtk.main_quit()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    pimg = PasteImg()
    pimg.main()
