source_file = "source.txt"
target_file = "target.txt"

with open(source_file, 'r') as source, open(target_file, 'w') as target:
    target.write(source.read())
