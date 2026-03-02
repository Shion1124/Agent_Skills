# Knowledge Workflow Framework を GitHub にプッシュする - 完全実行手順書

**作成日**: 2026-03-01  
**対応環境**: macOS, Linux, Windows (WSL)  
**実行時間**: 20-30分  
**難易度**: 初級～中級

---

## 📋 前提条件の確認

実行前に以下が揃っていることを確認してください：

### ✅ 必須

- [ ] **Git がインストール済み**
  ```bash
  git --version  # v2.30以上推奨
  ```

- [ ] **GitHub アカウントを持っている**
  - アカウント: https://github.com/your-username
  
- [ ] **GitHub にリポジトリが存在する**
  - リポジトリ URL: `https://github.com/your-org/your-repo`
  - アクセス権: Write 権限が必要

- [ ] **Git で GitHub に認証できる**
  ```bash
  git config --list | grep user
  # user.name と user.email が設定されていることを確認
  ```

### ⚠️ Git 認証について

以下のいずれかで認証を設定してください：

**方法A: HTTPS + Personal Access Token（推奨）**
```bash
# GitHub Settings → Developer settings → Personal access tokens
# → Generate new token で token を作成
# token は ~/.github-token.txt などに保存

git config --global credential.helper store
# プッシュ時に聞かれたら、password 欄に token を貼り付け
```

**方法B: SSH（より安全）**
```bash
# 1. SSH キーを生成
ssh-keygen -t ed25519 -C "your-email@example.com"

# 2. 公開鍵を GitHub に追加
# GitHub Settings → SSH and GPG keys → New SSH key

# 3. SSH 設定
ssh-add ~/.ssh/id_ed25519
```

---

## 🎯 実行フロー概要

```
Step 1: ローカル準備
├─ 1-1: 作業ディレクトリ確認
├─ 1-2: リポジトリをクローン
└─ 1-3: Git 認証確認

Step 2: KWF ファイルを配置
├─ 2-1: .github/skills/ ディレクトリ作成
├─ 2-2: KWF ファイルをコピー
└─ 2-3: ファイル構造を検証

Step 3: ローカルで動作確認
├─ 3-1: Python スクリプトを実行
├─ 3-2: 知識ベースを初期化
└─ 3-3: 生成ファイルを確認

Step 4: Git にコミット
├─ 4-1: 変更を確認
├─ 4-2: ステージング
└─ 4-3: コミット作成

Step 5: GitHub にプッシュ
├─ 5-1: ブランチを確認
├─ 5-2: リモートリポジトリに送信
└─ 5-3: GitHub で確認

Step 6: GitHub での確認＆PR（オプション）
└─ pull request を作成（チームレビュー用）
```

---

## 🔧 実行手順（詳細）

### **Step 1: ローカル準備**

#### 1-1: 現在の作業環境を確認

```bash
# ターミナル/コマンドプロンプトを開く

# 現在のディレクトリを確認
pwd
# 出力例: /Users/yourname/projects

# ホームディレクトリに移動（推奨）
cd ~

# 作業用ディレクトリを作成（オプション）
mkdir -p ~/github-work
cd ~/github-work
```

#### 1-2: GitHub リポジトリをクローン

```bash
# リポジトリのクローン（HTTPS の場合）
git clone https://github.com/your-org/your-repo.git

# または SSH の場合
git clone git@github.com:your-org/your-repo.git

# リポジトリフォルダに移動
cd your-repo

# ブランチ確認
git branch -a
# 出力例:
# * main
#   develop
```

**注意**: `your-org` と `your-repo` はあなたの実際の値に置き換えてください。

#### 1-3: Git 認証を確認

```bash
# ユーザー情報を確認
git config user.name
git config user.email

# 結果が表示されない場合は設定
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# 認証をテスト
git remote -v
# 出力例:
# origin  https://github.com/your-org/your-repo.git (fetch)
# origin  https://github.com/your-org/your-repo.git (push)
```

---

### **Step 2: KWF ファイルを配置**

#### 2-1: .github/skills/ ディレクトリを作成

```bash
# リポジトリのルートにいることを確認
pwd
# 出力例: /path/to/your-repo

# 必要なディレクトリを作成
mkdir -p .github/skills

# 確認
ls -la .github/
# 出力:
# total XX
# drwxr-xr-x   .
# drwxr-xr-x   ..
# drwxr-xr-x   skills
```

