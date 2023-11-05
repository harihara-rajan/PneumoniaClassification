import os
root_dir = "src"

list_dirs=[
    f"{root_dir}/components/__init__.py",
    f"{root_dir}/constants/__init__.py",
    f"{root_dir}/entity/__init__.py",
    f"{root_dir}/pipeline/__init__.py",
    f"{root_dir}/utils/__init__.py",
    f"{root_dir}/config/__init__.py",
    f"{root_dir}/yaml/__init__.py",
    f"{root_dir}/yaml/config.yaml",
    f"{root_dir}/yaml/params.yaml",
    f"{root_dir}/__init__.py",
    f"{root_dir}/main.py",
]

for dir in list_dirs:
    print(dir)
    if not os.path.exists(dir):
        dir_name = os.path.dirname(dir)
        # print(dir_name)
        os.makedirs(dir_name,exist_ok=True)
    with open(dir, 'w') as file:
        pass
    