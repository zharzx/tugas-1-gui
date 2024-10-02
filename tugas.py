import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung luas permukaan kubus
def hitung_kubus():
    try:
        sisi = float(entry_sisi.get())
        luas = 6 * (sisi ** 2)
        result_label.config(text=f"Luas Permukaan Kubus: {luas} unit²")
        result_label.grid(row=6, column=0, columnspan=2, pady=20)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk sisi kubus.")

# Fungsi untuk menghitung luas segitiga
def hitung_segitiga():
    try:
        alas = float(entry_alas.get())
        tinggi = float(entry_tinggi.get())
        luas = 0.5 * alas * tinggi
        result_label.config(text=f"Luas Segitiga: {luas} unit²")
        result_label.grid(row=6, column=0, columnspan=2, pady=20)
    except ValueError:
        messagebox.showerror("Input Error", "Masukkan nilai numerik yang valid untuk alas dan tinggi.")

# Fungsi untuk menampilkan input untuk menghitung kubus
def tampilkan_input_kubus():
    sembunyikan_semua_input()
    label_sisi.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_sisi.grid(row=3, column=1, padx=10, pady=10)
    button_hitung_kubus.grid(row=4, column=0, columnspan=2, pady=10)

# Fungsi untuk menampilkan input untuk menghitung segitiga
def tampilkan_input_segitiga():
    sembunyikan_semua_input()
    label_alas.grid(row=3, column=0, padx=10, pady=10, sticky="w")
    entry_alas.grid(row=3, column=1, padx=10, pady=10)
    label_tinggi.grid(row=4, column=0, padx=10, pady=10, sticky="w")
    entry_tinggi.grid(row=4, column=1, padx=10, pady=10)
    button_hitung_segitiga.grid(row=5, column=0, columnspan=2, pady=10)

# Fungsi untuk menyembunyikan semua input
def sembunyikan_semua_input():
    label_sisi.grid_forget()
    entry_sisi.grid_forget()
    button_hitung_kubus.grid_forget()

    label_alas.grid_forget()
    entry_alas.grid_forget()
    label_tinggi.grid_forget()
    entry_tinggi.grid_forget()
    button_hitung_segitiga.grid_forget()

# Fungsi untuk mengubah warna tombol saat di-hover
def on_enter(e):
    e.widget['background'] = '#007ACC'

def on_leave(e):
    e.widget['background'] = '#4CAF50' 

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Penghitung Luas oleh Moch Aris Rofii")
root.configure(bg="#f5f5f5")  # Mengatur warna background

# Label judul aplikasi
title_label = tk.Label(root, text="Penghitung Luas Bangun Datar & Ruang", font=("Helvetica", 16, "bold"), bg="#f5f5f5", fg="#333")
title_label.grid(row=0, column=0, columnspan=2, pady=20)

# Tombol untuk memilih rumus
label_pilihan = tk.Label(root, text="Pilih Rumus:", font=("Helvetica", 12), bg="#f5f5f5", fg="#333")
label_pilihan.grid(row=1, column=0, columnspan=2)

button_pilih_kubus = tk.Button(root, text="Hitung Luas Kubus", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=tampilkan_input_kubus, relief="flat", padx=20, pady=10)
button_pilih_kubus.grid(row=2, column=0, pady=10, padx=10)

button_pilih_segitiga = tk.Button(root, text="Hitung Luas Segitiga", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=tampilkan_input_segitiga, relief="flat", padx=20, pady=10)
button_pilih_segitiga.grid(row=2, column=1, pady=10, padx=10)

# Bagian input untuk kubus
label_sisi = tk.Label(root, text="Sisi Kubus:", font=("Helvetica", 12), bg="#f5f5f5")
entry_sisi = tk.Entry(root, font=("Helvetica", 12), width=10)
button_hitung_kubus = tk.Button(root, text="Hitung Luas Kubus", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=hitung_kubus, relief="flat", padx=10)

# Bagian input untuk segitiga
label_alas = tk.Label(root, text="Alas Segitiga:", font=("Helvetica", 12), bg="#f5f5f5")
entry_alas = tk.Entry(root, font=("Helvetica", 12), width=10)
label_tinggi = tk.Label(root, text="Tinggi Segitiga:", font=("Helvetica", 12), bg="#f5f5f5")
entry_tinggi = tk.Entry(root, font=("Helvetica", 12), width=10)
button_hitung_segitiga = tk.Button(root, text="Hitung Luas Segitiga", font=("Helvetica", 12), bg="#4CAF50", fg="white", command=hitung_segitiga, relief="flat", padx=10)

# Label untuk menampilkan hasil
result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f5f5f5", fg="#333")

# Tambahkan efek hover pada tombol
button_pilih_kubus.bind("<Enter>", on_enter)
button_pilih_kubus.bind("<Leave>", on_leave)
button_pilih_segitiga.bind("<Enter>", on_enter)
button_pilih_segitiga.bind("<Leave>", on_leave)
button_hitung_kubus.bind("<Enter>", on_enter)
button_hitung_kubus.bind("<Leave>", on_leave)
button_hitung_segitiga.bind("<Enter>", on_enter)
button_hitung_segitiga.bind("<Leave>", on_leave)

# Mengatur ukuran jendela secara otomatis
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())

# Menjalankan aplikasi
root.mainloop()