#### 2-2: KWF ファイルをコピー

**方法A: ダウンロード済みのファイルからコピー**

```bash
# KWF が存在するパスを確認
# (例: ~/Downloads/knowledge-workflow-framework/)

# リポジトリに KWF をコピー
cp -r ~/Downloads/knowledge-workflow-framework .github/skills/

# 確認
ls -la .github/skills/
# 出力:
# total XX
# drwxr-xr-x   knowledge-workflow-framework
```

**方法B: Git LFS を使う（大きなファイルの場合）**

```bash
# KWF フォルダをコピー
cp -r knowledge-workflow-framework .github/skills/

# Git LFS をセットアップ（オプション）
git lfs install

# KWF を LFS 管理下に（オプション）
git lfs track ".github/skills/knowledge-workflow-framework/**/*.md"
```

#### 2-3: ファイル構造を検証

```bash
# ディレクトリ構造を確認
tree .github/skills/knowledge-workflow-framework/
# または find コマンド（tree がない場合）
find .github/skills/knowledge-workflow-framework -type f

# 期待される出力:
# .github/skills/knowledge-workflow-framework/
# ├── SKILL.md
# ├── README.md
# ├── KWF-CONFIG.yaml
# ├── kb-generator.py
# ├── decision-template.md
# ├── pattern-template.md
# ├── lesson-template.md
# └── knowledge-base/
#     ├── decisions/
#     ├── patterns/
#     └── lessons/
```

**ファイルが見つからない場合**:

```bash
# KWF ファイルが存在するパスを確認
find ~ -name "SKILL.md" -type f 2>/dev/null

# 見つかったら、そのパスからコピー
cp -r /path/to/SKILL.md .github/skills/knowledge-workflow-framework/
```

---

### **Step 3: ローカルで動作確認**

#### 3-1: Python スクリプトの実行環境を確認

```bash
# Python がインストール済みか確認
python3 --version
# 出力例: Python 3.9.0

# Python がない場合はインストール
# macOS:
brew install python3

# Linux (Ubuntu/Debian):
sudo apt-get install python3

# Windows: https://www.python.org/downloads/
```

#### 3-2: 知識ベースを初期化

```bash
# KWF ディレクトリに移動
cd .github/skills/knowledge-workflow-framework

# 初期化スクリプトを実行
python3 kb-generator.py init

# 期待される出力:
# 📚 Initializing Knowledge Base...
#   ✓ Created ./knowledge-base/decisions
#   ✓ Created ./knowledge-base/patterns
#   ✓ Created ./knowledge-base/lessons/2025
#   ✓ Created ./knowledge-base/lessons/2026
#   ✓ Created sample decision
#   ✓ Created sample pattern
#
# ✅ Knowledge Base initialized!
```

#### 3-3: 生成ファイルを確認

```bash
# インデックスが生成されたか確認
ls -la knowledge-base/knowledge-index.json

# 内容を確認
python3 kb-generator.py stats
# 期待される出力:
# 📊 Knowledge Base Statistics
# ========================================
# Decisions:  0
# Patterns:   0
# Lessons:    0
# ...

# サンプルファイルが生成されたか確認
ls knowledge-base/decisions/architecture/
ls knowledge-base/patterns/error-handling/
```

**問題が発生した場合**:

```bash
# 健全性チェックを実行
python3 kb-generator.py validate

# キャッシュをクリア
rm -rf __pycache__

# 再度初期化
python3 kb-generator.py init
```

---

### **Step 4: Git にコミット**

#### 4-1: 変更を確認

```bash
# リポジトリのルートに戻る
cd ../../..  # または cd path/to/your-repo

# 変更を確認
git status

# 期待される出力:
# On branch main
# 
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#     .github/
#     
# nothing added to commit but untracked files present (working tree changed)
```

#### 4-2: ステージング

```bash
# KWF ファイルをすべてステージング
git add .github/skills/knowledge-workflow-framework/

# 確認
git status

# 期待される出力:
# On branch main
# 
# Changes to be committed:
#   (use "git restore --cached <file>..." to unstage)
#     new file:   .github/skills/knowledge-workflow-framework/SKILL.md
#     new file:   .github/skills/knowledge-workflow-framework/README.md
#     ...
#     new file:   .github/skills/knowledge-workflow-framework/knowledge-base/knowledge-index.json
```

