import os
from datetime import datetime, timedelta
from airflow import DAG

from airflow.operators.bash_operator import BashOperator

default_args = {
    'retries': 3,
    'retry_delay': timedelta(minutes=3),
    'start_date': datetime(2023, 12, 1),
    'schedule_interval': '0 9 * * *'
}

AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
cwd = os.path.join(AIRFLOW_HOME)

with DAG(dag_id='extract_and_load', schedule_interval="0 */1 * * *", start_date=datetime(2023, 8, 4), catchup=False) as dag:
    # write you extract and load airflow dag here
    # the dag should have three bash operators
    # migration >> extract >> load

    migration = BashOperator(
        task_id = 'migration',
        bash_command = f'python dags/scripts/migration.py',
        cwd = cwd,
        dag = dag
        )
    
    extract = BashOperator(
        task_id = 'extract',
        bash_command = f'python dags/scripts/extract.py',
        cwd = cwd,
        dag = dag
        )
    
    load = BashOperator(
        task_id = 'load',
        bash_command = f'python dags/scripts/load.py',
        cwd = cwd,
        dag = dag
        )

    migration >> extract >> load