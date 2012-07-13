"""
(This should have been a feature in the print dialog of applications like
Okular or Acrobat Reader, but I think, there isn't.

What I intent to do can be best explained with an example.
Suppose I wish to print A5 sized pages from numbers 1-12.
But I have a A4 printer. So, I print 2 pages per sheet, back-&-forth.
Later, I wish to cut these pages from the middle of the longer side of the
A4 sheet, to create a "handbook" or "pocket reference" book of A5 sized pages.
So, now the order in which you print the pages matter. If you print
sequentially, ie as it is in-order, you won't get what you expect when you cut
all the sheets into 2 (think why; infact, try to print 4 pages on 1 A4 paper,
both sides, and then cut into 2 and see if you got what you wanted - you
won't get it!)

So, this script generates the order in which pages should be printed so that
you can immediately "get" a handbook by cutting the stack of A4 sheets from
middle. After you cut the stack, put the entire RHS stack of now A5 sheets
below the last A5 sized page of the LHS stack of A5 sized sheets.
"""

#pylint: disable-msg=R0903,C0103

from pyPdf import PdfFileReader, PdfFileWriter
from math import floor

def gen_order(last_page, first_page=1):

    # Note: It would be best to have last_page - first_page + 1 divisible by 4.
    # If it is not, you might have atmost 3 1-sided pages, with atmost one
    # wrongly ordered page.
    # XXX. fix this in algo itself, to handle such cases.

    i = first_page
    t = t_initial = int(floor(last_page/4.0))*4/2 + 1

    while (i < t_initial):
        yield i
        yield t
        yield t + 1
        yield i + 1
        i += 2
        t += 2

def create_new_pdf(input_pdf_file_path, output_pdf_file_path):
    input = PdfFileReader(file(input_pdf_file_path, "rb"))
    print input.isEncrypted
    input.decrypt('')
    output = PdfFileWriter()

    total_pages = input.getNumPages()
    print 'total pages - ', total_pages
    return

    for page in gen_order(last_page=total_pages): pass

    # finally, write "output" to output_pdf_file_path
    outputStream = file(output_pdf_file_path, "wb")
    output.write(outputStream)
    outputStream.close()

#create_new_pdf('a.pdf', 'b.pdf')
order = [x for x in gen_order(210)]
print order
