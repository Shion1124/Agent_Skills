# Knowledge Workflow Framework + Playwright / Serena / Context7 統合戦略

**作成日**: 2026-03-01  
**対象**: KWF を Playwright, Serena, Context7 と統合したい組織  
**実装難度**: 中級  
**期待効果**: テスト品質 + コード品質 + バージョン管理 の完全統合

---

## 📊 統合アーキテクチャ概観

```
┌─────────────────────────────────────────────────────┐
│  Knowledge Workflow Framework (メタスキル)          │
│  ↓                                                  │
│  ┌─────────────┬──────────────┬──────────────┐    │
│  │ Playwright  │   Serena     │  Context7    │    │
│  │  統合スキル  │  統合スキル   │  統合スキル   │    │
│  └─────────────┴──────────────┴──────────────┘    │
│  ↓                                                  │
│  KB に自動記録                                      │
│  ├─ テスト結果（整合性測定）                        │
│  ├─ コード品質（ベストプラクティス）                │
│  └─ バージョン管理（ライブラリ統一）               │
└─────────────────────────────────────────────────────┘
```

---

## 🎯 各ツールの役割定義

### 1️⃣ **Playwright - RAG としてのシステム整合性測定**

**目的**: テスト駆動で知見を蓄積、検索可能にする

```
Playwright テスト実行
    ↓
① テスト結果の記録
② 失敗パターン → レッスン化
③ 成功パターン → パターン化
④ カバレッジ情報の記録
    ↓
KB に自動保存
    ↓
Copilot: "このコンポーネントのテスト方法は？"
→ 過去のテスト結果から参照
```

**記録対象**:
- ✅ テスト実行結果（成功/失敗）
- ✅ テストカバレッジ（行数、分岐数）
- ✅ テスト失敗時の根本原因
- ✅ テスト実行時間（パフォーマンス）
- ✅ E2E テストで発見したバグ
- ✅ フラッキーテストの記録と解決策

---

### 2️⃣ **Serena - コーディングベストプラクティス & 技術的負債削減**

**目的**: コード品質を自動チェック、知見を蓄積

```
Serena コード分析
    ↓
① 可読性スコア計算
② エラーパターン検出
③ ベストプラクティス違反検出
④ 技術的負債の量化
    ↓
KB に自動保存
    ↓
Copilot: "このコードの品質は？"
→ Serena の分析結果から参照
```

**記録対象**:
- ✅ コード品質スコア（可読性、保守性）
- ✅ よくあるエラーパターン
- ✅ 技術的負債（量と種類）
- ✅ ベストプラクティス違反
- ✅ リファクタリング提案
- ✅ セキュリティ問題

---

### 3️⃣ **Context7 - ライブラリバージョン統一管理**

**目的**: バージョン互換性を管理、依存関係を最適化

```
Context7 バージョン管理
    ↓
① ライブラリバージョンの統一確認
② 互換性チェック
③ セキュリティアップデート検出
④ 非推奨パッケージ検出
    ↓
KB に自動保存
    ↓
Copilot: "React 18 で使うべきライブラリバージョンは？"
→ Context7 の管理データから参照
```

**記録対象**:
- ✅ ライブラリバージョンポリシー（決定）
- ✅ バージョン互換性マトリックス
- ✅ セキュリティアップデート履歴
- ✅ 非推奨パッケージ一覧
- ✅ アップグレードガイド
- ✅ バージョン衝突の解決策

---

## 🛠️ 実装戦略（3段階）

### **Stage 1: 統合スキル作成（1-2週間）**

各ツール用に統合スキルを作成：

```
.github/skills/
├── knowledge-workflow-framework/        (既存)
├── playwright-integration/              (新規)
│   ├── SKILL.md
│   ├── playwright-collector.py
│   └── templates/
│       ├── test-result-template.md
│       └── test-lesson-template.md
│
├── serena-integration/                  (新規)
│   ├── SKILL.md
│   ├── serena-analyzer.py
│   └── templates/
│       ├── code-quality-template.md
│       └── refactoring-template.md
│
└── context7-integration/                (新規)
    ├── SKILL.md
    ├── context7-manager.py
    └── templates/
        ├── version-policy-template.md
        └── dependency-template.md
```

