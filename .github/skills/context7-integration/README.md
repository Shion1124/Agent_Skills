# Context7 Integration Skill

> Automated library version management and security vulnerability tracking

**Purpose**: Keep dependencies secure, up-to-date, and compliant  
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
Context7 Version Check Runs
        ↓
Libraries Analyzed
  ├─ Current versions detected
  ├─ Latest versions identified
  ├─ Compatibility checked
  └─ Security vulnerabilities scanned
        ↓
Reports Generated
  ├─ Version Report → decisions/dependency-management/
  │   (Current state of all dependencies)
  └─ Security Alert → lessons/security-updates/
      (If vulnerabilities found)
        ↓
Recommendations Provided
  ├─ Patch updates (apply automatically)
  ├─ Minor updates (review weekly)
  └─ Major updates (manual review)
        ↓
Auto-Indexed & Searchable
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Auto Detection** | Finds all project dependencies |
| **Version Tracking** | Current vs. latest version comparison |
| **Security Scanning** | CVE detection and reporting |
| **Compatibility Check** | Peer dependency validation |
| **Smart Updates** | Different policies for patch/minor/major |
| **Security Alerts** | Immediate notification of vulnerabilities |
| **Fallback Mode** | Demo data if Context7 not installed |

---

## 📋 Report Types

### 1. Version Report
**Saved to**: `decisions/dependency-management/version-report-*.md`

```markdown
---
name: context7-version-report
date: 2026-03-02T15:00:00
type: version-management
category: dependency-management
tags: version-management, dependencies, context7
---

# Library Version Management Report - Context7

**Date**: 2026-03-02 15:00:00
**Total Libraries**: 48
**Up-to-date**: 45 (93.8%)
**Outdated**: 3 (6.2%)

## Version Status

| Library | Current | Latest | Status |
|---------|---------|--------|--------|
| react | 18.2.0 | 19.0.0 | 🟡 Minor Update |
| typescript | 5.3.3 | 5.4.0 | 🟡 Minor Update |
| jest | 29.5.0 | 29.7.0 | 🟢 Patch Update |
| express | 4.18.2 | 4.18.2 | ✅ Current |
| lodash | 4.17.20 | 4.17.21 | 🔴 Security Update |

## Outdated Libraries Needing Updates

### 🔴 Critical (Security-Related)
- **lodash**: Update to 4.17.21 ASAP
  - Fix: Prototype Pollution vulnerability (CVE-2024-1234)

### 🟡 Important (Feature Updates)
- **react**: Consider updating to 19.0.0
  - New: Concurrent rendering improvements
- **typescript**: 5.4.0 available
  - Includes new decorators support

### 🟢 Optional (Minor Updates)
- **jest**: 29.7.0 available
  - Mostly bug fixes and improvements

## Compliance Summary
- Current Version Count: 48
- Up-to-date: 45
- Outdated: 3
- Compliance Rate: 93.8%
- Status: ✅ Good compliance

## Update Plan Priority

1. **Critical** - lodash (24 hours)
2. **Important** - React & TypeScript (next sprint)
3. **Optional** - Jest when convenient
```

### 2. Security Alert Report
**Saved to**: `lessons/security-updates/security-alert-*.md`

```markdown
---
name: context7-security-alert
date: 2026-03-02T15:05:00
type: security-alert
severity: high
category: security
tags: security, vulnerability, cve, context7
---

# Security Alert - Library Vulnerabilities Detected

**Date**: 2026-03-02 15:05:00
**Alert Level**: 🔴 HIGH

## Vulnerability Summary
- 🔴 Critical: 0
- 🔴 High: 1 (immediate action needed)
- 🟡 Medium: 1
- 🟢 Low: 0

**Total Vulnerabilities**: 2

## Detected Vulnerabilities

### CVE-2024-1234: Prototype Pollution
- **Severity**: HIGH 🔴
- **Package**: lodash <= 4.17.20
- **Description**: Prototype Pollution vulnerability allows unauthorized modification
- **Impact**: Application security vulnerability
- **Fixed In**: 4.17.21+
- **Action**: UPDATE IMMEDIATELY

### CVE-2024-5678: Information Disclosure
- **Severity**: MEDIUM 🟡
- **Package**: react < 19.0.0
- **Description**: Potential information disclosure in error messages
- **Impact**: May leak sensitive information
- **Fixed In**: 19.0.0+
- **Action**: Update in next sprint

## Remediation Steps

### Immediate (24 hours)
1. Update lodash: `npm update lodash@4.17.21`
2. Test all features: `npm test`
3. Deploy to production
4. Verify no issues: Check application logs

### This Week
1. Schedule React update
2. Test compatibility with current code
3. Review release notes for breaking changes
4. Plan gradual rollout if needed

### Follow-up
- Schedule security review meeting
- Update dependency policy
- Set up automated CVE monitoring
- Share findings in team KB

## Prevention Strategy
- Enable Dependabot alerts
- Review Context7 reports weekly
- Update critical patches immediately
- Plan minor/major updates in sprints
```

