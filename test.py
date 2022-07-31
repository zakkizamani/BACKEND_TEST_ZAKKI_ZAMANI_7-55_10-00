# maks = int(input("Masukkan maks jumlah kolom/baris : "))
# for b in range(0, 10, 1):
#     for a in range(0, b+1, 1):
#         print("* ", end="")
#     print("")

# def is_prima(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return "Bukan bilangan prima"

#     return "Bilangan prima"


# print(is_prima(4))

sample = ["1", "4", "0", "6", "9"]
# thislist.sort()
# print(thislist)


# def sort_list(sample):
#     sample.sort()
#     return sample


# print(sort_list(sample))


# def umur_emas():
#     umur = int(input("Masukkan umur anda : "))
#     tahun_ini = 2022
#     hasil = tahun_ini + umur
#     return "Anda akan berumur 50 tahun lagi pada tahun {}".format(hasil)


# print(umur_emas())

txt = "This is NoW!"


def capital_find(capital):
    varlist = []
    for c in capital:
        if c.isupper():
            varlist.append(c)
    return len(varlist)


print(capital_find("TXt"))

# for x in txt:
#     if x.isupper():
#         jlist.append(x)


# print(len(jlist))
