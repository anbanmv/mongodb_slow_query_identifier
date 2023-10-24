#!/usr/bin/env python3
 
# Author:       Anban Malarvendan
# License:      GNU GENERAL PUBLIC LICENSE Version 3 +
#               Section 7: Redistribution/Reuse of this code is permitted under the
#               GNU v3 license, as an additional term ALL code must carry the
#               original Author(s) credit in comment form.
 
 
import subprocess
 
log_file = '/var/log/mongo/mongod.log'
 
log_processing_command = (
    "grep '[0-9]ms$' {} | "
    "sed 's/^.*\\s\\([0-9]*\)ms$/\\1 \\0/' | "
    "sort -rn | "
    "sed 's/^[0-9]* //' | "
    "head -n 20"
)

try:
    process = subprocess.Popen(log_processing_command.format(log_file), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
 
    if process.returncode == 0:
        lines = output.split('\n')
         
        for i, line in enumerate(lines):
            if i == 20:
                break
            print(f"Slow Query {i + 1}: {line}")
    else:
        print(f"Error: {error}")
 
except Exception as e:
    print(f"An error occurred: {str(e)}")
