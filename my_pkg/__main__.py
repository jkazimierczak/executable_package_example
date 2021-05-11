import pkg_resources
import yaml


def main():
    # https://setuptools.readthedocs.io/en/latest/pkg_resources.html#basic-resource-access
    config_file = pkg_resources.resource_filename(__name__, 'config.yml')
    with open(config_file) as f:
        config = yaml.safe_load(f)
        print(config)


if __name__ == '__main__':
    main()
