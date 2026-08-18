                        #Leaner Search

sonlar=[3,4,1,33,4,5,6,8,9,10,11,13,23,12,34]
x_top=101 # 10  sonini royxatda bormi qidiryapmiz
def leaner_search(royxat,x):
    qadam=0
    for son in royxat:
        qadam+=1
        if son==x:
            return f"{qadam} qadam  bilan {x} soni topildi "
    return f"{x} soni royxatda topilmadi jami {qadam} ta qadam bosildi"

result=leaner_search(sonlar,x_top)


                        #Beanry Search
sonlar=[3,4,1,33,4,5,6,8,9,10,11,13,23,12,34]
s_sonlar=sorted(sonlar)
print(s_sonlar)
x_top=1
def beanry_search(royxat,x):
    left=0
    right=len(royxat)-1
    qadam=0
    while left<=right:
        qadam+=1
        mid=(left+right) //2
        if royxat[mid]==x_top:
            return f"{qadam} qadam bilan {x} soni topildi "
            
        elif royxat[mid] > x_top:
            right=mid-1
        else:
            left=mid+1
    return f"{x} soni royxatda yoq jami {qadam} qadam bosildi"
result=beanry_search(s_sonlar,x_top)


# 1-masala: "O'ylangan sonni topish" (Boshlang'ich)
# Shart: Kompyuter 1 dan 100 gacha bo'lgan oraliqda bir sonni yashirgan. Binary search ishlatib, shu sonni eng kam qadamda topadigan funktsiya yozing.

def sonni_top(left,right,target):
    step=0
    while left<=right:
        step+=1
        mid=(left+right)//2
        if mid==target:
            return f"{step} ta qadam bilan {target} soni topildi"
        elif mid>target:
            right=mid-1
        else:
            left=mid+1
    return f"{target} bu son  {left} va {right} sonlar orasida yo'q "
result=sonni_top(1,100,78)

# 2-masala: "Lug'atdan so'z qidirish" (O'rta)
# Shart: Sizga alifbo ketma-ketligida sarolangan so'zlar ro'yxati berilgan. Berilgan so'z ro'yxatda bor-yo'qligini Binary Search yordamida aniqlang.

sozlar = ["anor", "banan", "behi", "gilos", "olma", "shaftoli", "o'rik"]
x_soz = "gilos"
def soz_top(royxat,target):
    left=0
    right=len(royxat)-1
    step=0
    while left<=right:
        step+=1
        mid=(left+right)//2
        if royxat[mid] == target:
            return f"{step}-qadamda topildi! '{target}' so'zi {mid}-indeksda turibdi."
        elif royxat[mid] > target:
            right=mid-1
        else:
            left=mid+1
        return f"'{target}' so'zi lug'atda topilmadi."

result = soz_top(sozlar, x_soz)



# 3-masala: "Elementning birinchi va oxirgi o'rnini topish" (Murakkab)
# Shart: Sarolangan ro'yxatda bir xil sonlar bir nechta takrorlanishi mumkin. Binary search yordamida berilgan sonning birinchi uchrashgan indeksi va oxirgi uchrashgan indeksini toping.

Royxat=[1, 2, 4, 4, 4,4, 5, 6, 8, 8, 10]

x = 4

# Kutilayotgan natija: Birinchi indeks: 2, Oxirgi indeks: 4
def index1(royxat,x):
    left=0
    right=len(royxat)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if royxat[mid]==x:
            result=mid
            right=mid-1
        elif royxat[mid] > x:
            right=mid-1
        else:
            left=mid+1
    return result
def indexn(royxat,x):
    left=0
    right=len(royxat)-1
    result=-1
    while left<=right:
        mid=(left+right)//2
        if royxat[mid]==x:
            result=mid
            left=mid+1
        elif royxat[mid]>x:
            right=mid-1
        else:
            left=mid+1
    return result
birinchi_index=index1(Royxat,4)
oxirgi_index=indexn(Royxat,4)


# 4-masala: "Kvadrat ildizni hisoblash" (Mantiqiy)
# Shart: Musbat butun N soni berilgan. Tayyor math.sqrt() funktsiyasidan foydalanmasdan, Binary Search yordamida shu sonning butun kvadrat ildizini (floor(√N)) toping.

# Kiritish: N = 16 -> Chiqish: 4

# Kiritish: N = 28 -> Chiqish: 5 (chunki 5 * 5 = 25, 6 * 6 = 36)

def kv_ildiz(x):
    left=1
    right=x
    javob=0

    while left<=right:
        mid=(left+right)//2
        if mid*mid==x:
            return mid
        elif mid*mid < x:
            javob=mid
            left=mid+1
        else:
            right=mid-1
    
    return  f"{javob} (chunki {javob}*{javob} = {javob*javob}, {javob+1}*{javob+1} = {(javob+1)*(javob+1)})"


ildiz=kv_ildiz(19)


# 5-masala: "Tog' cho'qqisini topish" (Peak Index) — (O'rta)
# Shart: Sizga avval o'sib, keyin kamayadigan sonlar ro'yxati berilgan (ya'ni tog' ko'rinishida). Binary Search yordamida ro'yxatdagi eng katta elementning (cho'qqining) indeksini toping.

r=[1, 3, 5, 8, 12, 10, 6, 2]

# # Kutilayotgan natija: Eng katta son 12, uning indeksi: 4
def choqqini_top(royxat):
    l=1
    r=len(royxat)-1

    while l<=r:
        mid=(l+r)//2
        if royxat[mid] > royxat[mid+1]:
            return f" cho'qqi indexi -> {mid}"
        elif royxat[mid]<royxat[mid+1]:
            l=mid+1
        else:
            r=mid-1
natija=choqqini_top(r)




            



