---
name: serena-integration
description: |
  Code quality analysis and technical debt tracking.
  Evaluates source code against quality metrics, identifies code smells,
  and generates actionable improvement patterns. Automatically records
  quality insights into team knowledge base for reference and enforcement.
version: 1.0
authors:
  - Code Quality Lead
tags:
  - code-quality
  - static-analysis
  - technical-debt
  - metrics
  - agile-metrics
---

# Serena Integration Skill

## 🎯 Purpose

The Serena Integration skill:
- **Analyzes** source code for quality patterns and anti-patterns
- **Tracks** technical debt and code complexity
- **Identifies** improvement opportunities with priority
- **Documents** quality standards and best practices
- **Enforces** consistency across the codebase

This skill treats code quality as strategic knowledge, not just linting.

---

## 🏗️ Architecture

### Analysis Pipeline

```
Source Code
    ↓
Static Analysis (Sonarscan)
    ↓
Metric Calculation
    ↓
Quality Scoring
    ↓
Pattern Recognition
    ↓
Knowledge Generation
    ↓
KB Integration & Indexing
    ↓
Team Dashboard & Alerts
```

### Core Components

**1. Code Scanner**
- Scans source files (Python, JavaScript, TypeScript, Java, etc.)
- Counts lines of code, complexity, duplication
- Identifies code smells and anti-patterns
- Generates raw metrics

**2. Quality Calculator**
- Weight quality factors (maintainability, reliability, security)
- Calculate composite quality score (0-100)
- Rank issues by severity
- Trend analysis over time

**3. Pattern Recognizer**
- Identifies repeated quality issues
- Categorizes issues by type
- Links to historical patterns
- Suggests applicable solutions

**4. Knowledge Generator**
- Creates lesson entries for code issues
- Generates pattern entries for solutions
- Records quality decisions
- Maintains quality history

---

## 📋 Inputs & Outputs

### Inputs

**Configuration**
```yaml
serena:
  code_dirs: ["src/", "lib/", "apps/"]
  excluded_dirs: ["node_modules/", "dist/", "build/"]
  languages: ["python", "typescript", "javascript"]
  quality_gate_score: 80
  max_complexity: 15
  max_duplication: 10
```

**Supported Languages**
- Python (via pylint, flake8)
- JavaScript/TypeScript (via ESLint)
- Java (via SonarJava)
- Go, C++, C# (via language-specific tools)

### Outputs

**Quality Reports**
- `code-quality-report-YYYYMMDD-HHMMSS.md` - Executive summary
- `code-issues-YYYYMMDD-HHMMSS.md` - Detailed findings
- `quality-metrics-YYYYMMDD-HHMMSS.json` - Raw metrics

**Knowledge Base Entries**
```
knowledge-base/
├── decisions/
│   └── quality/decision-code-quality-standards.md
├── patterns/
│   ├── pattern-refactoring-legacy-code.md
│   ├── pattern-complexity-reduction.md
│   └── pattern-duplication-elimination.md
└── lessons/
    ├── lesson-code-smell-types.md
    ├── lesson-acceptable-complexity.md
    └── lesson-technical-debt-management.md
```

**Score Categories**
- **A (90-100)**: Excellent code quality
- **B (80-89)**: Good, minor improvements recommended
- **C (70-79)**: Fair, improvements needed
- **D (60-69)**: Poor, refactoring recommended
- **F (<60)**: Critical issues, immediate action required

---

## 🔌 Integration Points

### GitHub Actions

```yaml
- name: Analyze Code Quality with Serena
  run: |
    python .github/skills/serena-integration/serena_analyzer.py \
      --code-path src/ \
      --kb-path .github/skills/knowledge-workflow-framework \
      --generate-report \
      --update-kb
```

### GitHub PR Integration

- Comments with quality delta on PRs
- Blocks merges if score drops > 5%
- Links to applicable quality patterns
- Suggests refactoring patterns

### Knowledge Base Connection