### **Stage 2: KB カテゴリ拡張（1週間）**

KWF-CONFIG.yaml に新しいカテゴリを追加：

```yaml
decision_categories:
  # 既存
  architecture:
  tools:
  database:
  security:
  process:
  performance:
  # 新規
  testing-strategy:           # Playwright 用
    description: "テスト戦略と品質基準"
  code-quality-standards:     # Serena 用
    description: "コード品質とベストプラクティス"
  dependency-management:      # Context7 用
    description: "ライブラリバージョン管理"

pattern_categories:
  # 既存
  api-design:
  testing:
  database:
  security:
  performance:
  # 新規
  playwright-patterns:        # Playwright 用
  code-quality-patterns:      # Serena 用
  version-management:         # Context7 用
```

### **Stage 3: 自動化パイプライン構築（2-4週間）**

CI/CD パイプラインに統合：

```
GitHub Actions (CI/CD)
    ↓
① Playwright テスト実行
   → テスト結果を収集
   → KB に自動記録
    ↓
② Serena コード分析実行
   → 品質スコア計算
   → KB に自動記録
    ↓
③ Context7 バージョンチェック実行
   → ライブラリ検査
   → KB に自動記録
    ↓
④ KWF インデックス更新
   → knowledge-index.json 再生成
    ↓
結果: 最新データが常に KB に反映
```

---

## 📝 各ツールの具体的な統合方法

### **Playwright 統合の詳細**

#### 1. テスト結果の自動記録

```python
# playwright-collector.py
import subprocess
import json
from datetime import datetime
from pathlib import Path

class PlaywrightCollector:
    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
        self.timestamp = datetime.now().isoformat()
    
    def run_tests(self):
        """Playwright テストを実行して結果を収集"""
        # Playwright テスト実行
        result = subprocess.run(
            ["npx", "playwright", "test", "--reporter=json"],
            capture_output=True,
            text=True
        )
        
        # 結果をパース
        test_results = json.loads(result.stdout)
        return test_results
    
    def create_test_report(self, results):
        """テスト結果から KB エントリを作成"""
        report = {
            "date": self.timestamp,
            "total_tests": len(results["suites"]),
            "passed": sum(1 for s in results["suites"] if s.get("ok")),
            "failed": sum(1 for s in results["suites"] if not s.get("ok")),
            "duration": results.get("stats", {}).get("duration", 0),
            "coverage": self._calculate_coverage(results)
        }
        return report
    
    def save_to_kb(self, report, test_type="e2e"):
        """KB にテスト結果を保存"""
        filename = f"test-report-{test_type}-{self.timestamp}.md"
        filepath = self.kb_path / "lessons" / datetime.now().strftime("%Y") / filename
        
        content = f"""---
name: test-report-{test_type}
type: test-result
date: {self.timestamp}
test_type: {test_type}
---

# Test Report: {test_type.upper()} - {self.timestamp}

## Summary
- Total Tests: {report['total_tests']}
- Passed: {report['passed']}
- Failed: {report['failed']}
- Duration: {report['duration']}ms

## Coverage
- Line Coverage: {report['coverage']['lines']}%
- Branch Coverage: {report['coverage']['branches']}%
- Function Coverage: {report['coverage']['functions']}%

## Failed Tests
[失敗したテストの詳細]

## Insights
[学んだこと、改善点]
"""
        filepath.write_text(content)
        return filepath
```

#### 2. テスト失敗からのレッスン記録

```markdown
# Lesson: Flaky E2E Test - Modal Dialog Timing

**Date**: 2026-03-01  
**Test**: login-flow.spec.ts - "should handle modal dialog correctly"  
**Severity**: Medium

## Problem
ローカルでは成功、CI では 10% の確率で失敗する。

## Root Cause
Modal ダイアログの display アニメーションが完了するのを待たずに
クリックしていた。アニメーション時間が環境によって異なる。

## Solution
```typescript
// ❌ Before
await page.click('#confirm-button');

