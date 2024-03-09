# discord-bot

## 開発環境

### node

- node: 20.10.0 ([.node_version](.node-version))
- packages: [package.json](package.json)

## GitHub運用

### コミットメッセージ

[gitmoji](https://gitmoji.dev/) + Message

> ex: :see_no_evil: .gitignoreに開発環境とGitHub運用の追記

### ブランチ命名規則

- `dev-`: 開発用
- `fix-`: 修正用
- `test-`: テスト用

### 固定ブランチ

- [dev-document](https://github.com/Gabe-ds/discord-bot/tree/dev-document): ドキュメント更新用
- [dev-environment](https://github.com/Gabe-ds/discord-bot/tree/dev-environment): 開発環境更新用

## 環境変数

[.env.sample](.env.sample)のファイル名を`.env`に変更して，定義する．

## Bot起動方法

以下のコマンドを実行する．

```shell
npx ts-node {FILE_PATH}
```
