Link menuju aplikasi Heroku yang sudah kamu deploy
https://tugas-2-pbp-inez.herokuapp.com/katalog/


Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html;


Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Jawab : 
virtual environment (lingkungan virtual) berfungsi untuk memisahkan pengaturan dan package yang diinstal pada setiap proyek Django sehingga perubahan yang dilakukan pada satu proyek tidak mempengaruhi proyek lainnya. Dengan kata lain, setiap proyek Django sebaiknya memiliki virtualenv-nya sendiri

Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.
Jawab :
1. Membuat sebuah fungsi pada views.py yang dapat melakukan pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

2. Membuat sebuah routing untuk memetakan fungsi yang telah kamu buat pada views.py.

3. Memetakan data yang didapatkan ke dalam HTML dengan sintaks dari Django untuk pemetaan data template.

4. Melakukan deployment ke Heroku terhadap aplikasi yang sudah kamu buat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

 Pada file views.py di folder katalog membuat fungsi yang menerima parameter request dan mengembalikan render :  def show_katalog(request):
                                return render(request, "katalog.html", context).

    Pada folder katalog terdapat folder templates yang di dalamnya terdapat file katalog.html beserta isinya. Pada template isi tersebut terdapat code   <h5>Name: </h5> dan <h5>Student ID: </h5> diubah menjadi <h5>Name: </h5> dan <h5>Student ID: </h5>
                    <p>Fill me!</p>     <p>Fill me!</p>                      <p>{{nama}}</p>     <p>{{NPM}}</p>
    Selain itu juga menambahkan {% for katalog in list_katalog_barang %}
                                    <tr>
                                        <th>{{katalog.item_name}}</th>
                                        <th>{{katalog.item_price}}</th>
                                        <th>{{katalog.item_stock}}</th>
                                        <th>{{katalog.rating}}</th>
                                        <th>{{katalog.description}}</th>
                                        <th>{{katalog.item_url}}</th>
                                    </tr>
                                {% endfor %}
                                </table>.

    Pada folder katalog dengan file urls.py ditambahkan code from django.urls import path
                                                            from katalog.views import show_katalog
                                                            app_name = 'katalog'
                                                            urlpatterns = [
                                                                path('', show_katalog, name='show_katalog'),
                                                            ]
    yang berguna untuk melakukan routing terhadap fungsi views.py sehingga halaman HTML dapat dapat ditampilkan pada browser.

    Pada folder project_django terdapat file urls.py dimana ditambahkan code path('katalog/', include('katalog.urls')),