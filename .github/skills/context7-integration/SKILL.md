---
name: context7-integration
description: |
  Version and security dependency management.
  Tracks package versions, detects CVEs and known vulnerabilities,
  and generates security advisories. Automatically records security
  decisions and lessons into team knowledge base for compliance tracking.
version: 1.0
authors:
  - Security & DevOps Lead
tags:
  - security
  - dependency-management
  - vulnerability-detection
  - cve-tracking
  - compliance
---

# Context7 Integration Skill

## 🎯 Purpose

The Context7 Integration skill:
- **Monitors** all project dependencies and their versions
- **Detects** known vulnerabilities and security issues
- **Alerts** team to CVEs and required updates
- **Tracks** security decisions and compliance status
- **Documents** dependency management strategies

This skill treats security as continuous, data-driven team knowledge.

---

## 🏗️ Architecture

### Security Pipeline

```
Project Dependencies
    ↓
Version Audit (npm audit, pip audit, etc.)
    ↓
CVE Database Check
    ↓
Vulnerability Scoring (CVSS)
    ↓
Risk Assessment
    ↓
KB Knowledge Generation
    ↓
Security Alerts & Reports
    ↓
Compliance Dashboard
```

### Core Components

**1. Dependency Scanner**
- Scans `package.json`, `requirements.txt`, `Gemfile`, etc.
- Collects installed versions
- Identifies outdated packages
- Detects missing dependencies

**2. Vulnerability Detector**
- Checks against CVE databases (NVD, Snyk, npm audit)  
- Calculates CVSS scores
- Categorizes severity levels
- Links to advisories and patches

**3. Risk Analyzer**
- Evaluates exploitability
- Assesses impact on codebase
- Determines if outdated or vulnerable
- Provides update recommendations

**4. Knowledge Generator**
- Creates security decision entries
- Generates patch/update patterns
- Records lessons from incidents
- Maintains security history

---

## 📋 Inputs & Outputs

### Inputs

**Package Files**
- `package.json` (Node.js/npm)
- `requirements.txt`, `poetry.lock` (Python)
- `Gemfile`, `Gemfile.lock` (Ruby)
- `pom.xml`, `build.gradle` (Java)
- `go.mod` (Go)

**Configuration**
```yaml
context7:
  check_npm: true
  check_pip: true
  check_ruby: true
  severity_threshold: "high"  # critical, high, medium, low
  allow_dev_vulnerabilities: false
```

### Outputs

**Security Reports**
- `version-report-YYYYMMDD-HHMMSS.md` - Dependency audit
- `security-alert-YYYYMMDD-HHMMSS.md` - CVE findings
- `vulnerability-YYYYMMDD-HHMMSS.json` - Detailed scan results

**Knowledge Base Entries**
```
knowledge-base/
├── decisions/
│   └── security/decision-dependency-update-policy.md
├── patterns/
│   ├── pattern-supply-chain-attack-prevention.md
│   ├── pattern-zero-day-response.md
│   └── pattern-dependency-pinning-strategy.md
└── lessons/
    ├── lesson-cve-2025-critical-nodejs.md
    ├── lesson-transitive-dependency-risk.md
    └── lesson-dependency-license-compliance.md
```

**Alert Categories**
- **CRITICAL**: Immediate action required (CVSS >= 9.0)
- **HIGH**: Update recommended (CVSS 7.0-8.9)
- **MEDIUM**: Monitor and plan update (CVSS 4.0-6.9)
- **LOW**: Update with normal cadence (CVSS < 4.0)

---

## 🔌 Integration Points

### GitHub Actions

```yaml
- name: Check Vulnerabilities with Context7
  run: |
    python .github/skills/context7-integration/context7_manager.py \
      --kb-path .github/skills/knowledge-workflow-framework \
      --check-npm \
      --check-pip \
      --generate-alerts \
      --update-kb
```

### Webhook Notifications

- Slack alerts for CRITICAL/HIGH vulnerabilities
- GitHub Issues creation for medium-priority CVEs
- Email digest weekly (all projects)
- Dashboard updates real-time

### Knowledge Base Connection

Automatic searches for:
- Previous incidents with same CVE
- Applicable update/patch patterns
- Security decision precedents
- Dependency version history

---

## ⚙️ Configuration

### KWF-CONFIG.yaml Integration