// ✅ After
await page.waitForSelector('#confirm-button[visible]');
await page.click('#confirm-button');

// または更に確実に
await page.locator('#confirm-button').click();  // Playwright の推奨方法
```

## Prevention
- [pattern-010] "Playwright Best Practices" に追加
- すべてのダイアログテストでこのパターンを使用
- 定期的に信頼性テストを実行

## Related
- [decision-001] "Playwright vs Cypress"
- [pattern-010] "Playwright Best Practices"
```

#### 3. テスト駆動の知見活用

```
Copilot Chat での使用例：

You: "モーダルダイアログをテストする際のベストプラクティスは？"

Copilot: [KB を検索]

結果: 
- decision-001 "Playwright を選択した理由"
- pattern-010 "Playwright ベストプラクティス"
- lesson-047 "Flaky テスト修正 - モーダルタイミング"
- test-report-2026-02-28 (過去 7 日間のテスト結果)

を自動参照して最適なガイダンスを提供
```

---

### **Serena 統合の詳細**

#### 1. コード品質分析の自動記録

```python
# serena-analyzer.py
import subprocess
import json
from pathlib import Path

class SerenaAnalyzer:
    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
    
    def analyze_code(self, target_dir):
        """Serena でコード分析"""
        # Serena CLI を実行
        result = subprocess.run(
            ["serena", "analyze", target_dir, "--json"],
            capture_output=True,
            text=True
        )
        
        analysis = json.loads(result.stdout)
        return analysis
    
    def create_quality_report(self, analysis):
        """品質レポートを作成"""
        return {
            "timestamp": datetime.now().isoformat(),
            "overall_score": analysis.get("overall_quality_score"),
            "readability": analysis.get("readability_score"),
            "maintainability": analysis.get("maintainability_score"),
            "errors": self._extract_errors(analysis),
            "technical_debt": self._calculate_debt(analysis),
            "violations": analysis.get("violations", [])
        }
    
    def save_code_quality_pattern(self, report):
        """KB に品質パターンを保存"""
        # 高スコア (90+) なら成功パターンとして記録
        if report["overall_score"] >= 90:
            filename = f"good-code-pattern-{report['timestamp']}.md"
            # パターンとして記録
        
        # 低スコア (<70) なら改善候補として記録
        elif report["overall_score"] < 70:
            filename = f"refactoring-opportunity-{report['timestamp']}.md"
            # レッスンとして記録
```

#### 2. ベストプラクティス集の自動生成

```markdown
# Pattern: High-Quality Code Structure (Score: 95/100)

**Date**: 2026-03-01  
**Source**: Serena Analysis  
**Module**: UserAuthenticationService

## What Makes This Code High Quality

### Readability (98/100)
- Clear function names
- Proper variable naming
- Well-structured control flow
- Adequate comments

### Maintainability (93/100)
- Low cyclomatic complexity
- DRY principle applied
- Single responsibility principle
- Easy to test

### Key Metrics
```typescript
// ✅ Example from codebase

class UserAuthenticationService {
  /**
   * Authenticates a user with provided credentials.
   * @param email - User email
   * @param password - User password
   * @returns Promise<AuthToken>
   * @throws AuthenticationError if credentials invalid
   */
  async authenticate(email: string, password: string): Promise<AuthToken> {
    // Input validation
    this.validateCredentials(email, password);
    
    // Check user exists
    const user = await this.userRepository.findByEmail(email);
    if (!user) {
      throw new AuthenticationError("User not found");
    }
    
    // Verify password
    const isPasswordValid = await this.passwordService.verify(
      password,
      user.hashedPassword
    );
    if (!isPasswordValid) {
      throw new AuthenticationError("Invalid password");
    }
    
    // Generate token
    return this.tokenService.generate(user);
  }
}
```

## Why This Pattern Works
1. Clear responsibility separation
2. Proper error handling
3. Good naming conventions
4. Type safety (TypeScript)
5. Testability

## Learn From This
Apply to your code:
- [ ] Use similar function documentation
- [ ] Follow same error handling pattern
- [ ] Keep cyclomatic complexity < 5
- [ ] Use async/await properly
```

