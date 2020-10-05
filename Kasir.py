nama = str(input('Masukan Nama Barang :'))
harga = int(input('Masukan Harga Barang : '))
jumlah = int(input('Masukan Jumlah Barang : '))

hitung = harga * jumlah

if hitung >= 100000:
    diskon = hitung * (10/100)
    total = hitung - diskon
    print('Yang Harus Anda Bayarkan Untuk', jumlah, nama, 'adalah', total)
else:
    print('Yang Harus Anda Bayarkan Untuk', jumlah, nama, 'adalah', hitung)
