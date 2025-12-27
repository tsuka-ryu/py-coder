# py-coder

## 使い方

### コンテストディレクトリ作成
```bash
acc new abc321
```

### テスト実行
```bash
cd abc321/a
uv run oj test -c "python main.py"
```

### 提出
```bash
acc submit main.py -- --guess-python-interpreter pypy
```