# 7. Usia Emas
def umur_emas():
    umur = int(input("Masukkan umur anda : "))
    tahun_ini = 2022
    hasil = tahun_ini + umur
    return "Anda akan berumur 50 tahun lagi pada tahun {}".format(hasil)


print(umur_emas())
