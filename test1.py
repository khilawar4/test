from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import os





def _print_original_context(**context):
    print(context['dag'].full_filepath)
    head, tail = os.path.split(context['dag'].full_filepath)
    file_name=tail.split('.')[0]

    if file_name != context['dag'].dag_id:
        print('pass correct DAG ID same as DAG file name')
    # if !context['dag'].dag_id in context['dag'].full_filepath:
    #     print "Found!"
    # if (context['dag'].full_filepath)
    #context['dag'].dag_id='random'
    print (' file_name ===',file_name)
    print(context)


def _print_context(**context):
    print(context)


with DAG(
    dag_id="test1",
    schedule_interval=None,
    start_date=days_ago(0),
    tags=["example"],
) as dag:

    print_original_context = PythonOperator(
        task_id="print_original_context",
        python_callable=_print_original_context,
        provide_context=True,
        dag=dag
    )


    print_original_context
