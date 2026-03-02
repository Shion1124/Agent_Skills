# Serena Integration Skill

> Continuously analyze and track code quality across your codebase

**Purpose**: Make code quality visible, measurable, and actionable  
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
Serena Analysis Runs
        ↓
Code Quality Evaluated
  ├─ Readability score
  ├─ Maintainability score
  ├─ Testability score
  ├─ Security score
  └─ Violations identified
        ↓
Technical Debt Calculated
  ├─ Complexity issues
  ├─ Duplication
  ├─ Missing documentation
  └─ Error handling gaps
        ↓
Markdown Report Generated
        ↓
Smart Categorization:
  ├─ Score ≥85 → patterns/code-quality/
  │   (Example to follow)
  └─ Score <85 → lessons/code-quality-issues/
      (Problems to improve)
        ↓
Auto-Indexed & Searchable
```

---

## 🎯 Key Features

| Feature | Description |
|---------|-------------|
| **Automated Analysis** | Runs daily or on-demand |
| **Multi-dimensional Scoring** | Readability, Maintainability, Testability, Security |
| **Violation Detection** | Critical, High, Medium, Low severity issues |
| **Technical Debt Tracking** | Quantified in "debt points" |
| **Smart Storage** | High-quality code saved as patterns |
| **Fallback Mode** | Demo data if Serena not installed |
| **PR Comments** | Optional feedback on pull requests |

---

## 📈 Quality Scores Explained

### Readability (0-100)
```
90-100  ✅ Excellent  - Clean, self-documenting code
80-89   ⚠️ Good       - Mostly readable, minor improvements needed
70-79   🟡 Fair       - Needs refactoring for clarity
<70     🔴 Poor       - Confusing, requires significant cleanup
```

**What affects it:**
- Code complexity (cyclomatic complexity)
- Clarity of variable/function names
- Comment quality
- Code formatting consistency

### Maintainability (0-100)
```
90-100  ✅ Excellent  - Easy to modify and extend
80-89   ⚠️ Good       - Generally maintainable
70-79   🟡 Fair       - Takes effort to change
<70     🔴 Poor       - High risk of bugs when modifying
```

**What affects it:**
- Code duplication
- Function/class size
- Coupling between modules
- Test coverage

### Testability (0-100)
```
90-100  ✅ Excellent  - Easy to test, well-structured
80-89   ⚠️ Good       - Adequate test support
70-79   🟡 Fair       - Some testing challenges
<70     🔴 Poor       - Hard to test, needs refactoring
```

**What affects it:**
- Dependency injection patterns
- Function purity
- Side effects
- Design patterns used

### Security (0-100)
```
90-100  ✅ Excellent  - Few or no vulnerabilities
80-89   ⚠️ Good       - Minor security issues
70-79   🟡 Fair       - Should address concerns
<70     🔴 Poor       - Critical security problems
```

**What affects it:**
- Input validation
- Authentication/authorization
- Data encryption usage
- Known vulnerability avoidance

---

## 📝 Report Structure

### High-Quality Code Pattern Example

```markdown
---
name: serena-code-quality-report
date: 2026-03-02T14:00:00
type: code-quality-analysis
overall_score: 87
category: code-quality-patterns
tags: code-quality, serena, metrics, excellence
---

# Code Quality Analysis Report - High Quality Pattern

**Overall Grade**: A

## Quality Scores

| Metric | Score | Status |
|--------|-------|--------|
| Overall | 87/100 | ✅ |
| Readability | 89/100 | ✅ |
| Maintainability | 85/100 | ✅ |
| Testability | 84/100 | ✅ |
| Security | 88/100 | ✅ |

## Excellent Practices Found
✅ Clear naming conventions throughout
✅ Comprehensive error handling
✅ Proper use of design patterns
✅ High test coverage (92%)
✅ No critical vulnerability patterns

## Recommendations (Minor)
1. Consider extracting one large function
2. Add 2 missing JSDoc comments
3. Consolidate duplicate utility functions

## Pattern Notes
**Why this is a pattern:**
- Demonstrates best practices
- Good example for code review
- Reference for similar components
- Document what "good" looks like
```

### Issues/Improvement Needed Example

```markdown
---
name: serena-code-quality-report
date: 2026-03-02T14:15:00
type: code-quality-analysis
overall_score: 62
category: code-quality-issues
tags: code-quality, serena, technical-debt, improvement-needed
---

# Code Quality Analysis - Needs Improvement

