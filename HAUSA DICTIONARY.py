def main():
    # English-to-Hausa dictionary
    eng_to_hausa = {
        "water": "ruwa",
        "food": "abinci",
        "house": "gida",
        "school": "makaɗa",
        "book": "littafi",
        "pen": "alkalami",
        "sun": "rana",
        "moon": "wata",
        "star": "tauraro",
        "tree": "itace",
        "road": "hanya",
        "market": "kasuwa",
        "child": "yaro",
        "man": "namiji",
        "woman": "mace",
        "fire": "wuta",
        "rain": "ruwan sama",
        "mountain": "dutse",
        "river": "kogi",
        "friend": "aboki"
    }

    print("=== English to Hausa Dictionary ===")
    print("Type an English word to get its Hausa translation.")
    print("Type 'exit' to quit.\n")

    while True:
        word = input("Enter an English word: ").strip().lower()

        # Exit condition
        if word == "exit":
            print("Goodbye!")
            break

        # Validate input
        if not word.isalpha():
            print("❌ Please enter letters only.")
            continue

        # Translation lookup
        translation = eng_to_hausa.get(word)
        if translation:
            print(f"✅ Hausa for '{word}' is: {translation}\n")
        else:
            print(f"❌ '{word}' is not in the dictionary.\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted. Goodbye!")