# Playwright Integration Skill

> Automatically record Playwright E2E test results to Knowledge Base

**Purpose**: Transform raw test results into actionable team knowledge  
**Version**: 1.0  
**Status**: ✅ Production Ready

---

## 📖 このドキュメントについて

**README.md** をお読みです。

| ドキュメント | 用途 |
|-------------|------|
| **README.md** ← 今ここ | クイックスタート・使い方ガイド |
| **SKILL.md** | 詳細な技術仕様・アーキテクチャ・完全リファレンス |

### 何から始める？
- **初めての方**: このREADME.mdをお読みください ✅
- **詳細を知りたい**: [SKILL.md](./SKILL.md) をご参照ください
- **統合・カスタマイズ**: [SKILL.md](./SKILL.md) の「🏗️ Architecture」と「⚙️ Configuration」セクションをご確認ください

---

## 📊 What This Skill Does

```
Playwright Tests Run
        ↓
Results Collected
        ↓
Analysis Performed
  ├─ Pass rate calculation
  ├─ Failure pattern detection
  ├─ Flaky test identification
  ├─ Coverage metrics (if available)
  └─ Performance tracking
        ↓
Markdown Report Generated
        ↓
Saved to Knowledge Base:
  .github/skills/knowledge-workflow-framework/
  └─ knowledge-base/lessons/{year}/test-report-*.md
        ↓
Auto-Indexed & Searchable
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Auto Record** | Captures results after each test run |
| **Flaky Detection** | Identifies tests that fail intermittently |
| **Coverage Tracking** | Records test coverage metrics |
| **Performance Metrics** | Tracks test execution time |
| **Fallback Mode** | Uses demo data if Playwright not installed |
| **Smart Categorization** | Saves to patterns (good results) or lessons (issues) |

---

## 📝 Report Structure

### Test Report Format

Each report includes:

```markdown
---
name: playwright-test-report
date: 2026-03-02T08:00:00
type: test-results
category: test-failures
tags: playwright, testing, automation, e2e
---

# Playwright Test Results

**Date**: 2026-03-02 08:00:00
**Total Tests**: 24
**Passed**: 22 (91.7%)
**Failed**: 2 (8.3%)
**Skipped**: 0

## Test Summary
- ✅ Auth flow tests: 4/4 passed
- ✅ Dashboard tests: 8/8 passed
- ✅ API integration tests: 6/6 passed
- ❌ Mobile responsive: 2/4 passed (2 flaky)

## Failed Tests
- [FAILED] Mobile responsive - iPhone 12
- [FAILED] Mobile responsive - Pixel 5

## Performance Metrics
- Total Duration: 2m 45s
- Average Time per Test: 6.9s
- Slowest Test: Navigation test (12.3s)

## Flakiness Analysis
| Test | Pass Rate | Status |
|------|-----------|--------|
| Mobile responsive | 50% | 🔴 FLAKY |
| API timeout | 95% | ✅ Stable |

## Test Coverage
- Lines Covered: 2,847/3,200 (88.9%)
- Branches Covered: 156/180 (86.7%)
- Trend: +2.1% vs. last week

## Recommendations
1. Investigate mobile screenshot flakiness
2. Add retry logic for element visibility
3. Consider increasing timeout for slow network
4. Continue monitoring coverage trend
```

---

## ⚙️ Configuration

Located in `KWF-CONFIG.yaml`:

```yaml
playwright:
  script_path: ".github/skills/playwright-integration/playwright_collector.py"
  test_directory: "tests"
  browsers: ["chromium", "firefox", "webkit"]
  
  report_categories:
    test-results: "lessons"
    flaky-tests: "lessons"
    coverage-data: "patterns"
  
  flakiness_threshold: 3  # Mark as flaky after 3 failures
  
  metrics:
    track_duration: true
    track_coverage: true
    track_failure_patterns: true
    track_performance: true
```

---

## 🚀 Usage

### Manual Execution (Local)

```bash
# Run the collector directly
python3 .github/skills/playwright-integration/playwright_collector.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Expected output:
# 🎭 Playwright Test Result Collector
# ✅ Test report saved: knowledge-base/lessons/2026/test-report-*.md
# Tests: 24 total | 22 passed | 2 failed
```

### Automated Execution (GitHub Actions)

Runs automatically via `.github/workflows/knowledge-integration.yml`:

```yaml
- Job: Playwright Collection
- Trigger: Daily 02:00 UTC (configurable)
- Status: Recorded in workflow summary
```

Or manually trigger from GitHub Actions UI.

---

## 📊 Generated Knowledge

### Saved Locations

```
knowledge-base/
└── lessons/
    └── 2026/
        ├── test-report-20260302-120015.md
        ├── test-report-20260302-130045.md
        └── ... (one per run)
