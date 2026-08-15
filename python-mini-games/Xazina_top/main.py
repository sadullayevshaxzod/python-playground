import random

def xazina_yashir():
    """1 dan 20 gacha bo'lgan tasodifiy nuqtaga xazinani yashiradi"""
    return random.randint(1, 20)

def masofani_aniqla(xazina, taxmin):
    """Xazina va taxmin o'rtasidagi masofani hisoblab, ishora beradi"""
    # abs() funksiyasi manfiy sonni ham musbatga o'girib, haqiqiy masofani beradi
    masofa = abs(xazina - taxmin)
    
    if masofa == 0:
        return "TOPDINGIZ"
    elif masofa <= 2:
        return "🔥 Juda issiq! Xazina juda yaqin!"
    elif masofa <= 5:
        return "☀️ Issiq! To'g'ri yo'nalishdasiz."
    else:
        return "❄️ Sovuq! Xazina uzoqda."

def play():
    xazina = xazina_yashir()
    urinishlar = 0
    max_urinish = 5  # O'yinni qiziqroq qilish uchun 5 ta imkoniyat
    
    print("--- 🏴‍☠️ XAZINANI QIDIRISH O'YINI 🏴‍☠️ ---")
    print("Xazina 1 dan 20 gacha bo'lgan kataklardan biriga yashiringan.")
    print(f"Sizda {max_urinish} ta imkoniyat bor. O'yin boshlandi!\n")

    while urinishlar < max_urinish:
        try:
            taxmin = int(input(f"[{urinishlar + 1}-urinish] Katak raqamini kiriting (1-20): "))
            
            # Chegarani tekshirish
            if taxmin < 1 or taxmin > 20:
                print("⚠️ Iltimos, faqat 1 dan 20 gacha bo'lgan raqam kiriting!\n")
                continue
                
        except ValueError:
            print("⚠️ Iltimos, faqat raqam kiriting!\n")
            continue

        urinishlar += 1
        natija = masofani_aniqla(xazina, taxmin)

        if natija == "TOPDINGIZ":
            print(f"\n🎉 TABRIKLAYMIZ! Siz {urinishlar}-urinishda xazinani topdingiz! 🏆")
            break
        else:
            print(f"Natija: {natija}")
            print(f"Qolgan imkoniyatlar: {max_urinish - urinishlar}\n")

    # Agar imkoniyatlar tugab, xazina topilmagan bo'lsa
    if urinishlar == max_urinish and natija != "TOPDINGIZ":
        print("❌ Yutqazdingiz! Imkoniyatlaringiz tugadi.")
        print(f"🏴‍☠️ Xazina {xazina}-katakda yashiringan edi.")

# O'yinni ishga tushirish
play()