---

## ⚙️ Configuration

Located in `KWF-CONFIG.yaml`:

```yaml
context7:
  script_path: ".github/skills/context7-integration/context7_manager.py"
  
  version_locking:
    core_libraries:     # Lock major.minor
      - react
      - typescript
      - next.js
    development_tools:  # Lock major only
      - eslint
      - jest
      - prettier
  
  security:
    critical_response_hours: 24    # Must fix within 24 hours
    high_response_hours: 168       # Fix within 1 week
    medium_response_hours: 336     # Fix within 2 weeks
    auto_security_pr: true         # Auto-create PR for security fixes
  
  compatibility:
    track_peer_dependencies: true
    detect_conflicts: true
    suggest_updates: true
  
  report_categories:
    versions: "decisions/dependency-management"    # Where versions saved
    security: "lessons/security-updates"           # Where alerts saved
    compatibility: "patterns/version-management"   # Patterns/examples
  
  update_policy:
    patch: "automatic"        # Apply automatically
    minor: "weekly-review"    # Review weekly, can auto-apply
    major: "manual"           # Manual review required
```

---

## 📊 Update Policies Explained

### Patch Updates (e.g., 4.17.20 → 4.17.21)
```
What: Bug fixes, security patches, minor improvements
Risk: Very low - backward compatible
Action: Apply automatically ASAP
Example: jest 29.5.0 → 29.5.1 (security fix)
```

### Minor Updates (e.g., 18.2.0 → 18.3.0)
```
What: New features, improvements, backward compatible
Risk: Low - usually safe but verify
Action: Review weekly, test before applying
Example: React 18.2.0 → 18.3.0 (new hooks)
```

### Major Updates (e.g., 4.x → 5.x)
```
What: Breaking changes, significant rewrites
Risk: High - may require code changes
Action: Manual review, plan carefully, test extensively
Example: TypeScript 4.9.0 → 5.0.0 (new syntax)
```

---

## 🚀 Usage

### Manual Execution (Local)

```bash
# Run the manager directly
python3 .github/skills/context7-integration/context7_manager.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Expected output:
# 📦 Context7 Version Manager
# ✅ Version report saved: knowledge-base/decisions/dependency-management/version-report-*.md
# Total Dependencies: 48
# Up-to-date: 45
# Security Issues: 1 (CVE found - lodash)
# ⚠️ Security alert saved: knowledge-base/lessons/2026/security-alert-*.md
```

### Automated Execution (GitHub Actions)

```yaml
- Job: Context7 Check
- Trigger: Daily 02:30 UTC (after Serena)
- Duration: ~2-3 minutes for typical projects
- Auto-creates PR: If security fixes available
```

---

## 📊 Generated Knowledge

### Saved Locations

```
knowledge-base/
├── decisions/
│   └── dependency-management/
│       ├── version-report-20260302-150000.md
│       └── version-report-20260301-150015.md
│
└── lessons/
    └── security-updates/
        ├── security-alert-20260302-150005.md
        └── security-alert-20260301-150020.md
```

### Searchable Via Copilot

```
Query Examples:
- "Show me security vulnerabilities"
- "Which dependencies are outdated?"
- "What's our version compliance?"
- "How do we fix CVE-2024-1234?"
- "Show version management patterns"
```

---

## 🔒 Security Features

### Vulnerability Detection

Context7 automatically:
- ✅ Scans package.json for known CVEs
- ✅ Checks npm security database
- ✅ Identifies version conflicts
- ✅ Rates severity (critical/high/medium/low)

### Response Times

Based on severity:
```
Critical  → Fix within 24 hours
High      → Fix within 1 week
Medium    → Fix within 2 weeks
Low       → Include in regular updates
```

### Automated PRs

For security patches:
```
Context7 can automatically:
✅ Create PR with updated package.json
✅ Run tests to verify compatibility
✅ Add security alert reference
✅ Request review from security team
```

---

## 📈 Version Compliance Tracking

### Weekly Monitoring

```
Week 1: 93% compliant (45/48 current)
Week 2: 94% compliant (45/48 current)
Week 3: 96% compliant (46/48 current)
Week 4: 98% compliant (47/48 current)

Trend: Improving ✅
Goal: 100% compliant
```

### Monthly Reports

```
Copilot can show:
- Compliance trend (improving/stable/declining)
- Average time to update patches
- Security vulnerabilities resolved
- Major version upgrade readiness
```

---

## 🛠️ Troubleshooting

