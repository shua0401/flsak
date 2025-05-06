# flsak

このリポジトリは、FlaskとDockerを使用したシンプルなWebアプリケーションの開発・動作確認を目的としたテスト用プロジェクトです。FlaskアプリケーションのDocker化や、`docker-compose` を用いた環境構築の基本を学ぶのに適しています。

---

## ✅ 特徴

- PythonのWebフレームワーク「Flask」を使用
- Dockerおよびdocker-composeによる簡易な開発環境の構築
- 必要最小限の構成で、拡張が容易

---

## 📁 ディレクトリ構成

flsak/
├── Dockerfile # FlaskアプリのDockerイメージ定義
├── docker-compose.yml # コンテナ構成の定義
├── requirements.txt # 使用するPythonパッケージ
├── .gitignore # Gitで追跡しないファイルの設定
├── README.md # このファイル
└── opt/ # アプリケーションコード格納予定ディレクトリ

yaml
コピーする
編集する

---

## ⚙️ セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/shua0401/flsak.git
cd flsak
2. Dockerで起動
bash
コピーする
編集する
docker-compose up --build
3. アクセス確認
ブラウザで以下のURLにアクセス：

arduino
コピーする
編集する
http://localhost:5000
Flaskアプリケーションが表示されれば成功です。
