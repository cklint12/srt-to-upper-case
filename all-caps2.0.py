import os

srt_file = input("Enter file name: ")

while not os.path.isfile(srt_file):
    srt_file = input("File doesn't exist. Try again: ")

# Open the file
with open(srt_file, "r") as f:
    to_upper = f.read().upper()

# Make a new file containing uppercase letters
with open(srt_file.replace(".srt", "_uppercase.srt"), "w") as f:
    f.write(to_upper)


