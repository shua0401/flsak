# チャットボットシステム v3

このプロジェクトは、Google Sheets APIと生成系AI APIを使用したチャットボットシステムです。Moodleと連携して、学生からの質問に自動で回答する機能を提供します。

## 機能

- Google Sheetsを使用した質問回答データベース
- 同義語辞書と関連語辞書による質問マッチング
- 生成系AI APIを使用したAI回答機能
- 質問ログの記録と管理
- Moodleとの連携

## 必要条件

- Python 3.x
- Flask
- Google Sheets API
- OpenAI API

## セットアップ

※API鍵を用意してください。
※データベースは共有していません。
※ログインには学籍番号、シートの情報が必要です。
1. リポジトリをクローン
2. 必要なパッケージをインストール
3. 環境変数の設定
`.env.example`ファイルを`.env`にコピーし、以下の値を設定してください：
- `SPREADSHEET_KEY`: Google Sheetsのスプレッドシートキー
- `GOOGLE_API_KEY`: Google APIキー
- `OPENAI_API_KEY`: OpenAI APIキー

## 使用方法
1. サーバーを起動
```bash
python main.py
```
2. ブラウザで以下のURLにアクセス

## プロジェクト構造
- `main.py`: メインアプリケーションファイル
- `utils.py`: ユーティリティ関数
- `utils2.py`: 拡張ユーティリティ関数
- `templates/`: HTMLテンプレート
- `static/`: 静的ファイル
- `log/`: ログファイル

## ライセンス
このプロジェクトは[MITライセンス](LICENSE)の下で公開されています。 
