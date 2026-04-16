#Memanggil library pyspark.sql
from pyspark.sql import functions as F

#Membuat fungsi transform yang memproses data dari tahap ekstraksi
def transform(data):
    #Menghapus kolom yang tidak diperlukan
    data_dropped = data.drop("Unnamed: 0") 

    #Membersihkan baris kosong agar data siap diolah
    data_final = data_dropped.na.drop() 

    #Mengembalikan dataframe yang sudah bersih
    return data_final 