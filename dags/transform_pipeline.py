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

# Get the value of the AIRFLOW_HOME environment variable
AIRFLOW_HOME = os.getenv('AIRFLOW_HOME')
cwd = os.path.join(AIRFLOW_HOME)


with DAG(dag_id='transform', catchup=False, default_args=default_args) as dag:

    transform = BashOperator(
        task_id = 'transform',
        bash_command = f'dbt build --project-dir {cwd}/dbt_project --profiles-dir {cwd}/dbt_profile',
        cwd = cwd,
        env = os.environ.copy(),
        dag = dag
        )

    transform
