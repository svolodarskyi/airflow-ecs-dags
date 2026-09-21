from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator

with DAG(dag_id="hello_world_dup", schedule=None, tags=["training", "git-bundle"]) as dag:
    BashOperator(task_id="say_hello", bash_command="echo hello from ecs task-runner, loaded via GitDagBundle")
