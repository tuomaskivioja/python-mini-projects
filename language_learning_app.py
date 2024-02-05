import random

# edit this list - get more from Chat GPT
words = [
    {"spanish": "el", "english": "the"},
    {"spanish": "de", "english": "of/from"},
    {"spanish": "que", "english": "that/which"},
    {"spanish": "y", "english": "and"},
    {"spanish": "a", "english": "to/at"},
    {"spanish": "en", "english": "in/on"},
    {"spanish": "un", "english": "a/an"},
    {"spanish": "ser", "english": "to be"},
    {"spanish": "se", "english": "oneself/itself"},
    {"spanish": "no", "english": "no/not"},
    {"spanish": "haber", "english": "to have (auxiliary)"},
    {"spanish": "por", "english": "for/by"},
    {"spanish": "con", "english": "with"},
    {"spanish": "su", "english": "his/her/your/their"},
    {"spanish": "para", "english": "for/to"},
    {"spanish": "como", "english": "like/as"},
    {"spanish": "estar", "english": "to be"},
    {"spanish": "tener", "english": "to have"},
    {"spanish": "le", "english": "him/her/you (indirect object)"},
    {"spanish": "lo", "english": "it/him/you (direct object)"},
]

def quiz_user(words):
    """Quiz the user with words."""
    random.shuffle(words)  # Shuffle the list of words
    score = 0

    for word in words:
        print(f"What is the English translation of '{word['spanish']}'?")
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = word['english'].lower()

        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is '{word['english']}'.\n")

    print(f"Quiz complete! Your score: {score}/{len(words)}")

def main():
    print("Welcome to the Language Learning Flashcards App!")
    input("Press Enter to start the quiz...")
    quiz_user(words)

if __name__ == "__main__":
    main()
