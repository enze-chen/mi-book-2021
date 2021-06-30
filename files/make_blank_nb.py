'''
Copied liberally from the tool by Zach del Rosario, https://github.com/zdelrosario/jupyter-authoring
Enze Chen, 2021/06/06
'''
import os 
import sys
import nbformat
import re
from copy import deepcopy
from datetime import datetime

# command line interface
if len(sys.argv) != 2:
    print('Usage: python make_blank_nb.py [dirname]')
    sys.exit(1)
print(f'Starting cleaning at {datetime.now()}')
dirname = sys.argv[1]
files = os.listdir(dirname)
for f in files:
    if f.endswith('_master.ipynb'):

        # Process the master notebook file
        filename_orig = os.path.join(dirname, f)
        filename_blank = filename_orig.replace('master', 'blank')


        # load the notebook
        nb_orig  = nbformat.read(filename_orig, as_version=4)
        nb_blank = deepcopy(nb_orig)
        nb_solu  = deepcopy(nb_orig)

        for cell_id in range(len(nb_orig['cells'])):
            cell_orig = nb_orig['cells'][cell_id]
            text_blank = cell_orig['source']

            # process markdown and code cells
            if (cell_orig['cell_type'] == 'markdown') or (cell_orig['cell_type'] == 'code'):
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
        print(f"{filename_orig.split('/')[-1]} successfully scrubbed! Blank notebook created.")