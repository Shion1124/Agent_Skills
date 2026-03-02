# Playwright + Serena + Context7 統合 - KWF 設定ガイド

## 拡張 KWF-CONFIG.yaml

```yaml
# Enhanced KWF Configuration for Playwright, Serena, Context7 Integration

team:
  name: "Your Development Team"
  repository_url: "https://github.com/yourorg/yourrepo"
  contact: "your-team@example.com"

knowledge_base:
  location: ".github/skills/knowledge-workflow-framework/knowledge-base"
  auto_generate_index: true
  index_update_interval: "hourly"
  enable_search: true
  enable_versioning: true

# ================================================
# 拡張: Playwright, Serena, Context7 統合用カテゴリ
# ================================================

decision_categories:
  # 既存カテゴリ
  architecture:
    description: "Architectural decisions"
  tools:
    description: "Tool and library selections"
  database:
    description: "Database and data modeling decisions"
  security:
    description: "Security-related decisions"
  process:
    description: "Team process and workflow decisions"
  performance:
    description: "Performance optimization decisions"
  
  # ========== 新規: Playwright 関連 ==========
  testing-strategy:
    description: "Test strategy and quality standards"
    examples:
      - "E2E Testing Framework Selection"
      - "Test Coverage Target"
      - "Flaky Test Prevention Policy"
      - "Test Execution Strategy"
  
  test-standards:
    description: "Team testing standards and practices"
    examples:
      - "Unit Test Structure Guidelines"
      - "Integration Test Patterns"
      - "Test Data Management"
      - "Mock Strategy"
  
  # ========== 新規: Serena 関連 ==========
  code-quality-standards:
    description: "Code quality and best practices"
    examples:
      - "Readability Requirements"
      - "Maintainability Standards"
      - "Error Handling Patterns"
      - "Documentation Requirements"
  
  technical-debt-management:
    description: "Technical debt tracking and reduction"
    examples:
      - "Debt Priority Levels"
      - "Refactoring Schedule"
      - "Code Review Focus Areas"
      - "Legacy Code Handling"
  
  # ========== 新規: Context7 関連 ==========
  dependency-management:
    description: "Library version and dependency management"
    examples:
      - "Version Locking Strategy"
      - "Security Update Policy"
      - "Major Version Upgrade Plan"
      - "Monorepo Version Sync"
  
  security-updates:
    description: "Security vulnerability and update management"
    examples:
      - "CVE Response Timeline"
      - "Patch Policy"
      - "Dependency Audit Schedule"
      - "Supply Chain Security"

pattern_categories:
  # 既存カテゴリ
  api-design:
    description: "REST/GraphQL API patterns"
  testing:
    description: "Testing patterns and best practices"
  database:
    description: "Database design and optimization"
  security:
    description: "Security patterns and practices"
  performance:
    description: "Performance patterns"
  frontend:
    description: "Frontend development patterns"
  backend:
    description: "Backend development patterns"
  devops:
    description: "DevOps and infrastructure patterns"
  
  # ========== 新規: Playwright 関連 ==========
  playwright-patterns:
    description: "Playwright-specific testing patterns"
    examples:
      - "Playwright Best Practices"
      - "E2E Test Structure"
      - "Cross-browser Testing"
      - "Visual Regression Testing"
      - "Network Stubbing Patterns"
      - "Flaky Test Prevention"
  
  test-reliability:
    description: "Test reliability and stability patterns"
    examples:
      - "Wait Strategies"
      - "Retry Logic"
      - "Test Isolation"
      - "Data Cleanup"
  
  # ========== 新規: Serena 関連 ==========
  code-quality-patterns:
    description: "High-quality code patterns from Serena analysis"
    examples:
      - "Readable Code Structure"
      - "Maintainable Architecture"
      - "Error Handling Excellence"
      - "Documentation Best Practices"
      - "Type Safety Patterns"
      - "Testing Excellence"
  
  refactoring-patterns:
    description: "Proven refactoring approaches"
    examples:
      - "Function Extraction"
      - "Duplicate Code Removal"
      - "Complexity Reduction"
      - "Type Migration"
  
  # ========== 新規: Context7 関連 ==========
  version-management:
    description: "Library version management patterns"
    examples:
      - "Monorepo Dependency Lock"
      - "Version Compatibility Matrix"
      - "Upgrade Process"
      - "Dependency Pinning Strategy"
      - "Security Patch Application"
  
  dependency-resolution:
    description: "Solving dependency conflicts and issues"
    examples:
      - "Version Conflict Resolution"
      - "Peer Dependency Handling"
      - "Breaking Change Mitigation"
      - "Deprecation Migration"

lesson_categories:
  # 既存カテゴリ
  operations:
    description: "Operational issues and resolutions"
  performance:
    description: "Performance-related incidents"
  security:
    description: "Security incidents and vulnerabilities"
  development:
    description: "Development process issues"
  infrastructure:
    description: "Infrastructure and deployment issues"
  
  # ========== 新規: Playwright 関連 ==========
  test-failures:
    description: "Test failures and resolutions"
    examples:
      - "Flaky E2E Test Fix"
      - "Cross-browser Compatibility Issue"
      - "Test Timeout Problem"
  
  # ========== 新規: Serena 関連 ==========
  code-quality-issues:
    description: "Code quality problems and their fixes"
    examples:
      - "Technical Debt Accumulation"
      - "Readability Regression"
      - "Maintainability Decline"
  
  # ========== 新規: Context7 関連 ==========
  dependency-issues:
    description: "Dependency and version-related problems"
    examples:
      - "Version Mismatch Bug"
      - "Security Vulnerability Discovery"
      - "Peer Dependency Conflict"
      - "Major Version Breakage"

# ================================================
# 統合ツール設定
# ================================================

integrations:
  playwright:
    enabled: true
    auto_record_results: true
    record_interval: "after-each-run"  # after-each-run, daily, weekly
    include_coverage: true
    track_flakiness: true
    max_test_history: 30  # 最新 30 回分を保持
    
  serena:
    enabled: true
    auto_analyze: true
    analysis_interval: "daily"  # on-commit, daily, weekly
    quality_threshold: 70  # 70% 以下はレッスン化
    track_debt: true
    debt_update_interval: "weekly"
    
  context7:
    enabled: true
    auto_check: true
    check_interval: "daily"
    security_check: true
    compatibility_check: true
    track_updates: true

  github:
    enabled: true
    auto_create_issues_for_decisions: true
    auto_link_prs_to_decisions: true
    comment_on_pr: true
    add_labels: true
  
  slack:
    enabled: false
    webhook_url: ""
    notify_on_test_failure: true
    notify_on_quality_drop: true
    notify_on_security_issue: true

# ================================================
# Playwright 統合設定
# ================================================

playwright:
  script_path: ".github/skills/playwright-integration/playwright_collector.py"
  test_directory: "tests"
  browsers: ["chromium", "firefox", "webkit"]
  
  report_categories:
    test-results: "lessons"  # Markdown ファイルの保存先
    flaky-tests: "lessons"
    coverage-data: "patterns"
  
  flakiness_threshold: 3  # 3回失敗で "flaky" とマーク
  
  metrics:
    track_duration: true
    track_coverage: true
    track_failure_patterns: true
    track_performance: true

# ================================================
# Serena 統合設定
# ================================================

serena:
  script_path: ".github/skills/serena-integration/serena_analyzer.py"
  target_directories:
    - "src"
    - "lib"
  
  thresholds:
    overall: 70
    readability: 75
    maintainability: 70
    testability: 65
    security: 80
  
  violation_severity:
    critical: "refactoring-required"
    high: "attention-needed"
    medium: "improvement-suggested"
    low: "informational"
  
  report_categories:
    high_quality: "patterns/code-quality"
    issues: "lessons/code-quality"
    technical_debt: "lessons/technical-debt"
  
  auto_create_pr_comments: true
  pr_comment_threshold: 75  # スコアが 75% 以下なら PR にコメント

# ================================================
# Context7 統合設定
# ================================================

context7:
  script_path: ".github/skills/context7-integration/context7_manager.py"
  
  version_locking:
    core_libraries:  # Major.Minor でロック
      - react
      - typescript
      - next.js
    development_tools:  # Major でロック
      - eslint
      - jest
      - prettier
  
  security:
    critical_response_hours: 24
    high_response_hours: 168  # 1 week
    medium_response_hours: 336  # 2 weeks
    auto_security_pr: true
  
  compatibility:
    track_peer_dependencies: true
    detect_conflicts: true
    suggest_updates: true
  
  report_categories:
    versions: "decisions/dependency-management"
    security: "lessons/security-updates"
    compatibility: "patterns/version-management"
  
  update_policy:
    patch: "automatic"  # 自動適用
    minor: "weekly-review"  # 週1 レビュー
    major: "manual"  # 手動レビュー

# ================================================
# 自動化パイプライン設定
# ================================================

automation:
  generate_monthly_summary: true
  summary_template: "standard"
  
  quarterly_review_reminder: true
  decision_review_interval_days: 90
  
  auto_archive_old_lessons: true
  archive_after_days: 730
  
  # ========== 新規: ツール統合パイプライン ==========
  tool_integration:
    enabled: true
    
    playwright_pipeline:
      enabled: true
      trigger: "after-test-run"
      auto_index_update: true
    
    serena_pipeline:
      enabled: true
      trigger: "daily"
      time: "02:00"  # UTC
      auto_index_update: true
    
    context7_pipeline:
      enabled: true
      trigger: "daily"
      time: "03:00"  # UTC
      auto_index_update: true
      auto_security_alerts: true
    
    kb_update:
      enabled: true
      trigger: "after-tool-runs"
      validate_before_update: true

# ================================================
# カスタムフィールド拡張
# ================================================

custom_fields:
  decision:
    - name: "testing_impact"
      type: "text"
      required: false
      description: "How does this decision impact testing strategy?"
    
    - name: "code_quality_impact"
      type: "text"
      required: false
      description: "Expected impact on code quality metrics"
    
    - name: "dependency_implications"
      type: "text"
      required: false
      description: "Any new dependencies or version requirements?"
  
  pattern:
    - name: "test_coverage"
      type: "select"
      options: ["essential", "recommended", "optional"]
      required: false
      description: "Whether this pattern requires test coverage"
    
    - name: "quality_improvement"
      type: "number"
      required: false
      description: "Expected quality score improvement (0-100)"
    
    - name: "applicable_tools"
      type: "multi-select"
      options: ["playwright", "serena", "context7", "all"]
      required: false
      description: "Which integration tools apply to this pattern"
  
  lesson:
    - name: "tool_involved"
      type: "select"
      options: ["playwright", "serena", "context7", "other"]
      required: false
      description: "Which tool discovered or related to this issue"
    
    - name: "quality_impact"
      type: "number"
      required: false
      description: "Quality score impact of this issue"
    
    - name: "prevention_tool"
      type: "select"
      options: ["playwright", "serena", "context7", "manual"]
      required: false
      description: "How this issue could be prevented in future"

# ================================================
# レポートテンプレート
# ================================================

report_templates:
  playwright_test_report:
    format: "markdown"
    include_sections:
      - summary
      - pass_rate
      - failed_tests
      - performance_metrics
      - flakiness_analysis
      - coverage
      - recommendations
  
  serena_quality_report:
    format: "markdown"
    include_sections:
      - overall_score
      - category_scores
      - top_violations
      - technical_debt
      - recommendations
      - trends
  
  context7_version_report:
    format: "markdown"
    include_sections:
      - version_summary
      - mismatches
      - security_issues
      - outdated_packages
      - compatibility_matrix
      - update_recommendations

# ================================================
# メトリクスと測定
# ================================================

metrics:
  track_decision_usage: true
  track_pattern_effectiveness: true
  track_lesson_impact: true
  
  # ========== 新規: ツール統合メトリクス ==========
  tool_metrics:
    enabled: true
    
    playwright_metrics:
      track_test_pass_rate: true
      track_flakiness: true
      track_coverage_trend: true
      track_execution_time: true
    
    serena_metrics:
      track_quality_score_trend: true
      track_debt_accumulation: true
      track_violation_patterns: true
      track_team_improvement: true
    
    context7_metrics:
      track_version_compliance: true
      track_security_response_time: true
      track_update_cadence: true
      track_compatibility_issues: true
  
  dashboard_enabled: true
  dashboard_refresh_interval: "hourly"
  
  reports:
    weekly_report: true
    monthly_report: true
    quarterly_review: true
    
    # ========== 新規: ツール統合レポート ==========
    tool_integration_report: true
    tool_report_frequency: "weekly"

# ================================================
# パフォーマンスとサイズ制限
# ================================================

performance:
  index_cache: true
  search_cache: true
  cache_ttl_minutes: 60
  
  max_kb_size_mb: 500
  max_pattern_size_kb: 100
  max_lesson_size_kb: 100
  
  # ========== 新規: ツール統合パフォーマンス ==========
  tool_integration_limits:
    max_test_reports_kept: 30
    max_quality_reports_kept: 90
    max_version_reports_kept: 90
    archive_old_reports: true
    archive_after_days: 365

# ================================================
# 通知設定（拡張）
# ================================================

notifications:
  enable_notifications: true
  
  events:
    new_decision: true
    new_pattern: true
    new_lesson: true
    decision_updated: false
    pattern_deprecated: true
    lesson_follow_up_due: true
    
    # ========== 新規: ツール統合通知 ==========
    test_failure_rate_high: true
    quality_score_dropped: true
    security_vulnerability_detected: true
    version_mismatch_detected: true
  
  channels:
    email: true
    slack: false
    github_discussions: true

# ================================================
# ロギングと監視
# ================================================

logging:
  enabled: true
  log_file: ".github/skills/knowledge-workflow-framework/kwf.log"
  log_level: "INFO"
  
  # ========== 新規: ツール統合ロギング ==========
  tool_logs:
    playwright_log: ".github/skills/playwright-integration/playwright.log"
    serena_log: ".github/skills/serena-integration/serena.log"
    context7_log: ".github/skills/context7-integration/context7.log"
    log_rotation: true
    retention_days: 30

development:
  enabled: false
  verbose: false
  validate_on_startup: false
  
  # ========== 新規: ツール統合デバッグ ==========
  tool_debug:
    playwright_debug: false
    serena_debug: false
    context7_debug: false
```