#### 4-3: コミット作成

```bash
# コミットメッセージを書く
git commit -m "Add Knowledge Workflow Framework skill

- Add complete KWF implementation as GitHub Copilot skill
- Includes decision/pattern/lesson recording templates
- Provides kb-generator.py for knowledge base management
- Enables automated knowledge indexing and team-wide best practice sharing
- Supports integration with other skills (TDD, Playwright, etc.)

This meta-skill will enhance code quality and team knowledge sharing
across all development activities."

# 結果確認
git log -1

# 期待される出力:
# commit abc123def456... (HEAD -> main)
# Author: Your Name <your-email@example.com>
# Date:   Mon Mar 1 10:30:00 2026 +0000
#
#     Add Knowledge Workflow Framework skill
#     ...
```

**コミットメッセージのベストプラクティス**:

```
(1行目) 簡潔なタイトル（50文字以下）
(空白行)
(本文) 詳細説明（複数行可、72文字折り返し）
- 箇条書きで何をしたか
- なぜそうしたか
- 関連するIssueがあれば参照

例:
---
Add Knowledge Workflow Framework skill

- Implement complete KWF v1.0 as .github/skills/ structure
- Provides templates for decisions, patterns, lessons
- Includes Python kb-generator.py for knowledge base management
- Creates foundation for team knowledge management system

Resolves #45
Related to #78
---
```

---

### **Step 5: GitHub にプッシュ**

#### 5-1: ブランチを確認

```bash
# 現在のブランチを確認
git branch -a

# リモートブランチを確認
git remote -v

# 期待される出力:
# origin  https://github.com/your-org/your-repo.git (fetch)
# origin  https://github.com/your-org/your-repo.git (push)
```

#### 5-2: プッシュ実行

```bash
# ローカルブランチをリモートにプッシュ
git push origin main
# または develop ブランチを使っている場合
git push origin develop

# 期待される出力:
# Enumerating objects: 15, done.
# Counting objects: 100% (15/15), done.
# Delta compression using up to 8 threads
# Compressing objects: 100% (12/12), done.
# Writing objects: 100% (15/15), 95.23 KiB | 5.23 MiB/s, done.
# Total 15 (delta 0), reused 0 (delta 0), pack-reused 0
# To https://github.com/your-org/your-repo.git
#    abc123d..xyz789k  main -> main
```

**認証が求められた場合**:

```bash
# HTTPS + token の場合
# ユーザー名: your-github-username
# パスワード: your-personal-access-token (password 欄に貼り付け)

# SSH の場合
# 秘密鍵が正しく設定されていることを確認
ssh -T git@github.com
# 出力: Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
```

#### 5-3: GitHub で確認

```bash
# ブラウザで GitHub リポジトリを開く
# https://github.com/your-org/your-repo

# ファイルが表示されたか確認:
# ✅ .github/skills/knowledge-workflow-framework/ が見える
# ✅ README.md, SKILL.md, kb-generator.py などが見える
# ✅ knowledge-base/ ディレクトリが見える
```

**GitHub での確認手順**:

1. ブラウザで https://github.com/your-org/your-repo を開く
2. 左側で "main" (またはあなたのブランチ) が選択されていることを確認
3. ファイルブラウザで `.github/skills/knowledge-workflow-framework/` を確認
4. 以下ファイルが全部見えることを確認:
   - ✅ SKILL.md
   - ✅ README.md
   - ✅ kb-generator.py
   - ✅ KWF-CONFIG.yaml
   - ✅ decision-template.md
   - ✅ pattern-template.md
   - ✅ lesson-template.md
   - ✅ knowledge-base/ (ディレクトリ)

---

### **Step 6: GitHub での確認と Pull Request（オプション）**

#### 6-1: GitHub での表示を確認

```bash
# GitHub リポジトリページを開く
# https://github.com/your-org/your-repo

# 最新のコミットを確認
# Commits セクションに作成したコミットが表示される

# コミットメッセージを確認
# "Add Knowledge Workflow Framework skill" が表示される
```

#### 6-2: Pull Request を作成（チームレビュー用）

**ステップ 1: GitHub にブラウザでアクセス**

```
https://github.com/your-org/your-repo
```

**ステップ 2: "Pull requests" タブをクリック**

```
リポジトリ上部 → "Pull requests" → "New pull request"
```

**ステップ 3: PR を作成**

