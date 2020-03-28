# coding=utf-8
"""
Author:zywen
Email：1004324878@qq.com

Date:2020/3/17 23:42
Desc:
"""
# coding=utf-8
try:
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})
except Exception:
    import os
    os.system('pip install pyyaml')
    import yaml
    yaml.warnings({'YAMLLoadWarning': False})

def read_file(file):
    with open(file,"rb") as f:
        content = f.read()
        yaml_content = yaml.load(content)
        # print(web_elements)
        return yaml_content


if __name__ == '__main__':
    result = read_file("config.yml")
    print(result)