#### 3. 技術的負債の追跡

```markdown
# Technical Debt Inventory

**Date**: 2026-03-01  
**Serena Analysis Result**  
**Total Debt Score**: 2,400 points (Moderate)

## By Category

### High-Priority Debt (Fix within Sprint)
1. **Untyped Variables** (400 points)
   - Files: 12
   - Example: `let user = ...` (instead of `let user: User = ...`)
   - Fix: Add TypeScript types

2. **Long Functions** (350 points)
   - Files: 5
   - Example: PaymentService.processPayment (280 lines)
   - Fix: Refactor into smaller functions

### Medium-Priority Debt (Fix within 2 Sprints)
3. **Duplicate Code** (300 points)
   - 450 lines of duplicated code
   - Example: ValidationLogic repeated 3 times
   - Fix: Extract to utility functions

### Low-Priority Debt (Backlog)
4. **Outdated Comments** (200 points)
5. **Complex Conditionals** (150 points)

## ROI Estimation
- Fixing High-Priority: 10 hours → 2x faster debugging
- Fixing Medium-Priority: 8 hours → better maintainability
- Total Time: 18 hours → estimated payoff in 2 months

## Next Steps
- [ ] Create refactoring story for High-Priority items
- [ ] Include in sprint planning
- [ ] Review every sprint
```

---

### **Context7 統合の詳細**

#### 1. バージョン管理ポリシーの決定記録

```markdown
# Decision: Library Version Management Strategy

**Date**: 2026-03-01  
**Status**: ACCEPTED  
**Category**: dependency-management

## Context
Multiple projects using different versions of same libraries.
Creates incompatibility issues and security risks.

## Decision
Implement unified version management using Context7:
1. Pin major.minor versions in monorepo root
2. Allow patch updates automatically
3. Monthly security update review
4. Quarterly major version assessment

## Version Policy

### Core Libraries (Strict)
```yaml
React: 18.2.x        # Locked to minor version
TypeScript: 5.0.x    # Locked to minor version
Node.js: 20.x        # LTS version
```

### Development Tools (Flexible)
```yaml
ESLint: ^8.0.0       # Allow patch and minor
Prettier: ^3.0.0     # Allow patch and minor
Jest: ^29.0.0        # Allow patch and minor
```

### Security Policy
- Critical CVEs: Fix within 24 hours
- High CVEs: Fix within 1 week
- Medium CVEs: Fix within 2 weeks
- Low CVEs: Bundle with regular updates

## Tools
- Context7: Automated version checking
- Dependabot: Security alerts
- Renovate: Automated updates (configured for our policy)

## Related
- [pattern-230] "Monorepo Version Consistency"
- [lesson-089] "Version Mismatch Bug (React 17 vs 18)"
```

#### 2. バージョン互換性マトリックス

```markdown
# Pattern: React 18 + Ecosystem Compatibility

**Category**: version-management  
**Maintained By**: Platform Team  
**Last Updated**: 2026-03-01

## Verified Compatible Versions

| Library | Recommended | Minimum | Max Tested | Notes |
|---------|------------|---------|-----------|-------|
| React | 18.2.0 | 18.0.0 | 18.2.0 | Stable LTS |
| React-DOM | 18.2.0 | 18.0.0 | 18.2.0 | Must match React |
| Next.js | 14.x | 13.5.0 | 14.1.0 | App Router support |
| TypeScript | 5.0.x | 5.0.0 | 5.3.0 | Strict mode required |
| Tailwind | 3.3.x | 3.0.0 | 3.3.6 | Works perfectly |
| Zustand | 4.4.x | 4.0.0 | 4.4.0 | State management |
| Prisma | 5.x | 5.0.0 | 5.8.0 | ORM |

## Known Issues

### ⚠️ React 18 + React-Query 4
**Issue**: Strict mode double-renders cause unexpected API calls  
**Solution**: Use `suspense: false` config  
**Workaround**: [pattern-089] "React Query Setup"

### ⚠️ Next.js 14 + Old ESLint Config
**Issue**: ESLint v8 incompatible with new Next.js config  
**Solution**: Upgrade to ESLint 9  
**Impact**: 1-2 hours migration

## When to Update

### Patch Updates (Automatic)
- Auto-apply all patches
- Include in regular CI runs
- No manual review needed

### Minor Updates (Quarterly)
- Test on staging first
- Review for breaking changes
- Include in quarterly release

### Major Updates (Annually)
- Full regression testing required
- Documentation update needed
- Team training may be required
- Plan 2-4 weeks ahead

## See Also
- [decision-150] "Version Management Policy"
- [lesson-089] "React 17 → 18 Migration"
- [pattern-230] "Monorepo Dependency Lock"
```

