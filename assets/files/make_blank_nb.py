'''
Copied liberally from the tool by Zach del Rosario, https://github.com/zdelrosario/jupyter-authoring
Enze Chen, 2021/04/25
'''
import sys
import nbformat
import re
from copy import deepcopy

# command line interface
if len(sys.argv) != 2:
    print('Usage: python sep.py [filename.ipynb]')
    sys.exit(1)
filename_orig = sys.argv[1]
filename_blank = f"{filename_orig.split('.')[0]}_blank.ipynb"


# load the notebook
nb_orig  = nbformat.read(filename_orig, as_version=4)
nb_blank = deepcopy(nb_orig)
nb_solu  = deepcopy(nb_orig)

for cell_id in range(len(nb_orig['cells'])):
    cell_orig = nb_orig['cells'][cell_id]
    text_blank = cell_orig['source']

    # process markdown and code cells
    if (cell_orig['cell_type'] == 'markdown') or 
       (cell_orig['cell_type'] == 'code'):
        text_blank = re.sub(
            '<!-- solution-begin -->(\n|.)*?<!-- solution-end -->\n?',
            '',
            text_blank
        )
        text_blank = re.sub(
            '# solution-begin(\n|.)*?# solution-end',
            '',
            text_blank
        )

    else:
        raise ValueError(f'Unrecognized cell type {cell_orig["cell_type"]}.')

    # write the results
    nb_blank['cells'][cell_id]["source"] = text_blank


# write blank notebook to file
nbformat.write(nb_blank, filename_blank)
print(f'{filename_orig} successfully scrubbed! Blank notebook created.')