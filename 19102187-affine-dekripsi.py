# fungsi dekripsi
# enkripsi to dekripsi
# enkripsi = HFKN HRPIDMFS HFKN SVM ONF HFKN ORMFYFS KNGNA ODPFH OTD YEDZVSV DKKY GFZF
# keynya adalah 3 dan 5

def decrypt(s, a, b):
    output = ''

    # inisialisasi dan bentuk perulangan hasil bagi dari inverse modulo 26
    a_inv = 0
    while a * a_inv % 26 != 1:
        a_inv += 1

    #     perulangan untuk menentukan alfabet hasil dari inverse modulo 26 diatas
    for c in s:

        if ord(c) >= 0x41 and ord(c) <= 0x5a:
            i = ord(c) - 0x41
            i = (a_inv * (i - b)) % 26
            output += chr(i + 0x41)

        elif ord(c) >= 0x61 and ord(c) <= 0x7a:
            i = ord(c) - 0x61
            i = (a_inv * (i - b)) % 26
            output += chr(i + 0x61)

        else:
            output += c

    return output

#melakukan pemanggilan fungsi main
if __name__ == "__main__":
    print(decrypt("HFKN HRPIDMFS HFKN SVM ONF HFKN ORMFYFS KNGNA ODPFH OTD YEDZVSV DKKY GFZF", 3, 5))