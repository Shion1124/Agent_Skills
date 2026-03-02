# .github - GitHub Infrastructure and Automation

> GitHub Actions workflows and Agent Skills for knowledge management, testing, quality, and security automation

**Purpose**: Centralize all GitHub-specific automation and configuration  
**Version**: 1.0  
**Created**: 2026-03-02

---

## 📁 Directory Structure

```
.github/
├── README.md (you are here)
│   ↑ GitHub infrastructure documentation
│
├── workflows/
│   └── knowledge-integration.yml ......... Main automation pipeline (550+ lines)
│       ├─ Daily scheduled execution
│       ├─ 6 parallel/sequential jobs
│       ├─ Event triggers (schedule, push, manual)
│       └─ Error handling & notifications
│
└── skills/
    ├── README.md ........................ Skills system overview
    │
    ├── knowledge-workflow-framework/ ... Core KWF system (knowledge management)
    │   ├── SKILL.md ..................... Skill definition for Copilot
    │   ├── README.md ................... Detailed guide (874 lines)
    │   ├── INSTALLATION_GUIDE.md ....... Team setup & deployment (745 lines)
    │   ├── kb-generator.py ............ KB indexing & search tool (440 lines)
    │   ├── KWF-CONFIG.yaml ........... Configuration (519 lines, extended)
    │   ├── Templates/
    │   │   ├── decision-template.md .... Template: Architecture decisions
    │   │   ├── pattern-template.md ..... Template: Reusable patterns
    │   │   └── lesson-template.md ...... Template: Learnings & incidents
    │   └── knowledge-base/
    │       ├── knowledge-index.json ... Auto-generated search index
    │       ├── decisions/ ........... Architecture, tools, security, etc.
    │       ├── patterns/ .......... Frontend, backend, testing, etc.
    │       └── lessons/ ......... Learnings from incidents, tests, quality
    │
    ├── playwright-integration/ .............. Test automation skill
    │   ├── SKILL.md ...................... Skill definition
    │   ├── README.md ................... Guide (397 lines)
    │   └── playwright_collector.py ...... Implementation (250+ lines)
    │
    ├── serena-integration/ ................. Code quality skill
    │   ├── SKILL.md ...................... Skill definition
    │   ├── README.md ................... Guide (530 lines)
    │   └── serena_analyzer.py .......... Implementation (300+ lines)
    │
    └── context7-integration/ ............... Security & version skill
        ├── SKILL.md ..................... Skill definition
        ├── README.md .................. Guide (570 lines)
        └── context7_manager.py ........ Implementation (350+ lines)
```

---

## 🔄 GitHub Actions Workflow System

### File: `workflows/knowledge-integration.yml`

**Purpose**: Orchestrate daily automation of knowledge capture and analysis

**Size**: 550+ lines of YAML/Shell

**Location**: `.github/workflows/knowledge-integration.yml`

### Execution Timeline

```
Every Day at 02:00 UTC (configurable)

02:00 UTC ─── Job 1: Playwright Collection
            └─ Run Playwright tests (or use demo data)
            └─ Analysis: test count, pass rate, flaky detection
            └─ Output: test-report-*.md
            └─ Save to: knowledge-base/lessons/{year}/

02:15 UTC ─── Job 2: Serena Analysis
            └─ Analyze code quality (or use demo data)
            └─ Analysis: scores (readability, maintainability, etc)
            └─ Output: code-quality-report-*.md
            └─ Save to: knowledge-base/patterns/ or lessons/

02:30 UTC ─── Job 3: Context7 Check
            └─ Check library versions & security (or use demo data)
            └─ Analysis: version compliance, CVEs, updates needed
            └─ Output: version-report-*.md, security-alert-*.md
            └─ Save to: knowledge-base/decisions/ & lessons/

02:45 UTC ─── Job 4: KB Index Update
            └─ python3 kb-generator.py update-index
            └─ Generate: knowledge-index.json
            └─ Result: All entries searchable

03:00 UTC ─── Job 5: Auto-Commit & Push
            └─ git add knowledge-base/
            └─ git commit "Update Knowledge Base from integration tools"
            └─ git push origin branch
            └─ Result: Changes visible in GitHub

03:15 UTC ─── Job 6: Notifications
            └─ Create GitHub Actions summary
            └─ Optional: Send Slack/email (if configured)
            └─ Result: User sees workflow completion
```

### Workflow Triggers

