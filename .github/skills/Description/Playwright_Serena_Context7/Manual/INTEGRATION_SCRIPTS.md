# Playwright + Serena + Context7 統合スクリプト

## ファイル 1: playwright_collector.py

```python
#!/usr/bin/env python3
"""
Playwright テスト結果を Knowledge Base に自動記録
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
import argparse

class PlaywrightCollector:
    def __init__(self, kb_path, output_dir="test-results"):
        self.kb_path = Path(kb_path)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.timestamp = datetime.now()
    
    def run_tests(self, test_dir="tests", browser=None):
        """Playwright テストを実行"""
        cmd = [
            "npx", "playwright", "test",
            test_dir,
            "--reporter=json",
        ]
        
        if browser:
            cmd.extend(["--project", browser])
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Tests failed: {result.stderr}")
        
        return json.loads(result.stdout) if result.stdout else {}
    
    def analyze_results(self, results):
        """テスト結果を分析"""
        suites = results.get("suites", [])
        stats = results.get("stats", {})
        
        analysis = {
            "timestamp": self.timestamp.isoformat(),
            "total_tests": sum(len(s.get("tests", [])) for s in suites),
            "passed": sum(1 for s in suites if s.get("ok")),
            "failed": sum(1 for s in suites if not s.get("ok")),
            "skipped": sum(s.get("tests", []).count({"status": "skipped"}) for s in suites),
            "duration_ms": stats.get("duration", 0),
            "suites": len(suites),
            "failed_tests": self._extract_failed_tests(suites)
        }
        
        return analysis
    
    def _extract_failed_tests(self, suites):
        """失敗したテストを抽出"""
        failed = []
        for suite in suites:
            for test in suite.get("tests", []):
                if test.get("status") == "failed":
                    failed.append({
                        "title": test.get("title"),
                        "file": suite.get("file"),
                        "error": test.get("errors", [{}])[0].get("message", "Unknown")
                    })
        return failed
    
    def create_test_report_md(self, analysis):
        """Markdown レポートを作成"""
        failed_tests_md = "\n".join([
            f"- [{t['file']}] {t['title']}: {t['error']}"
            for t in analysis["failed_tests"]
        ])
        
        content = f"""---
name: playwright-test-report
date: {analysis['timestamp']}
type: test-result
total_tests: {analysis['total_tests']}
passed: {analysis['passed']}
failed: {analysis['failed']}
---

# Playwright Test Report

**Date**: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}  
**Duration**: {analysis['duration_ms']}ms

## Summary

| Metric | Count |
|--------|-------|
| Total Tests | {analysis['total_tests']} |
| Passed | {analysis['passed']} ✅ |
| Failed | {analysis['failed']} ❌ |
| Skipped | {analysis['skipped']} ⏭️ |
| Suites | {analysis['suites']} |

## Pass Rate
**{(analysis['passed'] / analysis['total_tests'] * 100 if analysis['total_tests'] > 0 else 0):.1f}%** ({'✅ Good' if analysis['passed'] / analysis['total_tests'] > 0.95 else '⚠️ Needs improvement'})

## Failed Tests

{failed_tests_md if analysis['failed_tests'] else 'No failed tests! 🎉'}

## Key Insights

### Reliability
- Flaky test count: {len([t for t in analysis['failed_tests'] if 'timing' in t['error'].lower()])}
- Most common error type: [To be analyzed]

### Performance
- Average test duration: {analysis['duration_ms'] / analysis['total_tests']:.0f}ms per test
- Slowest suite: [To be analyzed]

## Recommendations

1. **For Failed Tests**: 
   - Review [lesson-047] "Flaky E2E Test Fixes"
   - Check [pattern-010] "Playwright Best Practices"

2. **For Performance**:
   - Consider parallel execution
   - Profile slow tests

3. **For Reliability**:
   - Add retries for flaky tests
   - Improve wait strategies

## Related Knowledge
- [decision-001] "Playwright vs Cypress"
- [pattern-010] "Playwright Best Practices"
- [pattern-089] "Test Reliability Patterns"
"""
        
        return content
    
    def save_to_kb(self, analysis):
        """KB に保存"""
        report_md = self.create_test_report_md(analysis)
        
        # KB パスを作成
        year = self.timestamp.strftime("%Y")
        month = self.timestamp.strftime("%m-%d")
        filename = f"test-report-{month}-{self.timestamp.strftime('%H%M%S')}.md"
        
        lessons_dir = self.kb_path / "knowledge-base" / "lessons" / year
        lessons_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = lessons_dir / filename
        filepath.write_text(report_md)
        
        print(f"✅ Test report saved to: {filepath}")
        
        # サマリー を JSON で保存（自動処理用）
        json_file = self.output_dir / f"test-results-{self.timestamp.isoformat()}.json"
        json_file.write_text(json.dumps(analysis, indent=2))
        
        return filepath
    
    def run_and_save(self, test_dir="tests"):
        """テスト実行と保存を一度に"""
        print(f"🧪 Running Playwright tests...")
        results = self.run_tests(test_dir)
        
        print(f"📊 Analyzing results...")
        analysis = self.analyze_results(results)
        
        print(f"💾 Saving to knowledge base...")
        self.save_to_kb(analysis)
        
        return analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb-path", required=True, help="Knowledge base path")
    parser.add_argument("--test-dir", default="tests", help="Test directory")
    
    args = parser.parse_args()
    
    collector = PlaywrightCollector(args.kb_path)
    analysis = collector.run_and_save(args.test_dir)
    
    print(f"\n📈 Summary:")
    print(f"   Total: {analysis['total_tests']}")
    print(f"   Passed: {analysis['passed']} ✅")
    print(f"   Failed: {analysis['failed']} ❌")
```

