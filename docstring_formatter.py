# -*- coding: utf-8 -*-

"""
@author: Pushpak Dagade
@date: Thu Jun 21 14:26:06 2012

1. Trims extra newlines from beginning and end.
2. Replaces more than 1 whitespace characters(including tabs)
   by single whitespace
3. Removes common indentation, using textwrap.dedent
4. Adjusts output to the standard width of 79 characters (including indentation)
"""
import textwrap as tw

# customize this as you require
MY_DOCSTRING = """

"""
INDENT = ' '*4			# make it ' '*0 for no indentation


# the actual 1 line code!
MY_DOCSTRING = tw.fill(tw.dedent(' '.join(MY_DOCSTRING.split())), width=79,
                       drop_whitespace=True, initial_indent=INDENT,
                       subsequent_indent=INDENT)
print MY_DOCSTRING