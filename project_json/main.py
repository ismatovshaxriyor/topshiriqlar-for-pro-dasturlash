# Import Modules ==============>
from get_and_set.set_question import section1
from get_and_set.get_results import section2
from data.colors import cyan, clear


# Main Module =============>
while True:
    print(cyan + "Kim milliarder bo'lishni xohlaydi o'yiniga xush kelibsiz!")
    print("""
    Buyruqni tanlang:
        1 - o'yinni boshlash
        2 - natijalarni ko'rish

        0 - o'yindan chiqish""" + clear)

    section = input("        -> ")
    if section == "1":
        try:
            section1()
        except StopIteration:
            pass
    elif section == "2":
        section2()
    elif section == "0":
        break
    else:
        print("Noto'g'ri buyruq kiritildi!")
