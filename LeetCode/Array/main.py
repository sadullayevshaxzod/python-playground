# Type Easy
#Senga nums nomli butun sonlardan tashkil topgan massiv va val nomli butun son beriladi. Vazifa — massiv ichidagi val ga teng bo‘lgan barcha elementlarni olib tashlash. Buni yangi massiv yaratmasdan, ya’ni massivning o‘zini o‘zgartirgan holda bajarish kerak. val ga teng bo‘lmagan barcha elementlar massivning boshiga joylashtirilishi kerak. Ularning soni k bo‘ladi va funksiya k qiymatini qaytarishi kerak. Massivning birinchi k ta elementi val ga teng bo‘lmagan elementlardan iborat bo‘lishi shart. k dan keyingi elementlarning qanday qiymatda bo‘lishi muhim emas. Elementlarning tartibini o‘zgartirish mumkin. Masalan, nums = [3,2,2,3] va val = 3 bo‘lsa, 3 lar olib tashlanadi, birinchi ikkita element [2,2] bo‘ladi va funksiya 2 ni qaytaradi.
from typing import List
def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        for num in nums:
            if num != val:
                nums[index] = num
                index += 1

        return index


# Har bir element aksiyaning o‘sha kundagi narxini bildiradi. Bitta kunda sotib olib, undan keyingi boshqa bir kunda sotish kerak. Maqsad — sotib olish va sotish orasidagi eng katta foydani topish. Agar foyda qilishning iloji bo‘lmasa, 0 qaytariladi.
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit