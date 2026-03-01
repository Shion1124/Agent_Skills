---
name: knowledge-workflow-framework
description: |
  Unified knowledge management + development workflow methodology.
  Establishes team's "Way of Working" through recorded best practices,
  decision trees, and reusable patterns. Integrates with all other skills.
  Enables continuous improvement through automated knowledge capture,
  indexing, and enforcement.
version: 1.0
authors: 
  - Team Knowledge Manager
tags:
  - knowledge-management
  - workflow
  - methodology
  - framework
  - team-standardization
---

# Knowledge & Workflow Framework (KWF)

## 🎯 Purpose

The Knowledge & Workflow Framework is a **meta-skill** that:
- **Captures** everything learned during development (decisions, patterns, lessons)
- **Organizes** knowledge in a searchable, team-accessible way
- **Enforces** best practices across development workflows
- **Improves** iteratively based on feedback and metrics

Think of it as a **"Living Playbook"** that grows smarter every sprint.

---

## 📚 Architecture: 4 Phases

### Phase 1: Knowledge Capture

During development, document key artifacts:

#### A. **Decision Log (Architecture Decision Records)**

Every non-trivial decision is recorded:

```markdown
# Decision: Playwright over Cypress for E2E Testing

**Date**: 2026-02-15  
**Status**: ACCEPTED  
**Decision Makers**: @alice, @bob  

## Context
- Project needs cross-browser E2E testing
- Team has JS knowledge but no Cypress experience
- Performance and maintainability are critical

## Decision
Use Playwright instead of Cypress because:
1. Better multi-browser support (Chrome, Firefox, Safari, WebKit)
2. Faster execution (~3x faster than Cypress)
3. Native support for mobile emulation
4. Active development with modern TypeScript support

## Consequences
- Learning curve for team (~2-3 days)
- Need to install Playwright browsers on CI (adds ~200MB)
- Benefits: stable, maintainable tests that run faster

## Alternatives Considered
- Cypress: Good DX but slower, Chrome-only
- Selenium: Too verbose for modern web apps
- Puppeteer: Headless only, harder to debug

## Follow-up
- [Task-45] Train team on Playwright best practices
- [Decision-182] Review decision after 2 sprints
```

**Stored in**: `knowledge-base/decisions/<category>/<decision-id>.md`

#### B. **Pattern Library (Reusable Solutions)**

Common patterns documented with code examples:

```markdown
# Pattern: Secure API Client with Token Refresh

**Category**: API Design  
**Complexity**: Intermediate  
**Last Updated**: 2026-02-20  
**Author**: @carol  

## Problem
API clients need to:
- Handle authentication tokens
- Auto-refresh expired tokens
- Retry failed requests
- Log all requests for debugging

## Solution

### TypeScript Implementation
\`\`\`typescript
class APIClient {
  private token: string = '';
  private refreshPromise: Promise<string> | null = null;

  async request(endpoint: string, options = {}) {
    try {
      return await this.fetchWithToken(endpoint, options);
    } catch (error) {
      if (error.status === 401) {
        await this.refreshToken();
        return this.fetchWithToken(endpoint, options); // Retry
      }
      throw error;
    }
  }

  private async fetchWithToken(endpoint: string, options: any) {
    const headers = {
      ...options.headers,
      'Authorization': `Bearer ${this.token}`
    };
    
    console.log(`[API] ${options.method || 'GET'} ${endpoint}`);
    const response = await fetch(endpoint, { ...options, headers });
    
    if (!response.ok) {
      throw { status: response.status, message: response.statusText };
    }
    return response.json();
  }

  private async refreshToken() {
    // Prevent multiple simultaneous refresh attempts
    if (this.refreshPromise) return this.refreshPromise;
    
    this.refreshPromise = (async () => {
      const response = await fetch('/auth/refresh', {
        method: 'POST',
        credentials: 'include'
      });
      const { token } = await response.json();
      this.token = token;
      console.log('[AUTH] Token refreshed');
      return token;
    })();

    return this.refreshPromise;
  }
}
\`\`\`

## When to Use
- Any client that calls APIs with token-based auth
- When tokens can expire during long user sessions
- When you need reliable request logging

## When NOT to Use
- Simple read-only API calls (use simpler approach)
- Permanent credentials (API keys don't expire)

## Related Patterns
- [Pattern-12] Error Handling Strategy
- [Pattern-45] Logging Best Practices
```