```yaml
1. Schedule (Primary)
   - Trigger: Daily at 02:00 UTC
   - Cron: '0 2 * * *'
   - Allows: Consistent, predictable execution

2. Push Events
   - Trigger: Push to main/develop branches
   - Paths: .github/skills/** or tests/** or src/**
   - Allows: Run on relevant code changes

3. Manual Dispatch (Manual Trigger)
   - Trigger: Workflow dispatch from GitHub UI
   - Inputs: Select which jobs to run
   - Allows: On-demand execution for testing
```

### Feature Highlights

```yaml
✅ Error Handling
   └─ continue-on-error: true
   └─ All jobs run even if some fail
   └─ System never breaks completely

✅ Conditional Steps
   └─ Skips unnecessary runs
   └─ Dependencies handled correctly
   └─ Parallel execution where possible

✅ Artifact Management
   └─ Upload KB reports (90-day retention)
   └─ Downloadable from GitHub Actions
   └─ Useful for auditing

✅ Environment
   └─ Python 3.11
   └─ Ubuntu latest
   └─ Standard GitHub-hosted runner

✅ Notifications
   └─ Workflow summary in GitHub Actions
   └─ Optional: Slack, email, GitHub Discussions
   └─ Configurable in KWF-CONFIG.yaml
```

---

## 🛠️ Skills System

The `.github/skills/` directory contains all automation skills:

### 1. Knowledge Workflow Framework (KWF)

**Location**: `.github/skills/knowledge-workflow-framework/`

**Purpose**: Core system for capturing, organizing, indexing team knowledge

**Key Components**:
- `kb-generator.py` - KB management (init, index, search, validate, stats)
- `KWF-CONFIG.yaml` - Team configuration (519 lines, fully extensible)
- `knowledge-base/` - Organized repository of team knowledge
- Templates - Sample decision/pattern/lesson templates

**Output**: 
- Decision records (architecture, tools, process decisions)
- Pattern records (reusable solutions)
- Lesson records (learnings from incidents, tests, quality)

**Index**: Auto-generated `knowledge-index.json` for Copilot access

### 2. Playwright Integration

**Location**: `.github/skills/playwright-integration/`

**Purpose**: Automatically record E2E test results to Knowledge Base

**Key Component**: `playwright_collector.py` (250+ lines)
- Detects Playwright installation
- Runs: `npx playwright test --reporter=json`
- Falls back to demo data if not installed
- Analyzes results: pass rate, failures, flakiness, coverage
- Saves to KB: `lessons/{year}/test-report-*.md`

**Benefit**: Track test quality trends, identify flaky tests, monitor coverage

### 3. Serena Integration

**Location**: `.github/skills/serena-integration/`

**Purpose**: Continuously analyze and monitor code quality

**Key Component**: `serena_analyzer.py` (300+ lines)
- Detects Serena installation
- Runs: `npx serena analyze src --json`
- Falls back to demo data if not installed
- Measures: readability, maintainability, testability, security scores
- Identifies violations and technical debt
- Saves to KB: Patterns (score ≥85) or Lessons (score <85)

**Benefit**: Track quality trends, document excellence patterns, reduce technical debt

### 4. Context7 Integration

**Location**: `.github/skills/context7-integration/`

**Purpose**: Manage library versions and detect security vulnerabilities

**Key Component**: `context7_manager.py` (350+ lines)
- Detects Context7 installation
- Runs: `npx context7 check --format json`
- Falls back to demo data if not installed
- Checks: version compliance, outdated packages, CVEs
- Categorizes updates: patch (auto), minor (review), major (manual)
- Saves to KB: Decisions (version reports) & Lessons (security alerts)

**Benefit**: Automate security monitoring, track version compliance, reduce CVE risk

---

## ⚙️ Configuration Management

### KWF-CONFIG.yaml

**Located**: `.github/skills/knowledge-workflow-framework/KWF-CONFIG.yaml`

**Size**: 519 lines (extended, significantly beyond baseline)

**Structure**:

