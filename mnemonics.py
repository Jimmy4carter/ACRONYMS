# Developer: Jimmy Carter
# Contact: jimmy4carter@gmail.com
# Phone: +2348038660259
# GitHub: https://github.com/Jimmy4carter

def extract_initial_input(mnemonic):
    elements = mnemonic.split()
    input_text = ""

    for word in elements:
        if len(word) == 1:
            input_text += word
        else:
            input_text += word[0]

    return input_text

def generate_mnemonic(text):
    elements = text.split()
    mnemonic = ""

    for i, word in enumerate(elements):
        first_letter = word[0].upper()
        mnemonic += first_letter

    mnemonic_sentence = " ".join(mnemonic[i:i+4] for i in range(0, len(mnemonic), 4))

    return mnemonic_sentence

def main():
    input_text = input("Enter a paragraph or a list of items: ")

    mnemonic = generate_mnemonic(input_text)

    print(f"Mnemonic Sentence: {mnemonic}")

    # Reconstructing initial input from mnemonic
    reconstructed_input = extract_initial_input(mnemonic)
    print(f"Reconstructed Input: {reconstructed_input}")

if __name__ == "__main__":
    main()
