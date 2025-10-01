Tugas 2
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, membuat sebuah proyek Django baru dengan menjalankan perintah django-admin startproject football_shop . lalu menjalankan server.
Kedua, membuat aplikasi dengan nama main pada proyek tersebut dengan menjalankan perintah python manage.py startapp main. Direktori main akan berisi struktur awal untuk aplikasi Django. Lalu, mendaftarkan aplikasi main ke dalam proyek dengan cara menambahkan 'main' pada INSTALLED_APPS.
Ketiga, membuat dan mengisi berkas main.html sesuai dengan yang ingin ditampilkan yaitu nama aplikasi, nama, npm, dan kelas.
Keempat, membuat model pada aplikasi main dengan nama Product dan menambahkan atribut-atribut (name, price, description, thumbnail, category, dan is_featured).
Kelima, membuat fungsi show_main pada views.py untuk dikembalikan ke dalam template HTML yaitu main.html yang menampilkan nama aplikasi, nama, npm, dan kelas.
Keenam, melakukan sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py dengan cara menjalankan perintah berikut.
from django.urls import path
from main.views import show_main
app_name = 'main'
urlpatterns = [
    path('', show_main, name='show_main'),
]
di mana terdapat satu route '' yang akan memanggil view show_main. Kemudian melengkapi rute URL ke aplikasi main dengan menambahkan urls.py pada level proyek agar proyek dapat melakukan pemetaan ke rute URL pada aplikasi main.
Ketujuh, simpan semua perubahan ke GitHub dan PWS dengan melakukan add, commit, dan push.

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![bagan](images/bagan.png)

3. Jelaskan peran settings.py dalam proyek Django!
settings.py berperan sebagai pusat konfigurasi yang mengatur bagaimana aplikasi berjalan. Settings.py menentukan aplikasi apa yang digunakan (INSTALLED_APPS), mengatur database, mengatur lokasi file, dan mengatur keamanan (ALLOWED_HOSTS dan lain-lain).

4. Bagaimana cara kerja migrasi database di Django?
Migrasi adalah cara Django melacak perubahan pada model basis data. Pertama jalankan perintah python manage.py makemigrations untuk menciptakan berkas migrasi yang berisi perubahan model yang belum diaplikasikan ke dalam basis data. Lalu, jalankan perintah python manage.py migrate untuk mengaplikasikan perubahan model yang tercantum dalam berkas migrasi ke basis data.

5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django memiliki struktur yang jelas, memiliki banyak fitur bawaan yang sudah siap pakai, efisien dan hemat biaya, serta memiliki keamanan yang baik.

6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Tidak ada

Tugas 3
1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery diperlukan dalam pengimplementasian sebuah platform untuk memindahkan dan mendistribusikan data secara efisien, serta memungkinkan analisis data yang akurat sebab dalam mengembangkan suatu platform, ada saat di mana kita perlu mengirimkan data dari satu stack ke stack lainnya.

2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, JSON lebih sesuai untuk API web modern. JSON lebih populer dibandingkan XML karena JSON lebih mudah dibaca dan dimengerti di mana setiap elemennya mendeskripsikan dirinya sendiri atau self describing. Selain itu, meskipun sintaks JSON berasal dari objek JavaScript, JSON sebenarnya adalah format text.

3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() pada form Django berfungsi untuk memvalidasi data formulir sehingga mencegah kesalahan data dan menjaga keamanan dalam aplikasi web.

