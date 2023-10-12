import fire
import urllib.request as urllib
import zipfile
import csv

from configuration import Configuration


def run(configuration_file_path="resources/configuration.yml"):
    config = Configuration(configuration_file_path)
    print(config.ingestion_dataset_trains)
    print(config.ingestion_dataset_autobuses)
    for train in config.ingestion_dataset_trains:
        train_url = train["url"]
        print(f"extract {train['name']}")
        filehandle, _ = urllib.urlretrieve(train_url)
        zip_file_object = zipfile.ZipFile(filehandle, 'r')
        first_file = zip_file_object.namelist()[0]
        file = zip_file_object.open(first_file)
        content = file.read()
        print("content")
        print(content)
        # with open(train["output_path"], "w") as f:
        #     f.write(content.decode("utf-8"))


if __name__ == '__main__':
    fire.Fire(run)