**Overall Grade**: D
**Technical Debt**: 5,200 points (~104 hours to fix)

## Quality Scores

| Metric | Score | Status |
|--------|-------|--------|
| Overall | 62/100 | 🔴 Poor |
| Readability | 45/100 | 🔴 Poor |
| Maintainability | 58/100 | 🟡 Fair |
| Testability | 70/100 | ⚠️ Good |
| Security | 68/100 | ⚠️ Good |

## Critical Issues (Fix Immediately)
🔴 **[CRITICAL]** Missing input validation
   - Impact: Security vulnerability
   - Severity: HIGH
   - Fix: Add validation for 3 API endpoints

🔴 **[CRITICAL]** Complex function (cyclomatic: 12)
   - Impact: Unmaintainable, hard to test
   - Fix: Extract into 3 smaller functions

## High Priority Issues
🟠 **[HIGH]** Duplicate code (3 instances)
   - 450 lines of repeated logic needed
   - Extract to shared utility

🟠 **[HIGH]** Missing error handling (5 sites)
   - Potential runtime crashes
   - Add try-catch or error boundaries

## Recommendations
1. **Next Sprint**: Fix critical items
2. **Following Sprint**: Address high-priority issues
3. **Ongoing**: Bring readability up from 45 to >75

## Related Lessons
- lesson-123: "How we fixed complex functions"
- pattern-056: "Input validation patterns"
```

---

## ⚙️ Configuration

Located in `KWF-CONFIG.yaml`:

```yaml
serena:
  script_path: ".github/skills/serena-integration/serena_analyzer.py"
  target_directories:
    - "src"
    - "lib"
  
  thresholds:
    overall: 70      # Below this → lessons (issues)
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
    high_quality: "patterns/code-quality"  # Save excellent code
    issues: "lessons/code-quality"         # Save problems
    technical_debt: "lessons/technical-debt"  # Track debt
  
  auto_create_pr_comments: true    # Comment on PRs
  pr_comment_threshold: 75         # If score <75, comment
```

---

## 🚀 Usage

### Manual Execution (Local)

```bash
# Run the analyzer directly
python3 .github/skills/serena-integration/serena_analyzer.py \
  --kb-path .github/skills/knowledge-workflow-framework \
  --target-dir src

# Expected output:
# 📊 Serena Code Quality Analyzer
# ✅ High-quality pattern saved to: knowledge-base/patterns/code-quality/code-quality-report-*.md
# Code Quality Score: 87/100
```

### Automated Execution (GitHub Actions)

```yaml
- Job: Serena Analysis
- Trigger: Daily 02:15 UTC (after Playwright)
- Runs on: ubuntu-latest
- Duration: ~3-5 minutes for typical codebases
```

---

## 📊 Generated Knowledge

### Saved Locations

```
knowledge-base/
├── patterns/
│   └── code-quality/
│       ├── code-quality-report-20260302-140000.md  (Score ≥85)
│       └── code-quality-report-20260301-140015.md  (Score ≥85)
└── lessons/
    ├── code-quality-issues/
    │   ├── code-quality-report-20260302-140030.md  (Score <85)
    │   └── code-quality-report-20260301-140045.md
    └── technical-debt/
        ├── technical-debt-analysis-*.md
        └── ...
```

### Searchable Via Copilot

```
Query Examples:
- "Show me high-quality code patterns"
- "What code quality issues do we have?"
- "How's our technical debt trending?"
- "Which functions need refactoring?"
- "Show security-related code quality findings"
```

---

## 📈 Tracking Improvements

### Weekly Monitoring

```
Example: Track quality score over time

Week 1: Overall 72/100 (🟡 Fair)
Week 2: Overall 74/100 (slight improvement)
Week 3: Overall 76/100 (trending up)
Week 4: Overall 78/100 (approaching ⚠️ Good)

Action: Team commits to fixes
→ Goal: 80/100 by end of month
→ Actual: 81/100 (exceeded goal!)
```

### Monthly Reports

KWF can generate monthly summaries:
- Trend analysis (improving/stable/declining)
- Top categories improved
- Top categories needing work
- Team velocity in reducing technical debt

---

## 🛠️ Troubleshooting

### No Analysis Results

```
Problem: Script runs but no report generated

Causes:
1. Serena not installed
   → npx install -g serena (or demo data used)

2. Target directory not found
   → Verify src/ exists at repository root
   → Or update target_directories in KWF-CONFIG.yaml

3. No code files found
   → ls src/ should show JavaScript/TypeScript files
   → Check file extensions match Serena capabilities
