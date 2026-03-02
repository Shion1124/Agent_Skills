# Knowledge Workflow Framework - インストール＆セットアップガイド

**作成日**: 2026-03-01  
**バージョン**: 1.0  
**対応OS**: macOS, Linux, Windows (WSL)

---

## 📦 ファイル一覧

### KWF（Knowledge Workflow Framework）

```
knowledge-workflow-framework/
├── README.md                    # 使用方法ガイド（最初に読む）
├── SKILL.md                     # スキル技術仕様書（詳細ドキュメント）
├── INSTALLATION_GUIDE.md        # このファイル（セットアップ手順）
├── kb-generator.py              # 知識ベース管理ツール（Python）
├── KWF-CONFIG.yaml              # チーム設定ファイル（カスタマイズ推奨）
├── decision-template.md         # 決定記録用テンプレート
├── pattern-template.md          # パターン記録用テンプレート
├── lesson-template.md           # レッスン/インシデント記録用テンプレート
└── knowledge-base/              # 実際の知識を保存するディレクトリ
    ├── decisions/
    ├── patterns/
    └── lessons/
```

### 統合スキル（Integration Skills）

#### Playwright Integration
```
playwright-integration/
├── README.md                    # 使用ガイド（最初に読む）
├── SKILL.md                     # スキル技術仕様書（詳細ドキュメント）
├── playwright_collector.py      # テスト結果収集ツール
└── templates/                   # レポートテンプレート
```

#### Serena Integration
```
serena-integration/
├── README.md                    # 使用ガイド（最初に読む）
├── SKILL.md                     # スキル技術仕様書（詳細ドキュメント）
├── serena_analyzer.py           # コード品質分析ツール
└── templates/                   # レポートテンプレート
```

#### Context7 Integration
```
context7-integration/
├── README.md                    # 使用ガイド（最初に読む）
├── SKILL.md                     # スキル技術仕様書（詳細ドキュメント）
├── context7_manager.py          # 依存関係管理ツール
└── templates/                   # レポートテンプレート
```

### ドキュメント構造について

**README.md** vs **SKILL.md** の役割分担：

| 項目 | README.md | SKILL.md |
|------|-----------|----------|
| **対象読者** | チーム開発者 | 技術者・インテグレーター |
| **内容** | 使い方、例、クイックスタート | 完全な技術仕様、アーキテクチャ |
| **詳細度** | 実用的・簡潔 | 包括的・詳細 |
| **最初に読む** | ✅ こちら | 詳細が必要な場合 |
| **参考** | 日常利用 | 統合・トラブルシューティング |

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

## 🤖 統合スキルのセットアップ（オプション）

このKWFは3つの自動化スキルと統合できます。以下はチーム導入時の推奨セットアップです。

### Step A: 統合スキルをコピー

```bash
cd your-project-repo/.github/skills/

# 3つのスキルをすべてコピー
cp -r playwright-integration .
cp -r serena-integration .
cp -r context7-integration .

# 確認
ls -la | grep integration
```

### Step A-1: 各統合スキルのドキュメント確認

各スキルをセットアップする前に、ドキュメントを確認してください：

#### Playwright Integration
```bash
cd playwright-integration

# 最初に読む
cat README.md

# 詳細な技術情報
cat SKILL.md
```

詳細情報：
- **用途**: E2Eテスト結果の自動記録・分析
- **言語**: Python
- **依存**: Playwright 1.40.0+
- **実行**: `python3 playwright_collector.py`

#### Serena Integration
```bash
cd ../serena-integration

# 最初に読む
cat README.md

# 詳細な技術情報
cat SKILL.md
```

詳細情報：
- **用途**: コード品質分析・技術負債追跡
- **言語**: Python
- **依存**: ESLint, Pylint など
- **実行**: `python3 serena_analyzer.py`

#### Context7 Integration
```bash
cd ../context7-integration

# 最初に読む
cat README.md

# 詳細な技術情報
cat SKILL.md
```

詳細情報：
- **用途**: 依存関係管理・セキュリティ脆弱性検出
- **言語**: Python
- **依存**: npm audit, pip audit など
- **実行**: `python3 context7_manager.py`

### Step B: KWF-CONFIG.yaml を拡張版に更新

既存のKWF-CONFIG.yamlを拡張版に置き換え：

