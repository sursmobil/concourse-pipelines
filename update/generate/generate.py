#!/usr/bin/env python

class Project(object):
    def __init__(self, name, repository, template):
        self.name = name
        self.repository = repository
        self._template = template

class CI(object):
    def __init__(self, repository):
        self.repository = repository

class Config(object):
    def __init__(self, ci, projects):
        self.projects = [Project(**prj) for prj in projects]
        self.ci = CI(**ci)

def get_src(*path):
    from os.path import join
    from os import getenv
    return join(getenv('CI_SRC'), *path)

def get_gen(*path):
    from os.path import join
    from os import getenv
    return join(getenv('CI_GEN'), *path)

def load_config():
    import yaml
    config_file = get_src('config.yml')
    with open(config_file) as f:
        config = yaml.load(f)
    return Config(**config)

def create_jinja_env():
    from jinja2 import Environment, FileSystemLoader
    return Environment(
        loader=FileSystemLoader(get_src('templates')),
        autoescape=None
    )

def render_project(cfg, prj):
    template = env.get_template(prj._template)
    return template.render(
        project=prj.__dict__,
        ci=config.ci.__dict__
    )

def ensure_dir(path):
    from os.path import exists
    from os import makedirs
    if not exists(path):
        print(path)
        makedirs(path)

def save_project(prj, content):
    ensure_dir(get_gen('pipelines'))
    out_file = get_gen('pipelines', '{}.yml'.format(prj.name))
    with open(out_file, 'w') as f:
        f.write(content)
    return

def generate_project(cfg, prj):
    content = render_project(config, project)
    save_project(prj, content)
    return

env = create_jinja_env()
config = load_config()
for project in config.projects:
    generate_project(config, project)
