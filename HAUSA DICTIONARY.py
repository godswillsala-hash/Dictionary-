import streamlit as st
def main():

    st.set_page_config(page_title="English-Hausa Dictionary", page_icon="🇳🇬")


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


    st.title("🇳🇬 English to Hausa Dictionary")
    st.write("Type an English word below to get its Hausa translation.")


    word = st.text_input("Enter an English word:", placeholder="e.g. water").strip().lower()


    if word:

        if not word.isalpha():
            st.error("❌ Please enter letters only.")
        else:

            translation = eng_to_hausa.get(word)
            
            if translation:
                st.success(f"**Hausa translation:** {translation}")
                st.balloons()
            else:
                st.warning(f"❌ '{word}' is not in the dictionary.")


    with st.sidebar:
        st.subheader("About")
        st.info("This is a simple dictionary app built with Streamlit.")
        st.write(f"Words available: {len(eng_to_hausa)}")

if __name__ == "__main__":
    main()
