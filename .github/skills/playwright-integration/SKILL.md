---
name: playwright-integration
description: |
  End-to-end test automation and result collection.
  Executes Playwright test suites, captures results, and automatically
  converts test outcomes into team knowledge base entries. Enables
  continuous documentation of test patterns and quality metrics.
version: 1.0
authors:
  - QA Team Lead
tags:
  - testing
  - e2e-testing
  - playwright
  - qa-automation
  - test-reporting
---

# Playwright Integration Skill

## 🎯 Purpose

The Playwright Integration skill:
- **Automates** end-to-end test execution across browsers
- **Captures** test results and failure patterns
- **Documents** testing strategies and lessons learned
- **Integrates** test insights into team knowledge base
- **Reports** quality metrics for CI/CD pipeline

This skill treats testing as a knowledge-generating activity, not just quality gates.

---

## 🏗️ Architecture

### Data Flow

```
Test Execution
    ↓
Result Collection (JSON)
    ↓
Pattern Recognition
    ↓
Knowledge Entry Generation
    ↓
KB Indexing & Search
    ↓
Team Access (Copilot Chat)
```

### Components

**1. Test Runner**
- Executes Playwright test suites
- Collects timing information
- Records browser compatibility
- Captures stack traces on failure

**2. Result Parser**
- Reads Playwright JSON reports
- Extracts test metadata
- Calculates pass rates
- Identifies flaky tests

**3. Knowledge Generator**
- Creates decision entries for architecture choices
- Generates pattern entries for test strategies
- Records lessons learned from failures
- Tags entries for searchability

**4. KB Integrator**
- Writes entries to knowledge base
- Updates search index
- Maintains cross-references
- Archives historical data

---

## 📋 Inputs & Outputs

### Inputs

**Configuration**
```yaml
playwright:
  test_dir: "tests/e2e"
  config_file: "playwright.config.ts"
  browsers: [chromium, firefox, webkit]
  report_path: "playwright-report"
  timeout: 30000
```

**Test Files**
- `*.spec.ts` and `*.spec.js` test files
- Page objects and fixtures
- Test data and mocks

### Outputs

**Generated Reports**
- `test-report-YYYYMMDD-HHMMSS.md` - Human-readable summary
- `test-failures-*.md` - Detailed failure analysis
- `test-patterns-*.md` - Reusable test strategies

**Knowledge Base Entries**
```
knowledge-base/
├── decisions/
│   └── testing/decision-playwright-strategy.md
├── patterns/
│   ├── pattern-page-object-model.md
│   ├── pattern-async-handling.md
│   └── pattern-flaky-test-detection.md
└── lessons/
    ├── lesson-browser-compatibility.md
    └── lesson-performance-optimization.md
```

**Search Index Updates**
- Terms: browser, automation, E2E, performance, stability
- Links: test files, related patterns, failure history

---

## 🔌 Integration Points

### GitHub Actions

```yaml
- name: Run Playwright Tests
  run: |
    python .github/skills/playwright-integration/playwright_collector.py \
      --kb-path .github/skills/knowledge-workflow-framework \
      --test-dir tests/e2e \
      --browsers chromium,firefox,webkit
```

### Known Base Connection

All test results automatically:
1. Create relevant decision entries
2. Link to performance patterns
3. Record failure lessons
4. Update search index

### Knowledge Reference

When running tests, integration searches KB for:
- Previous similar failures
- Applicable test patterns
- Performance benchmarks
- Browser-specific issues

---

## ⚙️ Configuration

### KWF-CONFIG.yaml Integration

```yaml
playwright:
  enabled: true
  version: "1.40.0"
  schedule: "every 2 hours"
  browsers:
    - chromium
    - firefox
    - webkit
  timeout_ms: 30000
  retry_failed: true
  max_retries: 3
  screenshot_on_failure: true
  video_on_failure: true
  report_dir: "playwright-report"
  kb_integration:
    auto_generate_patterns: true
    track_flakiness: true
    performance_threshold_ms: 5000
    failure_threshold: 0.05
```

### Environment Variables

```bash
PLAYWRIGHT_BROWSERS_PATH=/tmp/pw-browsers
PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=0
PLAYWRIGHT_TIMEOUT=30000
KB_AUTO_COMMIT=true
```

---

## 📊 Usage Workflow

### 1. Local Testing

```bash
# Run all tests
python playwright_collector.py

# Run specific test file
python playwright_collector.py --test-file login.spec.ts

# Run with specific browser
python playwright_collector.py --browser chromium

# Generate KB entries
python playwright_collector.py --generate-kb
```

