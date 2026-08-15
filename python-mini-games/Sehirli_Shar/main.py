import random

# Shar berishi mumkin bo'lgan javoblar ro'yxati (List)
javoblar = [
    "✨ Albatta, shubhasiz!",
    "👍 Mening javobim — HA!",
    "🎯 Katta ehtimol bilan shunday.",
    "🤔 Hozir aytolmayman, birozdan keyin qayta so'rang.",
    "💭 Buni keyinroq o'ylab ko'rish kerak...",
    "🧐 Hozir buni bashorat qila olmayman.",
    "❌ Bunga shubham bor.",
    "🚫 Javobim — YO'Q!",
    "⚠️ Miyangizga ham keltirmang!"
]


def shar_javobi():
    """Ro'yxatdan tasodifiy javob tanlab qaytaradi"""
    return random.choice(javoblar)


def play():
    print("--- 🔮 SEHRLI SHAR 8 (MAGIC 8-BALL) 🔮 ---")
    print("Men kelajakni bashorat qila olaman! Menga savol bering...\n")

    while True:
        savol = input("❓ Savolingizni kiriting: ").strip()

        # Bo'sh matn kiritilishini tekshirish
        if len(savol) == 0:
            print("⚠️ Iltimos, bo'sh savol bermang! Biror narsa so'rang.\n")
            continue

        # Shar javobini chiqarish
        bashorat = shar_javobi()
        print(f"🔮 Shar javob beradi: {bashorat}\n")

        # Yana o'ynashni so'rash
        yana = input("Yana savol berasizmi? (ha/yo'q): ").strip().lower()

        # Agar javob "ha" bo'lmasa, siklni to'xtatamiz
        if yana != "ha":
            print("\n🔮 Sehrli Shar o'z ishini yakunladi. Xayr!")
            break
        print("-" * 40 + "\n")


# O'yinni ishga tushirish
play()