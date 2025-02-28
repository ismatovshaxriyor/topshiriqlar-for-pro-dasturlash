# Import Modules ==============>
from get_and_set.get_questions import get_question, get_answer
from data.colors import blue, red, yellow, green, clear
from get_and_set.set_results import set_result
from random import sample


# First section func. ============>
def section1():
    name = input("Ismingizni kiriting: ")
    quiz = get_question()
    answer = get_answer()
    next_a = next(quiz)
    next_b = next(answer)
    help_chance = 1
    count = 0
    i = 0

    while True:
        print(blue + f"\n{i + 1}-savol" + clear)
        print(next_a + "\n")
        print(f"a) {next_b[0]["key"]}")
        print(f"b) {next_b[1]["key"]}")
        print(f"c) {next_b[2]["key"]}")
        print(f"d) {next_b[3]["key"]}")
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
            if next_b[0]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                next_a = next(quiz)
                next_b = next(answer)

        elif input_ans == "b":
            if next_b[1]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                next_a = next(quiz)
                next_b = next(answer)

        elif input_ans == "c":
            if next_b[2]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                next_a = next(quiz)
                next_b = next(answer)

        elif input_ans == "d":
            if next_b[3]["isTrue"] != True:
                for_info()
                break
            else:
                count += 1
                i += 1
                full_result()
                next_a = next(quiz)
                next_b = next(answer)

        elif input_ans == "h":
            if help_chance >= 1:
                new_b = [i for i in next_b if i["isTrue"] == False]
                help_b = sample(new_b, 2)
                next_b = [quiz for quiz in next_b if quiz not in help_b]

                while help_chance >= 1:
                    print(blue + f"\n{i + 1}-savol" + clear)
                    print(next_a + "\n")
                    print(f"a) {next_b[0]["key"]}")
                    print(f"b) {next_b[1]["key"]}")
                    input_ans = input("Javob: ")

                    if input_ans == "a":
                        if next_b[0]["isTrue"] != True:
                            for_info()
                            break
                        else:
                            count += 1
                            i += 1
                            help_chance -= 1
                            full_result()
                            next_a = next(quiz)
                            next_b = next(answer)

                    elif input_ans == "b":
                        if next_b[1]["isTrue"] != True:
                            for_info()
                            break
                        else:
                            count += 1
                            i += 1
                            help_chance -= 1
                            full_result()
                            next_a = next(quiz)
                            next_b = next(answer)
                    else:
                        print("Bunday variant yo'q")
            else:
                print(red + "Sizda yordam imkoniyati tugadi!")

        else:
            print("Bunday variant yo'q")
