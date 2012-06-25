# -*- coding: utf-8 -*-

"""
@author: Pushpak Dagade
@date: Thu Jun 21 14:26:06 2012

1. Trims extra newlines from beginning and end.
2. Replaces more than 1 whitespace characters(including tabs)
   by single whitespace
3. Removes common indentation, using textwrap.dedent
4. Adjusts output to the std. width of 79 characters (including indentation)
"""
import textwrap as tw
import pyperclip

###############################################################################
# customize this as you require
MY_DOCSTRING = """
    The view whose config spec. would be modified temporarily as
    per the config file gives as input. Note that you need to first yourself
    set the view. Also, note that the config spec would be modified
    temporarily, so it might disturb your working in other areas where you are
    using this view while this script is running. This script would restore the
    original config spec at the end of its execution. See the note -
    'RESTRICTION WITH THE USE OF CLEARCASE VIEW' - below."""
INDENT = ' '*4              # make it '' for no indentation or '#' for comments
SUBSEQUENT_INDENT = INDENT
###############################################################################

# the actual 1 line code!
MY_DOCSTRING = tw.fill(tw.dedent(' '.join(MY_DOCSTRING.split())), width=79,
                       drop_whitespace=True, initial_indent=INDENT,
                       subsequent_indent=SUBSEQUENT_INDENT)

# copies the entire output to clipboard, so you can paste it directly.
# It also prints MY_DOCSTRING so that you can verify that it is formatted the
# way you wanted it to be.
pyperclip.copy(MY_DOCSTRING)
print MY_DOCSTRING,
