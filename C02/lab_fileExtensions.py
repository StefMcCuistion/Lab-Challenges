input = input("Enter file name: ")
file_extension = input.split('.')[-1]
print(file_extension)

# Figuring out the extension of a file is a common problem to solve.
# It opens up the possibilities of sorting and filtering through files
# by type.
#
# Don't know what's a file extension?
# Check out: https://www.howtogeek.com/356448/what-is-a-file-extension/
#
# Write a program that displays the file extension of any file.
# Prompt the user to enter any filename. (e.g. essay.doc, sunset.jpg)
# Using the techniques of string slicing, isolate the file extension
# (the part after the .) and display it on the screen.
#
# CHALLENGE: Your program correctly identifies the extensions of these
# types of filenames too:
# - sunset.jpeg -> jpeg
# - spaceship_rig.v001.fbx -> fbx
# - image_sequence.v001.0024.exr -> exr
