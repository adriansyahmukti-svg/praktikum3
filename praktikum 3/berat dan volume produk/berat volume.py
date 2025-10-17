
import random
import time

print("=== Sistem Otomatis Pengecekan Berat dan Volume Produk ===")
print("Simulasi berjalan...\n")

# nilai standar dan toleransi
berat_standar = 500.0
toleransi_berat = 5.0
volume_standar = 350.0
toleransi_volume = 5.0

for i in range(5):
    print("Data ke-", i+1)
    
    # Simulasi data 
    berat = round(random.uniform(490.0, 510.0), 1)
    volume = round(random.uniform(340.0, 360.0), 1)

    print("Berat produk  :", berat, "gram")
    print("Volume produk :", volume, "ml")

    # Cek berat
    if berat < (berat_standar - toleransi_berat):
        print("Status berat  : Terlalu ringan")
    elif berat > (berat_standar + toleransi_berat):
        print("Status berat  : Terlalu berat")
    else:
        print("Status berat  : Sesuai standar")

    # Cek volume
    if volume < (volume_standar - toleransi_volume):
        print("Status volume : Kurang isi")
    elif volume > (volume_standar + toleransi_volume):
        print("Status volume : Kelebihan isi")
    else:
        print("Status volume : Sesuai standar")

    # Hasil akhirnya
    if ((berat_standar - toleransi_berat) <= berat <= (berat_standar + toleransi_berat)) and \
       ((volume_standar - toleransi_volume) <= volume <= (volume_standar + toleransi_volume)):
        print("Kesimpulan    : Produk lulus uji\n")
    else:
        print("Kesimpulan    : Produk gagal uji\n")

    time.sleep(1)
