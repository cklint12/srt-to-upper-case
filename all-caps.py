# This script takes in an srt file and converts all the
# lower case letters to upper case

srt_file = input("Enter filename: ")

with open(srt_file, "r") as f:
    lower = f.read().upper()

with open("captions_uppercase.srt", "w") as f:
    f.write(lower)


