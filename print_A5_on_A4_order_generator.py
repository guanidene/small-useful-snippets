#!/usr/bin/python -u
# -*- coding: utf-8 -*-
"""
(This should have been a feature in the print dialog of applications like
Okular or Acrobat Reader, but I think, there isn't.

What I intent to do can be best explained with an example. Suppose I wish to
print A5 sized pages, from say, numbers 1-12. But I have a A4 printer. So, I
print 2 pages per sheet, back-&-forth on the A4 page. Later, I wish to cut
these pages from the middle of the longer side of the A4 sheet, and simply put
the now RHS stack of A5 sheets below the last page of LHS stack of now A5
sheets to create a "handbook" or "pocket reference" book of A5 sized pages. So,
now the order in which you print the pages matter. If you print sequentially,
ie as it is in-order, you won't get what you expect when you cut all the sheets
into 2 and put the RHS stack of A5 sheets below the last page of the LHS stack
of A4 sheets (think why; infact, try to print 4 pages on 1 A4 paper, both
sides, and then cut into 2 and see if you got what you wanted - you won't get
it!)


So, this script generates the order in which pages should be printed so that
you can immediately "get" a handbook by cutting the stack of A4 sheets from
middle. After you cut the stack, put the entire RHS stack of now A5 sheets
below the last A5 sized page of the LHS stack of A5 sized sheets.
"""

__author__ = 'पुष्पक दगड़े (Pushpak Dagade) <guanidene@gmail.com>'
__date__ = 'Wed Dec 12 12:14:27 2012 (note the date!)'
__version__ = '1.0.0'

#pylint: disable-msg=R0903,C0103

from argparse import ArgumentParser, RawDescriptionHelpFormatter
from math import ceil
from os.path import basename
from sys import stderr
from textwrap import dedent


def gen_order(list_page_nos, blank_page_no=-1):
    """
    The function containing algorithm for generating page numbers in required
    order.

    'blank_page_no' is required when (last-page - first_page_no + 1) is not
    divisible by 4, ie to fill up empty pages in between two non empty pages
    which can occur at the end.
    """
    list_page_nos = sorted(list_page_nos)
    first_page_index = 0
    last_page_index = len(list_page_nos) - 1
    shift = (first_page_index - 1)      # shift = -1; just for clearity

    # index for LHS pages
    j = first_page_index - shift

    # index for RHS pages
    k = k_initial = int(ceil(len(list_page_nos) / 4.0)) * 2 + 1

    while (j < k_initial):
        yield list_page_nos[j + shift]         # page #1
        # page #3
        yield list_page_nos[k + shift] if \
          k + shift <= last_page_index else blank_page_no
        # page #4
        yield list_page_nos[k + 1 + shift] if \
          k + 1 + shift <= last_page_index else blank_page_no
        # page #2
        yield list_page_nos[j + 1 + shift] if \
          j + 1 + shift <= last_page_index else blank_page_no
        j += 2
        k += 2


def parse_input_arguments():
    """
    Creates parser and parses the input arguments. Returns parsed arguments if
    they are in correct format, else displays error message and exits.

    XXX. not fully documented

    XXX. '--help' argument does not show help, but gives out an exception,
    somehow due to the variable argument 'pagenoset'.
    Try to fix it.
    """

    # create the documentation for the parser
    program_name = basename(__file__)
    about = dedent("""\nABOUT
    Author: %s
    Date: %s
    Version: %s
    """ % (__author__, __date__, __version__))
    description_main = dedent("""\
    """)
    help_listpageno = """
    Ex:
        #1
        $ %s 100        # only page no 100

        #2
        $ %s 1-100      # page no set from 1 to 100

        #3
        $ %s 4-7 10-11      # can separate 2 sets of pages by space

        #4
        $ %s 4-7, 10-11      # can separate 2 sets of pages by comma

        #5
        $ %s 10-11 4-7      # 2 sets of page no. need be in ascending order
    """

    help_blankpageno = """
    XXX. undocumented
    """
    # create the top level parser
    parser = ArgumentParser(epilog=__doc__ + about,
                            description=description_main,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('--version', action='version',
                        version="%s %s" % (program_name, __version__))
    parser.add_argument('--blankpageno', '-b', action='store', default=-1,
                        help=help_blankpageno)
    parser.add_argument('pagenoset', action='store', nargs='+',
                        help=help_listpageno)
    return parser.parse_args()


def generate_page_nos(list_pagenoset):
    """
    Generate list of integers from list of strings in list_pagenonset.

    Following examples show accepted type of pagenoset (ie element inside
    list_pagenoset)

    Ex:
        #1
        $ %s 100        # only page no 100

        #2
        $ %s 1-100      # page no set from 1 to 100

        #3
        $ %s 4-7 10-11      # can separate 2 sets of pages by space

        #5
        $ %s 10-11 4-7      # 2 sets of page no. need be in ascending order

    If some exception is caught while generating the list of integers,
    display exception and exit program
    """
    list_nos = []
    try:
        for pagenoset in list_pagenoset:
            if '-' in pagenoset:
                list_nos.extend(range(int(pagenoset.split('-')[0]),
                                      int(pagenoset.split('-')[1]) + 1))
            else:
                list_nos.append(int(pagenoset))
    except Exception as e:
        # stop program even if u get one error
        print str(e)
        raise SystemExit('Provide correct page no. set')

    return list_nos

if __name__ == '__main__':
    args = vars(parse_input_arguments())
    blank_page_no = int(args['blankpageno'])
    list_pagenoset = generate_page_nos(args['pagenoset'])
    order = [x for x in gen_order(list_pagenoset, blank_page_no)]
    nos = str(order)[1:-1]
    print nos, '\n'

    # try to copy nos to clipboard
    try:
        import pyperclip
        pyperclip.copy(nos)
        print '(Copied string to clipboard)'
    except Exception as e:
        print >> stderr, '(Could not copy to clipboard)'