#### 3. セキュリティアップデート追跡

```markdown
# Security Update Log

**Tracked By**: Context7  
**Last Updated**: 2026-03-01

## Recent CVEs Fixed

### Critical
- React 18.0.0 → 18.2.0: XSS vulnerability
  - Fixed in patch release
  - No code changes needed
  - ✅ Applied to production

### High
- Next.js 13.0.0 → 13.5.0: Server-side request forgery
  - Affects API routes
  - ✅ Applied to production
  - No impact on current code

## Upcoming Updates Required

### Next 30 Days
- TypeScript 5.2 → 5.3: 2 minor features
  - Breaking: None detected
  - Estimated time: 2 hours testing

### Next 90 Days
- Node.js 20.x → 22.x: LTS upgrade
  - Breaking: None detected
  - Estimated time: 1 week testing

## Policy Adherence
✅ All critical vulnerabilities patched  
✅ High vulnerabilities <1 week old  
✅ No major version mismatches  
⚠️ 3 low-severity items in backlog
```

---

## 🔄 自動化パイプライン（GitHub Actions）

```yaml
# .github/workflows/knowledge-integration.yml

name: Knowledge Integration Pipeline

on:
  push:
    branches: [main, develop]
  schedule:
    - cron: '0 2 * * *'  # Daily 2 AM

jobs:
  playwright-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Playwright Tests
        run: npx playwright test --reporter=json
      
      - name: Collect Test Results
        run: |
          python3 .github/skills/playwright-integration/playwright-collector.py \
            --test-results test-results.json \
            --kb-path .github/skills/knowledge-workflow-framework
      
      - name: Commit Test Report
        run: |
          git add .github/skills/knowledge-workflow-framework/lessons/
          git commit -m "Add test report: $(date +%Y-%m-%d)"
          git push

  code-quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Serena Analysis
        run: npx serena analyze src/ --json > serena-results.json
      
      - name: Update Code Quality KB
        run: |
          python3 .github/skills/serena-integration/serena-analyzer.py \
            --results serena-results.json \
            --kb-path .github/skills/knowledge-workflow-framework
      
      - name: Comment on PR
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v6
        with:
          script: |
            const fs = require('fs');
            const results = JSON.parse(fs.readFileSync('serena-results.json'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## Code Quality Report\n
              Overall Score: ${results.overall_score}/100\n
              Readability: ${results.readability}/100\n
              Maintainability: ${results.maintainability}/100`
            });

  dependency-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Run Context7 Check
        run: npx context7 check --json > context7-results.json
      
      - name: Update Version KB
        run: |
          python3 .github/skills/context7-integration/context7-manager.py \
            --results context7-results.json \
            --kb-path .github/skills/knowledge-workflow-framework
      
      - name: Alert on Issues
        run: |
          if grep -q "version-mismatch\|security-issue" context7-results.json; then
            echo "::warning::Version management issues detected"
          fi

  knowledge-index-update:
    needs: [playwright-tests, code-quality, dependency-check]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Update Knowledge Index
        run: |
          cd .github/skills/knowledge-workflow-framework
          python3 kb-generator.py update-index
      
      - name: Validate KB
        run: |
          cd .github/skills/knowledge-workflow-framework
          python3 kb-generator.py validate
      
      - name: Commit Updated Index
        run: |
          git add .github/skills/knowledge-workflow-framework/knowledge-base/knowledge-index.json
          git commit -m "Update KB index after tools run"
          git push
