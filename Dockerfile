# Dockerfile
# ベースイメージとしてPythonのスリム版を使用
FROM python:3.9-slim

# 作業ディレクトリを指定
WORKDIR /app

# 必要なファイルをコピー
COPY requirements.txt requirements.txt
COPY opt/app.py opt/app.py

# Flaskのインストール
RUN pip install -r requirements.txt

# アプリケーションの実行
CMD ["python3", "opt/app.py"]


