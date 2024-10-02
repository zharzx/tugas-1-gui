import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menghitung luas segitiga
def hitung_luas_segitiga():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        luas = 0.5 * alas * tinggi
        label_hasil.config(text=f"Luas Segitiga: {luas:.2f} unit²")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk alas dan tinggi.")

# Fungsi untuk menghitung luas permukaan kubus
def hitung_luas_kubus():
    try:
        sisi = float(entry_sisi.get())
        luas_permukaan = 6 * (sisi ** 2)
        label_hasil.config(text=f"Luas Permukaan Kubus: {luas_permukaan:.2f} unit²")
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk sisi kubus.")

# Fungsi untuk mengubah tampilan ke mode hitung luas segitiga
def tampil_segitiga():
    frame_kubus.pack_forget()
    frame_segitiga.pack(pady=10)

# Fungsi untuk mengubah tampilan ke mode hitung luas kubus
def tampil_kubus():
    frame_segitiga.pack_forget()
    frame_kubus.pack(pady=10)

# Membuat window
root = tk.Tk()
root.title("Penghitung Luas Bangun Datar & Ruang")
root.geometry("400x400")
root.configure(bg="#F5F5F5")

# Gaya tombol
style = ttk.Style()
style.configure("TButton", font=("Montserrat", 10), padding=6)

# Judul Aplikasi
label_judul = tk.Label(root, text="Penghitung Luas Bangun Datar & Ruang", font=("Montserrat", 14, "bold"), bg="#F5F5F5")
label_judul.pack(pady=20)

# Tombol untuk memilih perhitungan
frame_pilih = tk.Frame(root, bg="#F5F5F5")
frame_pilih.pack(pady=10)

btn_segitiga = ttk.Button(frame_pilih, text="Hitung Luas Segitiga", command=tampil_segitiga, style="TButton")
btn_segitiga.grid(row=0, column=0, padx=10)

btn_kubus = ttk.Button(frame_pilih, text="Hitung Luas Kubus", command=tampil_kubus, style="TButton")
btn_kubus.grid(row=0, column=1, padx=10)

# Frame untuk input segitiga
frame_segitiga = tk.Frame(root, bg="#F5F5F5")

label_alas = tk.Label(frame_segitiga, text="Alas Segitiga:", font=("Montserrat", 10), bg="#F5F5F5")
label_alas.grid(row=0, column=0, padx=10, pady=5)
entry_alas = ttk.Entry(frame_segitiga, font=("Montserrat", 10), width=10)
entry_alas.grid(row=0, column=1, pady=5)

label_tinggi = tk.Label(frame_segitiga, text="Tinggi Segitiga:", font=("Montserrat", 10), bg="#F5F5F5")
label_tinggi.grid(row=1, column=0, padx=10, pady=5)
entry_tinggi = ttk.Entry(frame_segitiga, font=("Montserrat", 10), width=10)
entry_tinggi.grid(row=1, column=1, pady=5)

btn_hitung_segitiga = ttk.Button(frame_segitiga, text="Hitung Luas Segitiga", command=hitung_luas_segitiga, style="TButton")
btn_hitung_segitiga.grid(row=2, columnspan=2, pady=10)

# Frame untuk input kubus
frame_kubus = tk.Frame(root, bg="#F5F5F5")

label_sisi = tk.Label(frame_kubus, text="Sisi Kubus:", font=("Montserrat", 10), bg="#F5F5F5")
label_sisi.grid(row=0, column=0, padx=10, pady=5)
entry_sisi = ttk.Entry(frame_kubus, font=("Montserrat", 10), width=10)
entry_sisi.grid(row=0, column=1, pady=5)

btn_hitung_kubus = ttk.Button(frame_kubus, text="Hitung Luas Kubus", command=hitung_luas_kubus, style="TButton")
btn_hitung_kubus.grid(row=1, columnspan=2, pady=10)

# Label untuk menampilkan hasil
label_hasil = tk.Label(root, text="Hasil akan ditampilkan di sini", font=("Montserrat", 12), bg="#F5F5F5")
label_hasil.pack(pady=20)

# Menampilkan frame segitiga secara default
tampil_segitiga()

# Menjalankan aplikasi
root.mainloop()
