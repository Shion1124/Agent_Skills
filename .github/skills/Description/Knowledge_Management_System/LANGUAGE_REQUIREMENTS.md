# KWF 言語要件 - Python / TypeScript 明確化ガイド

**作成日**: 2026-03-01  
**重要度**: ⭐⭐⭐ 必読  
**対象**: KWF を使用する全員

---

## ✅ 要約: 言語要件

| 言語 | 必須か | 用途 | 詳細 |
|------|------|------|------|
| **Python** | ✅ **必須** | KB 管理ツール | `kb-generator.py` を実行するために必須 |
| **TypeScript** | ❌ **任意** | テンプレート例 | パターンテンプレートのコード例に含まれるだけ |
| **JavaScript** | ❌ **任意** | テンプレート例 | パターンテンプレートのコード例に含まれるだけ |
| **その他言語** | ❌ **任意** | プロジェクト次第 | あなたのプロジェクト言語を使用 |

---

## 🔍 詳細説明

### **Python - 必須（✅ MUST HAVE）**

#### なぜ Python が必須か？

KWF の中核である `kb-generator.py` が Python で書かれているため：

```
kb-generator.py の役割
├─ init: 知識ベースの初期化
├─ update-index: Markdown → JSON インデックス生成
├─ validate: KB の健全性チェック
└─ search: ナレッジ検索
```

これらの機能は **Python スクリプト** でのみ提供されます。

#### Python のインストール

**macOS:**
```bash
# Homebrew を使用
brew install python3

# 確認
python3 --version
# Python 3.9以上推奨
```

**Linux (Ubuntu/Debian):**
```bash
# apt を使用
sudo apt-get update
sudo apt-get install python3 python3-pip

# 確認
python3 --version
```

**Windows:**
1. https://www.python.org/downloads/ にアクセス
2. "Download Python 3.x.x" をクリック
3. インストーラーを実行
4. ✅ "Add Python to PATH" にチェック
5. コマンドプロンプトで確認：
```bash
python --version
# または
python3 --version
```

#### Python のバージョン要件

```
要件: Python 3.8 以上
推奨: Python 3.9 以上

互換性確認:
✅ Python 3.8
✅ Python 3.9
✅ Python 3.10
✅ Python 3.11
✅ Python 3.12
```

#### Python で何ができるか？

```bash
# 1. KB を初期化
python3 kb-generator.py init
# 結果: ディレクトリ構造とサンプルファイルを生成

# 2. インデックスを生成（重要！）
python3 kb-generator.py update-index
# 結果: knowledge-index.json を自動生成
# → Copilot がこれを検索して参照

# 3. 健全性チェック
python3 kb-generator.py validate
# 結果: 壊れたリンク、欠落ファイルを検出

# 4. 検索
python3 kb-generator.py search "async error handling"
# 結果: 関連する決定/パターン/レッスンを検索
```

**これらは全て Python でのみ実行可能** ✅

---

### **TypeScript - オプション（❌ 不要）**

#### TypeScript がどこに出現するか？

KWF テンプレートには **コード例** が含まれています。

**例えば**: `pattern-template.md` では

```typescript
// これはテンプレートの「例」です
// あなたのプロジェクトの言語に置き換えられます

class ManagedConnection {
  private connection: DatabaseConnection;
  
  constructor(connection: DatabaseConnection) {
    this.connection = connection;
  }
  
  async execute<T>(
    query: string, 
    params: any[] = []
  ): Promise<T> {
    try {
      return await this.connection.query(query, params);
    } finally {
      await this.connection.release();
    }
  }
}
```

#### 重要: TypeScript は「例」にすぎない

テンプレートに TypeScript が含まれているのは：

✅ **理由**: 最新のベストプラクティス例を示すため  
❌ **制限**: TypeScript を使う必要があるわけではない

#### 実際の使い方

パターンを記録するときに：

```markdown
# Pattern: Resource Cleanup in Async Code

## Solution

### Version 1: TypeScript Example
\`\`\`typescript
// ... TypeScript コード
\`\`\`

### Version 2: Python Example
\`\`\`python
# ... Python コード
\`\`\`

### Version 3: Java Example
\`\`\`java
// ... Java コード
\`\`\`
```

**つまり**：
- テンプレートはスターティングポイント
- あなたのプロジェクト言語に合わせて **いくらでも変更可能**

---

## 📊 言語の使い分け（チェックリスト）

### あなたが Python を使っている場合

```
✅ Python が必須（KB 管理用）
✅ テンプレートの例を Python に置き換え
✅ 他言語のプロジェクトメンバー向けに説明を追加

例:
# Pattern: Async Error Handling

## Python Implementation
\`\`\`python
async def fetch_data(url):
    conn = await get_connection()
    try:
        return await conn.query(url)
    finally:
        await conn.release()
\`\`\`
```

### あなたが TypeScript を使っている場合

