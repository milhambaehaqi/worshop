Struktur Data Pandas
Saya telah menyebutkan salah satu struktur data pandas di atas, DataFrame. Saya akan menjelaskan struktur data ini di dalam section ini sebagai tambahan untuk struktur data pandas lainnya, Series. Ada struktur data lainnya bernama Panel, namun saya tidak akan menjelaskan itu di dalam tutorial ini karena itu tidak sering digunakan, seperti yang disebutkan di dalam dokumentasi. DataFrame adalah struktur data 2D, Series adalah struktur data 1D, dan Panel adalah struktur data 3D dan lebih tinggi.

DataFrame
DataFrame adalah struktur data tabular yang disusun pada kolom dan baris berurut. Untuk membuatnya lebih jelas, mari lihat contoh pembuatan sebuah DataFrame (tabel) dari kamus sebuah daftar. Contoh berikut menunjukkan sebuah kamus berisi dua kunci, Name dan Age, dan daftar nilainya.

import pandas as pd
import numpy as np
 
name_age = {'Name' : ['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
'Age' : [32, 55, 20, 43, 30]}
data_frame = pd.DataFrame(name_age)
print data_frame

Perhatikan bahwa constructor DataFrame mengurutkan kolom secara alfabetis. Jika kamu ingin mengubah urutan kolom, kamu dapat mengetikkan hal berikut di bawah data_frame di atas:

1
data_frame_2 = pd.DataFrame(name_age, columns = ['Name', 'Age'])
Untuk melihat hasilnya, cukup ketik: print data_frame_2.

Katakan kamu tidak ingin menggunakan label default 0,1,2..., dan ingin menggunakan a, b, c,... sebagai gantinya. Dalam kasus itu, kamu dapat menggunakan index di dalam script di atas sebagai berikut:

1
data_frame_2 = pd.DataFrame(name_age, columns = ['Name', 'Age'], index = ['a', 'b', 'c', 'd', 'e'])
Itu sangat bagus, bukan? Dengan menggunakan DataFrame, kita dapat melihat data kita tertata dalam sebuah bentuk tabular.

Series
Series adalah struktur data pandas kedua yang akan saya bicarakan. Series adalah object satu dimensi (1D) yang serupa dengan kolom di dalam tabel. Jika kita ingin membuat sebuah Series untuk daftar nama, kita dapat melakukan di bawah ini:

series = pd.Series(['Ali', 'Bill', 'David', 'Hany', 'Ibtisam'],
index = [1, 2, 3, 4, 5])
print series

Function Pandas
Dalam section ini, saya akan menunjukkan contoh beberapa function yang dapat kita gunakan dengan DataFrame dan Series.

Head dan Tail
Function head() dan tail() mengijinkan kita untuk melihat sebuah sampel data, khususnya ketika kita memiliki jumlah entri yang besar. Jumlah default dari elemen yang ditampilkan adalah 5, namun kamu dapat mengkustomasi angkanya sesukamu.

Mari katakan kita memiliki sebuah Series yang disusun dari 20,000 item (angka) secara acak:


import pandas as pd
import numpy as np
series = pd.Series(np.random.randn(20000))
Dengan menggunakan method head() dan tail() untuk mengamati lima item pertama dan lima item terakhir, kita dapat melakukan di bawah ini:


print series.head()
print series.tail()

Add
Mari ambil contoh function add(), dimana kita akan berusaha untuk menambahkan dua data frames sebagai berikut:

import pandas as pd
 
dictionary_1 = {'A' : [5, 8, 10, 3, 9],
'B' : [6, 1, 4, 8, 7]}
dictionary_2 = {'A' : [4, 3, 7, 6, 1],
'B' : [9, 10, 10, 1, 2]}
data_frame_1 = pd.DataFrame(dictionary_1)
data_frame_2 = pd.DataFrame(dictionary_2)
data_frame_3 = data_frame_1.add(data_frame_2)
print data_frame_1
print data_frame_2
print data_frame_3

Kamu dapat juga melakukan proses penambahan ini dengan cukup menggunakan operator +: data_frame_3 = data_frame_1 + data_frame_2.

Describe
Sebuah function pandas yang sangat bagus adalah describe(), yang membuat berbagai ringkasan statistik data kita. Sebagai contoh dalam section terakhir, mari lakukan berikut ini:

print data_frame_3.describe()

Sumber Lebih Lanjut
Ini hanyalah sebuah goresan pada permukaan pandas dalam Python. Untuk lebih detail, kamu dapat memeriksa dokumentasi pandas, dan kamu juga dapat memeriksa beberapa buku seperti Mempelajari Pandas dan Menguasai Pandas.

Kesimpulan
Ilmuwan terkadang perlu melakukan beberapa operasi statistik dan menampilkan beberapa grafik rapi yang menuntut mereka untuk menggunakan sebuah bahasa pemrograman. Namun, pada saat yang sama, mereka tidak ingin menghabiskan terlalu banyak waktu atau dihadapkan dengan kurva pembelajaran yang serius dalam melakukan tugas semacam itu.

Seperti yang kita lihat dalam tutorial ini, pandas mengijinkan kita untuk menyajikan ulang data dalam bentuk tabular dan melakukan beberapa operasi pada tabel tersebut dalam cara yang sangat sederhana. Dengan mengkombinasikan pandas dengan librari Python lainnya, ilmuwan bahkan dapat melakukan lebih banyak tugas lanjutan seperti menggambar grafik khusus untuk data mereka.

Dengan demikian, pandas merupakan sebuah librari dan titik awal yang berguna untuk ilmuwan, ahli ekonomi, ahli statistik, dan siapapun yang ingin melakukan beberapa tugas analisis data.