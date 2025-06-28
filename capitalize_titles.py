import re
from titlecase import titlecase

# Input and output BibTeX files
my_file = 'bib.bib'
new_file = 'bib_capitalized.bib'  # Output file (does not overwrite the original)

# Compile a regex pattern to match lines with 'title' or 'journal' fields
# Captures leading whitespace or punctuation, the field name, and the content
pattern = re.compile(r'(\W*)(title|journal)\s*=\s*{(.*)},')

# Read the input .bib file line by line
with open(my_file, 'r', encoding='utf8') as fid:
    lines = fid.readlines()

newlines = []  # List to store processed lines

# Process each line
for line in lines:
    match_obj = pattern.match(line)

    if match_obj is not None:
        # Extract components from the matched line
        prefix = match_obj.group(1)       # leading space or punctuation
        field_name = match_obj.group(2)   # 'title' or 'journal'
        field_value = match_obj.group(3)  # the actual title/journal text

        # Convert field value to title case
        new_field_value = titlecase(field_value)

        # Reconstruct the line with the titlecased value
        newline = f"{prefix}{field_name} = {{{new_field_value}}},\n"
        newlines.append(newline)
    else:
        # Leave non-matching lines unchanged
        newlines.append(line)

# Write the processed lines to a new .bib file
with open(new_file, 'w', encoding='utf8') as fid:
    fid.writelines(newlines)
