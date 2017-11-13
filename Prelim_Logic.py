class Prelim_Logic:
    def __init__(self, text=""):
        Prelim_Logic.text = text

    # Splits string into a list of words
    def split_line(self, text=""):
        Prelim_Logic.words = text.split_line()
        return Prelim_Logic.words

    # Rudimentary Logic for checking desired one word match

    def checktext(self):
        for word in Prelim_Logic.words:
            if word == "heart":
                print "LED  OUTPUT"
            if word == "clock":
                print "LED  OUTPUT"

    # Rudimentary logic for checking desired two word match
    def checktexttwo(self):
        for word in Prelim_Logic.words:
            if word == "heart" and Prelim_Logic.words[word + 1] == "on":
                print "LED  OUTPUT"
            elif word == "heart" and Prelim_Logic.words[word + 1] == "off":
                print "LED OUTPUT"
            elif word == "clock" and Prelim_Logic.words[word + 1] == "on":
                print "LED  OUTPUT"
            elif word == "clock" and Prelim_Logic.words[word + 1] == "off":
                print "LED  OUTPUT"
