.PHONY: help build push build-push up down restart logs clean test

IMAGE_NAME := uhub.service.ucloud.cn/vst_repository/${project_name}
VERSION ?= latest

help: ## 显示帮助信息
	@echo "Sign Vision API - Docker 管理命令"
	@echo ""
	@echo "使用方法: make [命令]"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-15s %s\n", $$1, $$2}'

build: ## 构建 Docker 镜像
	@echo "🔨 构建镜像: $(IMAGE_NAME):$(VERSION)"
	docker build -t $(IMAGE_NAME):$(VERSION) .
	@if [ "$(VERSION)" != "latest" ]; then \
		docker tag $(IMAGE_NAME):$(VERSION) $(IMAGE_NAME):latest; \
	fi
	@echo "✅ 构建完成"

push: ## 推送镜像到 UCloud
	@echo "📤 推送镜像: $(IMAGE_NAME):$(VERSION)"
	docker push $(IMAGE_NAME):$(VERSION)
	@if [ "$(VERSION)" != "latest" ]; then \
		docker push $(IMAGE_NAME):latest; \
	fi
	@echo "✅ 推送完成"

build-push: build push ## 构建并推送镜像（一键操作）
	@echo "🎉 构建并推送完成！"

pull: ## 从 UCloud 拉取镜像
	@echo "📥 拉取镜像: $(IMAGE_NAME):$(VERSION)"
	docker pull $(IMAGE_NAME):$(VERSION)
	@echo "✅ 拉取完成"

up: ## 启动服务（docker-compose）
	@echo "🚀 启动服务..."
	docker-compose up -d
	@echo "✅ 服务已启动"
	@echo "📍 API: http://localhost:8000"
	@echo "📍 文档: http://localhost:8000/docs"

down: ## 停止服务
	@echo "🛑 停止服务..."
	docker-compose down
	@echo "✅ 服务已停止"

restart: ## 重启服务
	@echo "🔄 重启服务..."
	docker-compose restart
	@echo "✅ 服务已重启"

logs: ## 查看日志
	docker-compose logs -f

clean: ## 清理未使用的 Docker 资源
	@echo "🧹 清理 Docker 资源..."
	docker system prune -f
	@echo "✅ 清理完成"

clean-all: ## 清理所有 Docker 资源（包括镜像）
	@echo "⚠️  清理所有 Docker 资源..."
	docker system prune -a -f
	@echo "✅ 清理完成"

shell: ## 进入容器 Shell
	docker exec -it sign-vision-api /bin/bash

login: ## 登录 UCloud 容器镜像仓库
	@echo "🔐 登录 UCloud 容器镜像仓库..."
	docker login uhub.service.ucloud.cn

dev: ## 开发模式（带卷挂载）
	@echo "🔧 启动开发模式..."
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up

deploy: build push ## 构建并推送（完整发布流程）
	@echo "🎉 部署完成！"
	@echo "在服务器上运行: docker pull $(IMAGE_NAME):$(VERSION) && docker-compose up -d"


