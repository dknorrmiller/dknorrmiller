# -*- coding: utf-8 -*-
"""Hangman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lv4935pEfJrjRsIo6nXo2bgr7ZBgGCh6
"""

#Import
import random
from os import system, name

#Clear screen
def clear():
    #Windows
    if name == 'nt':
        _= system('cls')    
    #Mac or Linux
    else: _= system('clear')

#List of words
countries = "Afghanistan/Albania/Algeria/Andorra/Angola/Antigua and Barbuda/Argentina/Armenia/Australia/Austria/Azerbaijan/Bahamas/Bahrain/Bangladesh/Barbados/Belarus/Belgium/Belize/Benin/Bhutan/Bolivia/Bosnia and Herzegovina/Botswana/Brazil/Brunei/Bulgaria/Burkina Faso/Burundi/Cabo Verde/Cambodia/Cameroon/Canada/Chad/Chile/China/Colombia/Comoros/Congo/Costa Rica/Côte d’Ivoire/Croatia/Cuba/Cyprus/Czech Republic/Denmark/Djibouti/Dominica/Dominican Republic/East Timor/Ecuador/Egypt/El Salvador/Equatorial Guinea/Eritrea/Estonia/Eswatini/Ethiopia/Fiji/Finland/France/Gabon/Gambia/Georgia/Germany/Ghana/Greece/Grenada/Guatemala/Guinea/Guinea-Bissau/Guyana/Haiti/Honduras/Hungary/Iceland/India/Indonesia/Iran/Iraq/Ireland/Israel/Italy/Jamaica/Japan/Jordan/Kazakhstan/Kenya/Kiribati/North Korea/South Korea/Kosovo/Kuwait/Kyrgyzstan/Laos/Latvia/Lebanon/Lesotho/Liberia/Libya/Liechtenstein/Lithuania/Luxembourg/Madagascar/Malawi/Malaysia/Maldives/Mali/Malta/Marshall Islands/Mauritania/Mauritius/Mexico/Micronesia/Moldova/Monaco/Mongolia/Montenegro/Morocco/Mozambique/Myanmar/Namibia/Nauru/Nepal/Netherlands/New Zealand/Nicaragua/Niger/Nigeria/North Macedonia/Norway/Oman/Pakistan/Palau/Panama/Papua New Guinea/Paraguay/Peru/Philippines/Poland/Portugal/Qatar/Romania/Russia/Rwanda/Saint Lucia/Samoa/San Marino/Sao Tome and Principe/Saudi Arabia/Senegal/Serbia/Seychelles/Sierra Leone/Singapore/Slovakia/Slovenia/Solomon Islands/Somalia/South Africa/Spain/Sri Lanka/Sudan/South Sudan/Suriname/Sweden/Switzerland/Syria/Taiwan/Tajikistan/Tanzania/Thailand/Togo/Tonga/Trinidad and Tobago/Tunisia/Turkey/Turkmenistan/Tuvalu/Uganda/Ukraine/United Arab Emirates/United Kingdom/United States/Uruguay/Uzbekistan/Vanuatu/Vatican/Venezuela/Vietnam/Yemen/Zambia/Zimbabwe/"
countriesUP = countries.upper()
words = list(countriesUP.split('/'))

def hangman():
    clear()

    #Welcome
    print("Welcome to Hangman")
    print("What is the word(countries names)?")
    word = random.choice(words) #Chosing a random word in a list
    word_game = ['_' for l in word] #Undiscoveres/Discovered letters
    wrong = [] #Wrong letters
    chances = 6 #Chances
    
    while chances > 0: #Loop while have chances
        #prints
        print(" ".join(word_game))
        print("\nRemaning chances: ", chances)
        print("Wrong letters: ", " ".join(wrong))

        tries = input("\nType a letter: ").upper() #User tries a letters
        
        if tries in word: #Tried letter in word
            index = 0
            
            for letter in word: #Changing to discovered letters
                if tries == letter:
                    word_game[index] = letter
                index +=1
        else: 
            chances -=1 #Losing a chance
            wrong.append(tries) #Show wrong letters tried
        
        if "_" not in word_game: #Win message
            print("\nCongratulations! YOU WIN!!!")
            break
    if chances == 0: print("You lose! The country was: ", word) #Lose message
 
#Main
if __name__ == "__main__":
    hangman()