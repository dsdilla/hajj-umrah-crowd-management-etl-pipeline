#Memanggil library pyspark 
from pyspark.sql import SparkSession

#Membuat fungsi load data yang mengembalikan Spark Dataframe
def load_data(file_path):
    #Menginisialisasi session Spark
    spark = SparkSession.builder.appName("HajjDataETL").getOrCreate()
    
    #Membaca data csv
    data = spark.read.csv(file_path, header=True, inferSchema=True) #proses Extract
    
    #Memberikan output berupa Spark Dataframe agar bisa diproses transform.py
    return data