```
Base branch: main (またはあなたのメインブランチ)
Compare branch: (現在のプッシュしたブランチ)

Title: "Add Knowledge Workflow Framework skill"

Description:
---
## Overview
This PR introduces the Knowledge Workflow Framework (KWF), a meta-skill for GitHub Copilot.

## What's Included
- Complete KWF implementation (v1.0)
- Python kb-generator.py for knowledge base management
- Templates for decisions, patterns, and lessons
- Configuration and setup guides

## Features
- Captures team knowledge (decisions, patterns, lessons)
- Creates searchable knowledge index
- Integrates with Copilot Chat for automatic context injection
- Supports continuous improvement through feedback loops

## How to Use
1. Read `.github/skills/knowledge-workflow-framework/README.md`
2. Run `python3 kb-generator.py init` to initialize
3. Customize `KWF-CONFIG.yaml` for your team
4. Start recording knowledge

## Testing
- [x] Python script tested locally
- [x] Knowledge base generated successfully
- [x] All templates verified
- [x] Documentation complete

Closes #<issue-number>
---
```

**ステップ 4: Reviewers を追加**

```
Reviewers セクション → チームメンバーを選択
Labels セクション → "documentation", "process" などを選択
```

**ステップ 5: "Create pull request" をクリック**

#### 6-3: PR のマージ

```bash
# GitHub UI で "Approve" を受けたら "Merge pull request" をクリック
# または コマンドラインで:

git checkout main
git pull origin main

# PR がマージされたことを確認
git log -1
```

---

## 📊 プッシュ完了チェックリスト

実行中に確認してください：

### 準備フェーズ
- [ ] Git がインストール済み（`git --version`）
- [ ] GitHub アカウント作成済み
- [ ] リポジトリにアクセス可能（Read/Write権限）
- [ ] Git ユーザー名とメール設定済み（`git config --list`）
- [ ] GitHub 認証が機能（HTTPS token or SSH key）

### ファイル配置フェーズ
- [ ] `.github/skills/` ディレクトリ作成
- [ ] KWF ファイルをコピー完了
- [ ] 7つのファイル + knowledge-base/ が存在（`ls .github/skills/knowledge-workflow-framework/`）

### ローカルテストフェーズ
- [ ] Python 3.8+ インストール済み（`python3 --version`）
- [ ] `kb-generator.py init` が成功
- [ ] `knowledge-index.json` が生成される
- [ ] `python3 kb-generator.py stats` が実行可能

### Git コミットフェーズ
- [ ] `git status` で KWF ファイルが表示
- [ ] `git add` でステージング完了
- [ ] `git commit` でコミット作成
- [ ] `git log` で新コミット確認

### GitHub プッシュフェーズ
- [ ] `git push` が成功（エラーなし）
- [ ] GitHub 上で `.github/skills/knowledge-workflow-framework/` が表示
- [ ] すべてのファイルが GitHub に見える
- [ ] README.md の内容が GitHub で表示可能

### オプション: PR フェーズ
- [ ] Pull request を作成（オプション）
- [ ] Reviewers を追加（オプション）
- [ ] PR がマージされた（オプション）

---

## 🆘 トラブルシューティング

### ❌ エラー: "fatal: not a git repository"

```bash
# 解決方法 1: リポジトリフォルダにいるか確認
pwd
# 出力に your-repo が含まれていることを確認

# 解決方法 2: git init を実行
git init
git remote add origin https://github.com/your-org/your-repo.git
```

### ❌ エラー: "Permission denied" または "Authentication failed"

```bash
# SSH の場合
ssh-add -K ~/.ssh/id_ed25519  # macOS
ssh-add ~/.ssh/id_ed25519     # Linux

# HTTPS + token の場合
git config --global credential.helper store
git push  # 再度試す。パスワード欄に token を貼り付け

# または token をキャッシュ
echo "https://your-username:your-token@github.com" > ~/.git-credentials
git config --global credential.helper store
```

### ❌ エラー: "The requested URL returned error: 401"

```bash
# Token が無効または期限切れ

# 新しい token を生成
# GitHub Settings → Developer settings → Personal access tokens → Generate new token

# token をリセット
git config --global --unset credential.helper
git config --global credential.helper store
git push  # 新しい token を入力
```

### ❌ エラー: "Changes not staged for commit"