---

## 実装ステップバイステップガイド

### Phase 1: セットアップ（1日）

#### Step 1.1: スキルディレクトリを作成

```bash
mkdir -p .github/skills/playwright-integration
mkdir -p .github/skills/serena-integration
mkdir -p .github/skills/context7-integration

# テンプレートディレクトリ
mkdir -p .github/skills/playwright-integration/templates
mkdir -p .github/skills/serena-integration/templates
mkdir -p .github/skills/context7-integration/templates
```

#### Step 1.2: スクリプトをコピー

```bash
# 前述の INTEGRATION_SCRIPTS.md からスクリプトをコピー

cp playwright_collector.py .github/skills/playwright-integration/
cp serena_analyzer.py .github/skills/serena-integration/
cp context7_manager.py .github/skills/context7-integration/

# 実行可能にする
chmod +x .github/skills/*/\*.py
```

#### Step 1.3: KWF 設定を拡張

```bash
# 既存の KWF-CONFIG.yaml をバックアップ
cp .github/skills/knowledge-workflow-framework/KWF-CONFIG.yaml \
   .github/skills/knowledge-workflow-framework/KWF-CONFIG.yaml.bak

# 上記の拡張設定を適用
# (または既存の config に新しいセクションをマージ)
```

### Phase 2: ローカルテスト（1日）

