# Helen Li
# April 10, 2015
# Assignment #7: Problem #2b

name = input("Name: ")

# convert to lowercase
name1 = str.lower(name)

newname=""
reduction = 0

# can only contain alpha characters
for character in name1:
    if character.isalpha() == True:
        newname += character
        a = ord(character)
        b = int(a)
        reduction += (b-96)
    else:
        newname += ""
print ("Your 'cleaned up' name is:", newname)
print ("Reduction:", reduction)

# reduce name until it matches one of the classic numerology numbers
while True:
    if reduction == 0:
        print ("Your name reduces to ...", reduction, "- Emptiness, Nothingness, Blank")
        break
    elif reduction == 1:
        print ("Your name reduces to ...", reduction, "- Independence, Loneliness, Creativity, Originality, Dominance, Leadership, Impatience")
        break
    elif reduction == 2:
        print ("Your name reduces to ...", reduction, "- Quiet, Passive, Diplomatic, Co-operation, Comforting, Soothing, Intuitive, Compromising, Patient")
        break
    elif reduction == 3:
        print ("Your name reduces to ...", reduction, "- Charming, Outgoing, Self expressive, Extroverted, Abundance, Active, Energetic, Proud")
        break
    elif reduction == 4:
        print ("Your name reduces to ...", reduction, "- Harmony, Truth, Justice, Order discipline, Practicality")
        break
    elif reduction == 5:
        print ("Your name reduces to ...", reduction, "- New directions, Excitement, Change, Adventure")
        break
    elif reduction == 6:
        print ("Your name reduces to ...", reduction, "- Love, Harmony, Perfection, Marriage, Tolerance, Public service")
        break
    elif reduction == 7:
        print ("Your name reduces to ...", reduction, "- Spirituality, Completeness, Isolation, Introspection")
        break
    elif reduction == 8:
        print ("Your name reduces to ...", reduction, "- Organization, Business, Commerce, New beginnings")
        break
    elif reduction == 9:
        print ("Your name reduces to ...", reduction, "- Romantic, Rebellious, Determined, Passionate, Compassionate")
        break
    elif reduction == 11:
        print ("Your name reduces to ...", reduction, "- Idealism, Visionary, Inspirational")
        break
    elif reduction == 12:
        print ("Your name reduces to ...", reduction, "- Perfectionist, Discriminating")
        break
    elif reduction == 22:
        print ("Your name reduces to ...", reduction, "- Builder, Leader, Humanitarian, Practical, Honest")
        break
    else:
        c = str(reduction)
        reduction = 0
        for x in c:
            y = int(x)
            reduction += y
        print ("Reduction:", reduction)
