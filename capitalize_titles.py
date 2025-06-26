import re
from titlecase import titlecase

# Input and output files
my_file = 'bib.bib'
new_file = 'bib_capitalized.bib' # in case you don't want to overwrite

# Match title or journal segment allowing for whitespace (UPDATED 8/12/19)
pattern = re.compile(r'(\W*)(title|journal)\s*=\s*{(.*)},')

# Read in old file
with open(my_file, 'r', encoding ='utf8') as fid:
    lines = fid.readlines()

# Search for title strings and replace with titlecase
newlines = []
for line in lines:
    # Check if line contains title
    match_obj = pattern.match(line)
    if match_obj is not None:
        # Need to "escape" any special chars to avoid misinterpreting them in the regular expression.
        oldtitle = re.escape(match_obj.group(3))

        # Apply titlecase to get the correct title.
        newtitle = titlecase(match_obj.group(3))

        # Replace and add to list
        p_title = re.compile(oldtitle)
        newline = p_title.sub(newtitle, line)
        newlines.append(newline)
    else:
        # If not title, add as is.
        newlines.append(line)

# Print output to new file
with open(new_file, 'w', encoding='utf8') as fid:
    fid.writelines(newlines)
