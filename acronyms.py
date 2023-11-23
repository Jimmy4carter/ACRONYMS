# Developer: Jimmy Carter
# Contact: jimmy4carter@gmail.com
# Phone: +2348038660259
# GitHub: https://github.com/Jimmy4carter

def generate_acronym(phrase, style='traditional'):
    if not phrase.strip():
        return "Please enter a valid phrase."
    
    words = phrase.split()
    acronym = ""
    
    for word in words:
        acronym += word[0].upper()
    
    if style == 'camel_case':
        acronym = acronym[0].upper() + acronym[1:].lower()
    elif style == 'custom_separator':
        separator = input("Enter the separator: ")
        acronym = separator.join(acronym)
    
    return acronym

def display_stats(phrase, acronym):
    words_count = len(phrase.split())
    phrase_length = len(phrase)
    acronym_length = len(acronym)
    
    stats = f"Original Phrase Length: {phrase_length} characters\nNumber of Words: {words_count}\nGenerated Acronym: {acronym}\nAcronym Length: {acronym_length} characters"
    return stats

def main():
    print("Welcome to the Acronym Generator!")
    user_input = input("Enter a phrase: ")
    
    # Choose acronym style
    acronym_style = input("Choose acronym style (traditional/camel_case/custom_separator): ").lower()
    
    generated_acronym = generate_acronym(user_input, acronym_style)
    
    if generated_acronym != "Please enter a valid phrase.":
        print(f"Generated Acronym: {generated_acronym}")
        print(display_stats(user_input, generated_acronym))
    else:
        print(generated_acronym)

if __name__ == "__main__":
    main()
