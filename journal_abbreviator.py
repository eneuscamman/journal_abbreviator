import sys
import os
import re
import string

##################################################################################################
#
# Usage:  python journal_abbreviator.py to_abbreviate.bib
#
# This will replace journal names with their abbreviations according to the list below.
#
##################################################################################################

replacements = [ ['The Journal of Chemical Physics' , 'J. Chem. Phys.'],
                 ['Journal of Chemical Physics' , 'J. Chem. Phys.'],
                 ['The Journal of Computational Chemistry' , 'J. Comput. Chem.'],
                 ['Journal of Computational Chemistry' , 'J. Comput. Chem.'],
                 ['Physical Chemistry Chemical Physics' , 'Phys. Chem. Chem. Phys.'],
                 ['The Journal of Computational Physics' , 'J. Comput. Phys.'],
                 ['Journal of Computational Physics' , 'J. Comput. Phys.'],
                 ['Proceedings of the National Academy of Sciences of the United States of America', 'Proc. Natl. Acad. Sci. USA'],
                 ['Proceedings of the National Academy of Sciences', 'Proc. Natl. Acad. Sci. USA'],
                 ['The International Journal of Quantum Chemistry' , 'Int. J. Quantum Chem.'],
                 ['International Journal of Quantum Chemistry' , 'Int. J. Quantum Chem.'],
                 ['The Journal of Physical Chemistry Letters' , 'J. Phys. Chem. Lett.'],
                 ['The Journal of Physical Chemistry A' , 'J. Phys. Chem. A'],
                 ['The Journal of Physical Chemistry B' , 'J. Phys. Chem. B'],
                 ['The Journal of Physical Chemistry C' , 'J. Phys. Chem. C'],
                 ['The Journal of Physical Chemistry' , 'J. Phys. Chem.'],
                 ['Journal of Physical Chemistry Letters' , 'J. Phys. Chem. Lett.'],
                 ['Journal of Physical Chemistry A' , 'J. Phys. Chem. A'],
                 ['Journal of Physical Chemistry B' , 'J. Phys. Chem. B'],
                 ['Journal of Physical Chemistry C' , 'J. Phys. Chem. C'],
                 ['Journal of Physical Chemistry' , 'J. Phys. Chem.'],
                 ['Chemical Physics Letters' , 'Chem. Phys. Lett.'],
                 ['The Journal of Chemical Theory and Computation' , 'J. Chem. Theory Comput.'],
                 ['Journal of Chemical Theory and Computation' , 'J. Chem. Theory Comput.'],
                 ['The Journal of the American Chemical Society' , 'J. Am. Chem. Soc.'],
                 ['Journal of the American Chemical Society' , 'J. Am. Chem. Soc.'],
                 ['The Journal of Physics: Conference Series', 'JPCS'],
                 ['Journal of Physics: Conference Series', 'JPCS'],
                 ['Nature Chemistry', 'Nat. Chem.'],
                 ['Physical Review Letters', 'Phys. Rev. Lett.'],
                 ['Physical Review A', 'Phys. Rev. A'],
                 ['Physical Review B', 'Phys. Rev. B'],
                 ['Physical Review C', 'Phys. Rev. C'],
                 ['Physical Review X', 'Phys. Rev. X'],
                 ['Physical Review', 'Phys. Rev.'],
                 ['Reviews of Modern Physics', 'Rev. Mod. Phys.'],
                 ['Chemical Society Reviews', 'Chem. Soc. Rev.'],
                 ['Chemical Physics', 'Chem. Phys.'],
                 ['Annals of Physics', 'Ann. Phys.'],
                 ['Molecular Physics', 'Mol. Phys.'],
                 ['Chemical Reviews', 'Chem. Rev.'],
                 ['Angewandte Chemie', 'Angew. Chem.'],
                 ['Theoretical Chemistry Accounts. Theory. Computation. and Modeling .Theoretica Chimica Acta.', 'Theoret. Chim. Acta'],
                 ['Theoretical Chemistry Accounts. Theory, Computation, and Modeling', 'Theor. Chem. Acc.'],
                 ['Theoretical Chemistry Accounts', 'Theor. Chem. Acc.'],
                 ['Theoretica Chimica Acta', 'Theoret. Chim. Acta'],
                 ['The New Journal of Physics', 'New J. Phys.'],
                 ['New Journal of Physics', 'New J. Phys.'],
                 ['Annual Review of Physical Chemistry', 'Annu. Rev. Phys. Chem.'],
                 ['Journal of Physics: Condensed Matter', 'J. Phys. Condens. Matter'],
                 ['Journal of Physics Condensed Matter', 'J. Phys. Condens. Matter'],
                 ['Europhysics Letters', 'EPL'],
                 ['Communications on Pure and Applied Mathematics', 'Commun. Pure Appl. Math.'],
                 ['Philosophical Transactions of the Royal Society of London A: Mathematical, Physical and Engineering Sciences', 'Philos. Trans. Royal Soc. A'],
                 ['Philosophical Transactions of the Royal Society of London A: Mathematical Physical and Engineering Sciences', 'Philos. Trans. Royal Soc. A'],
                 ['Philosophical Transactions of the Royal Society of London A Mathematical Physical and Engineering Sciences', 'Philos. Trans. Royal Soc. A'],
                 ['Philosophical Transactions of the Royal Society of London A', 'Philos. Trans. Royal Soc. A'],
                 ['Canadian Journal of Chemistry', 'Can. J. Chem.'],
                 ['Israel Journal of Chemistry', 'Isr. J. Chem.'],
               ]

# get name of the original bib file
orig_file_name = sys.argv[1]

# get name for the temporary file we will write to
temp_file_name = 'temp_' + orig_file_name
maxit = 30
for i in range(maxit+5):
  if not os.path.exists(temp_file_name):
    break
  elif i == maxit:
    raise RuntimeError('failed to create a file name for the abbreviation temporary file')
  else:
    temp_file_name = 'x' + temp_file_name

# open original bib file
f = open(orig_file_name, 'r')

# open new bib file to be written
g = open(temp_file_name, 'w')

# loop over the lines in the original file and make replacements as appropriate
for original_line in f:

  # only edit journal lines
  line = original_line.strip()
  if string.lower(line[:7]) == 'journal':
    line = "" + original_line
    # replace all unabbreviated titles with their abbreviations
    for rep in replacements:
      pattern = re.compile(rep[0], re.IGNORECASE)
      line = pattern.sub(rep[1], line)
    g.write(line)

  # non-journal lines are left alone
  else:
    g.write(original_line)

# close files
f.close()
g.close()

# move the temporary file to overwrite the original file
os.remove(orig_file_name)
os.rename(temp_file_name, orig_file_name)
