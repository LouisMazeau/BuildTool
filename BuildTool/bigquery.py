import pandas_gbq

def big(table):
    project_id = 'data-bootcamp-lectures'

    sql = """
    SELECT *
    FROM `bigquery-public-data.{table}`
    """
    df = pandas_gbq.read_gbq(sql, project_id=project_id)

    return df
