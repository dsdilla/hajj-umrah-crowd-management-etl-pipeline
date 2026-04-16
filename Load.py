#Memanggil library pymongo
import pymongo

#Membuat fungsi load yang menyimpan data ke MongoDB
def load_to_mongo(df, connection_string, db_name, collection_name):
    
    #Mengubah Spark Dataframe menjadi format yang dipahami MongoDB
    data_dict = [row.asDict() for row in df.collect()] 

    #Membuat koneksi ke database MongoDB Atlas 
    client = pymongo.MongoClient(connection_string) 

    #Menentukan nama database dan tabel (collection) tujuan di cloud
    db = client[db_name] 
    collection = db[collection_name] 

    #Menyimpan banyak data sekaligus ke database
    collection.insert_many(data_dict) 
    
    #Memberikan tanda bahwa proses pemindahan data sudah berhasil
    print(f"Data Berhasil Disimpan ke Atlas di tabel: {collection_name}")