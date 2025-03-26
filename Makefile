# Biến cài đặt
PYTHON := python3
VENV_NAME := .soiz
VENV_ACTIVATE := $(VENV_NAME)/bin/activate
REQUIREMENTS := requirements.txt
MAIN_FILE := main.py

# Tạo môi trường ảo
env: $(VENV_NAME)

$(VENV_NAME):
	@echo "Tạo môi trường ảo..."
	@python3 -m venv $(VENV_NAME)
	@. $(VENV_ACTIVATE) && pip install --upgrade pip

# Cài đặt các gói từ requirements.txt
install: env
	@echo "Cài đặt các gói từ requirements.txt..."
	@. $(VENV_ACTIVATE) && pip install -r $(REQUIREMENTS)

# Chạy chương trình chính (main.py)
run: env $(MAIN_FILE)
	@echo "Chạy chương trình..."
	@. $(VENV_ACTIVATE) && $(PYTHON) $(MAIN_FILE)

down: env $(MAIN_FILE)
	@echo "Chạy chương trình..."
	@. $(VENV_ACTIVATE) && $(PYTHON) down.py

# Định dạng mã nguồn với black
format: env
	@echo "Định dạng mã nguồn với black..."
	@. $(VENV_ACTIVATE) && black .

# Kiểm tra mã nguồn với flake8
lint: env
	@echo "Kiểm tra mã nguồn với flake8..."
	@. $(VENV_ACTIVATE) && flake8 .

# Kiểm tra lỗi tiềm ẩn với pylint
check: env
	@echo "Kiểm tra lỗi tiềm ẩn với pylint..."
	@. $(VENV_ACTIVATE) && pylint $(MAIN_FILE)

# Kiểm tra an toàn mã nguồn với bandit
security: env
	@echo "Kiểm tra an toàn mã nguồn với bandit..."
	@. $(VENV_ACTIVATE) && bandit -r $(MAIN_FILE)

# Chạy test với pytest
test: env
	@echo "Chạy thử nghiệm..."
	@. $(VENV_ACTIVATE) && $(PYTHON) test.py

# Xóa các file tạm thời và cache
clean:
	@echo "Dọn dẹp các file tạm thời và cache..."
	@rm -rf __pycache__ .pytest_cache *.pyc *.pyo

# Tạo file requirements.txt từ môi trường hiện tại
freeze: env
	@echo "Đóng băng các gói vào requirements.txt..."
	@. $(VENV_ACTIVATE) && pip freeze > $(REQUIREMENTS)

# Hiển thị trợ giúp
help:
	@echo "Các mục tiêu có sẵn:"
	@echo "  run       - Chạy chương trình chính"
	@echo "  env       - Tạo môi trường ảo (nếu chưa tồn tại)"
	@echo "  install   - Cài đặt các gói từ requirements.txt"
	@echo "  format    - Định dạng mã nguồn với black"
	@echo "  lint      - Kiểm tra mã nguồn với flake8"
	@echo "  check     - Kiểm tra lỗi tiềm ẩn với pylint"
	@echo "  security  - Kiểm tra an toàn mã nguồn với bandit"
	@echo "  test      - Chạy test với pytest"
	@echo "  clean     - Dọn dẹp các file tạm và cache"
	@echo "  freeze    - Tạo/cập nhật file requirements.txt"
	@echo "  help      - Hiển thị trợ giúp này"

# Chạy tất cả kiểm tra một cách tự động
full_check: lint check security