**Stored in**: `knowledge-base/patterns/<category>/<pattern-id>.md`

#### C. **Lessons Learned (Post-Mortem & Retrospectives)**

After incidents or sprints, capture learnings:

```markdown
# Lesson: Database Connection Pool Exhaustion (Incident #47)

**Date**: 2026-02-10  
**Severity**: Critical (30 min downtime)  
**Root Cause**: Unclosed database connections in error handler  
**Assignee**: @dave  

## What Happened
Production API started returning "ECONNREFUSED" errors. All DB queries failed.
Customers couldn't log in for ~30 minutes.

## Root Cause Analysis
Engineers discovered that when a query timeout occurred, the connection wasn't
returned to the pool. After ~500 timeout errors, pool exhausted.

```python
# ❌ BAD - Unclosed connection on error
async def query_user(id):
    conn = await db.getConnection()
    try:
        return await conn.query("SELECT * FROM users WHERE id = ?", [id])
    except TimeoutError:
        return None  # Connection leaked!
```

## Fix Applied
```python
# ✅ GOOD - Always close connection
async def query_user(id):
    conn = await db.getConnection()
    try:
        return await conn.query("SELECT * FROM users WHERE id = ?", [id])
    except TimeoutError:
        return None
    finally:
        await conn.release()  # Always release
```

Better yet, use context manager:
```python
# ✅ BEST - Automatic resource management
async def query_user(id):
    async with db.getConnection() as conn:
        try:
            return await conn.query("SELECT * FROM users WHERE id = ?", [id])
        except TimeoutError:
            return None  # Connection auto-released
```

## Prevention Checklist
- [ ] All DB operations use context managers (with/async with)
- [ ] Connection pool monitoring enabled in production
- [ ] Alerts set for connection pool usage > 80%
- [ ] Code review checklist includes "resource cleanup"
- [ ] New team members trained on this pattern

## Related Learning
- Added to Pattern Library: [Pattern-89] "Resource Cleanup in Async Code"
- Updated code review checklist (item #12)
- Added monitoring dashboard for DB connections
```

**Stored in**: `knowledge-base/lessons/<year>/<incident-or-sprint>.md`

---

### Phase 2: Knowledge Indexing

Automated knowledge base generation and searchability:

#### Index Structure

```
knowledge-base/
├── decisions/
│   ├── architecture/
│   │   ├── decision-001-playwright-vs-cypress.md
│   │   ├── decision-002-microservices-vs-monolith.md
│   │   └── decision-index.json
│   ├── tools/
│   │   ├── decision-010-nextjs-vs-remix.md
│   │   └── decision-index.json
│   └── DECISIONS-README.md
│
├── patterns/
│   ├── api-design/
│   │   ├── pattern-001-secure-api-client.md
│   │   ├── pattern-002-pagination-strategy.md
│   │   └── pattern-index.json
│   ├── testing/
│   │   ├── pattern-010-playwright-best-practices.md
│   │   ├── pattern-011-test-data-factory.md
│   │   └── pattern-index.json
│   ├── database/
│   │   ├── pattern-020-query-optimization.md
│   │   └── pattern-index.json
│   └── PATTERNS-README.md
│
├── lessons/
│   ├── 2025/
│   │   ├── incident-001-db-connection-exhaustion.md
│   │   ├── retro-q4-2025.md
│   │   └── lessons-index.json
│   ├── 2026/
│   │   └── lessons-index.json
│   └── LESSONS-README.md
│
├── knowledge-index.json (master searchable index)
├── KWF-CONFIG.yaml (framework configuration)
└── README.md
```

#### Master Index Example