```yaml
context7:
  enabled: true
  version: "3.0"
  schedule: "every 6 hours"  # Frequent checks due to security
  
  package_managers:
    npm:
      enabled: true
      files: ["package.json", "package-lock.json"]
      check_transitive: true
      allow_prerelease: false
    
    pip:
      enabled: true
      files: ["requirements.txt", "poetry.lock", "setup.py"]
      check_prerelease: false
    
    ruby:
      enabled: true
      files: ["Gemfile", "Gemfile.lock"]
      bundler_audit: true
  
  vulnerability_checks:
    cve_database: ["nvd", "snyk", "npm-audit"]
    cvss_threshold: 4.0  # Report anything 4.0 and above
    check_outdated: true
    check_deprecated: true
  
  alerts:
    critical_channels: ["slack", "email", "github-issue"]
    high_channels: ["slack", "github-issue"]
    medium_channels: ["email", "dashboard"]
    low_channels: ["dashboard"]
  
  kb_integration:
    auto_create_decisions: true
    track_update_patterns: true
    link_cve_advisories: true
    maintain_compliance_audit: true
```

### Severity Handling

```yaml
# .context7-rules.yaml
severity_overrides:
  # Sometimes npm reports false positives
  packages:
    "some-dev-dependency":
      if_dev_only: ignore
    "optional-security-lib":
      cvss_floor: 7.0  # Ignore lower scores
  
  cves:
    "CVE-2024-1234":
      affected_versions: ["1.0.0", "1.0.1"]
      status: "monitoring"  # Not yet patched upstream
      review_date: "2026-04-01"
```

---

## 📊 Usage Workflow

### 1. Local Scanning

```bash
# Check all dependencies
python context7_manager.py

# Check only npm packages
python context7_manager.py --npm-only

# Check only Python packages
python context7_manager.py --pip-only

# Generate security report
python context7_manager.py --report

# Create KB security entries
python context7_manager.py --generate-kb

# Export for compliance audit
python context7_manager.py --compliance-export
```

### 2. CI/CD Integration

Vulnerability checks run:
- On every commit to `main`
- On every pull request (blocks if CRITICAL found)
- Scheduled every 6 hours (frequent for security)
- Manual trigger for immediate scan

### 3. Update Management

```bash
# Check for available updates
python context7_manager.py --list-outdated

# Simulate update (dry-run)
python context7_manager.py --update --dry-run

# Auto-update development dependencies only
python context7_manager.py --auto-update --dev-only

# Update specific package
python context7_manager.py --update-package lodash@4.17.21
```

---

## 🎓 Knowledge Generation Examples

### Generated Decision Entry

```markdown
# Decision: Dependency Update Policy (Security-First)

**Status**: ACCEPTED  
**Date**: 2026-03-02

## Security Update SLA

- **CRITICAL (CVSS 9-10)**: Update within 24 hours
- **HIGH (CVSS 7-8.9)**: Update within 1 week
- **MEDIUM (CVSS 4-6.9)**: Update within 2 weeks
- **LOW (CVSS < 4)**: Update with normal cadence

## Development Dependencies
- Auto-update allowed
- Test coverage must pass
- No production impact allowed

## Production Dependencies
- Manual review required
- Changelog review mandatory
- Staged rollout preferred

## References
- Lesson: lesson-transitive-dependency-risk.md
- Pattern: pattern-supply-chain-attack-prevention.md
```

### Generated Pattern Entry

```markdown
# Pattern: Responding to Critical CVE

**Complexity**: Advanced  
**Tags**: incident-response, security, zero-day

## Scenario
Critical CVE discovered in directly used dependency (CVSS 9+).
Patch available. What's your response?

## Incident Response Process

### Phase 1: Assess (< 1 hour)
1. Verify vulnerability scope
   - Does it affect our code?
   - What minimum version is safe?
   - Is patch already released?

2. Determine impact
   - Exploitable in our environment?
   - Authentication required?
   - Known active exploitation?

### Phase 2: Patch (< 4 hours)
1. Test patch in staging
   - Run full test suite
   - Check compatibility
   - Performance regression check

2. Deploy to production
   - Use phased rollout if possible
   - Monitor error rates
   - Verify patch effectiveness

### Phase 3: Document (< 24 hours)
1. Record incident in KB
2. Update security decision
3. Create lesson learned
4. Notify stakeholders

## Timeline Guardrails
- < 1h: Assess severity
- < 4h: Deploy patch (if non-breaking)
- < 24h: Full deployment + documentation

## Links
- Decision: decision-dependency-update-policy.md
- Lesson: lesson-cve-2025-critical-nodejs.md
```

### Generated Lesson Entry

