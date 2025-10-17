import random
import time

print(" Sistem Pengendali Suhu dan Kelembaban Otomatis \n")

# Nilai standar dan toleransi
Ss = 25.0  # Suhu standar (°C)
Ts = 2.0   # Toleransi suhu (°C)
Ks = 60.0  # Kelembaban standar (%)
Tk = 5.0   # Toleransi kelembaban (%)

# Loop hanya 5 kali
for i in range(5):
    print(f"--- Pembacaan Sensor ke-{i+1} ---")

    # Simulasi pembacaan sensor
    Sa = round(random.uniform(20.0, 30.0), 1)
    Ka = round(random.uniform(50.0, 70.0), 1)

    print(f"Suhu: {Sa}°C | Kelembaban: {Ka}%")

    # Logika kontrol suhu
    if Sa < (Ss - Ts):
        print("Tindakan: Aktifkan Pemanas")
    elif Sa > (Ss + Ts):
        print("Tindakan: Aktifkan Pendingin")
    else:
        print("Tindakan: Suhu Stabil")

    # Logika kontrol kelembaban
    if Ka < (Ks - Tk):
        print("Tindakan: Aktifkan Pelembab\n")
    elif Ka > (Ks + Tk):
        print("Tindakan: Aktifkan Pengering\n")
    else:
        print("Tindakan: Kelembaban Stabil\n")

    time.sleep(2)  # jeda 2 detik sebelum pembacaan berikutnya

print("=== Simulasi Selesai ===")
