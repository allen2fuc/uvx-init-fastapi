# init-fastapi
这是fastapi的脚手架

## 克隆项目
```bash
$ git clone https://github.com/allen2fuc/uvx-init-fastapi.git
```

## 查看克隆的位置
```bash
# 克隆在～/code目录下
$ ls ~/Code/uvx-init-fastapi
```

## 创建新项目
```bash
# 进入到代码位置
$ cd ~/Code
# 利用脚手架创建一个 myapp 的项目，项目位置：~/Code/myapp
$ uvx --from ~/Code/uvx-init-fastapi --no-cache init-fastapi myapp
```

## 查看项目目录结构
```bash
# 查看项目的结构
$ tree myapp
myapp
├── Dockerfile
├── Makefile
├── README.md
├── app
│   └── app.py
├── docker-compose.yml
└── pyproject.toml
```

## 同步项目
```bash
# 同步项目
$ cd ~/code/myapp
$ uv sync
```