### No Version Report Generated

```
Problem: Script runs but no report created

Causes:
1. Context7 not installed
   → npm install -g context7 (or demo data used)

2. No package.json found
   → ls package.json
   → Verify in repo root

3. Permission issues
   → chmod 755 knowledge-base/
```

### Security Alert Not Created

```
Problem: Vulnerabilities exist but no alert saved

Causes:
1. No CVEs detected yet
   → Normal! Means dependencies are secure

2. CVE detection disabled
   → Verify security_check: true in KWF-CONFIG.yaml

3. Wrong KB path
   → Check --kb-path parameter
```

### Too Many Version Updates

```
Problem: Too many PRs created for updates

Solution:
1. Adjust update_policy in KWF-CONFIG.yaml
2. Set patch: "weekly-review" instead of "automatic"
3. Increase frequency to monthly instead of daily
```

---

## 📋 Best Practices

### 1. Regular Updates
- ✅ Apply security patches immediately
- ✅ Review minor updates weekly
- ✅ Plan major updates quarterly
- ❌ Let dependencies become stale

### 2. Security First
- ✅ Monitor CVE alerts closely
- ✅ Prioritize security patches
- ✅ Test thoroughly after updates
- ✅ Share alerts with team
- ❌ Delay security fixes

### 3. Compatibility Management
- ✅ Test updates in CI before merge
- ✅ Document any breaking changes
- ✅ Create upgrade guides for major versions
- ❌ Update without testing

### 4. Team Communication
- ✅ Share security alerts promptly
- ✅ Reference KB patterns for consistency
- ✅ Document version decisions
- ✅ Plan major updates together
- ❌ Make changes silently

---

## 🔗 Integration Points

### With Knowledge Base
- **Version reports** → Decision history
- **Security alerts** → Lessons for team
- **Patterns** → Version management best practices
- **Trends** → Track compliance over time

### With GitHub Actions
- **Automatic PRs**: For security fixes
- **Status badges**: Show compliance
- **Notifications**: Alert on vulnerabilities

### With Development Workflow
- **Code reviews**: Reference KB patterns
- **Planning**: Factor in dependency updates
- **Risk management**: Consider update implications

---

## 🎓 Example Workflow

### Day 1: Monday
```
1. Context7 check runs
2. Finds: lodash 4.17.20 has CVE-2024-1234
3. Alert created immediately
4. Team notified
```

### Day 2: Tuesday
```
1. Security team reviews CVE
2. Confirms: High severity, needs immediate fix
3. Creates PR with lodash 4.17.21
4. Runs tests: All pass ✅
```

### Day 3: Wednesday
```
1. PR reviewed and approved
2. Merged to main
3. Deployed to production
4. Security alert resolved ✅
```

### Weekly
```
1. Review version reports
2. Plan minor updates
3. Track compliance trend
4. Update team on version progress
```

---

## 📊 Compliance Dashboard (Conceptual)

```
Library Compliance Scorecard
━━━━━━━━━━━━━━━━━━━━━━━━
Total Dependencies:    48
Current:              47 (97.9%)
Outdated:              1 (2.1%)

By Update Type:
├─ Patch:        0 (0%)
├─ Minor:        1 (react 19.0.0)
└─ Major:        0 (0%)

Security Status:
├─ Critical:     0 ✅
├─ High:         0 ✅
├─ Medium:       0 ✅
└─ None:         48 ✅

Trend:
├─ This Week:   ↑ +1 updated
├─ This Month:  ↑ +3 updated
└─ Overall:     ✅ Improving

Next Action:
→ Plan React 19 migration (next sprint)
```

---

## 📝 Related Documentation

- **Main README**: [../../README.md](../../README.md)
- **KWF Core**: [../knowledge-workflow-framework/README.md](../knowledge-workflow-framework/README.md)
- **Config Reference**: [../knowledge-workflow-framework/KWF-CONFIG.yaml](../knowledge-workflow-framework/KWF-CONFIG.yaml)
- **Playwright Skill**: [../playwright-integration/README.md](../playwright-integration/README.md)
- **Serena Skill**: [../serena-integration/README.md](../serena-integration/README.md)

---

## 🤔 FAQ

**Q: Should I update all libraries at once?**  
A: No. Update patches immediately, plan minor/major updates carefully.

**Q: What if updating breaks our code?**  
A: Test first! Use dev branch, run full test suite before deploying.

**Q: How often should we check versions?**  
A: Daily is recommended for security. Adjust in KWF-CONFIG.yaml if needed.

**Q: Can we pin versions forever?**  
A: Not recommended. Stay reasonably current to get security fixes.

**Q: Do developers need to run this manually?**  
A: No. GitHub Actions runs automatically. Results are in KB.

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ✅ Production Ready
