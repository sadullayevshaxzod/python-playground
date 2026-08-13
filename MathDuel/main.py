import random

amallar = ["*", "//", "-", "+"]  # '/' o'rniga '//' ishlatdik


def sonlar(x=100):
    son1 = random.randint(1, x)
    son2 = random.randint(1, x)
    return son1, son2


def amal():
    return random.choice(amallar)


def savol_yarat():
    """Savol va uning to'g'ri javobini bir vaqtda qaytaradi"""
    son1, son2 = sonlar()
    amall = amal()

    if amall == "+":
        haqiqiy_javob = son1 + son2
    elif amall == "-":
        haqiqiy_javob = son1 - son2
    elif amall == "*":
        haqiqiy_javob = son1 * son2
    elif amall == "//":
        haqiqiy_javob = son1 // son2

    return son1, amall, son2, haqiqiy_javob


def play():
    user_yurak = 3
    ochko = 0

    print("--- MATEMATIK DUEL O'YINI ---")

    # Jonlar tugaguncha o'yin davom etadi
    while user_yurak > 0:
        son1, amall, son2, haqiqiy_javob = savol_yarat()

        print(f"\nSanoq: {son1} {amall} {son2} = ?")

        try:
            javob_user = int(input(">>> "))
        except ValueError:
            print("Iltimos, faqat raqam kiriting!")
            continue

        if javob_user == haqiqiy_javob:
            ochko += 1
            print(f"✅ To'g'ri! Ochko: {ochko}")
        else:
            user_yurak -= 1
            print(
                f"❌ Xato! To'g'ri javob {haqiqiy_javob} edi. Qolgan jonlar:"
                f" {user_yurak}"
            )

    print(f"\nO'yin tugadi! Siz toplagan ochko: {ochko}")


play()