```yaml
team:
  name: "Your Team"
  repository_url: "https://github.com/yourorg/yourrepo"
  # ↑ IMPORTANT: Points to the project using this framework

knowledge_base:
  location: ".github/skills/knowledge-workflow-framework/knowledge-base"
  auto_generate_index: true
  enable_search: true

decision_categories:
  # Pre-configured: architecture, tools, database, security, etc.
  # Extensible: Add your own categories

pattern_categories:
  # Pre-configured: api-design, testing, database, etc.
  # Extensible: Add your own categories

lesson_categories:
  # Pre-configured: operations, performance, security, etc.
  # Extensible: Add your own categories

integrations:
  playwright:
    enabled: true/false       # Toggle skill on/off
  serena:
    enabled: true/false
  context7:
    enabled: true/false

playwright:
  test_directory: "tests"
  browsers: ["chromium", "firefox", "webkit"]
  metrics:
    track_flakiness: true
    track_coverage: true

serena:
  target_directories: ["src", "lib"]
  thresholds:
    overall: 70
    readability: 75
    security: 80

context7:
  version_locking:
    core_libraries: [react, typescript]
    development_tools: [eslint, jest]
  security:
    critical_response_hours: 24

automation:
  tool_integration:
    playwright_pipeline:
      time: "02:00"      # UTC
    serena_pipeline:
      time: "02:15"
    context7_pipeline:
      time: "02:30"

metrics:
  track_decision_usage: true
  track_pattern_effectiveness: true
  # ... extensive monitoring configuration

notifications:
  enable_notifications: true
  events:
    test_failure_rate_high: true
    quality_score_dropped: true
    security_vulnerability_detected: true
```

**Customization**: 
- Team name, repository URL (mandatory)
- Enable/disable skills (by feature)
- Adjust schedules (timing, frequency)
- Configure thresholds (quality scores, CVE severity)
- Set notification preferences

---

## 🔄 Data Flow

### From Tools to Knowledge Base

```
┌──────────────────────────────────────┐
│ Tool Execution                       │
│ (Playwright/Serena/Context7)         │
└──────────────────┬───────────────────┘
                   ↓
        ┌──────────────────────┐
        │ Result Analysis      │
        │ (Python scripts)     │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Markdown Generation  │
        │ (Formatted reports)  │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Smart Storage        │
        │ decisions/           │
        │ patterns/            │
        │ lessons/             │
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ KB Index Generation  │
        │ (knowledge-index.json)
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Git Commit & Push    │
        │ (Auto-saved to GitHub)
        └──────────┬───────────┘
                   ↓
        ┌──────────────────────┐
        │ Copilot Chat Access  │
        │ (Query via AI)       │
        └──────────────────────┘
```

---

## 🚀 Deployment Steps

### Step 1: Verify Directory Structure

```bash
# Check that all files are in place
ls -la .github/skills/knowledge-workflow-framework/
ls -la .github/skills/playwright-integration/
ls -la .github/skills/serena-integration/
ls -la .github/skills/context7-integration/
ls -la .github/workflows/knowledge-integration.yml
```

### Step 2: Configure

```bash
# Edit configuration
nano .github/skills/knowledge-workflow-framework/KWF-CONFIG.yaml

# Update:
# - team.name
# - team.repository_url (IMPORTANT!)
# - Any skills you want to disable
# - Timing adjustments (if needed)
```

### Step 3: Test Locally

```bash
cd .github/skills/knowledge-workflow-framework

# Initialize KB
python3 kb-generator.py init

# Test each skill
python3 ../playwright-integration/playwright_collector.py --kb-path .
python3 ../serena-integration/serena_analyzer.py --kb-path .
python3 ../context7-integration/context7_manager.py --kb-path .

# Update index
python3 kb-generator.py update-index
python3 kb-generator.py stats
```

### Step 4: Deploy

```bash
# Add all files
git add .github/

# Commit with descriptive message
git commit -m "Deploy Knowledge Workflow Framework with Playwright, Serena, Context7 integrations

- Core KWF for knowledge management
- Playwright skill for E2E test recording
- Serena skill for code quality analysis
- Context7 skill for security & version management
- GitHub Actions automation pipeline (daily execution)
- Complete documentation for team deployment

Production ready: assumes continuous operation"

# Push to GitHub
git push origin main
```

### Step 5: Verify

```bash
# Check GitHub Actions
# Repository → Actions tab
# Should see: "Knowledge Integration Pipeline" workflow

# Wait for first run (or trigger manually)
# Repository → Actions → Knowledge Integration Pipeline
# Click "Run workflow" → Select branch → "Run workflow"

# Monitor execution
# Watch 6 jobs execute in sequence
# See KB entries get created
```

---

## 📊 Monitoring & Maintenance

### Regular Checks

```
Daily:
  ├─ GitHub Actions execution completes
  ├─ No critical errors in logs
  └─ KB entries generated (>0 files)

Weekly:
  ├─ Review KB entries generated
  ├─ Check quality trends
  ├─ Verify security alerts processed
  ├─ Confirm test results recorded

Monthly:
  ├─ Full KB audit (stats)
  ├─ Configuration review
  ├─ Performance check
  └─ Team feedback session

Quarterly:
  ├─ Strategic review of knowledge collected
  ├─ Team retrospective
  ├─ Adjust categories/thresholds as needed
  └─ Plan improvements
```

### Common Issues

