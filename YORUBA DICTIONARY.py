def main():
    # English to Yoruba dictionary
    eng_to_yoruba = {
        "water": "omi",
        "fire": "ina",
        "sun": "oorun",
        "moon": "osupa",
        "star": "irawọ",
        "earth": "ayé",
        "sky": "ọrun",
        "tree": "igi",
        "leaf": "ewé",
        "house": "ilé",
        "food": "ounjẹ",
        "child": "ọmọ",
        "man": "ọkùnrin",
        "woman": "obinrin",
        "love": "ifẹ",
        "peace": "àlàáfíà",
        "money": "owó",
        "book": "iwe",
        "school": "ile-iwe",
        "friend": "ọrẹ"
    }

    print("=== Yoruba Dictionary ===")
    print("Mode: English → Yoruba")
    print("Type 'exit' to quit.\n")

    while True:
        english_word = input("Enter an English word: ").strip().lower()

        # Exit condition
        if english_word == "exit":
            print("Exiting Yoruba Dictionary. Goodbye!")
            break

        # Translation lookup
        translation = eng_to_yoruba.get(english_word)
        if translation:
            print(f"Yoruba translation of '{english_word}': {translation}\n")
        else:
            print(f"Sorry, '{english_word}' is not in the dictionary.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")