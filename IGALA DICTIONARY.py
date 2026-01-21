# Igala Dictionary Program

# Dictionary of 20 Igala words and their English meanings
igala_dict = {
    "Olu": "Sun",
    "Oma": "Child",
    "Ene": "Person",
    "Attah": "King",
    "Omi": "Water",
    "Una": "Light",
    "Uchu": "Yam",
    "Ohimini": "River",
    "Ukpo": "Cloth",
    "Akpete": "Stool",
    "Ojo": "Day",
    "Igbele": "Lady",
    "Onukwu": "friend",
    "Omaye": "Sibling",
    "Omanyo": "Good child",
    "Unyi": "House",
    "Ododo": "Flower",
    "Eko": "Leopard",
    "Okwuta": "stone",
    "Obala": "Cat"
}

# Function to search for a word
def search_word(word):
    meaning = igala_dict.get(word)
    if meaning:
        print(f"{word} means '{meaning}' in English.")
    else:
        print(f"Sorry, '{word}' is not in the dictionary.")

# Main program loop
print("Welcome to the Igala-English Dictionary!")
print("Type a word to search, or 'exit' to quit.")

while True:
    user_input = input("Enter an Igala word: ").strip()
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    search_word(user_input)