4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token adalah token unik yang dibuat server untuk setiap sesi pengguna dan disertakan dalam formulir, lalu server akan memverifikasi token tersebut saat terdapat request untuk memastikan request tersebut berasal dari pengguna yang sah. csrf_token dibutuhkan saat membuat form di Django untuk melindungi dari serangan CSRF, yaitu serangan keamanan yang memanfaatkan authenticated cookie korban untuk melakukan aksi tidak sah dari situs lain. Jika kita tidak menambahkan csrf_token pada form Django, Django akan menolak request, tetapi jika proteksi csrf juga dinonaktifkan, Django dapat menerima request tanpa mengecek token. Hal ini dapat dimanfaatkan oleh penyerang dengan cara mengirim form tidak sah menggunakan cookie korban.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, membuat suatu skeleton sebagai kerangka views.
Kedua, membuat form untuk menginput dan menampilkan data Football Shop pada aplikasi yaitu dengan menambahkan file forms.py pada folder main. Kemudian, menambahkan file views.py pada folder main dan menambahkan fungsi show_main(), create_product(), dan show_product(). Lalu, menambahkan path url pada urls.py.
Ketiga, menambahkan tombol "Add" yang akan redirect ke halaman form. Lalu, menambahkan file create_product.html yang menampilkan halaman form input dan file product_detail.html yang menampilkan detail dari suatu produk.
Keempat, mengembalikan data dalam bentuk XML yaitu dengan menambahkan fungsi show_xml pada views.py lalu menambahkan path url pada urls.py.
Kelima, mengembalikan data dalam bentuk JSON yaitu dengan menambahkan fungsi show_json pada views.py lalu menambahkan path url pada urls.py.
Keenam, mengembalikan data berdasarkan id dalam bentuk XML yaitu dengan menambahkan fungsi show_xml_by_id pada views.py lalu menambahkan path url pada urls.py.
Ketujuh, mengembalikan data berdasarkan id dalam bentuk JSON yaitu dengan menambahkan fungsi show_json_by_id pada views.py lalu menambahkan path url pada urls.py.

6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada

Screenshot Postman:
![bentuk XML](images/show_xml.png)
![bentuk JSON](images/show_json.png)
![bentuk XML berdasarkan ID](images/show_xml_by_id.png)
![bentuk JSON berdasarkan ID](images/show_json_by_id.png)

Tugas 4
1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah form bawaan dari framework Django yang digunakan untuk proses login user dengan memastikan bahwa username dan password yang dimasukkan sesuai dengan data yang tersimpan di database.
Kelebihannya adalah memiliki fitur autentikasi lengkap, dirancang dengan fitur keamanan yang kuat, dapat disesuaikan untuk kebutuhan spesifik proyek, dan menyediakan kerangka kerja yang sudah siap pakai untuk menangani proses login dan register.
Kekurangannya adalah terbatas pada field bawaan yaitu username dan password saja sehingga jika perlu login dengan field custom, harus membuat subclass sendiri.

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaimana Django mengimplementasikan kedua konsep tersebut?
Autentikasi memverifikasi identitas user melalui password, sidik jari, atau biometrik lainnya, sedangkan otorisasi menentukan hak akses di mana otorisasi memberikan atau menolak akses ke sumber daya atau fungsi tertentu berdasarkan permission dan peran user yang terautentikasi.
Autentikasi ditangani oleh modul django.contrib.auth (fungsi authenticate(), login(), logout(), backends).
Otorisasi ditangani oleh modul django.contrib.auth lewat sistem permissions, groups, dan decorator seperti @login_required atau @permission_required.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Kelebihan session yaitu lebih aman karena data sensitif disimpan di server sehingga tidak terlihat user, dapat menyimpan data yang lebih besar, cocok untuk data sensitif, dan berfungsi sebagai memori jangka pendek karena menyimpan informasi tentang aktivitas user selama waktu session.
Kekurangan session yaitu terbatas pada durasi session di mana data akan hilang ketika session habis serta meningkatkan beban server karena menyimpan datanya di server.
Kelebihan cookies yaitu mengurangi beban server karena data disimpan di browser, memungkinkan data disimpan dalam jangka panjang, dan dapat digunakan untuk berbagi token sesi antar subdomain dalam satu aplikasi.
Kekurangan cookies yaitu hanya dapat menyimpan data dalam jumlah kecil sehingga tidak cocok untuk data besar, berpotensi masalah privasi karena dapat digunakan untuk melacak user, dan rentan terhadap serangan.

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Penggunaan cookies tidak sepenuhnya aman secara default karena terdapat risiko serangan seperti CSRF dan XSS. Django menangani hal tersebut dengan menyediakan perlindungan bawaan, seperti penandaan cookie dengan HttpOnly dan Secure, serta atribut SameSite untuk mengurangi serangan CSRF.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, membuat fungsi dan form registrasi dengan cara menambahkan fungsi register pada views.py yang berfungsi untuk menghasilkan form registrasi secara otomatis dan menghasilkan akun pengguna ketika data di-submit dari form. Lalu, membuat file register.html pada direktori main/templates. Kemudian, lakukan routing di urls.py.
Kedua, membuat fungsi login dengan cara menambahkan fungsi login_user pada views.py yang berfungsi untuk mengautentikasi pengguna yang ingin login. Kemudian, membuat file login.html pada direktori main/templates. Lalu, lakukan routing di urls.py.
Ketiga, membuat fungsi logout dengan cara menambahkan fungsi logout_user pada views.py yang berfungsi untuk melakukan mekanisme logout. Kemudian, menambahkan button logout pada main.html. Lalu, lakukan routing di urls.py.
Keempat, merestriksi akses halaman main dan shop detail dengan cara menambahkan decorator login_required pada fungsi show_main dan show_product.
Kelima, menambahkan last_login yang berisi timestamp terakhir kali pengguna melakukan login dengan memodifikasi fungsi login_user dan logout_user.
Keenam, menghubungkan model Product dengan User dengan menambahkan user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) pada class Product yang berfungsi untuk menghubungkan satu product dengan satu user melalui sebuah relationship.
Ketujuh, me-run server lalu mencoba melakukan registrasi, login dan menambahkan data.

