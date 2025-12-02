import sys
import os
import shutil
import importlib.resources as pkg_resources
from string import Template
import init_fastapi.templates as templates_pkg

def main():
    if len(sys.argv) < 2:
        print("Usage: init-fastapi <project_name>")
        return

    project_name = sys.argv[1]
    print(f"Creating FastAPI project: {project_name}")

    # 创建 app 目录
    os.makedirs(f"{project_name}/app", exist_ok=True)

    # 写 app/main.py
    with open(f"{project_name}/app/app.py", "w") as f:
        f.write(
            f"from fastapi import FastAPI\n\n"
            f"app = FastAPI()\n\n"
            f"@app.get('/')\n"
            f"def root():\n"
            f"    return {{'message': 'Hello from {project_name}!'}}\n"
        )

    # 复制模板文件，并渲染 {{ project_name }}
    for resource in pkg_resources.contents(templates_pkg):
        if pkg_resources.is_resource(templates_pkg, resource):
            with pkg_resources.path(templates_pkg, resource) as template_path:
                with open(template_path, "r", encoding="utf-8") as f:
                    content = f.read()

                # 使用 string.Template 渲染变量
                t = Template(content)
                rendered = t.safe_substitute(project_name=project_name)

                # 写入生成项目
                dst_path = os.path.join(project_name, resource)
                with open(dst_path, "w", encoding="utf-8") as out_f:
                    out_f.write(rendered)

    print(f"Project {project_name} created successfully!")

