# 5. Buatlah function yang menghitung jumlah huruf kapital dalam sebuah file
def capital_find(capital):
    varlist = []
    for c in capital:
        if c.isupper():
            varlist.append(c)
    return len(varlist)


print(capital_find("TXt"))  # 2
