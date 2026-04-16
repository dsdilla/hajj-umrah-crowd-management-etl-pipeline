#Memanggil library untuk penggunaan airflow
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

#Untuk mengatur default argument sesuai kriteria 
default_args = {
    'owner': 'dilla',
    #Mulai pada 1 November 2024
    'start_date': dt.datetime(2024, 11, 1),
    #jumlah percobaan ulang jika gagal
    'retries': 1,
    #Delay selama 5 menit jika gagal
    'retry_delay': dt.timedelta(minutes=5),
}

#Membuat DAG dengan jadwal Sabtu jam 09:10, 09:20, 09:30
#Schedule '10,20,30 9 * * 6' -> Menit 10,20,30 | Jam 9 | Setiap Hari | Setiap Bulan | Hari ke-6 (Sabtu)
with DAG('P2M3_Dianah_Salsha_Dilla_DAG_bash',
         default_args=default_args,
         schedule_interval='10,20,30 9 * * 6', 
         catchup=False,
         ) as dag:
    
#Menjalankan script Extract.py menggunakan Bash
    python_extract = BashOperator(
        task_id='python_extract', 
        bash_command='python /opt/airflow/scripts/Extract.py' #untuk menjalankan extract
    )

    #Menjalankan script Transform.py menggunakan Bash
    python_transform = BashOperator(
        task_id='python_transform', 
        bash_command='python /opt/airflow/scripts/Transform.py' #untuk menjalankan transform
    )

    #Menjalankan script Load.py menggunakan Bash
    python_load = BashOperator(
        task_id='python_load', 
        bash_command='python /opt/airflow/scripts/Load.py' #untuk menjalankan load
    )

#Mengatur urutan eksekusi tugas
python_extract >> python_transform >> python_load