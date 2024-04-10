from googleapiclient.discovery import build


def trigger_df_job(cloud_event,environment):   
 
    service = build('dataflow', 'v1b3')
    project = "nishant-project-task"

    template_path = "gs://dataflow-templates-us-central1/latest/GCS_Text_to_BigQuery"

    template_body = {
    "jobName": "loading-population-data-to-bq",  # Provide a unique name for the job
    "parameters": {
        "inputFilePattern": "gs://task-fiirst-metadata-files/macrotrends.csv",
        "JSONPath": "gs://task-fiirst-metadata-files/bq.json",
        "outputTable": "nishant-project-task:population_growth_data.population_growth_table",
        "bigQueryLoadingTemporaryDirectory": "gs://task-fiirst-metadata-files",
        "javascriptTextTransformGcsPath": "gs://task-fiirst-metadata-files/udf.js",
        "javascriptTextTransformFunctionName": "transform"
    }
    }

    request = service.projects().templates().launch(projectId=project,gcsPath=template_path, body=template_body)
    response = request.execute()
    print(response)