```json
{
  "knowledge_base_version": "1.0",
  "last_updated": "2026-03-01T10:30:00Z",
  "entries": [
    {
      "id": "decision-001",
      "type": "decision",
      "title": "Playwright over Cypress",
      "category": "architecture",
      "status": "accepted",
      "date": "2026-02-15",
      "tags": ["testing", "e2e", "frontend"],
      "related_patterns": ["pattern-010"],
      "related_lessons": [],
      "path": "decisions/architecture/decision-001.md",
      "search_content": "playwright cypress e2e testing cross-browser..."
    },
    {
      "id": "pattern-010",
      "type": "pattern",
      "title": "Playwright Best Practices",
      "category": "testing",
      "complexity": "beginner",
      "date_added": "2026-02-16",
      "last_updated": "2026-02-28",
      "tags": ["testing", "e2e", "playwright", "quality"],
      "related_decisions": ["decision-001"],
      "related_lessons": [],
      "path": "patterns/testing/pattern-010.md",
      "examples_count": 4,
      "search_content": "playwright locators waits..."
    },
    {
      "id": "incident-001",
      "type": "lesson",
      "title": "Database Connection Pool Exhaustion",
      "category": "operations",
      "severity": "critical",
      "date": "2026-02-10",
      "resolved_date": "2026-02-10",
      "tags": ["database", "operations", "resource-management"],
      "related_patterns": ["pattern-089"],
      "prevention_checklist_items": 5,
      "path": "lessons/2026/incident-001.md",
      "search_content": "database connection pool timeout..."
    }
  ],
  "search_tags": [
    "testing", "e2e", "api-design", "database", "security", "operations",
    "performance", "architecture", "frontend", "backend"
  ],
  "total_decisions": 15,
  "total_patterns": 42,
  "total_lessons": 8,
  "stats": {
    "most_referenced": ["pattern-010", "pattern-089"],
    "most_recent": ["incident-001", "pattern-089"],
    "by_category": {
      "testing": 12,
      "api-design": 8,
      "database": 7,
      "operations": 5
    }
  }
}
```

---

### Phase 3: Workflow Enforcement

Copilot automatically references KB when relevant:

#### 3.1 Automatic Context Injection

When Copilot Chat detects a development task, it:

1. **Analyzes** the task (e.g., "Write a test for login flow")
2. **Searches** knowledge-index.json for related entries
3. **Injects** relevant context (decisions, patterns, lessons)
4. **Suggests** best practices from team's KB

#### 3.2 Skill Integration Map

This skill coordinates with others:

```
┌─────────────────────────────────────────┐
│  Knowledge Workflow Framework (THIS)    │
│  (Central Knowledge Hub)                │
└──────────┬──────────────────────────────┘
           │
     ┌─────┴──────────────────┐
     │                        │
     ▼                        ▼
┌──────────────────┐  ┌────────────────────┐
│  When TDD Skill  │  │  When Playwright   │
│  is used:        │  │  Skill is used:    │
│                  │  │                    │
│  Copilot refs:   │  │  Copilot refs:     │
│  - Testing       │  │  - Test patterns   │
│    patterns      │  │  - Related lessons │
│  - Test data     │  │  - Best practices  │
│    factories     │  │  - Performance     │
│  - Related       │  │    considerations  │
│    lessons       │  │                    │
└──────────────────┘  └────────────────────┘
```

#### 3.3 Knowledge-Aware Prompts

When Copilot proposes code, it includes:

```
You (Developer): "Create a login test with Playwright"

Copilot Response:
"Based on your team's decision (decision-001) to use Playwright,
and pattern-010 (Playwright Best Practices), here's the recommended approach:

✓ Use locator()instead of XPath (pattern-010)
✓ Wait for network idle before assertions (pattern-010)
✓ Include trace on failure (pattern-010)

Reference: decision-001, pattern-010

[Generated test code follows...]

Pro tip: Similar test created in [incident-#8]. See 
https://github.com/yourteam/knowledge-base/lessons/2026/incident-008.md
for how we fixed a flaky version."
```

---

### Phase 4: Continuous Improvement Loop

#### 4.1 Feedback Integration

After Copilot proposes code:

```
Developer receives Copilot suggestion
    ↓
Developer uses code (or modifies it)
    ↓
Developer provides feedback (👍 / 👎 / 📝 improve)
    ↓
System records feedback
    ↓
Quarterly review: Update patterns/decisions based on
what worked well vs. what didn't
    ↓
KB evolves with team experience
```

#### 4.2 Metrics Collection

Track knowledge effectiveness:

```json
{
  "kb_metrics": {
    "decision-001": {
      "referenced_count": 47,
      "times_followed": 45,
      "times_deviated": 2,
      "deviation_notes": "mobile-only app needed different tool",
      "usefulness_score": 9.2,
      "last_reviewed": "2026-02-28"
    },
    "pattern-010": {
      "applied_count": 23,
      "times_solved_issue": 18,
      "times_caused_issue": 0,
      "maintenance_effort": "low",
      "last_updated": "2026-02-28"
    }
  }
}
```

#### 4.3 Knowledge Update Trigger

Quarterly sprint review checks:

- [ ] Any decisions that should be revisited?
- [ ] Any new patterns emerged that aren't documented?
- [ ] Any patterns that failed and need replacement?
- [ ] Any lessons not yet added to KB?
- [ ] Should any patterns be deprecated?

---

## 🔧 How to Use This Skill

### For Developers

#### 1. **Search the Knowledge Base**

```
You: "How should we handle API authentication?"

Copilot: Searches knowledge-index.json for "authentication" or "api"
Result: Shows decision-008, pattern-015, and related lessons
```

#### 2. **Record a Decision**

When making an architectural choice:

```
You: "@Copilot record decision: We chose PostgreSQL over MongoDB"

Copilot: Prompts for context and creates decision-YYY.md
Stores: decisions/database/decision-YYY.md
Updates: knowledge-index.json
```

#### 3. **Add a Pattern**

When you've solved something reusable:

```
You: "@Copilot add pattern: Error handling in async functions"

Copilot: Guides you through pattern template
Creates: patterns/error-handling/pattern-ZZZ.md
References: Related decisions, similar patterns
```

#### 4. **File a Lesson**

After an incident or debugging session:

```
You: "@Copilot lesson learned: N+1 query bug took 3 hours to find"

Copilot: Creates lessons/2026/incident-XXX.md
Adds: Root cause analysis, fix, prevention checklist
Suggests: Related pattern updates
```

---

## 📊 Integration with Other Skills

This skill acts as the "brain" that other skills reference:

### When using `playwright-testing` skill:
- Receives: "Write an E2E test for registration"
- Copilot checks: Does KB have related decision/pattern?
- Output: Test code follows team's Playwright patterns + decision rationale

### When using `agentops-tracing` skill:
- AgentOps logs which KB items were referenced
- Metrics show: "Pattern-010 saved 2 hours of debugging this sprint"
- Metrics logged to: `knowledge-base/metrics/agentops-integration.json`

### When using `llmops-validation` skill:
- Code generated with KB context is evaluated
- Results: "Following pattern-010 resulted in 0 test flakes (vs. 3 before)"
- Feedback updates pattern's effectiveness score

---

## 🛠️ Setup Instructions

### Prerequisites
- GitHub repository with Copilot enabled
- `.github/skills/` or `.claude/skills/` directory
- Python 3.8+ (for knowledge base generation)

### Step 1: Create Directory Structure

```bash
mkdir -p .github/skills/knowledge-workflow-framework
cd .github/skills/knowledge-workflow-framework

# Create subdirectories
mkdir -p knowledge-base/{decisions,patterns,lessons}/{2026,2025}
```

### Step 2: Copy Core Files

```
.github/skills/knowledge-workflow-framework/
├── SKILL.md (this file)
├── kb-generator.py
├── KWF-CONFIG.yaml
├── knowledge-base/
│   ├── decisions/
│   ├── patterns/
│   ├── lessons/
│   ├── knowledge-index.json (generated)
│   └── README.md
└── README.md
```

### Step 3: Initialize Knowledge Base

```bash
python kb-generator.py init
# Creates: knowledge-index.json, sample decisions/patterns/lessons
```

### Step 4: Configure for Your Team

Edit `KWF-CONFIG.yaml`:

```yaml
team_name: "Your Team"
repository_url: "https://github.com/yourorg/yourrepo"
kb_location: ".github/skills/knowledge-workflow-framework/knowledge-base"
decision_categories:
  - architecture
  - tools
  - database
  - security
pattern_categories:
  - api-design
  - testing
  - database
  - security
  - performance
indexed_fields:
  - title
  - description
  - tags
  - category
auto_generate_index: true
index_update_interval: "hourly"
```

### Step 5: Use in Copilot Chat

In VS Code with Copilot:

```
@copilot How should we structure our API error responses?

Copilot: [Searches KB]
Found relevant decision and 2 patterns. Applying team standards...
```