```
✅ Python が必須（KB 管理用）
✅ テンプレートの TypeScript 例はそのまま使用可
✅ 必要に応じて Python 例も追加

例:
# Pattern: Async Error Handling

## TypeScript Implementation (そのままで OK)
\`\`\`typescript
class ManagedConnection { ... }
\`\`\`

## Python Implementation (チームメンバー向け追加)
\`\`\`python
async with get_connection() as conn:
    ...
\`\`\`
```

### あなたが Java/Go/Rust などを使っている場合

```
✅ Python が必須（KB 管理用）
✅ テンプレートの例を Java/Go/Rust に置き換え
✅ 言語別の説明を記載

例:
# Pattern: Resource Cleanup

## Java Implementation
\`\`\`java
try (Connection conn = getConnection()) {
    // use connection
} catch (Exception e) {
    // handle
}
\`\`\`
```

---

## 🎯 実践例

### シナリオ: Python + Node.js チーム

あなたのチームが Python と Node.js の両方を使っている場合：

#### Step 1: 決定を記録（言語に依存しない）

```markdown
# Decision: Error Handling Strategy

**Status**: ACCEPTED

## Context
We need consistent error handling across Python and Node.js services.

## Decision
Use try/finally pattern for all resource cleanup, regardless of language.

## Examples

### Python
\`\`\`python
try:
    result = await db.query()
finally:
    await db.release()
\`\`\`

### Node.js
\`\`\`javascript
try {
    const result = await db.query();
} finally {
    await db.release();
}
\`\`\`
```

#### Step 2: Python 用パターンを記録

```markdown
# Pattern: Database Resource Cleanup (Python)

## Solution

\`\`\`python
async def fetch_user(user_id):
    conn = await db.get_connection()
    try:
        return await conn.query("SELECT ...")
    finally:
        await conn.release()
\`\`\`
```

#### Step 3: Node.js 用パターンを記録

```markdown
# Pattern: Database Resource Cleanup (Node.js)

## Solution

\`\`\`typescript
async function fetchUser(userId: string) {
    const conn = await db.getConnection();
    try {
        return await conn.query("SELECT ...");
    } finally {
        await conn.release();
    }
}
\`\`\`
```

#### Step 4: KB を更新（Python スクリプト）

```bash
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py update-index
```

**結果**: 両方のパターンが検索可能に ✅

---

## ❓ よくある質問

### Q1: 「TypeScript をインストールする必要があるか？」

**A: いいえ、不要です。**

- KWF は TypeScript を実行しません
- テンプレートの例にすぎません
- あなたのプロジェクト言語があれば十分

### Q2: 「Python 3.8 は古くないか？」

**A: 推奨は 3.9以上ですが、3.8 でも動作します。**

```bash
# 現在のバージョンを確認
python3 --version

# 推奨: 3.9 以上をインストール
# macOS:
brew install python3.11

# Linux:
sudo apt-get install python3.11
```

### Q3: 「Python のパッケージ（pip）をインストールする必要があるか？」

**A: いいえ。kb-generator.py は標準ライブラリのみ使用。**

- pip をインストール不要
- 追加パッケージ不要
- `python3 kb-generator.py` で即実行可能

```bash
# pip が必要か確認
python3 kb-generator.py init
# → 成功すれば、pip は不要
```

### Q4: 「テンプレートの TypeScript を削除して Python に置き換えてよいか？」

**A: はい。むしろ推奨します。**

```markdown
# Pattern: Template

\`\`\`python
# Python コード例に置き換え
\`\`\`
```

### Q5: 「マルチ言語プロジェクトでは？」

**A: 各言語の例を記載してください。**

```markdown
# Pattern: Async Error Handling

## Python
\`\`\`python
...
\`\`\`

## TypeScript
\`\`\`typescript
...
\`\`\`

## Java
\`\`\`java
...
\`\`\`
```

### Q6: 「テンプレートの JavaScript/TypeScript 部分は要らない？」

**A: 削除するか、あなたのプロジェクト言語に置き換えてください。**

#### Option A: 削除

```markdown
# Pattern: Resource Cleanup

## Problem
Resources leak if not properly released.

## Solution
Always use try/finally (or context managers).

※ コード例は削除
```

#### Option B: 置き換え

```markdown
# Pattern: Resource Cleanup

## Solution (Python)

\`\`\`python
with get_connection() as conn:
    # Use connection
\`\`\`
```

### Q7: 「Python がない環境では使えない？」

**A: KB を**編集**のみなら OK。ただし、管理（init, update-index）には Python が必須。**

```bash
# できること（Python 不要）
# - .md ファイルをエディタで編集
# - Git で管理
# - GitHub で閲覧

# できないこと（Python 必須）
# - python3 kb-generator.py init
# - python3 kb-generator.py update-index
# - python3 kb-generator.py validate
# - python3 kb-generator.py search
```

本来は Python 環境が必須です。

---

## 📋 言語セットアップチェックリスト

### Python（必須）

