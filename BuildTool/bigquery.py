from google.cloud import bigquery


def big(table):

    project_id = 'test-2022-wagon'
    client = bigquery.Client(project=project_id)

    sql = f"""
    SELECT *
    FROM `test.ratings`
    LIMIT 3
    """
    df = client.query(sql)

    return df
