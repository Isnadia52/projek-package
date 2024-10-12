# **Statistic Method**

**Statistic Method** adalah sebuah package yang dirancang untuk menyederhanakan pengolahan data numerik dalam bahasa Python. Package ini menawarkan berbagai method statistik yang mendukung analisis mendalam terhadap dataset, seperti perhitungan mean, median, modus, desil, kuartil, variansi, simpangan rata-rata, kurtosis, dan skewness. Setiap method memiliki peran penting dalam membantu pengguna menganalisis data secara efisien dan akurat. Dengan **Statistik Data**, pengguna dapat dengan mudah mengolah data numerik tanpa perlu mengimplementasikan algoritma statistik dari awal, sehingga mempermudah proses analisis secara keseluruhan.

``` import StatisticMethod ```

## **Mean**
Method ini berfungsi untuk menghitung nilai rata-rata dari suatu kolom, memberikan gambaran umum tentang titik tengah data, serta mempermudah perbandingan dalam analisis statistik.

``` StatisticMethod.mean(self, nama_kolom)```

Parameter: nama_kolom
Tipe: str
Deskripsi: Parameter ini digunakan untuk menentukan nama kolom dari mana data akan diambil untuk menghitung rata-rata. 

## **Median**
Method median menghitung nilai tengah dari suatu kolom, yang bermanfaat untuk memberikan representasi yang lebih akurat dari distribusi data, terutama ketika data mengandung nilai-nilai ekstrem.

``` StatisticMethod.median(self, nama_kolom) ```


## **Modus**
Method modus digunakan untuk menghitung nilai yang paling sering muncul dalam suatu kolom data. Mengetahui nilai method membantu dalam mengidentifikasi pola atau kecenderungan dalam dataset.

``` StatisticMethod.modus(self, nama_kolom) ```


## **Varians**
Method variansi memberikan informasi tentang seberapa jauh data tersebar dari nilai rata-rata. Method ini juga berguna untuk membandingkan variasi di antara beberapa grup data. Method ini berisi 2 function yaitu,  hitung varians sampel, hitung varians populasi dan penentuan jenis varians yang akan di pakai oleh pengguna

``` StatisticMethod.varians(self, nama_kolom, jenis_varians): ```


## **Desil**
Desil adalah method yang membagi data menjadi 10 bagian yang sama besar. Hal ini memungkinkan analisis yang lebih terperinci terkait distribusi data dalam setiap bagian.

``` StatisticMethod.decile(self, nama_kolom,k) ```


## **Kuartil**
Method kuartil berguna untuk membagi data menjadi empat bagian yang sama besar. Selain itu, method ini digunakan untuk menghitung rentang interkuartil (Q3 - Q1) yang memberikan informasi penting tentang penyebaran data.

``` StatisticMethod.quartile(self, nama_kolom) ```


## **Simpangan Baku**
Method simpangan baku menghitung ukuran variasi atau penyebaran data. Semakin kecil simpangan baku, semakin dekat nilai-nilai data terhadap rata-rata, dan sebaliknya.

``` StatisticMethod.standard_deviation(self, nama_kolom) ```


## **Simpangan Rata-Rata**
Method ini dirancang untuk menghitung simpangan rata-rata dari dataset, yang memberikan indikasi tentang tingkat sebaran data dan konsistensi nilai-nilai dalam dataset tersebut. Informasi ini dapat digunakan untuk mendukung pengambilan keputusan yang berbasis data.

``` StatisticMethod.mean_deviation(self, nama_kolom) ```


## **Skewness dan Kurtosis**
Method skewness mengukur derajat kemiringan distribusi data, sedangkan kurtosis memberikan informasi tentang bentuk distribusi, terutama apakah data menunjukkan distribusi yang lebih rata atau lebih memusat.

``` StatisticMethod.skewness_kurtosis() ```



---

**Statistic Method** mempermudah pengguna dengan memberikan akses langsung ke analisis statistik hanya dengan menghubungkan Python ke file Excel yang ada di komputer. Package ini menyediakan berbagai alat yang intuitif dan efisien untuk mendukung analisis statistik yang mendalam, menjadikannya solusi yang tepat bagi siapa pun yang ingin memproses data numerik dengan cepat dan akurat.