```
Issue: Workflow doesn't run
Fix: 
  1. Check: Settings → Actions → General (enabled?)
  2. Verify: .github/workflows/knowledge-integration.yml exists
  3. Test: Manual trigger from Actions UI

Issue: KB not updating
Fix:
  1. Check: Log output in GitHub Actions
  2. Verify: Python scripts have correct paths
  3. Test: Run locally: python3 kb-generator.py validate

Issue: Copilot can't find KB entries
Fix:
  1. Check: knowledge-index.json exists
  2. Verify: Entries in knowledge-base/ directories
  3. Test: python3 kb-generator.py search "keyword"
  4. Ensure: Repository is accessible to Copilot
```

---

## 🔐 Security Considerations

### Data Storage
```
Location: .github/skills/knowledge-workflow-framework/knowledge-base/
Access: Via GitHub repository permissions
Backup: Standard GitHub repository backup
Sharing: Same as repository (follows GitHub access control)
```

### Secrets
```
DO:
  ✅ Store sensitive data in GitHub Secrets
  ✅ Reference secrets in workflow environment
  ✅ Use GitHub Secrets API

DON'T:
  ❌ Store passwords in KWF-CONFIG.yaml
  ❌ Commit API keys to repository
  ❌ Store credentials in KB markdown files
```

### Access Control
```
- Repository access = KB access (via Copilot)
- Workflow access = Repository admin
- GitHub Actions = Repository secrets available
- Copilot Chat = Inherits repository permissions
```

---

## 📈 Performance Optimization

### Reducing Workflow Duration

```
If workflow takes >15 minutes:

1. Reduce scope:
   - Fewer test files (selective testing)
   - Smaller target directories for Serena
   - Limit package.json size for Context7

2. Parallel execution:
   - Modify workflow to run jobs in parallel
   - Reduce dependencies between jobs

3. Resource allocation:
   - Use faster GitHub-hosted runners (if available)
   - Optimize Python scripts (reduce file I/O)

4. Caching:
   - Cache Python dependencies
   - Cache npm modules (if running real tools)
```

### Reducing KB Size

```
If knowledge-base grows too large:

Configure in KWF-CONFIG.yaml:

performance:
  max_kb_size_mb: 500
  archive_old_reports: true
  archive_after_days: 365

Result:
  - Older reports automatically archived
  - Index remains performant
  - Search remains fast
```

---

## 📚 Additional Resources

### GitHub Documentation
- [GitHub Actions Docs](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [GitHub Copilot Docs](https://docs.github.com/en/copilot)
- [Protected Branches](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository)

### This Project
- [Root README.md](../README.md)
- [Skills Overview](./skills/README.md)
- [KWF Guide](./skills/knowledge-workflow-framework/README.md)
- [Installation Guide](./skills/knowledge-workflow-framework/INSTALLATION_GUIDE.md)
- [Workflow File](./workflows/knowledge-integration.yml)

---

## 🎯 Quick Reference

### Workflow Timings (Configurable)

```yaml
.github/workflows/knowledge-integration.yml:
  schedule:
    - cron: '0 2 * * *'  # 02:00 UTC daily
    # To change:
    # - cron: '0 9 * * *'  # 09:00 UTC (example)
```

### Key Configuration File

```yaml
.github/skills/knowledge-workflow-framework/KWF-CONFIG.yaml
- Update team name and repository URL (mandatory)
- Enable/disable skills (optional)
- Adjust schedules, thresholds, categories (optional)
```

### Checking KB Status

```bash
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py stats
# Shows: # of decisions, patterns, lessons, tags, last updated
```

### Manual KB Update

```bash
cd .github/skills/knowledge-workflow-framework
python3 kb-generator.py update-index
# Regenerates search index
```

### Manual Skill Execution

```bash
# Playwright
python3 .github/skills/playwright-integration/playwright_collector.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Serena
python3 .github/skills/serena-integration/serena_analyzer.py \
  --kb-path .github/skills/knowledge-workflow-framework

# Context7
python3 .github/skills/context7-integration/context7_manager.py \
  --kb-path .github/skills/knowledge-workflow-framework
```

---

## 📞 Support

When troubleshooting:

1. **Check logs**: GitHub Actions → Workflow run → Check step outputs
2. **Read guides**: See documentation links above
3. **Verify config**: KWF-CONFIG.yaml settings
4. **Test locally**: Run skills from command line
5. **Ask team**: Use your team's communication channel

---

**Version**: 1.0  
**Status**: ✅ Production Ready  
**Last Updated**: 2026-03-02

For the main project documentation, see [../README.md](../README.md)
