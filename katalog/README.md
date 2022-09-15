Link menuju aplikasi Heroku yang sudah kamu deploy
https://tugas-2-pbp-inez.herokuapp.com/katalog/


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;
Jawab :![tugas 2 pbp](https://user-images.githubusercontent.com/112611192/190313674-727cc450-b0c4-4bca-b1c1-b0a4cc0ad4f3.jpg)

Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab : 
virtual environment (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Dengan kata lain, setiap proyek Django sebaiknya memiliki virtualenv-nya sendiri


Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab :
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
