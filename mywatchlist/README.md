# Tautan menuju aplikasi Heroku yang sudah di deploy: 

Aplikasi HTML : https://tugas-3-pbp-inez.herokuapp.com/mywatchlist/HTML/

Aplikasi XML : https://tugas-3-pbp-inez.herokuapp.com/mywatchlist/XML/

Aplikasi JSON : https://tugas-3-pbp-inez.herokuapp.com/mywatchlist/JSON/

# Perbedaan antara JSON, XML, dan HTML

- JSON (JavaScript Object Notation) adalah sebuah format yang digunakan untuk menyimpan, membaca, serta menukar informasi dari web server sehingga dapat dibaca oleh para pengguna

- XML (Extensible Markup Language) adalah sebuah markup language dan format file untuk menyimpan, mentransmisikan, dan merekonstruksi data arbitrer.

- HTML (HyperText Markup Language) adalah sebuah markup language untuk dokumen yang dirancang untuk ditampilkan di browser web 

# Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan untuk memudahkan user untuk mengirim data dari satu platform ke platform lainnya.

# Bagaimana cara kamu mengimplementasikan checklist di atas
1. Membuka folder dan repository yang saya gunakan untuk tugas 2 PBP
2. Membuat dan menyalakan virtual environment
3. Membuat django-app bernama mywatchlist
4. Membuka file models.py di folder wishlist, kemudian saya membuat model bernama WatchList dengan fields watched, title, rating, release_date, dan review. 
5. Melakukan migrasi agar model terbuat pada database
6. Buatlah sebuah folder bernama fixtures di dalam folder aplikasi wishlist dan buatlah sebuah berkas bernama initial_mywatchlist_data.json, isi 10 data film
7. Jalankan perintah python manage.py loaddata initial_mywatchlist_data.json untuk memasukkan data tersebut ke dalam database Django lokal
8. Mengimplimentasi Views dengan cara membuka berkas views.py pada folder mywatchlist dan buatlah sebuah fungsi yang menerima parameter request dan mengembalikan render(request, "mywatchlist.html")
9. Membuka berkas urls.py yang ada pada folder project_django dengan menambahkan potongan kode path('mywatchlist/', include('mywatchlist.urls')), pada variabel urlpatterns
10. Melakukan add, commit, dan push ke repository github
11. Melakukan deployment ke heroku dengan cara menghubungkan heroku dan akun github (masukkan email dan password), update app name, dan deploy projek saya


# Screenshot tiga URL menggunakan Postman
- HTML

![Screenshot (800)](https://user-images.githubusercontent.com/112611192/191660935-d3fc1a9b-eb5d-40a2-8d3b-87886b562b23.png)

- JSON

![Screenshot (802)](https://user-images.githubusercontent.com/112611192/191661089-858b956f-21ab-4a9a-9c94-bec0b3efe47f.png)

- XML

![Screenshot (801)](https://user-images.githubusercontent.com/112611192/191661157-330db4f6-8b0c-4704-b107-405e56ed606d.png)

