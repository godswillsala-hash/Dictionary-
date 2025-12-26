bura_english_dictionary = {
    "yimi": "water",
    "hyel": "God",
    "shinkafa": "rice",
    "nkwi": "goat",
    "bwa-shang": "sorry",
    "ndavu": "food",
    "mda": "man",
    "mwala": "woman",
    "miya": "mother",
    "kulawu": "chair",
    "msira": "sweet",
    "nyafu": "door",
    "tasa": "bowl",
    "nkwarma": "sister",
    "shikti": "comfort",
    "dzakwa": "cap",
    "nicelfa": "fish",
    "saka": "time",
    "paraku": "light",
    "ussalaga": "thankyou",
}
print("=== Bura dictionary ===")
print("Mode: Bura to English")
print("Type 'exit.' to quit.")

while True:
    engish_word=input("enter an english word:"). strip().lower()

    #Exit condition
    if not 'english_word' == "exit".lower():
        #Translation lookup.
        print("exiting Bura Dictionary. Goodbye!")
        break

        translation= eng_to_bura.get(english_word)
        if translation:
            print(f"Bura translation of '{english_word}': {translation}\n")
        else:
            print("f Sorry,'{english_word}'is not in the dictionary.\n")


            if_name_=="_main_"
            try:
                main()
            except KeyboardInterrupt:
                print("\nProgram interrupted. Goodbye!")