Automatic KB searches for:
- Previous similar code smells
- Applicable refactoring patterns
- Quality decision precedents
- Historical trends

---

## ⚙️ Configuration

### KWF-CONFIG.yaml Integration

```yaml
serena:
  enabled: true
  version: "2.0"
  schedule: "every 4 hours"
  analysis_type: "comprehensive"  # comprehensive, fast, incremental
  
  metrics:
    track_complexity: true
    track_duplication: true
    track_maintainability: true
    track_coverage: true
  
  quality_gates:
    overall_score_minimum: 80
    max_cyclomatic_complexity: 15
    max_nesting_depth: 4
    max_duplication_percentage: 10
  
  languages:
    python:
      enabled: true
      rules: "pylint"
      exclude_patterns: ["test_*.py", "*_test.py"]
    
    typescript:
      enabled: true
      rules: "eslint"
      config_file: ".eslintrc.json"
  
  kb_integration:
    auto_generate_patterns: true
    track_improvements: true
    alert_on_degradation: true
    link_to_decisions: true
```

### Analysis Rules

```yaml
# .serena-config.yaml
rules:
  # Complexity
  max_function_complexity: 15
  max_file_complexity: 100
  
  # Duplication
  min_line_count: 3
  similarity_threshold: 80
  
  # Maintainability
  acceptable_cyclomatic: 10
  allowed_nesting: 4
  
  # Security
  check_sql_injection: true
  check_hardcoded_secrets: true
```

---

## 📊 Usage Workflow

### 1. Local Analysis

```bash
# Analyze current code
python serena_analyzer.py

# Analyze specific directory
python serena_analyzer.py --path src/

# Generate detailed report
python serena_analyzer.py --detailed

# Compare against baseline
python serena_analyzer.py --compare-baseline

# Generate KB entries
python serena_analyzer.py --generate-kb
```

### 2. CI/CD Integration

Quality checks run:
- On every push to `main`
- On every pull request
- Scheduled every 4 hours
- Manual trigger for full analysis

### 3. Quality Gates

```bash
# Stop pipeline if score < 80
quality_score=$(python serena_analyzer.py --json | jq '.overall_score')
if [ $quality_score -lt 80 ]; then
  echo "Quality score too low: $quality_score"
  exit 1
fi
```

---

## 🎓 Knowledge Generation Examples

### Generated Decision Entry

```markdown
# Decision: Enforce Maximum Cyclomatic Complexity of 15

**Status**: ACCEPTED  
**Date**: 2026-03-01

## Rationale
Functions with complexity > 15 become difficult to test and maintain.
Industry benchmark supports limit of 10-15.

## Implementation
- ESLint rule: `complexity: ["error", 15]`
- Pylint: `max-locals=15`
- Code review gatekeeping

## References
- Pattern: pattern-complexity-reduction.md
- Lesson: lesson-acceptable-complexity.md
```

### Generated Pattern Entry

```markdown
# Pattern: Refactoring Deeply Nested Conditionals

**Complexity**: Intermediate  
**Tags**: refactoring, readability, maintainability

## Problem
Deep nesting (> 3 levels) reduces code readability and testability:
\`\`\`python
if condition_a:
  if condition_b:
    if condition_c:
      if condition_d:
        # Logic here
\`\`\`

## Solution

### Option 1: Early Returns
\`\`\`python
def process(a, b, c, d):
  if not condition_a: return None
  if not condition_b: return None
  if not condition_c: return None
  if not condition_d: return None
  # Logic here
\`\`\`

### Option 2: Guard Clause Pattern
\`\`\`python
def process(a, b, c, d):
  if not (condition_a and condition_b 
          and condition_c and condition_d):
    return None
  # Logic here
\`\`\`
```

### Generated Lesson Entry

