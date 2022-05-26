def split_string(string):
    """Function to convert string into list of individual characters."""
    return [char for char in string]


morse = {
    "a": ". ---",
    "b": "--- . . .",
    "c": "--- . --- .",
    "d": "--- . .",
    "e": ".",
    "f": ". . --- .",
    "g": "--- --- .",
    "h": ". . . .",
    "i": ". .",
    "j": ". --- --- ---",
    "k": "--- . ---",
    "l": ". --- . .",
    "m": "--- ---",
    "n": "--- .",
    "o": "--- --- ---",
    "p": ". --- --- .",
    "q": "--- --- . ---",
    "r": ". --- .",
    "s": ". . .",
    "t": "---",
    "u": ". . ---",
    "v": ". . . ---",
    "w": ". --- ---",
    "x": "--- . . ---",
    "y": "--- . --- ---",
    "z": "--- --- . .",
    "1": ". --- --- --- ---",
    "2": ". . --- --- ---",
    "3": ". . . --- ---",
    "4": ". . . . ---",
    "5": ". . . . .",
    "6": "--- . . . .",
    "7": "--- --- . . .",
    "8": "--- --- --- . .",
    "9": "--- --- --- --- .",
    "0": "--- --- --- --- ---",
    " ": "    ",
}

# get input from user
text_string = input(
    "Welcome to the Morse Code Converter. What string of text would you like to convert?: "
).lower()

# Use split_string function to create list of morse code characters corresponding to input characters
morse_list = [morse[_] for _ in split_string(text_string)]
# convert the list of morse code characters into a string, with 3 spaces between characters
morse_output = "   ".join(str(x) for x in morse_list)
# print the users morse code output
print(f"Your morse code output is: {morse_output}.")