```bash
cd knowledge-workflow-framework

# バックアップ作成
cp KWF-CONFIG.yaml KWF-CONFIG.yaml.backup

# 拡張版で置き換え（下記の設定をコピー&ペースト、または https://github.com/... から入手）
# 重要なセクション:
#   - integrations.playwright: true/false
#   - integrations.serena: true/false
#   - integrations.context7: true/false
#   - playwright, serena, context7 セクション各々の設定
```

### Step C: GitHub Actions ワークフローを配置

```bash
cd your-project-repo

# ワークフロー用ディレクトリ
mkdir -p .github/workflows

# ワークフローファイルをコピー
cp knowledge-integration.yml .github/workflows/

# 確認
ls -la .github/workflows/
```

### Step D: 各統合スキルの設定確認

各スキルの設定ファイルを確認・カスタマイズします：

#### Playwright Integration 設定
```bash
cd .github/skills/playwright-integration

# README で設定箇所を確認
grep -A 20 "Configuration" README.md

# または SKILL.md の設定セクションを確認
grep -A 30 "KWF-CONFIG.yaml" SKILL.md
``

デフォルト設定は KWF-CONFIG.yaml に記載されています。

#### Serena Integration 設定
```bash
cd .github/skills/serena-integration

# README で設定箇所を確認
grep -A 20 "Configuration" README.md

# または SKILL.md の設定セクションを確認
grep -A 30 "KWF-CONFIG.yaml" SKILL.md
```

コード分析対象ディレクトリを設定できます。

#### Context7 Integration 設定
```bash
cd .github/skills/context7-integration

# README で設定箇所を確認
grep -A 20 "Configuration" README.md

# または SKILL.md の設定セクションを確認
grep -A 30 "KWF-CONFIG.yaml" SKILL.md
```

脆弱性検出の重大度レベルを設定できます。

### Step E: 最初のテスト実行

```bash
# 各統合スキルをローカルで実行してテスト

# Playwright テスト記録
echo "🎭 Testing Playwright Integration..."
python3 .github/skills/playwright-integration/playwright_collector.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Serena 品質分析
echo "📊 Testing Serena Integration..."
python3 .github/skills/serena-integration/serena_analyzer.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Context7 バージョン確認  
echo "🔒 Testing Context7 Integration..."
python3 .github/skills/context7-integration/context7_manager.py \
  --kb-path .github/skills/knowledge-workflow-framework

# KB インデックス更新
echo "🔍 Updating Knowledge Base Index..."
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py update-index

# 統計確認（11+ エントリが表示されるはず）
echo "📈 Knowledge Base Statistics:"
python3 kb-generator.py stats
```

### Step F: GitHub Actions で見る

```bash
# Commit and Push
git add .github/skills/
git add .github/workflows/
git commit -m "Add KWF with Playwright, Serena, Context7 integrations"
git push origin main

# GitHub で確認
# リポジトリ → Actions タブ
# → knowledge-integration ワークフロー
# → 次の実行を待つ（スケジュール: 毎日 02:00 UTC）
# または手動トリガー (workflow_dispatch)
```

---

## ⚙️ 設定エディタ向けガイド

チーム導入時、以下の項目をカスタマイズ：

### KWF-CONFIG.yaml で設定

```yaml
team:
  name: "Your Team Name"
  repository_url: "https://github.com/yourorg/yourrepo"  # ← ここを変更
  contact: "team@example.com"

integrations:
  playwright:
    enabled: true   # false にするとPlaywrightスキル無効化
  serena:
    enabled: true   # false にするとSerenaスキル無効化
  context7:
    enabled: true   # false にするとContext7スキル無効化

playwright:
  test_directory: "tests"  # テストディレクトリ
  browsers: ["chromium", "firefox", "webkit"]

serena:
  target_directories:
    - "src"         # 分析対象ディレクトリ
    - "lib"

automation:
  tool_integration:
    playwright_pipeline:
      trigger: "after-test-run"
      time: "02:00"  # UTC時刻
    serena_pipeline:
      trigger: "daily"
      time: "02:15"  # UTC時刻
    context7_pipeline:
      trigger: "daily"
      time: "02:30"  # UTC時刻
```

### ワークフローで設定

`.github/workflows/knowledge-integration.yml`:

```yaml
schedule:
  - cron: '0 2 * * *'  # 毎日 02:00 UTC
  # 変更例: 毎日 09:00 UTC にしたい場合
  # - cron: '0 9 * * *'
