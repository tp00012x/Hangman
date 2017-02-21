import random
with open("wordlist.txt", "rb") as mywordlist:
    wordlist = [i.strip() for i in mywordlist.readlines() if not ("-" in i or "(" in i)]

hangman = ["-----|    ",
           "|  (. .) ",
           "|  --|-- ",
           "| /  |  \\",
           "|    |   ",
           "|  ----- ",
           "| /     \\",
           "| |     |",
           "---------"]
deadhangman = ["-----|    ",
           "|  (x x) ",
           "|  --|-- ",
           "| /  |  \\",
           "|    |   ",
           "|  ----- ",
           "| /     \\",
           "| |     |",
           "---------"]
