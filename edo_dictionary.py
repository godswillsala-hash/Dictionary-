# Edo Language Dictionary (English to Edo)

edo_dictionary = {
    "hello": "Koyo" ,
    "goodbye": "O re",
    "thank you": "Oshalobua",
    "yes": "Iye",
    "no": "Owa",
    "man": "Okpia",
    "woman": "Okhuo",
    "child": "Omwan",
    "food": "Ema",
    "water": "Ame",
    "house": "Owa",
    "father": "Baba",
    "mother": "Iye",
    "friend": "Ibvio",
    "love": "Ibviedo",
    "money": "Igho",
    "school": "Isukulu",
    "book": "Ewe",
    "come": "Za",
    "go": "Khuo",
}
print("Welcome to the Edo Language Dictionary")
print("Available language: Edo")

choice = input("Type 'edo' to translate from English to Edo: ").lower()

if choice == "edo":
    word = input("Enter an English word: ").lower()

    if word in edo_dictionary:
        print(f"The Edo word for '{word}' is '{edo_dictionary[word]}'")
    else:
       print("Sorry, that word is not in the dictionary.")
else:
  print("Invalid choice. Please restart the program.")


