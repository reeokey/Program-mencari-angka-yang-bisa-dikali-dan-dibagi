def cari_angka_special():
    '''
    Fungsi ini mencari angka-angka dalam deret yang dapat dibagi
    dan dikali dengan angka tertentu.Penggunaan dapat memasukkan
    deret angka, angka pembagi, dan angka pengali.
    '''
    
    # meminta user untuk memasukkan deret angka
    input_deret = input("Masukkan deret angka (pisahkan dengan spasi): ")
    deret_angka =  [int(angka) for angka in input_deret.split()]
    
    # meminta pengguna memasukkan angka pembagi
    pembagi = int(input("Masukkan angka pembagi: "))
    
    # meminta pengguna memasukkan angka pengali
    pengali =  int(input("Masukkan angka pengali: "))
    
    # inisialisai list untuk menyimpan hasil
    angka_yang_bisa_dibagi = []
    angka_yang_bisa_dikali = []
    hasil_pembagian = []
    hasil_perkalian = []
    
    # iterasi melalui deret angka
    for angka in deret_angka:
     # memeriksa apakah angka dapat dibagi
     if angka % pembagi == 0:
       angka_yang_bisa_dibagi.append(angka)
       hasil_pembagian.append(angka / pembagi)
    
     # memeriksa apakah angka dapat dikali
     if angka % pengali == 0:
       angka_yang_bisa_dikali.append(angka)
       hasil_perkalian.append(angka * pengali)
    
    # menampilkan hasil
    print("\nDeret Angka:", deret_angka)
    print("Angka Yang Bisa Dibagi {}: {}".format(pembagi, angka_yang_bisa_dibagi))
    print("Hasil Pembagian:",hasil_pembagian)
    print("Angka Yang Bisa Dikali {}: {}".format(pengali, angka_yang_bisa_dikali))
    print("Hasil Perkalian:", hasil_perkalian)
    
# memanggil function / fungsi
cari_angka_special()
