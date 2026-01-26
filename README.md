# Courier Incident Log Module

Modul ini digunakan untuk mencatat dan menangani insiden operasional kurir secara sederhana dan terstruktur.

## Manual Testing – Incident Workflow

Langkah berikut digunakan untuk menguji alur utama modul **Courier Incident Log**:

### 1. Create Incident

1. Login ke Odoo sebagai **Internal User**.
2. Buka menu **Courier Core → Insiden**.
3. Klik tombol **NEW**.
4. Isi data berikut:

   * Judul Insiden
   * Pelanggan
   * Tipe Insiden
   * Urgensi
   * No. Resi
   * Waktu Insiden (Sudah otomatis terisi, mengambil waktu sekarang)
   * Kronologi
   * Catatan
5. Sudah Automate **Save**.
6. Pastikan status awal insiden adalah **Draft**.

---

### 2. Mark Follow-up

1. Buka data insiden dengan status **Draft**.
2. Klik tombol **Mark Follow Up** di bagian header.
3. Status insiden berubah menjadi **Follow Up**.
4. Isi **Catatan Follow-up** jika diperlukan.
5. Sudah Automate **Save**.

---

### 3. Resolve Incident

1. Buka insiden dengan status **Follow Up**.
2. Klik tombol **Resolve**.
3. Pastikan Catatan sudah diisi jika belum ada peringatan
4. Status insiden berubah menjadi **Done**.


