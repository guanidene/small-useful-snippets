from numpy import *
from matplotlib.pyplot import figure as mpl_figure
from matplotlib import rc as mpl_rc

"""
This is a customizable template file for plotting using matplotlib.
It removes small annoyances of matplotlib and generates perfect images (at 
specified location).
Currently it does the following - 
1. Creates images with large font sized titles, labels, x/y ticks, etc. (so 
   that there are no issues when inserting the image in a report/pdf)
2. Removes extra annoying white space around saved figures
3. You can easily customize as per your needs the plots, titles, labels,
   figure size, figure dpi, figure save location.
"""

# pythonic stuff
fig = mpl_figure()
plt = fig.add_subplot(111)

############################### CUSTOMIZE THIS AS REQ #########################

# x-axis/y-axis labels, titles, etc.
xlabel = 'Vgs (V)'
ylabel = 'Ids (mA)'
title = 'I-V plot of mosfet'
output_file = "/home/home/IITD/Sem9/iec-lab/assignments/1/submission/latex/images/nmos1.png" # location for saving img file
figsize = (30.0, 14.0)    # figure size as (width, height) in inches
dpi = 150
# make your plots here
a = arange(1,10, 0.01)
plt.plot(a, sin(a), label = 'asd')
plt.plot(a, cos(a), label = 'asd2')

###############################################################################

# plotting stuff
fig.set_size_inches(figsize)
font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 44}
mpl_rc('font', **font)
plt.set_xlabel(xlabel)
plt.set_ylabel(ylabel)
plt.set_title(title)
plt.legend()
plt.grid(True)
fig.savefig(output_file, dpi=dpi, bbox_inches='tight')
