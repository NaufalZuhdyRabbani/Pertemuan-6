import tkinter as tk

# Fungsi untuk menampilkan hasil prediksi
def hasil_prediksi():
    # Mengabaikan nilai input dan langsung menampilkan prodi Teknologi Informasi
    hasil_label.config(text="Prodi Pilihan: Teknologi Informasi", fg='blue', bg='lightyellow')

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.configure(bg='#87ceeb')  # Background jendela utama

# Membuat label judul
judul_label = tk.Label(root, 
                        text="Aplikasi Prediksi Prodi Pilihan", 
                        font=("Arial", 16), 
                        bg='#87ceeb', 
                        fg='white')
judul_label.grid(row=0, column=0, columnspan=2, pady=10)

# Membuat input nilai mata pelajaran
nilai_labels = []
nilai_entries = []

for i in range(1, 11):
    label = tk.Label(root, 
                     text=f"Nilai Mata Pelajaran {i}:", 
                     bg='#e0f7fa',  # Warna latar belakang label
                     fg='black')     # Warna teks label
    label.grid(row=i, column=0, padx=10, pady=5)

    entry = tk.Entry(root, 
                     width=15, 
                     bg='white', 
                     fg='black', 
                     relief=tk.RIDGE)
    entry.grid(row=i, column=1, padx=10, pady=5)

    nilai_labels.append(label)
    nilai_entries.append(entry)

# Membuat button untuk hasil prediksi dengan warna hijau
prediksi_button = tk.Button(root, 
                            text="Hasil Prediksi", 
                            command=hasil_prediksi,
                            bg="#4caf50",   # Background hijau
                            fg='white',
                            font=("Arial", 12))
prediksi_button.grid(row=11, column=0, columnspan=2, pady=10)

# Membuat label untuk menampilkan hasil prediksi dengan warna latar belakang
hasil_label = tk.Label(root, text="", font=("Arial", 14), bg='#87ceeb', fg='black')
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

# Menjalankan aplikasi
root.mainloop()