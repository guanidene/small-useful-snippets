from os import walk
from os.path import join
from os import sep
#from pprint import pprint


# XXX. rename the function arguments. They don't reflect what they actual are
# Ex: ignore_folder_contents (see the docstring for what it does.)
def generate_hierarchy(orig_root, ignore_folder_contents = [],
                       ignore_files = [], sorted=False):
    """
    Generates a sorted list of strings representing the folder hierarchy
    in the folder orig_root.

    ignore_folder_contents --> list containing folder names whose contents should not printed. The folder name (in this list) would be printed.

    XXX.
    You can add an option of "filter_pattern" to ignore out files/folders
    matching the given pattern.

    XXX. some problem -
    does not list bitwise_dsp folder in the output
    """
    hierarchy = []
    for root, dirs, files in walk(orig_root):
        for dir in dirs:
            path = join(root, dir)
            hierarchy.append(('DIR', path[len(orig_root):].replace(sep, ',')))
            if dir in ignore_folder_contents: dirs.remove(dir)
        for file in files:
            path = join(root, file)
            hierarchy.append(('FILE', path[len(orig_root):].replace(sep, ',')))
    if sorted:
        return sorted(hierarchy)
    else:
        return hierarchy

a = (generate_hierarchy(r'C:\Documents and Settings\x0183507\My Documents\spyder workspace\Copy of omap_autogen',
     ['omap4430']))

for item in a: print item