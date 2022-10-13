import yaml


def load_config():
    with open('config.yml', 'r') as yf:
        data = yaml.safe_load(yf)
    return data