---

## 📖 Commands Reference

When chatting with Copilot:

| Command | Purpose |
|---------|---------|
| `@record decision: <title>` | Create new ADR (Architecture Decision Record) |
| `@add pattern: <name>` | Document a reusable solution |
| `@lesson: <title>` | Record post-mortem or retrospective learning |
| `@search: <query>` | Search knowledge base |
| `@show stats` | KB statistics and most-used items |
| `@update index` | Regenerate knowledge-index.json |
| `@kb health check` | Validate KB structure and completeness |

---

## 🎓 Best Practices

### For Recording Decisions

✅ **DO**:
- Document BEFORE implementation (not after)
- Include alternatives considered
- Note date and decision makers
- Link to related patterns/decisions
- Set review date (quarterly at minimum)

❌ **DON'T**:
- Record trivial decisions (variable naming)
- Forget to explain context
- Leave decisions "PENDING" forever
- Disconnect from implementation

### For Recording Patterns

✅ **DO**:
- Include working code examples (at least 2)
- Explain when to use and when NOT to use
- Reference related patterns
- Keep examples short and clear
- Update when team learns something new

❌ **DON'T**:
- Document only abstract concepts (include code!)
- Create patterns for one-off solutions
- Forget edge cases
- Use outdated libraries

### For Recording Lessons

✅ **DO**:
- Conduct thorough root cause analysis
- Create actionable prevention checklist
- Reference related patterns to update
- Share blameless post-mortems
- Update related patterns afterward

❌ **DON'T**:
- Blame individuals (focus on systems)
- Leave lessons incomplete
- Duplicate incident records
- Ignore follow-ups

---

## 📈 Expected Benefits Timeline

| Period | Impact |
|--------|--------|
| **Week 1-2** | Team members learn framework, document existing knowledge |
| **Week 3-4** | Patterns and decisions catch up to current practices |
| **Month 2** | New code starts referencing KB; fewer "how did we do this?" questions |
| **Month 3** | First incident prevented by existing lesson; productivity +10-15% |
| **Quarter 2** | Onboarding 40% faster for new team members |
| **Quarter 3** | Major decision makes reference 20+ patterns; quality improves noticeably |

---

## 🔄 Maintenance

### Monthly
- Review new entries for consistency
- Update metrics dashboard
- Fix broken cross-references

### Quarterly
- Full KB health check
- Archive outdated patterns/decisions
- Team retrospective on KB effectiveness

### Yearly
- Major KB reorganization if needed
- Merge similar patterns
- Celebrate learnings

---

## 🚀 Integration with CI/CD

Add to your GitHub Actions workflow:

```yaml
name: Knowledge Base Validation

on: [pull_request]

jobs:
  kb-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Validate Knowledge Base
        run: |
          python .github/skills/knowledge-workflow-framework/kb-generator.py validate
      
      - name: Update Index
        run: |
          python .github/skills/knowledge-workflow-framework/kb-generator.py update-index
      
      - name: Check for Orphaned Entries
        run: |
          python .github/skills/knowledge-workflow-framework/kb-generator.py orphan-check
```

---

## 📚 Related Skills

This skill enhances:
- `playwright-testing` - references testing patterns
- `agentops-tracing` - logs KB references and impact
- `llmops-validation` - evaluates code quality vs. patterns
- `tdd-workflow` - uses test patterns and lessons
- `devsecops-pipeline` - references security decisions/patterns

---

## ✅ Checklist: Ready to Use

Before committing to your repo:

- [ ] `SKILL.md` in place
- [ ] `kb-generator.py` tested
- [ ] `KWF-CONFIG.yaml` customized for your team
- [ ] Sample decisions/patterns/lessons added
- [ ] `knowledge-index.json` generated
- [ ] Team members trained on commands
- [ ] GitHub Actions workflow updated
- [ ] First decision/pattern recorded

---

## 📞 Support & Questions

For issues or improvements:
1. Check `knowledge-base/README.md`
2. Search existing decisions for similar scenarios
3. Reference pattern library for how-tos
4. File lesson learned if stuck for 30+ minutes

---

**Version**: 1.0  
**Last Updated**: 2026-03-01  
**Status**: ACTIVE  
**Next Review**: 2026-06-01
