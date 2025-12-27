# py-coder

## 使い方

### VS Code Tasks（推奨）

`Cmd+Shift+P` → 「Tasks: Run Task」で以下のタスクを実行:

- **acc new**: コンテストディレクトリ作成（コンテスト名を入力プロンプトで指定）
- **execute python**: 現在のPythonファイルを実行
- **oj test**: テスト実行（現在のファイル）
- **acc submit**: 提出（現在のファイル）

### コマンドライン

#### コンテストディレクトリ作成
```bash
acc new abc321
```

#### テスト実行
```bash
cd abc321/a
uv run oj t -c "python main.py" -d tests
```

#### 提出
```bash
cd abc321/a
echo abc$(basename $(pwd)) | acc s main.py -- --guess-python-interpreter pypy
```