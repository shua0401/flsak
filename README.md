# Flaskを使ったDockerの勉強

FlaskとDockerを使用したシンプルなWebアプリケーションの開発・動作確認を目的としたテスト用プロジェクトです。FlaskアプリケーションのDocker化や、`docker-compose` を用いた環境構築の基本を学ぶのに適しています。

---

## ✅ 特徴

- PythonのWebフレームワークを使用
- Docker,docker-composeによる開発環境の構築

---

## 📁 ディレクトリ構成

flsak/
├── Dockerfile # FlaskアプリのDockerイメージ定義
├── docker-compose.yml # コンテナ構成の定義
├── requirements.txt # 使用するPythonパッケージ
├── .gitignore # Gitで追跡しないファイルの設定
├── README.md # このファイル
└── opt/ # アプリケーションコード格納予定ディレクトリ
---

## ⚙️ セットアップ手順
### 1. リポジトリのクローン
```bash
git clone https://github.com/shua0401/flsak.git
```
2. Dockerで起動
```bash
docker-compose up --build
```
3. アクセス確認