---

## ファイル 2: serena_analyzer.py

```python
#!/usr/bin/env python3
"""
Serena コード品質分析結果を Knowledge Base に自動記録
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
import argparse

class SerenaAnalyzer:
    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
        self.timestamp = datetime.now()
    
    def analyze_code(self, target_dir="src"):
        """Serena でコード分析"""
        cmd = [
            "npx", "serena", "analyze",
            target_dir,
            "--json"
        ]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Analysis failed: {result.stderr}")
            return {}
        
        return json.loads(result.stdout) if result.stdout else {}
    
    def create_quality_report(self, analysis):
        """品質レポートを作成"""
        return {
            "timestamp": self.timestamp.isoformat(),
            "overall_score": analysis.get("overall_quality_score", 0),
            "readability": analysis.get("readability_score", 0),
            "maintainability": analysis.get("maintainability_score", 0),
            "testability": analysis.get("testability_score", 0),
            "security": analysis.get("security_score", 0),
            "violations": analysis.get("violations", []),
            "technical_debt_points": analysis.get("technical_debt_points", 0)
        }
    
    def create_quality_report_md(self, report):
        """Markdown レポートを作成"""
        score = report["overall_score"]
        grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D"
        
        violations_md = "\n".join([
            f"- [{v['severity']}] {v['type']}: {v['message']}"
            for v in report["violations"][:10]  # 最初の10個のみ
        ])
        
        content = f"""---
name: serena-code-quality-report
date: {report['timestamp']}
type: code-quality-analysis
overall_score: {report['overall_score']}
---

# Code Quality Analysis Report

**Date**: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}  
**Overall Grade**: {grade}

## Quality Scores

| Metric | Score | Status |
|--------|-------|--------|
| Overall | {report['overall_score']}/100 | {'✅' if report['overall_score'] >= 80 else '⚠️'} |
| Readability | {report['readability']}/100 | {'✅' if report['readability'] >= 80 else '⚠️'} |
| Maintainability | {report['maintainability']}/100 | {'✅' if report['maintainability'] >= 80 else '⚠️'} |
| Testability | {report['testability']}/100 | {'✅' if report['testability'] >= 80 else '⚠️'} |
| Security | {report['security']}/100 | {'✅' if report['security'] >= 80 else '⚠️'} |

## Issues Found

### By Severity
- 🔴 Critical: {len([v for v in report['violations'] if v['severity'] == 'critical'])}
- 🟠 High: {len([v for v in report['violations'] if v['severity'] == 'high'])}
- 🟡 Medium: {len([v for v in report['violations'] if v['severity'] == 'medium'])}
- 🔵 Low: {len([v for v in report['violations'] if v['severity'] == 'low'])}

### Detailed Issues
{violations_md}

## Technical Debt

- **Total Debt Points**: {report['technical_debt_points']} 
- **Estimated Remediation**: {report['technical_debt_points'] // 50} hours

### High-Priority Items
{self._extract_high_priority_debt(report['violations'])}

## Recommendations

1. **Immediate Actions**:
   - Fix all critical violations
   - Add missing type annotations
   - Improve error handling

2. **Short-term (This Sprint)**:
   - Refactor long functions
   - Remove duplicate code
   - Add JSDoc comments

3. **Long-term (Backlog)**:
   - Increase test coverage
   - Improve documentation
   - Plan refactoring sessions

## Related Patterns
- [pattern-015] "High-Quality Code Structure" - Reference for improvement
- [pattern-089] "Error Handling Best Practices"
- [lesson-050] "Technical Debt Impact Analysis"

## Action Items
- [ ] Review critical violations
- [ ] Create refactoring tasks
- [ ] Schedule code review session
- [ ] Update team guidelines based on findings
"""
        
        return content
    
    def _extract_high_priority_debt(self, violations):
        """優先度の高い技術的負債を抽出"""
        high_priority = [v for v in violations if v.get("severity") in ["critical", "high"]]
        
        return "\n".join([
            f"- {v['type']}: {v['message']}"
            for v in high_priority[:5]
        ]) or "No high-priority items detected ✅"
    
    def save_to_kb(self, report):
        """KB に保存"""
        report_md = self.create_quality_report_md(report)
        
        year = self.timestamp.strftime("%Y")
        filename = f"code-quality-{self.timestamp.strftime('%Y-%m-%d')}.md"
        
        # pattern として高スコアなら保存
        if report["overall_score"] >= 85:
            patterns_dir = self.kb_path / "knowledge-base" / "patterns" / "code-quality"
            patterns_dir.mkdir(parents=True, exist_ok=True)
            filepath = patterns_dir / filename
        else:
            # lesson として低スコアなら保存
            lessons_dir = self.kb_path / "knowledge-base" / "lessons" / year
            lessons_dir.mkdir(parents=True, exist_ok=True)
            filepath = lessons_dir / filename
        
        filepath.write_text(report_md)
        print(f"✅ Code quality report saved to: {filepath}")
        
        return filepath
    
    def run_and_save(self, target_dir="src"):
        """分析実行と保存を一度に"""
        print(f"🔍 Analyzing code quality...")
        analysis = self.analyze_code(target_dir)
        
        print(f"📊 Creating report...")
        report = self.create_quality_report(analysis)
        
        print(f"💾 Saving to knowledge base...")
        self.save_to_kb(report)
        
        return report

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb-path", required=True, help="Knowledge base path")
    parser.add_argument("--target-dir", default="src", help="Target directory to analyze")
    
    args = parser.parse_args()
    
    analyzer = SerenaAnalyzer(args.kb_path)
    report = analyzer.run_and_save(args.target_dir)
    
    print(f"\n📈 Summary:")
    print(f"   Overall Score: {report['overall_score']}/100")
    print(f"   Readability: {report['readability']}/100")
    print(f"   Maintainability: {report['maintainability']}/100")
```

