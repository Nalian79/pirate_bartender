import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit o' sweetness wit yer poison?",
    "fruity": "Are ye one fer a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "splash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

def style_o_drink():
    """This function gathers the users drink preferences for a dict.

    Use raw_input() to create a dictionary with boolean values for their
    responses.
    """
    answers = {}
    answers["strong"] = raw_input(questions["strong"] + " Type Y or N: ").upper()
    answers["salty"] = raw_input(questions["salty"] + " Type Y or N: ").upper()
    answers["bitter"] = raw_input(questions["bitter"] + " Type Y or N: ").upper()
    answers["sweet"] = raw_input(questions["sweet"] + " Type Y or N: ").upper()
    answers["fruity"] = raw_input(questions["fruity"] + " Type Y or N: ").upper()
    for key in answers:
        if answers[key] == "Y":
            answers[key] = True
        else:
            answers[key] = False
    return answers

def make_drink(x):
    """Create a drink randomly based on the users choices."

    This function takes the answers from the style_o_drink function
    and then creates a drink out of the ingrediants list, based on those
    user inputs.
    """
    drink = []
    for key in x:
        if x[key] == True:
            item = random.choice(ingredients[key])
            print "You said you liked " + key + " drinks, so",
            print "I'm going to add in a " + item
            drink.append(item)
        else:
            pass
    return drink

if __name__ == '__main__':
    # Create the user-generated answer dictionary
    answers = style_o_drink()

    # Use the dictionary to make a random drink
    drink = make_drink(answers)

    
