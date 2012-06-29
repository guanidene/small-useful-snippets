# -*- coding: utf-8 -*-

"""
@author: Pushpak Dagade
@date: Thu Jun 21 14:26:06 2012

1. Trims extra newlines from beginning and end.
2. Replaces more than 1 whitespace characters(including tabs)
   by single whitespace
3. Removes common indentation, using textwrap.dedent
4. Adjusts output to the std. width of 79 characters (including indentation)
5. Copies the output to clipboard, so you can directly paste it wherever you
   want.
"""
import textwrap as tw
import pyperclip

###############################################################################
# customize this as you require
MY_DOCSTRING = """
These python snippets are made by me, using little or no
external api directly. This is different from my other project
named 'my-first-encounters' as in that one, I have snippets which demonstrate the use of some api.
"""
INDENT = ' '*0              # make it '' for no indentation or '#' for comments
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
