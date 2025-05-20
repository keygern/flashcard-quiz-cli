from flashcard import Flashcard
from utils import load_data, save_data
import random

data_path = "flashcard_appv2/flashcards.json" 

def new_flashcard(data):
    new_question = input("What question do you want to add to the quiz\n")
    new_answer = input("What answer do you want to add \n")
    if not new_question or not new_answer:
        print("⚠️ Question and answer cannot be empty.\n")
        return
    data.append({"prompt":new_question,"answer":new_answer})
    save_data(data_path, data)
    print("\n NEW FLASHCARD ADDED")


def flashcard_quiz(questions):
    while True:
        score = 0
        for fc in questions:
            if fc.ask():
                score +=1
                print("\n✅ Correct!\n")
            else: 
                print(f"\n❌ Wrong! The correct answer is {fc.answer}\n")
        print(f"You got {score}/{(len(questions))} correct")
        if score < len(questions):
            while True:
                tryagain = input("Do you want to try again? Y/N ").strip()
                if tryagain.upper() == "Y":
                    break
                elif tryagain.upper() == "N":
                    return False
                else:
                    print("invalid input select Y or N")
    
def main():
    data = load_data(data_path)
    questions = [Flashcard(fc["prompt"], fc["answer"]) for fc in data
             if "prompt" in fc and "answer" in fc] 
    random.shuffle(questions)
    flashcard_quiz(questions)
    while True:
        add_flashcard = input("\n\n Do you want to add a new flashcard to the quiz? (Y/N)\n").strip()
        if add_flashcard.upper() == "Y":
            new_flashcard(data)
        elif add_flashcard.upper() == "N":
            break
        else:
            print("invalid input select Y or N")
if __name__ == "__main__":
    main()