#### Step 2.1: Playwright スクリプトをテスト

```bash
python3 .github/skills/playwright-integration/playwright_collector.py \
  --kb-path .github/skills/knowledge-workflow-framework \
  --test-dir tests

# 期待される結果: knowledge-base/lessons に test-report-*.md が生成
```

#### Step 2.2: Serena スクリプトをテスト

```bash
python3 .github/skills/serena-integration/serena_analyzer.py \
  --kb-path .github/skills/knowledge-workflow-framework \
  --target-dir src

# 期待される結果: knowledge-base/patterns または lessons に code-quality-*.md が生成
```

#### Step 2.3: Context7 スクリプトをテスト

```bash
python3 .github/skills/context7-integration/context7_manager.py \
  --kb-path .github/skills/knowledge-workflow-framework

# 期待される結果: knowledge-base/decisions に version-report-*.md が生成
```

### Phase 3: GitHub Actions パイプライン（2日）

#### Step 3.1: ワークフローファイルを作成

```bash
# PLAYWRIGHT_SERENA_CONTEXT7_INTEGRATION.md の
# "自動化パイプライン（GitHub Actions）" セクションをコピー

cp knowledge-integration.yml .github/workflows/
```

#### Step 3.2: ワークフローをテスト

```bash
# main にプッシュして実行
git add .github/workflows/knowledge-integration.yml
git commit -m "Add knowledge integration workflow"
git push
```

### Phase 4: チーム導入（3日）

#### Step 4.1: ドキュメント作成

```bash
# 各スキル用の README を作成
cat > .github/skills/playwright-integration/README.md << 'EOF'
# Playwright Integration Skill

This skill automatically records Playwright test results to the Knowledge Base.

## Features
- Auto-record test results
- Track flaky tests
- Monitor coverage
- Generate recommendations

## Configuration
See KWF-CONFIG.yaml `playwright` section

## Usage
Results are automatically recorded on each test run.
EOF
```

#### Step 4.2: チームトレーニング

```
チームミーティングで説明：
1. ツール統合の概要
2. Playwright テスト結果の見方
3. Serena コード品質分析の活用
4. Context7 バージョン管理の重要性
```

---

## 検証チェックリスト

- [ ] スクリプトが KB に正しく保存している
- [ ] GitHub Actions ワークフローが正常に実行
- [ ] KB インデックスが正しく更新されている
- [ ] Copilot Chat が KB から検索できる
- [ ] チーム全員が使い方を理解している

---

**Version**: 1.0  
**Created**: 2026-03-01  
**Status**: Ready for Implementation ✅
