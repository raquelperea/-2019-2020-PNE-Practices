# Write a program that opens the U5.txt file and prints on the console all the lines except the first one

from pathlib import Path

FILENAME = "U5.txt"

file_contents = Path(FILENAME).read_text()

body = file_contents.split("\n")[1:]
body_string = " "
body_string = body_string.join(body)

print ("Body of the U5.txt file:\n",body_string)