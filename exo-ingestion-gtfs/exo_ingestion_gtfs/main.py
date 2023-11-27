import fire
import urllib.request as urllib
import zipfile

from configuration import Configuration
from databricks.sdk import WorkspaceClient

def run(environment="dev"):
    w = WorkspaceClient()
    for i in w.dbfs.list("/"):
        print(i.path)


    # configuration_file_path = f"resources/configuration-{environment.lower()}.yml"
    # config = Configuration(configuration_file_path)
    # print(config.ingestion_dataset_trains)
    # print(config.ingestion_dataset_autobuses)
    #
    # for autobus in config.ingestion_dataset_autobuses:
    #     content = get_content(autobus["url"])
    #     with open(autobus["output_path"], "w") as file:
    #         file.write()

    # for train in config.ingestion_dataset_trains:
    #     content = get_content(train["url"])
    #     with open(train["output_path"], "w") as file:
    #         file.write(content.decode())


def get_content(url):
    filehandle, _ = urllib.urlretrieve(url)
    zip_file_object = zipfile.ZipFile(filehandle, 'r')
    first_file = zip_file_object.namelist()[0]
    file = zip_file_object.open(first_file)
    content = file.read()
    return content


if __name__ == '__main__':
    fire.Fire(run)