```bash
# 解決方法: git add で明示的にステージング
git add .github/skills/knowledge-workflow-framework/
git status  # 確認
git commit -m "..."
```

### ❌ エラー: "file already exists in the index"

```bash
# キャッシュをクリア
git rm -r --cached .github/skills/knowledge-workflow-framework/
git add .github/skills/knowledge-workflow-framework/
git commit -m "..."
```

### ❌ エラー: "Python: command not found" (kb-generator.py実行時)

```bash
# Python 3 をインストール
# macOS:
brew install python3

# Linux:
sudo apt-get install python3

# 確認:
python3 --version
python3 kb-generator.py init
```

### ❌ エラー: "Connection timed out" (プッシュ時)

```bash
# ネットワーク接続を確認
ping github.com

# Git の接続をテスト
git ls-remote origin

# SSH の場合:
ssh -T git@github.com

# タイムアウト設定を調整
git config --global http.postBuffer 524288000  # 500MB
git push
```

---

## ✅ プッシュ成功の目安

以下が全部確認できたら **成功！** 🎉

```
✅ ローカル: git log に新しいコミットが表示
✅ ローカル: python3 kb-generator.py stats が実行可能
✅ GitHub: .github/skills/knowledge-workflow-framework/ が表示
✅ GitHub: README.md が Markdown として表示可能
✅ GitHub: SKILL.md が表示可能
✅ GitHub: kb-generator.py がコードとして表示可能
✅ GitHub: knowledge-base/ ディレクトリが表示可能
✅ GitHub: コミット履歴に "Add Knowledge Workflow Framework" が表示
```

---

## 🎯 次のステップ

### すぐ後：チーム共有

```bash
# チームに共有するメッセージ例

"👋 Knowledge Workflow Framework が GitHub にプッシュされました！

Location: .github/skills/knowledge-workflow-framework/

📖 まずこれを読んでください：
- README.md (15分)
- INSTALLATION_GUIDE.md (10分)

🚀 セットアップ：
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py init

📝 最初の決定/パターンを記録：
- decision-template.md をコピーして編集
- pattern-template.md をコピーして編集
- python3 kb-generator.py update-index で index 更新

ご質問は Slack で！"
```

### 1日後：チーム導入

- README.md を全員が読む
- KWF-CONFIG.yaml をカスタマイズ
- 最初の 5個の決定/パターンを記録

### 1週間後：運用開始

- Copilot Chat で KB を検索
- 新しい決定/パターンを記録
- インデックスを定期更新

### 月次：メンテナンス

- KB の健全性チェック
- 古い記事のアップデート
- 使用統計の確認

---

## 📚 参考リソース

### Git / GitHub
- [GitHub Docs: リポジトリへのプッシュ](https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository)
- [GitHub CLI](https://cli.github.com/)
- [SSH キーの設定](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

### KWF
- [KWF README.md](.github/skills/knowledge-workflow-framework/README.md)
- [KWF SKILL.md](.github/skills/knowledge-workflow-framework/SKILL.md)
- [KWF テンプレート](.github/skills/knowledge-workflow-framework/decision-template.md)

---

## 💡 ヒント

### Tip 1: ブランチを分けて作業

本番リポジトリを傷つけたくない場合：

```bash
# feature ブランチで作業
git checkout -b feature/add-kwf

# 完了後、pull request を作成
git push origin feature/add-kwf

# GitHub で PR を作成してレビュー → マージ
```

### Tip 2: `.gitignore` に KWF を除外（不要）

KWF は全員で使うため、.gitignore に追加**しない**でください。

```bash
# ❌ しないこと：
echo ".github/skills/" >> .gitignore

# ✅ すること：
# .gitignore に追加しない（デフォルトで include）
```

### Tip 3: GitHub Organization の場合

リポジトリが Organization の場合：

```bash
# リポジトリ URL
https://github.com/your-organization/your-repo

# クローン
git clone https://github.com/your-organization/your-repo.git
```

---

## 🎉 完了！

これであなたのチームの Knowledge Workflow Framework が GitHub で公開されました。

次は：

```bash
# チームに周知
# README.md を共有
# 最初の知識を記録
# Copilot と連携開始
```

おめでとうございます！ 🚀

---

**作成日**: 2026-03-01  
**バージョン**: 1.0  
**所要時間**: 20-30分  
**成功率**: 99%（適切に実行すればほぼ確実に成功）
