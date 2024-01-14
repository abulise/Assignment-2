import codecs

encrypted_code = """
tybony_inevnoyr = 100

zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr= 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
        if tybony_inevnoyr % 2 == 0:
            ahzoref.erzbir(tybony_inevnoyr)
        ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
erfhyg =cebprff_ahzoref(ahzoref=zl_frg)


qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xr14'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs Zl_frg vf abg Abar naq zl_qvpg['xr14'] ==10:
    cevag("pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""

# Decoding using ROT13
decrypted_code = codecs.decode(encrypted_code, 'rot_13')

print(decrypted_code)