```

---

## 🆘 ヘルプが必要?

### インストール関連
1. **README.md** を読んでみる
2. **SKILL.md** で詳細を確認
3. **テンプレート** で例を見る

### 統合スキル関連
- **Playwright**: [playwright-integration/README.md](../playwright-integration/README.md)
- **Serena**: [serena-integration/README.md](../serena-integration/README.md)
- **Context7**: [context7-integration/README.md](../context7-integration/README.md)

### Copilot に聞く
```
@copilot show me how to use the Knowledge Workflow Framework
@copilot what's in the knowledge base?
@copilot are there any security vulnerabilities?
```

---

## 📊 本番運用チェックリスト

セットアップ完了前に確認：

### KWF セットアップ
- [ ] ファイル配置完了
- [ ] Python 3.11+ インストール確認
- [ ] kb-generator.py init 実行
- [ ] サンプル KB エントリ生成確認

### 統合スキル（オプション）
- [ ] 3つのスキルディレクトリ配置
- [ ] KWF-CONFIG.yaml 設定更新
- [ ] ローカルテスト実行（3つすべて）
- [ ] KB インデックス更新

### GitHub Actions
- [ ] ワークフローファイル配置
- [ ] リポジトリに Push
- [ ] Actions タブで確認
- [ ] スケジュール実行まで待つ（または手動トリガー）

### チーム準備
- [ ] README.md チーム内で共有
- [ ] KB アクセス方法を説明
- [ ] Copilot Chat 使用例を示す
- [ ] 最初のレッスンをチーム全員で記録

### 最初の 1 週間
- [ ] 日次でワークフロー実行確認
- [ ] KB に新しいエントリが増えるのを確認
- [ ] チームメンバーが KB にアクセスできるか確認
- [ ] 改善フィードバック収集

---

## 🎉 次のステップ

セットアップ完了後：

### Day 1: 基本理解
```
1. README.md を読む（15分）
2. KB 構造を確認する（10分）
3. 最初の決定を記録する（15分）
```

### Day 2-3: チームの慣れ
```
1. 全員が「決定」を 1 つ記録
2. 全員が「パターン」を 1 つ記録
3. Copilot で KB を検索してみる
```

### Week 1: 継続的改善
```
1. 統合スキルの結果を確認
2. チームで KB を活用する方法を議論
3. 必要に応じて KWF-CONFIG.yaml を調整
```

### Week 2+: 本運用
```
1. 毎日のワークフロー実行を監視
2. KB を活用した効率改善を測定
3. チーム文化に組み込む
```

---

## 🚀 ゼロから本番運用まで - タイムライン

```
Total: 1-2 営業日

Day 1 Morning (1-2時間):
  ├─ ファイル配置
  ├─ Python インストール/確認
  ├─ ローカルテスト実行
  └─ 動作確認
  
Day 1 Afternoon (30分):
  ├─ GitHub 設定
  ├─ ワークフロー配置
  ├─ リポジトリ Push
  └─ GitHub Actions 確認
  
Day 2 (1時間):
  ├─ チーム向け README 共有
  ├─ アクセス確認（全員）
  ├─ 最初のレッスン記録
  └─ 本運用開始
```

---

## 📚 関連ドキュメント

### このプロジェクト内
- **プロジェクト概要**: [.github/skills/README.md](../../README.md)
- **KWF 詳細**: [README.md](README.md)
- **スキル仕様**: [SKILL.md](SKILL.md)
- **設定リファレンス**: [KWF-CONFIG.yaml](KWF-CONFIG.yaml)

### 統合スキル
- **Playwright Integration**: [../playwright-integration/README.md](../playwright-integration/README.md)
- **Serena Integration**: [../serena-integration/README.md](../serena-integration/README.md)
- **Context7 Integration**: [../context7-integration/README.md](../context7-integration/README.md)

### 外部リソース
- **GitHub Actions**: https://docs.github.com/en/actions
- **YAML 基本**: https://yaml.org/
- **Markdown 基本**: https://www.markdownguide.org/

---

**準備完了？では開始しましょう！** 🚀

```bash
# KWF 初期化
cd your-project-repo/.github/skills/knowledge-workflow-framework
python3 kb-generator.py init
python3 kb-generator.py stats

# 統合スキルテスト（オプション）
python3 ../playwright-integration/playwright_collector.py --kb-path .
python3 ../serena-integration/serena_analyzer.py --kb-path .
python3 ../context7-integration/context7_manager.py --kb-path .

# GitHub Actions 確認
cd ../..
git add .github/
git commit -m "Setup KWF with automation skills"
git push origin main
```

お疲れ様でした！ご質問があればお気軽に。
