# init-fastapi
这是fastapi的脚手架

## 克隆项目
```bash
$ git clone https://github.com/allen2fuc/uvx-init-fastapi.git
```

## 查看项目位置
```bash
$ ls ~/Code/uvx-init-fastapi
```

## 创建新项目
```bash
$ cd ~/Code
$ uvx --from ~/Code/uvx-init-fastapi --no-cache init-fastapi myapp
```

## 查看项目目录结构
```bash
$ tree myapp
myapp
├── Dockerfile
├── Makefile
├── README.md
├── app
│   └── main.py
├── docker-compose.yml
└── pyproject.toml
```

## 同步项目
```bash
$ cd ~/code/myapp
$ uv sync
```