---

## ファイル 3: context7_manager.py

```python
#!/usr/bin/env python3
"""
Context7 ライブラリバージョン管理結果を Knowledge Base に自動記録
"""

import json
import subprocess
from datetime import datetime
from pathlib import Path
import argparse

class Context7Manager:
    def __init__(self, kb_path):
        self.kb_path = Path(kb_path)
        self.timestamp = datetime.now()
    
    def check_versions(self):
        """Context7 でバージョンチェック"""
        cmd = ["npx", "context7", "check", "--json"]
        
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"Version check failed: {result.stderr}")
            return {}
        
        return json.loads(result.stdout) if result.stdout else {}
    
    def analyze_versions(self, check_result):
        """バージョン情報を分析"""
        return {
            "timestamp": self.timestamp.isoformat(),
            "mismatches": check_result.get("mismatches", []),
            "security_issues": check_result.get("security_issues", []),
            "outdated": check_result.get("outdated_packages", []),
            "compatible": check_result.get("compatible_versions", {}),
            "status": "ok" if not check_result.get("issues") else "warning"
        }
    
    def create_version_report_md(self, analysis):
        """バージョンレポートを作成"""
        mismatches_md = "\n".join([
            f"- {m['package']}: {m['versions']} (affected: {', '.join(m['affected_projects'])})"
            for m in analysis["mismatches"]
        ]) or "No version mismatches detected ✅"
        
        security_md = "\n".join([
            f"- {s['package']} {s['version']}: {s['vulnerability']} (CVE: {s['cve_id']})"
            for s in analysis["security_issues"]
        ]) or "No security issues detected ✅"
        
        outdated_md = "\n".join([
            f"- {p['package']}: {p['current']} → {p['latest']}"
            for p in analysis["outdated"]
        ]) or "All packages up to date ✅"
        
        content = f"""---
name: context7-version-report
date: {analysis['timestamp']}
type: version-management
status: {analysis['status']}
---

# Library Version Management Report

**Date**: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}  
**Status**: {'✅ Healthy' if analysis['status'] == 'ok' else '⚠️ Issues Found'}

## Version Mismatches

{mismatches_md}

## Security Issues

{security_md}

## Outdated Packages

{outdated_md}

## Compatible Versions Matrix

| Library | Recommended | Min | Max Tested |
|---------|-------------|-----|-----------|
{self._create_compatibility_table(analysis['compatible'])}

## Policy Compliance

- ✅ Core libraries locked to minor version
- {'✅' if not analysis['mismatches'] else '❌'} No version mismatches
- {'✅' if not analysis['security_issues'] else '❌'} No critical security issues
- {'✅' if not analysis['outdated'] else '⚠️'} Outdated packages review needed

## Recommendations

### Immediate (within 24 hours)
{self._immediate_actions(analysis)}

### Short-term (within 1 week)
{self._short_term_actions(analysis)}

### Long-term (within 1 month)
{self._long_term_actions(analysis)}

## Related
- [decision-150] "Version Management Policy"
- [pattern-230] "Monorepo Dependency Lock"
- [pattern-240] "Security Update Process"

## Next Steps
- [ ] Review security issues
- [ ] Schedule updates
- [ ] Test compatibility
- [ ] Document changes
"""
        
        return content
    
    def _create_compatibility_table(self, compatible):
        """互換性テーブルを作成"""
        rows = []
        for package, versions in compatible.items():
            rows.append(
                f"| {package} | {versions['recommended']} | "
                f"{versions['minimum']} | {versions['max_tested']} |"
            )
        return "\n".join(rows) or "No compatible versions data available"
    
    def _immediate_actions(self, analysis):
        """即座のアクション"""
        if analysis["security_issues"]:
            return f"- Fix {len(analysis['security_issues'])} security vulnerabilities"
        return "- No immediate actions required"
    
    def _short_term_actions(self, analysis):
        """短期のアクション"""
        if analysis["mismatches"]:
            return f"- Resolve {len(analysis['mismatches'])} version mismatches"
        if analysis["outdated"]:
            return f"- Update {len(analysis['outdated'])} outdated packages"
        return "- Regular dependency review"
    
    def _long_term_actions(self, analysis):
        """長期のアクション"""
        return "- Plan major version upgrades\n- Monitor ecosystem trends"
    
    def save_to_kb(self, analysis):
        """KB に保存"""
        report_md = self.create_version_report_md(analysis)
        
        year = self.timestamp.strftime("%Y")
        filename = f"version-report-{self.timestamp.strftime('%Y-%m-%d')}.md"
        
        # decision として保存
        decisions_dir = self.kb_path / "knowledge-base" / "decisions" / "dependency-management"
        decisions_dir.mkdir(parents=True, exist_ok=True)
        
        filepath = decisions_dir / filename
        filepath.write_text(report_md)
        
        print(f"✅ Version report saved to: {filepath}")
        
        return filepath
    
    def run_and_save(self):
        """チェック実行と保存を一度に"""
        print(f"📦 Checking library versions...")
        check_result = self.check_versions()
        
        print(f"📊 Analyzing versions...")
        analysis = self.analyze_versions(check_result)
        
        print(f"💾 Saving to knowledge base...")
        self.save_to_kb(analysis)
        
        return analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--kb-path", required=True, help="Knowledge base path")
    
    args = parser.parse_args()
    
    manager = Context7Manager(args.kb_path)
    analysis = manager.run_and_save()
    
    print(f"\n📈 Summary:")
    print(f"   Version Mismatches: {len(analysis['mismatches'])}")
    print(f"   Security Issues: {len(analysis['security_issues'])}")
    print(f"   Outdated Packages: {len(analysis['outdated'])}")
    print(f"   Status: {analysis['status']}")
```

---

## 使用方法

```bash
# Playwright テスト結果を記録
python3 playwright_collector.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Serena コード品質分析を記録
python3 serena_analyzer.py \
  --kb-path .github/skills/knowledge-workflow-framework \
  --target-dir src

# Context7 バージョンチェックを記録
python3 context7_manager.py \
  --kb-path .github/skills/knowledge-workflow-framework
```

## GitHub Actions での実行例

```yaml
# これらのスクリプトを .github/workflows/knowledge-integration.yml から呼び出し
# 上記の PLAYWRIGHT_SERENA_CONTEXT7_INTEGRATION.md の GitHub Actions セクション参照
```

**Version**: 1.0  
**Created**: 2026-03-01  
**Status**: Ready for Implementation ✅
