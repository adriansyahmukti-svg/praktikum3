# ===============================================
# Program Kasir Sederhana (Tanpa Input Manual)
# ===============================================

print("=== Program Kasir Sederhana ===\n")

# Data sudah ditentukan langsung di dalam program
harga = 20000          # Harga per unit barang
jumlah = 2             # Jumlah barang
diskon_persen = 10     # Diskon tetap 10%

# Perhitungan otomatis
total = harga * jumlah
diskon = total * (diskon_persen / 100)
total_akhir = total - diskon

# Tampilkan hasil
print("=== HASIL PERHITUNGAN ===")
print(f"Harga per unit       : Rp {harga}")
print(f"Jumlah barang        : {jumlah}")
print(f"Total sebelum diskon : Rp {total}")
print(f"Diskon ({diskon_persen}%)        : Rp {int(diskon)}")
print(f"Total setelah diskon : Rp {int(total_akhir)}")
