# perancangan-analisi-algoritma
Repositori ini berisi penjelasan mengenai materi dari tugas yang dikerjakan oleh mahasiswa. Penjelasan beserta link setiap tugas telah tertera di bawah.

Dosen : Randi Proska Sandra, M.Sc<br>
Kode Kelas : INF1.62.4001 <br>
Seksi : 202423430074<br>
Mahasiswa : adinda denada (23343024)<br><br>

## Horner's Rule



<p align="justify">
Horner's Rule adalah algoritma untuk mengevaluasi polinomial yang diperkenalkan oleh William George Horner, meskipun metode ini telah digunakan oleh matematikawan Cina dan Persia sebelumnya. Algoritma ini memungkinkan evaluasi polinomial dengan jumlah operasi aritmatika minimal, yaitu nnn kali penjumlahan dan nnn kali perkalian untuk polinomial derajat</p>

<p align="justify">
Langkah-langkah algoritma Horner's rule adalah sebagai berikut: </p>
<ol>
 <li>Inisialisasi variabel result dengan nilai 0.</li>
 <li>Iterasi melalui setiap koefisien polinomial dari kiri ke kanan (koefisien pangkat tertinggi ke terendah).</li>
 <li>Perbarui hasil dengan rumus: result=result×x+coef\text{result} = \text{result} \times x + \text{coef}.</li>
 <li>Kembalikan hasil setelah semua koefisien diproses.</li>
</ol>