```markdown
# Lesson: Duplication as Early Warning Sign

**Date**: 2026-02-25  
**Severity**: Medium

## Discovery
Project scan identified 12% code duplication (> 10% threshold).
Root cause: Copy-paste implementation of similar features.

## Impact
- 3 bugs fixed in one function but not others
- Maintenance burden increased 40%
- Testing effort multiplied

## Prevention
- Implement shared utility functions
- Use composition over duplication
- Add duplication checks to CI/CD

## Status
Refactoring in progress (estimated: 2 weeks)
```

---

## 📊 Quality Metrics

### Standard Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Cyclomatic Complexity | Decision points in code | < 15 per function |
| Code Duplication | Duplicated lines / total lines | < 10% |
| Maintainability Index | Combined complexity measure | > 80 |
| Technical Debt Ratio | Estimated effort to fix issues | < 5% |
| Code Coverage | Lines covered by tests | > 80% |

### Scoring Breakdown

```
Overall Quality Score (0-100)
├── Maintainability (30%): Based on complexity, duplication
├── Reliability (30%): Based on error handling, exceptions
├── Security (20%): Based on vulnerability detection
├── Performance (10%): Based on worst-practice detection
└── Conformance (10%): Based on style guide compliance
```

---

## 🔄 Maintenance Schedule

### Daily
- Monitor quality breaches
- Alert on score degradation > 5%
- Track high-complexity functions

### Weekly
- Analyze patterns in code issues
- Review technical debt trends
- Update quality metrics

### Monthly
- Deep dive into quality drivers
- Inspect duplicate code clusters
- Plan refactoring efforts

### Quarterly
- Quality strategy review
- Complexity baseline update
- Tool and rule effectiveness evaluation

---

## 🐛 Error Handling

### Common Issues & Resolution

**Issue**: Report shows high duplication but code looks different
```
Solution:
1. Check for similar patterns (logging, error handling)
2. Review pattern: pattern-duplication-elimination.md
3. Consider functional equivalence = duplication
4. Extract common function
5. Update KB with lesson
```

**Issue**: Complexity score spikes after refactoring
```
Solution:
1. Likely caused by new abstractions increasing metrics
2. Compare against pattern baseline
3. Review lesson: lesson-acceptable-complexity.md
4. Verify test coverage maintained
5. Update decision if threshold change needed
```

**Issue**: Quality gate prevents merge but score looks acceptable
```
Solution:
1. Check trending data (regression detection)
2. Review PR baseline comparison
3. Verify all files analyzed
4. Check quality decision criteria
```

---

## 🔗 Related Skills

Integrates with:
- **knowledge-workflow-framework** - Core KB system
- **playwright-integration** - Test coverage metrics
- **context7-integration** - Dependency quality impacts
- **github-actions** - CI/CD quality gates

---

## 🎯 Continuous Improvement

### Month 1
- Establish quality baseline
- Document existing code patterns
- Set realistic improvement targets

### Month 2-3
- Refactor 20% lowest-scoring code
- Implement complexity refactoring patterns
- Reduce duplication by 30%

### Month 4+
- Maintain quality > 85 score
- Continuous pattern refinement
- Proactive code improvement

---

## ✅ Deployment Checklist

Before production use:

- [ ] Serena analyzer installed and configured
- [ ] Code directories identified and scoped
- [ ] Language rules configured appropriately
- [ ] `serena_analyzer.py` in correct location
- [ ] GitHub Actions workflow includes serena job
- [ ] Quality gate thresholds defined
- [ ] Baseline metrics established
- [ ] Team trained on quality standards
- [ ] First run successful
- [ ] KB entries generated correctly
- [ ] Metrics dashboard accessible
- [ ] Alert thresholds configured

---

## 📞 Support & Troubleshooting

For issues:
1. Check `README.md` in this directory
2. Review `serena_analyzer.py` source code
3. Search KB for quality patterns
4. Check GitHub Actions logs
5. Review quality decision documents

**Common Sources**:
- Complexity guidance → `decision-code-quality-standards.md`
- Duplication resolution → `pattern-duplication-elimination.md`
- Maintenance issues → `lesson-technical-debt-management.md`

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ACTIVE  
**Next Review**: 2026-06-02