### 2. CI/CD Integration

Tests run automatically on:
- Every commit to `main`
- Every pull request
- Scheduled daily runs (02:00 UTC)
- Manual trigger for regression

### 3. Report Generation

- HTML reports in `playwright-report/`
- Markdown summaries in knowledge base
- Performance metrics dashboard
- Failure trend analysis

---

## 🎓 Knowledge Generation Examples

### Generated Decision Entry

```markdown
# Decision: Use Page Object Model for Test Maintenance

**Status**: ACCEPTED  
**Date**: 2026-03-02

## Rationale
Experience shows POM reduces maintenance burden by 40% compared
to inline selectors. Reduces test fragility.

## Pattern Reference
See `pattern-page-object-model.md` for implementation guide.

## Lessons Applied
From past effort (lesson-test-maintenance-costs.md)
```

### Generated Pattern Entry

```markdown
# Pattern: Handling Asynchronous Navigation in Playwright

**Complexity**: Intermediate  
**Tags**: async, navigation, timing

## Problem
Tests fail intermittently when page changes aren't fully loaded.

## Solution
Use `page.waitForLoadState()` after navigation triggers:
\`\`\`typescript
await page.click('button[type="submit"]');
await page.waitForLoadState('networkidle');
\`\`\`
```

### Generated Lesson Entry

```markdown
# Lesson: Browser-Specific CSS Selector Issues in Safari

**Date**: 2026-02-28  
**Severity**: Medium

## Issue
CSS selectors using pseudo-elements fail in Safari on iOS.

## Resolution
Use explicit data attributes instead:
- ❌ Bad: `input[placeholder="Search"]`
- ✅ Good: `input[data-testid="search-input"]`

## Prevention
All new tests must use data-testid attributes.
```

---

## 📈 Metrics & Monitoring

### Key Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Test Pass Rate | > 98% | Per run |
| Flaky Test Ratio | < 5% | Daily |
| Avg Execution Time | < 5min | Per run |
| Browser Coverage | 3+ | Per run |
| KB Entry Freshness | Weekly | Review |

### Health Checks

```bash
python playwright_collector.py --health-check
```

Output includes:
- Browser compatibility status
- Flaky test detection
- Performance regression alerts
- KB integration validation

---

## 🔄 Maintenance Schedule

### Daily
- Monitor test pass rates
- Check for new flaky tests
- Review failed test logs

### Weekly
- Analyze failure patterns
- Update test patterns in KB
- Check selector deprecation

### Monthly
- Full regression test suite
- Performance baseline review
- KB entry pruning

### Quarterly
- Browser version updates
- Test strategy review
- Pattern effectiveness evaluation

---

## 🐛 Error Handling

### Common Issues & Resolution

**Issue**: Tests timeout randomly
```
Solution:
1. Check network conditions
2. Increase timeout for specific tests
3. Review lesson: lesson-timeout-handling.md
4. Update pattern: pattern-async-handling.md
```

**Issue**: Tests pass locally, fail in CI
```
Solution:
1. Check browser version differences
2. Review CI environment setup
3. Enable video recording for debugging
4. Check for flakiness pattern
```

**Issue**: Screenshot/video storage full
```
Solution:
1. Implement rotation policy
2. Archive old reports
3. Update KB with lesson learned
4. Configure retention period
```

---

## 🔗 Related Skills

Integrates with:
- **knowledge-workflow-framework** - Core KB system
- **serena-integration** - Code quality patterns
- **context7-integration** - Dependency version compatibility
- **github-actions** - CI/CD orchestration

---

## ✅ Deployment Checklist

Before production deployment:

- [ ] Playwright installed (`npm install -D @playwright/test`)
- [ ] Test files organized in `tests/e2e/`
- [ ] `playwright.config.ts` configured
- [ ] `playwright_collector.py` in correct location
- [ ] KB path configured in script
- [ ] GitHub Actions workflow includes playwright job
- [ ] Browser compatibility matrix defined
- [ ] Timeout values set appropriately
- [ ] Report directory configured
- [ ] First test run successful
- [ ] KB entries generated correctly
- [ ] Search index updated

---

## 📞 Support & Troubleshooting

For issues:
1. Check `README.md` in this directory
2. Review `playwright_collector.py` source code
3. Search KB for similar issues
4. Check GitHub Actions logs
5. Review Playwright documentation

**Common Sources**:
- Playwright errors → `pattern-error-handling.md`
- Timing issues → `lesson-async-handling.md`
- Failure patterns → `decision-test-strategy.md`

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ACTIVE  
**Next Review**: 2026-06-02
