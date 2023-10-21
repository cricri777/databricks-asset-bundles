import yaml


class Configuration:
    """Configuration class to parse configuration-dev.yml"""
    def __init__(self, configuration_file_path):
        with open(configuration_file_path, "r") as config_yaml_file:
            config = yaml.safe_load(config_yaml_file)
        self.ingestion_dataset_autobuses = config["exo"]["ingestion"]["dataset"]["autobuses"]
        self.ingestion_dataset_trains = config["exo"]["ingestion"]["dataset"]["trains"]
