import fire


def run(configuration_file_path="resources/configuration.yml"):
    config = get_yaml_config(configuration_file_path)


if __name__ == '__main__':
    fire.Fire(run)