```markdown
# Lesson: Transitive Dependency Vulnerabilities Are Real

**Date**: 2026-02-20  
**Severity**: High
**Status**: RESOLVED (with pattern update)

## Incident Summary
Security scan found HIGH CVE in `lodash@3.10.1`.
Our `package.json` never directly depends on lodash 3.x.
Root cause: `request@2.88.2` → `lodash@3.10.1` (transitive).

## Timeline
- Feb 15: CVE published
- Feb 18: Automatic scan detected
- Feb 19: Root cause investigation
- Feb 20: `request` library updated, vulnerability cleared

## Key Insights
1. Direct dependencies get scrutiny; transitive ones often missed
2. Old libraries with transitive deps are risk vectors
3. `npm ls <package>` is crucial debugging tool
4. Security scanning must include transitive deps

## Prevention
- Add `npm audit --audit-level moderate` to CI gates
- Review `npm shrinkwrap` at least monthly
- Audit production dependencies quarterly
- Link security decisions to dependency graphs

## Pattern Applied
See: pattern-supply-chain-attack-prevention.md
```

---

## 📊 Security Metrics

### Tracking Metrics

| Metric | Target | Frequency |
|--------|--------|-----------|
| Avg Dependency Age | < 6 months | Monthly |
| Outdated Count | < 5% | Weekly |
| CRITICAL CVEs | 0 | Per scan |
| HIGH+ CVEs | < 2 | Per scan |
| Unpatched Dependencies | 0 | Daily |
| License Violations | 0 | Monthly |

### Compliance Reporting

```
Compliance Status Dashboard
├── CRITICAL Issues: 0
├── HIGH Issues: 1 (patching in progress)
├── MEDIUM Issues: 3 (planned update)
├── Compliance Score: 94/100
└── Last Scan: 2026-03-02 14:23:45 UTC
```

---

## 🔄 Maintenance Schedule

### Hourly
- Continuous CVE database monitoring
- Immediate alert on critical discoveries

### Daily
- Scan all dependencies
- Check for new HIGH vulnerability patches
- Monitor update status

### Weekly
- Review vulnerability trends
- Analyze root causes
- Plan update campaigns

### Monthly
- Comprehensive dependency audit
- License compliance review
- Security strategy evaluation

### Quarterly
- Supply chain risk assessment
- Update policy effectiveness review
- New threat analysis

---

## 🐛 Error Handling

### Common Issues & Resolution

**Issue**: npm audit reports false positives
```
Solution:
1. Check npmjs.com for vulnerability details
2. Verify if affects your specific use case
3. If legitimate false positive:
   - Document in .context7-rules.yaml
   - Reference NPM issue/PR number
   - Track for future upstream fixes
4. Update KB pattern: pattern-supply-chain-attack-prevention.md
```

**Issue**: Can't update dependency due to breaking changes
```
Solution:
1. Isolate impact of breaking change
2. Check if major version can be skipped
3. Review migration guide
4. Create pattern: pattern-migration-<package>.md
5. Plan phased update with testing
6. Update decision if you choose to defer
```

**Issue**: Transitive dependency has critical CVE but package unmaintained
```
Solution:
1. Find alternative maintained package
2. Check for monkey-patch solutions
3. Evaluate workarounds for security
4. Document decision to defer
5. Create contingency plan
6. Record lesson on maintenance risk
```

---

## 🔗 Related Skills

Integrates with:
- **knowledge-workflow-framework** - Core KB system
- **playwright-integration** - Dependency version impacts on tests
- **serena-integration** - Code quality of dependency usage
- **github-actions** - Automated vulnerability scanning

---

## 🛡️ Security Best Practices

### Do's ✅
- Scan dependencies at least daily
- Update CRITICAL vulnerabilities within 24 hours
- Monitor both direct and transitive dependencies
- Maintain audit trail of all updates
- Review security advisories for context

### Don'ts ❌
- Ignore vulnerability reports
- Update dependencies without testing
- Skip security scanning "for performance"
- Keep dependencies with known exploits
- Assume transitive deps have no risk

---

## ✅ Deployment Checklist

Before production use:

- [ ] Context7 manager installed and configured
- [ ] Package managers configured (npm, pip, ruby, etc.)
- [ ] CVE database sources configured
- [ ] `context7_manager.py` in correct location
- [ ] GitHub Actions workflow includes context7 job
- [ ] Alert channels configured (Slack, email, etc.)
- [ ] Severity thresholds appropriate for team
- [ ] Baseline vulnerability scan completed
- [ ] KB entries generated correctly
- [ ] GitHub Issues templates for CVE filing created
- [ ] Update SLA documented
- [ ] Compliance audit trail initialized

---

## 📞 Support & Troubleshooting

For issues:
1. Check `README.md` in this directory
2. Review `context7_manager.py` source code
3. Search KB for similar vulnerabilities
4. Check GitHub Actions logs
5. Review security decision documents

**Common Sources**:
- Update guidance → `decision-dependency-update-policy.md`
- CVE response → `pattern-supply-chain-attack-prevention.md`
- Historical incidents → `lesson-*.md` files

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ACTIVE  
**Next Review**: 2026-06-02