```

### Reports Not Saved to KB

```
Problem: Analysis runs but KB not updated

Causes:
1. Write permission issue
   → chmod 755 knowledge-base/
   → Verify directory writable

2. Wrong KB path
   → Verify --kb-path parameter
   → Should be .github/skills/knowledge-workflow-framework

3. Directory structure not initialized
   → Run kb-generator.py init first
```

---

## 📊 Best Practices

### 1. Regular Review
- ✅ Check reports weekly
- ✅ Discuss findings in retros
- ✅ Plan improvements in sprints
- ❌ Ignore declining scores

### 2. Act on Findings
- ✅ Create tickets for critical issues
- ✅ Refactor gradually
- ✅ Include in sprint planning
- ❌ Let technical debt grow

### 3. Share Knowledge
- ✅ Use high-quality patterns as examples
- ✅ Document lessons in KB
- ✅ Reference in code reviews
- ❌ Duplicate problems across team

### 4. Continuous Improvement
- ✅ Set realistic improvement targets
- ✅ Review trends monthly
- ✅ Celebrate improvements
- ✅ Learn from high-quality code

---

## 🔗 Integration Points

### With Knowledge Base
- **High-Quality Code** → patterns for team to follow
- **Issues Found** → lessons for team to learn from
- **Technical Debt** → tracked and searchable
- **Improvements** → documented progress

### With GitHub Actions
- **Status**: Can add badge to README
- **Artifacts**: Reports downloadable
- **Notifications**: Optional Slack alerts

### With Development Workflow
- **Pull Requests**: Automatic quality comments
- **Code Reviews**: Use KB patterns as standards
- **Refactoring**: Plan based on debt reports

---

## 📋 Quality Improvement Checklist

When score is below target:

```
For Readability Issues (< 75):
☐ Review variable a names - are they clear?
☐ Check function length - any >50 lines?
☐ Verify comments explain "why", not "what"
☐ Ensure consistent code style
☐ Add JSDoc for public functions

For Maintainability Issues (< 70):
☐ Check for duplicate code
☐ Look for circular dependencies
☐ Verify proper abstraction levels
☐ Ensure clear separation of concerns
☐ Add integration tests

For Testability Issues (< 65):
☐ Reduce function side effects
☐ Use dependency injection
☐ Extract logic from components
☐ Create testable helper functions
☐ Add unit tests

For Security Issues (< 80):
☐ Verify input validation everywhere
☐ Check data encryption at rest
☐ Audit authentication flow
☐ Review external dependencies
☐ Run security scanner
```

---

## 🎓 Example Workflow

### Day 1: Monday
```
1. Serena analysis runs
2. Overall score: 74/100 (⚠️ Fair)
3. Key issue: High complexity in payment module
4. Team reviews findings in standup
```

### Days 2-4: Tuesday-Thursday
```
1. Two developers work on refactoring
2. Extract 4 complex functions
3. Add additional tests
4. Code review using KB patterns
```

### Day 5: Friday
```
1. Reanalysis scheduled
2. Overall score: 78/100 (⚠️ Good)
3. Improvement: +4 points
4. New patterns documented for team reference
```

### Weekly
```
Score trend: 72 → 74 → 78 → 80 (improving!)
Team uses KB patterns as standards
Quality culture strengthens
```

---

## 📝 Related Documentation

- **Main README**: [../../README.md](../../README.md)
- **KWF Core**: [../knowledge-workflow-framework/README.md](../knowledge-workflow-framework/README.md)
- **Config Reference**: [../knowledge-workflow-framework/KWF-CONFIG.yaml](../knowledge-workflow-framework/KWF-CONFIG.yaml)
- **Playlist Skill**: [../playwright-integration/README.md](../playwright-integration/README.md)
- **Context7 Skill**: [../context7-integration/README.md](../context7-integration/README.md)

---

## 🤔 FAQ

**Q: What's a good code quality score?**  
A: 80+ is excellent. 70-79 is acceptable. Below 70 needs attention.

**Q: How often should we run analysis?**  
A: Daily is recommended. Can be adjusted in KWF-CONFIG.yaml.

**Q: Can I fix all issues at once?**  
A: Better to fix incrementally. Plan improvements in sprints.

**Q: Do developers need to see every report?**  
A: No. Lead dev or architect reviews weekly. Copilot Chat makes it accessible when needed.

---

**Version**: 1.0  
**Last Updated**: 2026-03-02  
**Status**: ✅ Production Ready
