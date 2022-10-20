# !/usr/bin/env python3

# This super simple script was to automate including a bunchhh of images into a thesis

## EXAMPLE text to be generated 

# \begin{figure}[]
#     \centering
#     \includegraphics[scale=0.5]{PSUThesis/Appendix-C/Figures/1_1.jpg}
#     \caption{This will be changed, there are just too many images}
#     \label{}
# \end{figure}

import os


for root, dirs, files in os.walk("C:\\Users\\wnxgo\\Downloads\\Images-20221014T232158Z-001\\Images", topdown=False):
    for name in files: # walks through the given directory and prints the names of the files
        print(f"\n\\begin{{figure}}[h]\n\t\\includegraphics[width=1.0\\textwidth]{{PSUThesis/Appendix-C/Figures/{name}}}\n\t\\caption{{This will be changed, there are just too many images}}\n\t\\label{{{name}}}\n\\end{{figure}}")
    # for name in dirs:
        # print(os.path.join(root, name))