# ParseScript
Read scripts as png files and create a wizard to aid in creation of a Director's Notebook

ParseScript is written in python and uses PDFMiner as a dependency.
It works by reading the raw pdf file, converting the information to text, and then printing that text.

TODO:

CHARACTERS
Check for text that has been centered.
If so, match the text against an array of previously created objects to check for duplicates.
If not, create a new object within the character class.
Assign the text in the line as the name attribute.

SCENE
Check to see if a line includes the text INT or EXT.
If so, create a new scene object.
Assign the location as all the text in the line, skipping any dashes and DAY, NIGHT, MORNING, and EVENING.
Assign the corresponding information under to the time attribute.

After parsing the entire script, output the objects and their attributes to JSON format.
