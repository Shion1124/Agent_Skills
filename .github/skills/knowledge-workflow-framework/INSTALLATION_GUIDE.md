# Knowledge Workflow Framework - インストール＆セットアップガイド

**作成日**: 2026-03-01  
**バージョン**: 1.0  
**対応OS**: macOS, Linux, Windows (WSL)

---

## 📦 ファイル一覧

KWFフォルダに含まれるファイル：

```
knowledge-workflow-framework/
├── README.md                    # セットアップ＆使用方法（このファイルを先に読む！）
├── SKILL.md                     # 完全なスキルドキュメント
├── kb-generator.py              # 知識ベース管理ツール（Python）
├── KWF-CONFIG.yaml              # チーム設定ファイル（カスタマイズ推奨）
├── decision-template.md         # 決定記録用テンプレート
├── pattern-template.md          # パターン記録用テンプレート
└── lesson-template.md           # レッスン/インシデント記録用テンプレート
```

---

## 🚀 インストール手順（3ステップ）

### Step 1: ファイルをリポジトリにコピー

```bash
# あなたのプロジェクトリポジトリに移動
cd your-project-repo

# skills フォルダを作成
mkdir -p .github/skills/

# KWF フォルダをコピー
cp -r knowledge-workflow-framework .github/skills/

# 正しくコピーされたか確認
ls -la .github/skills/knowledge-workflow-framework/
```

期待される出力：
```
total XX
drwxr-xr-x   KB-generator.py
drwxr-xr-x   KWF-CONFIG.yaml
drwxr-xr-x   README.md
drwxr-xr-x   SKILL.md
drwxr-xr-x   decision-template.md
drwxr-xr-x   lesson-template.md
drwxr-xr-x   pattern-template.md
```

### Step 2: 知識ベースを初期化

```bash
# KWF ディレクトリに移動
cd .github/skills/knowledge-workflow-framework

# 初期化（ディレクトリ構造と見本ファイルを作成）
python3 kb-generator.py init
```

期待される出力：
```
📚 Initializing Knowledge Base...
  ✓ Created ./knowledge-base/decisions
  ✓ Created ./knowledge-base/patterns
  ✓ Created ./knowledge-base/lessons/2025
  ✓ Created ./knowledge-base/lessons/2026
  ✓ Created sample decision
  ✓ Created sample pattern

✅ Knowledge Base initialized!
   Location: ./knowledge-base
   Next: Add your team's decisions, patterns, and lessons
```

### Step 3: チーム設定をカスタマイズ

```bash
# KWF-CONFIG.yaml をテキストエディタで開く
vim KWF-CONFIG.yaml
# または
nano KWF-CONFIG.yaml
```

**編集項目**（必須）:

```yaml
team:
  name: "あなたのチーム名"           # 変更してください
  repository_url: "https://github.com/yourorg/yourrepo"  # 変更してください
  contact: "your-team@example.com"   # 変更してください
```

**編集項目**（推奨）:

- `decision_categories`: あなたのチームに合わせて調整
- `pattern_categories`: あなたのチームに合わせて調整
- `integrations`: Slack通知など（オプション）

保存して終了します（vim: `:wq`、nano: `Ctrl+X` → `Y` → `Enter`）

---

## ✅ セットアップ確認

セットアップが正しくできたか確認します：

```bash
# ディレクトリ構造を確認
cd .github/skills/knowledge-workflow-framework
ls -la knowledge-base/

# インデックスを更新
python3 kb-generator.py update-index

# 統計を表示
python3 kb-generator.py stats
```

期待される出力：
```
📊 Knowledge Base Statistics
========================================
Decisions:  0
Patterns:   0
Lessons:    0
Total:      0

Tags:       0

By Category:

Last Updated: 2026-03-01T10:30:00Z
```

---

## 🔧 トラブルシューティング

### 問題 1: `python3: command not found`

```bash
# Python がインストールされているか確認
python --version

# Python 3 をインストール
# macOS:
brew install python3

# Linux (Ubuntu/Debian):
sudo apt-get install python3

# Windows: 
# https://www.python.org/downloads/ からインストール
```

### 問題 2: `Permission denied` エラー

```bash
# スクリプトを実行可能にする
chmod +x kb-generator.py

# 再度実行
python3 kb-generator.py init
```

### 問題 3: ディレクトリが見つからない

```bash
# 正しいディレクトリにいるか確認
pwd  # 現在のパスを表示

# 正しいパスを表示するはず:
# /.../your-project-repo/.github/skills/knowledge-workflow-framework

# いなければ移動
cd .github/skills/knowledge-workflow-framework
```

### 問題 4: `knowledge-index.json` が生成されない

```bash
# インデックスを手動で更新
python3 kb-generator.py update-index

# ファイルが生成されたか確認
ls -la knowledge-base/knowledge-index.json

# 見えないなら、権限を確認
ls -la knowledge-base/
```

---

## 📚 次のステップ

### 1. GitHub にコミット（5分）

```bash
# 設定をプレビュー
cd your-project-repo
git status

# ステージング
git add .github/skills/knowledge-workflow-framework/

# コミット
git commit -m "Add Knowledge Workflow Framework skill

- Initialize KWF with decision, pattern, lesson templates
- Configure for team use
- Ready for team to start recording knowledge"

# プッシュ
git push origin main  # または develop
```

### 2. README を読む（10分）

```bash
# README を読む（VS Code、エディタ、またはブラウザ）
open .github/skills/knowledge-workflow-framework/README.md
```

**重要なセクション**：
- "使い方"（How to Use）
- "概念説明"（Key Concepts）
- "コマンドリファレンス"（Commands Reference）

### 3. 最初の決定を記録（15分）