```bash
# ✅ インストール確認
python3 --version

# ✅ バージョン確認（3.8以上）
python3 -c "import sys; print(sys.version_info)"

# ✅ スクリプト実行確認
python3 kb-generator.py init

# ✅ すべて成功したら OK
echo "Python setup: OK ✅"
```

### TypeScript（オプション - テンプレートの例用）

テンプレートに TypeScript 例が含まれているだけです。

```bash
# TypeScript をインストール（任意）
npm install -g typescript

# あなたのプロジェクトで使っているなら設定済みでしょう
# インストール不要な可能性が高い
```

### あなたのプロジェクト言語

```bash
# あなたのプロジェクトの言語が何であれ：
# - Java, Go, Rust, C++, C#, PHP, Ruby...
# 
# その言語の環境は既にあるはず。
# テンプレートはそれに合わせてカスタマイズするだけ。
```

---

## 🎓 言語別ガイド

### Python プロジェクトの場合

```
✅ Python: 必須（KB 管理）
✅ TypeScript テンプレート: Python に置き換え
✅ 結果: Python 例のみの KB

例:
# Pattern: Database Connection

## Solution (Python)

\`\`\`python
async def query_user(id):
    async with db.get_connection() as conn:
        return await conn.query(...) 
\`\`\`
```

### TypeScript/Node.js プロジェクトの場合

```
✅ Python: 必須（KB 管理）
✅ TypeScript テンプレート: そのままで OK
✅ 結果: TypeScript 例の KB

※ テンプレートが既に TypeScript なので変更不要
```

### Java プロジェクトの場合

```
✅ Python: 必須（KB 管理）
✅ TypeScript テンプレート: Java に置き換え
✅ 結果: Java 例の KB

例:
# Pattern: Resource Management

## Solution (Java)

\`\`\`java
try (Connection conn = getConnection()) {
    // use connection
}
\`\`\`
```

### Go/Rust/C++ etc. プロジェクトの場合

```
✅ Python: 必須（KB 管理）
✅ TypeScript テンプレート: あなたの言語に置き換え
✅ 結果: あなたの言語の KB

例:
# Pattern: Error Handling

## Solution (Rust)

\`\`\`rust
match resource.lock() {
    Ok(mut conn) => { ... },
    Err(e) => { ... }
}
\`\`\`
```

---

## 💡 推奨事項

### テンプレートのカスタマイズ方法

#### Before（デフォルト）

```markdown
# Pattern: Resource Cleanup

## Solution

\`\`\`typescript
async function fetchUser(id: string) {
    const conn = await db.getConnection();
    try {
        return await conn.query(...);
    } finally {
        await conn.release();
    }
}
\`\`\`
```

#### After（Python プロジェクト向けに置き換え）

```markdown
# Pattern: Resource Cleanup

## Solution

\`\`\`python
async def fetch_user(id):
    conn = await db.get_connection()
    try:
        return await conn.query(...)
    finally:
        await conn.release()
\`\`\`
```

#### After（マルチ言語プロジェクト）

```markdown
# Pattern: Resource Cleanup

## Python

\`\`\`python
async def fetch_user(id):
    async with db.get_connection() as conn:
        return await conn.query(...)
\`\`\`

## TypeScript

\`\`\`typescript
async function fetchUser(id: string) {
    const conn = await db.getConnection();
    try {
        return await conn.query(...);
    } finally {
        await conn.release();
    }
}
\`\`\`

## Go

\`\`\`go
func FetchUser(id string) (User, error) {
    conn := db.GetConnection()
    defer conn.Release()
    return conn.Query(...)
}
\`\`\`
```

---

## ✅ 最終確認

| 項目 | 確認 | 結果 |
|------|------|------|
| Python 3.8+ インストール済み | `python3 --version` | ✅ 必須 |
| kb-generator.py が実行可能 | `python3 kb-generator.py init` | ✅ 必須 |
| TypeScript のインストール | オプション | ✅ 不要 |
| プロジェクト言語への置き換え | テンプレートをカスタマイズ | ✅ 推奨 |

---

## 🎉 結論

### 簡潔に言うと

> **Python は必須。TypeScript はテンプレートの例にすぎず、あなたのプロジェクト言語に置き換え可能。**

```
KWF をセットアップするのに必要な言語:
├─ Python: ✅ 必須
├─ TypeScript: ❌ 不要（テンプレート例のみ）
├─ あなたのプロジェクト言語: ✅ あれば参照可
└─ その他: ❌ 不要
```

### 初日にすること

```bash
# 1. Python がインストール済みか確認
python3 --version

# 2. KWF を初期化
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py init

# 3. テンプレートを開いて、プロジェクト言語に合わせてカスタマイズ
vim decision-template.md
vim pattern-template.md
vim lesson-template.md

# 4. GitHub にプッシュ
git add ...
git commit ...
git push ...
```

これで OK ✅

---

**最後に**: Python があれば、KWF は完全に機能します。TypeScript は単なるテンプレート例です。遠慮なくカスタマイズしてください！

**Version**: 1.0  
**Updated**: 2026-03-01  
**Status**: Final ✅
