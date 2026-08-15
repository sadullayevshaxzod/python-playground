import random

# Tanlovlar ro'yxati
x = ["tosh", "qaychi", "qog'oz"]


def tanla():
    """Foydalanuvchidan tanlovni qabul qiladi va matn shaklida qaytaradi."""
    print(
        "\nTosh, qaychi, qog'oz o'yini.\nQuyidagilardan birini tanlang:"
        "\nTosh (1)\nQaychi (2)\nQog'oz (3)"
    )

    try:
        tanladi = int(input(">>> "))
        if tanladi in [1, 2, 3]:
            matnli_tanlov = x[tanladi - 1]
            return matnli_tanlov
        else:
            print("❌ Noto'g'ri raqam kiritdingiz! 1, 2 yoki 3 ni tanlang.")
            return tanla()  # Noto'g'ri kiritilsa, qayta so'raydi
    except ValueError:
        print("❌ Iltimos, faqat raqam kiriting!")
        return tanla()


def tanla_pc():
    """Kompyuter uchun tasodifiy tanlov qiladi."""
    return random.choice(x)


def play():
    """Asosiy o'yin sikli va ochkolarni hisoblash."""
    user_ochko = 0
    pc_ochko = 0

    print("--- O'YIN BAShLANDI ---")

    while True:
        user_t = tanla()
        pc_t = tanla_pc()

        print(f"\nSiz: {user_t.upper()} | Kompyuter: {pc_t.upper()}")

        # Durang holati
        if user_t == pc_t:
            print("🤝 Durang!")

        # Foydalanuvchi g'alaba qozonadigan barcha holatlar
        elif (
            (user_t == "tosh" and pc_t == "qaychi")
            or (user_t == "qaychi" and pc_t == "qog'oz")
            or (user_t == "qog'oz" and pc_t == "tosh")
        ):
            print("🎉 Siz ushbu raundda yutdingiz!")
            user_ochko += 1

        # Qolgan barcha holatlarda kompyuter yutadi
        else:
            print("💻 Kompyuter ushbu raundda yutdi!")
            pc_ochko += 1

        # Hozirgi hisobni ko'rsatish
        print(f"📊 UMUMIY HISOB -> Siz: {user_ochko} | Kompyuter: {pc_ochko}")

        # O'yinni davom ettirish yoki to'xtatish
        yana = (
            input("\nYana o'ynaysizmi? (ha/yo'q): ").strip().lower()
        )
        if yana != "ha":
            print("\nO'yin yakunlandi!")
            print(
                f"🏆 YAKUNIY HISOB -> Siz: {user_ochko} | Kompyuter:"
                f" {pc_ochko}"
            )

            if user_ochko > pc_ochko:
                print("🥳 Tabriklaymiz, siz umumiy hisobda g'olib bo'ldingiz!")
            elif pc_ochko > user_ochko:
                print("🤖 Bu safar kompyuter g'olib bo'ldi.")
            else:
                print("🤝 Do'stlik g'alaba qozondi (Durang)!")
            break


# O'yinni ishga tushirish
play()