```bash
# decision-template.md をコピーして新しい決定を作成
cp .github/skills/knowledge-workflow-framework/decision-template.md \
   .github/skills/knowledge-workflow-framework/knowledge-base/decisions/architecture/decision-001-your-topic.md

# エディタで編集
vim .github/skills/knowledge-workflow-framework/knowledge-base/decisions/architecture/decision-001-your-topic.md
```

テンプレートに従って記入します。

### 4. インデックスを更新（1分）

```bash
cd .github/skills/knowledge-workflow-framework

# インデックスを再生成
python3 kb-generator.py update-index

# 検索してみる
python3 kb-generator.py search "your-topic"
```

### 5. Copilot で使ってみる（5分）

VS Code で:

```
@copilot help me understand our team's knowledge base about async error handling

Copilot should now reference your KB!
```

---

## 🎯 推奨されるチーム活動

### 初回ミーティング（1時間）

1. **紹介** (10分)
   - KWFが何か
   - なぜ作ったか
   - チームへのメリット

2. **デモ** (15分)
   - kb-generator.py コマンドのデモ
   - Copilot Chat での検索デモ
   - テンプレートの説明

3. **練習** (25分)
   - 最初の決定を一緒に記録
   - 最初のパターンを一緒に記録
   - 検索機能を試す

4. **Q&A** (10分)
   - 質問受け付け
   - 次のステップ確認

### 初日後

```
✅ README.md を全員が読む
✅ 既存知識を KB に追加開始
✅ テンプレートに慣れる
✅ Copilot Chat で検索してみる
```

### 1 週間後

```
✅ 少なくとも 5 個の決定が記録されている
✅ チーム内で KB が参照されている
✅ フィードバックを収集
✅ 必要に応じて設定を調整
```

---

## 📊 稼働状況チェックリスト

初期セットアップ完了の目安：

- [ ] ファイルが `.github/skills/knowledge-workflow-framework/` にある
- [ ] `python3 kb-generator.py init` が正常に実行できた
- [ ] `knowledge-base/` ディレクトリが存在する
- [ ] `KWF-CONFIG.yaml` をカスタマイズした
- [ ] `knowledge-index.json` が生成された
- [ ] GitHub にコミットされた
- [ ] README.md を読んだ
- [ ] 最初の決定/パターンを記録した
- [ ] Copilot Chat で検索してみた
- [ ] チーム全員にシェアした

すべてチェックできたら ✅ **セットアップ完了！**

---

## 🚀 これからの使い方

### 毎日
```
開発中：Copilot に質問 → KB が参照される
コードレビュー：KB のパターンを参照
```

### 毎週
```
新しい決定 or パターン → KB に記録
インデックス更新：python3 kb-generator.py update-index
```

### 毎月
```
KB の健全性チェック：python3 kb-generator.py validate
古い記事の更新：必要に応じてアップデート
```

### 毎四半期
```
チーム レビュー：KB の有効性評価
削除/統合：古い/重複する項目の整理
メトリクス：KB の影響を測定
```

---

## 📖 参考資料

### ドキュメント
- `README.md` - 使い方ガイド（**最初に読む**）
- `SKILL.md` - 完全な技術ドキュメント
- `KWF-CONFIG.yaml` - 設定リファレンス

### テンプレート
- `decision-template.md` - 決定の記録方法
- `pattern-template.md` - パターンの記録方法
- `lesson-template.md` - レッスン/インシデントの記録方法

---

## 💡 Tips

### Tip 1: テンプレートをカスタマイズ

テンプレートはあなたのチームに合わせて調整しましょう。

```bash
# 自分たちのテンプレートをコピー
cp decision-template.md decision-template-custom.md

# カスタマイズ
vim decision-template-custom.md

# これをベースに記録
cp decision-template-custom.md knowledge-base/decisions/architecture/decision-001.md
```

### Tip 2: ショートカット作成

```bash
# KB ディレクトリへのエイリアス作成
echo 'alias kb="cd .github/skills/knowledge-workflow-framework"' >> ~/.bashrc

# 再ログインするか:
source ~/.bashrc

# これで簡単にアクセス
kb
python3 kb-generator.py stats
```

### Tip 3: GitHub Issues との連携

```bash
# GitHub Issue を KB リンク
# Issue: #123 "How should we structure React components?"
# 関連 Issue に記録:
# Related KB: [pattern-045] "React Component Architecture"
# See: .github/skills/knowledge-workflow-framework/knowledge-base/patterns/frontend/pattern-045.md
```

---

## ⚠️ よくある質問

**Q: Python がない場合？**  
A: Python をインストールしてください（上記トラブルシューティング参照）

**Q: チーム全員が操作する?**  
A: はい、誰でも決定/パターン/レッスンを追加できます

**Q: Git にコミットする?**  
A: はい、KB はプロジェクトの一部です

**Q: オフラインで使える?**  
A: はい、ローカル KB として機能します

**Q: ウェブで公開できる?**  
A: 将来的には可能（今は GitHub リポジトリに限定）

---

## 🆘 ヘルプが必要?

1. **README.md** を読んでみる
2. **SKILL.md** で詳細を確認
3. **テンプレート** で例を見る
4. Copilot に聞く: `@copilot how do I use the Knowledge Workflow Framework?`

---

## 🎉 次はコレ!

セットアップ後、すぐに使い始めましょう：

1. **README.md** を読む（10分）
2. **最初の決定** を記録（15分）
3. **Copilot** で検索してみる（5分）
4. **チームで共有** する（5分）

**Total: 35分で完全に稼働開始！**

---

**準備完了？では開始しましょう！** 🚀

```bash
cd your-project-repo/.github/skills/knowledge-workflow-framework
python3 kb-generator.py init
python3 kb-generator.py stats
```

お疲れ様でした！
