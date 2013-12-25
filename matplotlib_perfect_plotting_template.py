from numpy import *
from matplotlib.pyplot import figure as mpl_figure, show as fig_show
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

# matplotlib stuff
fig = mpl_figure(figsize=(30.0, 10.0))
plt = fig.add_subplot(111)
mpl_rc('lines', **{"linewidth": 2.0})   # plot lines with default linewidth 5
font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 20}
mpl_rc('font', **font)

############################### CUSTOMIZE THIS AS REQ #########################

# x-axis/y-axis labels, titles, etc.
xlabel = 'Vgs (V)'
ylabel = 'log10( Ids (mA) )'
title = ''
path_csv = '/home/home/IITD/Sem9/iec-lab/assignments/1/submission/csv/nmos-2-1.csv'
output_file = "/home/home/IITD/Sem9/iec-lab/assignments/1/submission/latex/images/nmos-2-1.png" # location for saving img file
figsize = (30.0, 10.0) # XXX. not working    # figure size as (width, height) in inches
dpi = 150
compile_pdf = False
#compile_pdf = True

# make your plots here
x, i1, i2, i3, i4 = loadtxt(path_csv, delimiter=',',
                            usecols=(0, 1, 2, 3, 4), unpack=True, skiprows=1)
plt.plot(x, log10(-i1), label = 'Vds = 1.2V')
plt.plot(x, log10(-i3), label = 'Vds = 1.0V')
plt.plot(x, log10(-i4), label = 'Vds = 0.8V')
plt.plot(x, log10(-i2), label = 'Vds = 0.5V')

# get the slopes
#print 1/(diff(log10(-i1))[32]) for vds = 1.2
#print 1/(diff(log10(-i2))[33]) for vds = 0.5
###############################################################################

# plotting stuff
#fig.set_size_inches(figsize) # XXX. not working
plt.set_xlabel(xlabel)
plt.set_ylabel(ylabel)
plt.set_title(title)
plt.legend(loc=4)
#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=10,
#       ncol=2, mode="expand", borderaxespad=0.)
plt.grid(True)
fig_show()
fig.savefig(output_file, dpi=dpi, bbox_inches='tight')

# compile latex to pdf!
if compile_pdf == True:
    from subprocess import check_output
    print check_output('cd /home/home/IITD/Sem9/iec-lab/assignments/1/submission/latex/; bash pdflatex.sh', shell=True)
