#!/usr/bin/python -u
# -*- coding: utf-8 -*-
#
# author: 'पुष्पक दगड़े (Pushpak Dagade) <guanidene@gmail.com>'
# date: 'Thu Nov 21 14:16:59 2013'
# version: '1.0.0 (XXX. correct it)'

"""
Simple script to generate latex table from a table copied form a pdf

pdf_table should be the string returned by copying a table using okular
from the weste harris book
"""

def get_latex_table(pdf_table):
    """
    pdf_table should be the string returned by copying a table using okular
    from the weste harris book
    """

    #1
    temp = pdf_table.strip('\n').replace("\n ", " & ")

    #2
    temp2 = temp.split('\n')
    temp2[0] = ' & '.join([r'\textbf{%s}' % _ for _ in temp2[0].split(' & ')])
    temp2 = ['\hline ' + line + r" \\" for line in temp2]
    temp2.append('\hline')
    temp2.insert(1, '\hline')
    temp3 = '\n'.join(temp2)

    #3 find no. of columns
    no = len(temp2[-2].split('&'))
    col_string = '|l|' + 'c|'*(no-1)

    #4
    temp3 = "%s\n%s\n%s" % \
(r"""\begin{table}
\centering
\begin{tabular}{%s}""" %col_string,
temp3,
r"""\end{tabular}
\caption{XXX} \label{tab:XXX}
\end{table}"""
)

    return temp3


if __name__ == '__main__':
    pdf_table = """
B
 DV
 Ceff(A)
 MCF
Constant
 VDD
 Cgnd + Cadj
 1
Switching same direction as A
 0
 Cgnd
 0
Switching opposite to A
 2VDD
 Cgnd + 2Cadj
 2
"""

    print get_latex_table(pdf_table)