```

---

## 📊 統合後の使用フロー

### ユースケース 1: "このテストをどう書く？"

```
Copilot Chat:
You: "@copilot モーダルダイアログの E2E テストを書きたい"

Copilot処理:
1. KB 検索: "Playwright E2E テスト"
   → decision-001 "Playwright選択理由"
   → pattern-010 "Playwright ベストプラクティス"
   → test-report-2026-02-28 "過去のテスト結果"
   → lesson-047 "Flaky テスト対策 - モーダル"

2. 検索結果をコンテキストに追加

3. 提案:
"Based on your team's Playwright experience and past test results,
here's the recommended approach:

✓ Use locator() instead of XPath (pattern-010)
✓ Handle modal animations properly (lesson-047)
✓ Add network idle wait (best practice from reports)

Generated code:
\`\`\`typescript
test('modal dialog interaction', async ({ page }) => {
  // Based on pattern-010 and lesson-047
  await page.goto('/page-with-modal');
  
  // Wait for modal animation
  await page.locator('.modal').isVisible();
  
  // Interact with modal
  await page.locator('[data-testid="confirm"]').click();
  
  // Wait for network
  await page.waitForLoadState('networkidle');
});
\`\`\`"
```

### ユースケース 2: "このコード品質どう？"

```
Copilot Chat:
You: "@copilot このサービスクラスのコード品質評価"

Copilot処理:
1. Serena 分析を実行
2. KB から類似パターンを検索
   → pattern-015 "High Quality Code Structure"
   → technical-debt-report-2026-02

3. フィードバック:
"Code Quality Analysis:
- Overall Score: 78/100 (Good)
- Readability: 82/100 ✅
- Maintainability: 72/100 (可改善)

Suggestions:
1. Split into smaller functions (pattern-015)
2. Add error handling types (technical-debt report)
3. Consider dependency injection (pattern-089)

Time to fix: ~3 hours
Estimated payoff: Better testability, easier debugging"
```

### ユースケース 3: "このライブラリのバージョンは？"

```
Copilot Chat:
You: "@copilot React のベストバージョンは？"

Copilot処理:
1. Context7 バージョン情報取得
2. KB から互換性マトリックス検索
   → pattern-230 "React 18 Compatibility"
   → decision-150 "Version Management Policy"
   → security-update-log

3. 回答:
"React Version Recommendation:

Current Policy: 18.2.x (locked to minor)
Latest Stable: 18.2.0

✅ Compatible Ecosystem:
- Next.js: 14.x
- React Query: 4.4.x
- TypeScript: 5.0.x
- Tailwind: 3.3.x

⚠️ Known Issues:
- Strict mode double-renders with react-query
  Solution: Use suspense: false

🔒 Security Status:
✅ All CVEs patched
✅ No critical vulnerabilities
Last updated: 2 days ago"
```

---

## ✅ 統合チェックリスト

### Phase 1: 準備（1週間）

- [ ] Playwright 統合スキルを作成
- [ ] Serena API/CLI を確認
- [ ] Context7 セットアップ
- [ ] テンプレートを作成
- [ ] KWF-CONFIG.yaml を拡張

### Phase 2: 実装（2-3週間）

- [ ] playwright-collector.py を実装
- [ ] serena-analyzer.py を実装
- [ ] context7-manager.py を実装
- [ ] GitHub Actions ワークフローを作成
- [ ] ローカルでテスト

### Phase 3: 運用（継続）

- [ ] 日次: 自動パイプライン実行
- [ ] 週次: KB 検索精度確認
- [ ] 月次: 統合フローのレビュー
- [ ] 四半期: ツール設定の調整

---

## 🎯 期待効果

### テスト品質面
- テスト カバレッジ向上
- Flaky テスト 80% 削減
- 新規テスト作成時間 50% 短縮

### コード品質面
- 技術的負債の可視化
- リファクタリング効率 3倍
- バグ検出率 40% 向上

### 依存関係管理
- セキュリティ問題 対応時間 90% 短縮
- バージョン衝突 ゼロ
- メジャーアップグレード計画立案が容易

---

**Version**: 1.0  
**Created**: 2026-03-01  
**Status**: Ready for Implementation