```

### Searchable Via

```
Copilot Chat Query Examples:
- "Show me test results from last week"
- "How many flaky tests do we have?"
- "What's our test coverage trend?"
- "Which tests failed on mobile?"
```

---

## 🔍 Interpretation Guide

### Understanding Report Metrics

**Pass Rate**
```
90-100% ✅ Excellent - Stable, production-ready
80-89%  ⚠️ Good - Address failures
70-79%  🔴 Fair - Needs improvement
<70%    ❌ Poor - Take action immediately
```

**Flaky Tests**
```
0-1 failures  ✅ Stable
2-3 failures  ⚠️ Monitor closely
4+ failures   🔴 Investigate immediately
```

**Coverage**
```
>85%  ✅ Excellent
75-85% ⚠️ Good
<75%  🔴 Needs improvement
```

---

## 🛠️ Troubleshooting

### No Test Results Generated

```
Problem: playwright_collector.py runs but no report created

Possible Causes:
1. Playwright not installed
   → Solution: Install with `npm install -D @playwright/test`
   → Fallback: Uses demo data

2. Wrong KB path
   → Solution: Verify --kb-path parameter
   → Example: python3 ... --kb-path .github/skills/knowledge-workflow-framework

3. Permission issues
   → Solution: Ensure write access to knowledge-base/ directory
   → Command: chmod +x knowledge-workflow-framework/

4. No tests found
   → Solution: Ensure tests exist in configured test_directory
   → Default: tests/
   → Verify: ls tests/ shows test files
```

### Reports Not Appearing in GitHub

```
Problem: Local runs work, but GitHub Actions doesn't generate reports

Possible Causes:
1. Workflow not triggered
   → Solution: Check .github/workflows/knowledge-integration.yml schedule
   → Verify: Repository has Actions enabled

2. Python version mismatch
   → Solution: Ensure Python 3.11+ installed
   → Verify: python3 --version

3. Artifact upload failed
   → Solution: Check GitHub Actions job logs
   → Verify: Storage quota not exceeded
```

---

## 📈 Best Practices

### 1. Regular Execution
- ✅ Run tests daily or on every commit
- ✅ Keep test suite fast (<5 minutes if possible)
- ❌ Let tests sit untouched for weeks

### 2. Active Monitoring
- ✅ Review reports regularly
- ✅ Act on flaky test alerts
- ✅ Track coverage trends
- ❌ Ignore declining coverage

### 3. Knowledge Sharing
- ✅ Reference KB when discussing test issues
- ✅ Document test patterns as lessons
- ✅ Use Copilot to share learnings
- ❌ Keep test knowledge siloed

### 4. Continuous Improvement
- ✅ Fix flaky tests proactively
- ✅ Increase coverage over time
- ✅ Optimize slow tests
- ❌ Accept constant failures

---

## 🔗 Integration Points

### With Knowledge Base

- **Tests Results** → stored as lessons
- **Coverage Data** → stored as patterns
- **Failures** → actionable items for refactoring
- **Performance** → baseline for optimization

### With GitHub Actions

- **Trigger**: Daily or on-demand
- **Duration**: ~5-15 minutes (depends on test suite)
- **Output**: KB entries + GitHub Actions summary
- **Notifications**: Optional Slack/email alerts

### With Copilot

```
Developer: "According to our tests, what's failing?"
Copilot searches KB:
  → Recent test reports
  → Failure patterns
  → Recommended fixes
  → Historical context

Result: Faster debugging with team context
```

---

## 📊 Example Workflow

### Day 1: Monday 02:00 UTC

```
1. Playwright tests run
2. Results: 24 tests, 22 passed, 2 flaky
3. Report generated and saved
4. Developer reviews during morning standup
5. "Mobile rendering" marked for investigation
```

### Day 8: Next Monday 02:00 UTC

```
1. Tests run again
2. "Mobile rendering" now stable ✅
3. Report shows improvement
4. Team notes: "Fix was element visibility wait"
5. Pattern documented for future reference
```

### Month Later: Quarterly Review

```
Copilot can show:
- Test pass rate trend (improving/stable/declining)
- Which flaky tests got fixed
- Coverage improvements
- Most problematic areas historically
- Recommended next focus areas
```

---

## 🎓 When to Use (And When Not To)

### ✅ Use This Skill When:
- You run E2E tests with Playwright
- You care about test reliability
- Your team needs to track test quality
- You want historical test data accessible

### ❌ Might Not Need When:
- You don't use Playwright (but Copilot can still use demo data)
- You have tests but don't care about trends
- Reports are only checked once per month

---

## 📝 Related Documentation

- **Main README**: [../../README.md](../../README.md)
- **KWF Core**: [../knowledge-workflow-framework/README.md](../knowledge-workflow-framework/README.md)
- **Config Reference**: [../knowledge-workflow-framework/KWF-CONFIG.yaml](../knowledge-workflow-framework/KWF-CONFIG.yaml)
- **Installation**: See root INSTALLATION_GUIDE.md

---

## 🤔 FAQ

**Q: Can I run this without Playwright installed?**  
A: Yes! Demo data is used automatically. Real data is preferred but optional.

**Q: How long are reports kept?**  
A: Configured in KWF-CONFIG.yaml → `tool_integration_limits` → `max_test_reports_kept: 30`

**Q: Can I customize the report template?**  
A: Yes! Edit the markdown generation in `playwright_collector.py` or use templates.

**Q: Do I need special GitHub permissions?**  
A: Only standard push access to the repository.

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ✅ Production Ready