Tugas 5
1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
1) Inline style yaitu CSS langsung di atribut elemen (<div style="color: red;">)
2) ID selector (#idname)
3) Class, pseudo-class, attribute selector (.classname, :hover, [type="text"])
4) Element/tag selector (div, p, h1)
5) Universal selector (*) dan inheritance

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Responsive design penting untuk aplikasi web karena memastikan pengalaman pengguna (UX) yang konsisten dan optimal di semua perangkat (mobile ataupun desktop) sehingga meningkatkan kepuasan pengguna, membantu aplikasi web lebih mudah ditemukan dan mendapatkan peringkat yang lebih tinggi di mesin pencarian seperti Google, serta menghemat waktu dan biaya pengembangan dan pemeliharaan karena hanya memerlukan satu kode dasar untuk berbagai ukuran layar.
Contoh aplikasi yang sudah menerapkan responsive design adalah Instagram sehingga ketika dibuka di laptop tampil grid, di HP tampil feed 1 kolom.
Contoh aplikasi yang belum menerapkan responsive design adalah website lama suatu institusi sehingga biasanya teks terlalu kecil di HP, layout melebar, tabel rusak. Hal ini dikarenakan layout fix pakai pixel absolute, bukan persentase/viewport.

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah ruang luar antara elemen dengan elemen lain. Border adalah garis tepi kotak yang mengelilingi content dan padding. Padding adalah ruang dalam antara content dengan border.
Untuk mengimplementasikannya, gunakan properti CSS, misalnya
.box {
  margin: 20px;
  border: 2px solid black;
  padding: 10px;
}

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box dan grid layout adalah dua sistem layout CSS untuk menyusun elemen pada halaman web, di mana flex box cocok untuk tata letak satu dimensi dan mengutamakan fleksibilitas konten, sedangkan grid dirancang untuk tata letak dua dimensi dengan kontrol lebih besar untuk struktur halaman yang kompleks. Kegunaannya adalah Flexbox untuk menata komponen, sedangkan Grid untuk mengatur garis besar seluruh halaman. 

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
Pertama, menambahkan Tailwind ke aplikasi.
Kedua, menambahkan fitur edit product pada aplikasi dengan menambahkan fungsi edit_product pada views.py dan menambah file edit_product.html. Lalu, lakukan routing pada urls.py. Tambahkan juga tombol edit pada main.html.
Ketiga, menambahkan fitur hapus product pada aplikasi dengan menambahkan fungsi delete_product pada views.py. Lalu, routing pada urls.py. Tambahkan juga tombol delete pada main.html.
Keempat, menambahkan navigation bar pada aplikasi dengan membuat file navbar.html. Lalu tautkan navbar ke dalam main.html.
Kelima, konfigurasi static files pada aplikasi dengan menambahkan middleware WhiteNoise pada settings.py.
Keenam, lakukan styling pada aplikasi dengan tailwind dan external CSS. Caranya yaitu dengan menambahkan global.css lalu hubungkan global.css dan script tailwind ke base.html. Setelah itu, tambahkan custom styling ke global.css. Kemudian, lakukan styling navbar pada navbar.html, styling halaman login pada login.html, styling halaman register pada register.html, styling halaman home pada card_product.html, styling halaman detail product pada product_detail.html, styling halaman create product pada create_product.html, dan styling halaman edit product pada edit_product.html.