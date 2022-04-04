# fungsi enkripsi
# enkripsi to dekripsi
# enkripsi = SATU SEMBILAN SATU NOL DUA SATU DELAPAN TUJUH DIMAS DWI PRIYONO ITTP JAYA
# keynya adalah 3 dan 5

def encrypt(s, a, b):
    output = ''

    # Fungsi perulangan untuk mencari hasil dari modulo 26
    for c in s:

        # pernyataan kondisi untuk menentukan alfabet hasil dari modulo 26
        if ord(c) >= 0x41 and ord(c) <= 0x5a:
            i = ord(c) - 0x41
            i = (i * a + b) % 26
            output += chr(i + 0x41)

        elif ord(c) >= 0x61 and ord(c) <= 0x7a:
            i = ord(c) - 0x61
            i = (i * a + b) % 26
            output += chr(i + 0x61)

        else:
            output += c

    return output

# memanggil fungsi untuk dicetak
if __name__ == "__main__":
    # masukkan kalimat enkripsi sesuai ketentuan dengan key a dan b sesuai dengan ketentuan.
    print(encrypt("SATU SEMBILAN SATU NOL DUA SATU DELAPAN TUJUH DIMAS DWI PRIYONO ITTP JAYA", 3, 5))