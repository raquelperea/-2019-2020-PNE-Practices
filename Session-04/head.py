from pathlib import Path

# -- Constant with the new of the file to open
FILENAME = "RNU6_269P.txt"

# -- Open and read the file
file_contents = Path(FILENAME).read_text()

file_head = file_contents.split("\n")

# -- Print the contents on the console
print(file_head)