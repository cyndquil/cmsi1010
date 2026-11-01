# ----------------------------------------------------------------------
# This is the file mad_libs.py
#
# The intent is to give you practice writing a complete, interactive
# Python program using a lot of Python data types, especially lists,
# sets, and dictionaries.
#
# Remove ALL of the existing comments in this file prior to submission.
# You can, and should, add your own comments, but please remove all the
# comments that are here now.
#
# Things to do:
#
# Define a bunch of templates in which some of the words begin with a colon (:).
# The words that begin with a colon are the words that you will ask the user
# to fill in. An example of a template is:
#
#     "The :color :animal :action over the :adjective :plant."
#
# You should define a list of at least 10 templates. Be creative!
#
# Your app should begin by selecting a random template. Then, for each word
# that begins with a colon in the template, prompt the user for a word
# that fits the description. Make sure that their input is between 1 and 30
# characters long, to prevent them from making too much of a mess of things.
#
# After the user has filled in all of the words, print the completed
# template with the user's words filled in. Then after a blank line, print
# a line crediting the author of the template. Then, print a couple of blank
# lines and ask them if they want to play again. If they say "yes" (or "sí"
# or "oui") or any acceptable version of an affirmative answer, start over
# with a new random template. Otherwise, say "no", print "Thanks for playing!"
# and exit the program.
#
# Here are some constraints:
#
#   1. The templates should be a list of dictionaries, in which each entry
#      has a "text" fields and an "author" field. The "text" field should
#      contain the template string, and the "author" field should contain
#      the name of the person who wrote the template.
#
#   2. The possible "yes" answers should be stored in a set.
# ----------------------------------------------------------------------



#print(templates[0]["text"]) 
# #this is taking our first[0] listed named template and printing 
#the text contained in it by taking its first dictionary. 
# [text] is the key that we are using to get the value in the dictionary.

#story = templates[0]["text"] #this is defining our variable story to hold the first template text

#adjective = input("Enter an adjective:")
# we ared defining our variable adjective to hold the input from a user. 
#the text in our string is what will appear when a user is prompted.

#story = story.replace(":adjective", adjective) 
#this is replacing the :adjective in the story variable with the user input stored in the adjective bariable

#print(story)

import random

templates = [
    {
        "text": "The :adjective ghost is behind you!",
        "author": "Professor Toal"
    },
    {
        "text": "Some :adjective :creature with a :weapon is eating :dessert",
        "author": "Professor Toal"
    },
    {
        "text": "Look! There is a :adverb :adjective :verb :noun in the :place.",
        "author": "whole class"
                },
    {
        "text": "The :adjective :animal :verb over the :adjective :object.",
        "author": "Professor Toal"
    },
    {
        "text": "The :adjective",
        "author": "Professor Toal"
    },

    {
        "text": "The :color pumpkin :action through the :adjective house.",
        "author": "Cynthia Chavez"
    },

    {
        "text": "The :color :animal :action over down the :adjective lit street.",
        "author": "Cynthia Chavez"
    },
    {
        "text": "Five :adjective children :action  on halloween night.",
        "author": "Cynthia Chavez"
    },
    {
        "text": "The :color haunted house was actually a :adjective :object.",
        "author": "Cynthia Chavez"
    
    },
    {
        "text": ":color bats flew into the :adjective :object,",
        "author": "Cynthia Chavez"

    },
    {
        "text": "Learning python can be quite :adjective",
        "author": "Cynthia Chavez"
    },    
    
]

yes_answers = {"yes", "y", "yeah", "yep", "sí", "si", "oui", "yuh"}

while True:
    template = random.choice(templates)
    story = template["text"]
    completed_words = []

    for word in story.split():
        if word.startswith(":"):
            placeholder = word.rstrip(".,!?;:")
            description = placeholder[1:]

            answer = input("Enter a word for " + description + ": ").strip()

            while len(answer) < 1 or len(answer) > 30:
                print("Please enter between 1 and 30 characters.")
                answer = input(
                    "Enter a word for " + description + ": "
                ).strip()

            word = word.replace(placeholder, answer, 1)

        completed_words.append(word)

    completed_story = " ".join(completed_words)

    print()
    print(completed_story)
    print()
    print(template["author"])
    print()
    print()

    response = input(
        "Would you like to play again? Enter yes, no, or exit: "
    ).strip().lower()

    if response == "exit":
        print("Thanks for playing!")
        break
    elif response not in yes_answers:
        print("Thanks for playing!")
        break