# 02. Find Variable Names in Sentences
import re
line = input()

pattern = r'\b_([a-zA-Z0-9]+)\b'

matches = re.findall(pattern, line)

print(",".join(matches))