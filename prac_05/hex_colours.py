#create a program that allows you to look up hexadecimal colour codes like those
#at http://www.color-hex.com/color-names.html
#Use a constant dictionary of about 10 colour names and write a program that
#allows a user to enter a name and get the code, e.g. entering AliceBlue should show #f0f8ff.
#Entering an invalid colour name should not crash.
#Allow the user to enter names until they enter a blank one to stop the loop

HEX_COLORS = {"goldenrod1": "#ffc125", "AliceBlue": "#f0f8ff", "DarkOliveGreen3": "#a2cd5a", "coral": "#ff7f50",
              "burlywood2": "#eec591", "blue4": "#0008b", "firebrick": "#b22222", "cornsilk2": "#eee8cd", "FloralWhite": "#fffaf0",
              "DarkOrchid": "#9932cc"}
print("Color options are: ")
for key in HEX_COLORS:
    print(key)
print()

color = input("Enter color for hex code: ")

while color != "":
    if color in HEX_COLORS:
        print("Hex code for ", color, "is", HEX_COLORS[color])
    else:
        print("Color not listed.")
    color = input("Enter color: ")


