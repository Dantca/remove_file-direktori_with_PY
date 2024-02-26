import os 
print("Hallo user welcome TO reality show!!")
users_new=input("apakah kamu ingin menghapus file direktori?(Y/N)\n").capitalize()
if users_new not in ("N","Y"):
    print("kamu memasukan data yang salah bisa mengulangi lagi yah !!")
if users_new == "N" :
     print("kamu telah melawati hidup yang begitu bagus")
if users_new == "Y":
    try : 
      user_masuk = input("kamu ingin menghapus direktori atau file? (dir/file)\n ").lower()
      if user_masuk not in ("dir", "file") :
        print(f'kamu memasukan data yang salah tolol {user_masuk} ')
    except OSError: 
        print("kamu gagal masukan data dengan benar") 
        print("kamu gagal memasukan data dengan benar")
    if user_masuk == "dir": 
       try : 
           lokasi_dir = input("masukan lokasi direktori yang ingin di hapus : \n")
           os.rmdir(lokasi_dir)
           print ("direktori berhasil di hapus  < < dont cry  > >")
       except FileNotFoundError :
             print("lokasi yang kamu masukan gagal")
    if user_masuk == "file":
           try : 
               lokasi_file = input("masukan lokasi file yang ingin di hapus\n")
               os.remove(lokasi_file)
               print("kamu berhasil menghapus file jadi jangan menangis dengan kejadian ini yah !! ")
           except FileNotFoundError :
               print("tidak di temukan file yang di maksud")
           except OSError :
               print("kamu gagal menghapus file")           
print (" kode Berhasil di akhiri !! have fun the cyber space")
