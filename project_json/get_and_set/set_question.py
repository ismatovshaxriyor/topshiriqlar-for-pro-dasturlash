# Import Modules ==============>
from get_and_set.get_questions import get_question, get_answer
from data.colors import blue, red, yellow, green, clear
from get_and_set.set_results import set_result


# First section func. ============>
def section1():
    name = input("Ismingizni kiriting: ")
    quiz = get_question()
    answer = get_answer()
    a = next(quiz)
    b = next(answer)
    count = 0
    i = 0

    while True:
        print(blue + f"\n{i + 1}-savol" + clear)
        print(a + "\n")
        print(f"a) {b[0]["key"]}")
        print(f"b) {b[1]["key"]}")
        print(f"c) {b[2]["key"]}")
        print(f"d) {b[3]["key"]}")
        print("h - yordam")
        input_ans = input("Javob: ")

        def for_info():
            print(red + "Noto'g'ri javob")
            print(blue + f"Ishtirokchi: {name}")
            print(yellow + f"Natija: {count}/10\n" + clear)
            set_result(name, count)
        
        def full_result():
            if count == 10:
                print(green + "\nENG YUQORI NATIJA")
                print(blue + f"Ishtirokchi: {name}")
                print(yellow + f"Natija: {count}/10\n" + clear)
                set_result(name, count)

        if input_ans == "a":
            if b[0]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                a = next(quiz)
                b = next(answer)

        elif input_ans == "b":
            if b[1]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                a = next(quiz)
                b = next(answer)

        elif input_ans == "c":
            if b[2]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                a = next(quiz)
                b = next(answer)

        elif input_ans == "d":
            if b[3]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                a = next(quiz)
                b = next(answer)

        elif input_ans == "h":
            pass
        else:
            print("Bunday variant yo'q")
