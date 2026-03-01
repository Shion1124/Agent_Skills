# Knowledge Workflow Framework (KWF)

> A unified system for capturing, organizing, and enforcing development best practices across your team.

**Status**: ✅ Production Ready  
**Version**: 1.0  
**Last Updated**: 2026-03-01

---

## 📚 What Is This?

The Knowledge Workflow Framework is a **meta-skill** that turns your team's collective experience into an organizational asset. It:

1. **Captures** decisions, patterns, and lessons learned
2. **Organizes** them in a searchable, interconnected knowledge base
3. **Enforces** best practices through GitHub Copilot integration
4. **Improves** continuously as your team learns

Think of it as a **"Living Playbook"** that makes your team smarter with every sprint.

### The Problem It Solves

> 🤔 "How did we decide to use Playwright instead of Cypress?"  
> 🤔 "What's the pattern for handling async errors?"  
> 🤔 "Didn't we learn something like this before?"

Without KWF: Knowledge lives in peoples' heads or scattered emails.  
With KWF: Knowledge is organized, searchable, and automatically applied.

---

## 🚀 Quick Start (5 minutes)

### Step 1: Copy This Skill to Your Repository

```bash
# Clone your repo
cd your-project-repo

# Create skills directory
mkdir -p .github/skills/

# Copy KWF
cp -r knowledge-workflow-framework .github/skills/
```

### Step 2: Initialize the Knowledge Base

```bash
cd .github/skills/knowledge-workflow-framework

# Initialize (creates directories and sample files)
python3 kb-generator.py init

# Generate index
python3 kb-generator.py update-index

# Check health
python3 kb-generator.py validate
```

Expected output:
```
📚 Initializing Knowledge Base...
  ✓ Created ./knowledge-base/decisions
  ✓ Created ./knowledge-base/patterns
  ✓ Created ./knowledge-base/lessons/2025
  ✓ Created ./knowledge-base/lessons/2026
  ✓ Created sample decision
  ✓ Created sample pattern

✅ Knowledge Base initialized!
```

### Step 3: Customize for Your Team

Edit `KWF-CONFIG.yaml`:

```yaml
team:
  name: "Your Team Name"
  repository_url: "https://github.com/yourorg/yourrepo"

decision_categories:
  # Keep or modify based on your needs
  architecture:
  tools:
  database:
  security:
  process:
  performance:

pattern_categories:
  # Same here - customize
  api-design:
  testing:
  database:
  # ... etc
```

### Step 4: Commit and Use!

```bash
# Commit KWF to your repo
git add .github/skills/knowledge-workflow-framework/
git commit -m "Add Knowledge Workflow Framework"
git push

# Now use in Copilot Chat (in VS Code):
# @copilot how should we handle async errors in this codebase?
# Copilot will automatically reference your KB!
```

---

## 📁 Directory Structure

```
.github/skills/knowledge-workflow-framework/
│
├── SKILL.md                          # Main skill documentation
├── README.md                         # This file
├── kb-generator.py                   # Knowledge base management tool
├── KWF-CONFIG.yaml                   # Team configuration
│
├── decision-template.md              # Template for recording decisions
├── pattern-template.md               # Template for recording patterns
├── lesson-template.md                # Template for recording lessons
│
└── knowledge-base/
    ├── README.md
    ├── knowledge-index.json          # Generated searchable index
    │
    ├── decisions/
    │   ├── architecture/
    │   ├── tools/
    │   ├── database/
    │   ├── security/
    │   ├── process/
    │   └── performance/
    │
    ├── patterns/
    │   ├── api-design/
    │   ├── testing/
    │   ├── database/
    │   ├── security/
    │   ├── performance/
    │   ├── frontend/
    │   ├── backend/
    │   └── devops/
    │
    └── lessons/
        ├── 2025/
        └── 2026/
```

---

## 💻 How to Use

### Use Case 1: Record a Decision

When your team makes an architectural choice:

```
You (in VS Code Copilot Chat):
"@copilot record decision: We'll use Next.js instead of Create React App"

Copilot:
"I'll help you record this decision. Here are the key questions:
1. What's the context/problem?
2. What are the consequences?
3. What alternatives did you consider?

[Creates decision-YYYY.md from decision-template.md]
[Updates knowledge-index.json]"
```

Created file: `knowledge-base/decisions/framework/decision-NNN.md`

### Use Case 2: Document a Pattern

When you've solved something reusable:

```
You: "@copilot add pattern: Error handling in TypeScript async code"

Copilot:
[Guides through pattern template]
[Creates knowledge-base/patterns/error-handling/pattern-NNN.md]
[Links to related patterns and decisions]
```

### Use Case 3: Learn from Incidents

After debugging or an incident:

```
You: "@copilot lesson: Database connection pool exhaustion - took 30 min to debug"

Copilot:
[Guides through lesson template]
[Creates knowledge-base/lessons/2026/incident-NNN.md]
[Suggests: Update related patterns, add to checklists]
```

### Use Case 4: Search the Knowledge Base

```
You: "@copilot search: How should we handle API authentication?"

Copilot:
[Searches knowledge-index.json]
Found 3 related items:
- decision-012: Authentication Strategy
- pattern-045: Secure API Client
- incident-008: Authentication Bypass (Lesson Learned)

[Shows relevant excerpts and guidance]
```

---

## 🎯 Key Concepts

### Decisions (Architecture Decision Records - ADRs)

**What**: Important technical choices with rationale  
**When**: Before/during implementation  
**Examples**:
- "Use Playwright for E2E testing"
- "Adopt microservices architecture"
- "Migrate from PostgreSQL to MongoDB"

**File**: `knowledge-base/decisions/<category>/<decision-id>.md`

**Template**: See `decision-template.md`

### Patterns (Reusable Solutions)

**What**: Tested solutions to common problems  
**When**: After you've solved something worth repeating  
**Examples**:
- "Secure API Client with Token Refresh"
- "Error Handling in Async Code"
- "React Component Composition"

**File**: `knowledge-base/patterns/<category>/<pattern-id>.md`

**Template**: See `pattern-template.md`

### Lessons (Post-Mortems & Retrospectives)

**What**: Learning from incidents, bugs, or design flaws  
**When**: After resolving issues or sprints  
**Examples**:
- "Database Connection Pool Exhaustion"
- "N+1 Query Bug Cost 2 Hours to Debug"
- "Forgot to Escape User Input - XSS Vulnerability"

**File**: `knowledge-base/lessons/<year>/<incident-id>.md`

**Template**: See `lesson-template.md`

---

## 🔍 Searching the Knowledge Base

### Via CLI

```bash
# Search the knowledge base
python3 kb-generator.py search "authentication"

# Output:
# 🔎 Searching for: 'authentication'
#
#   Found 8 results:
#
#   [DECISION] Authentication Strategy Decision
#     Path: decisions/security/decision-012.md
#     Tags: security, api-design, oauth
#
#   [PATTERN] Secure API Client with JWT
#     Path: patterns/api-design/pattern-045.md
#     Tags: security, authentication, api
#
#   ... etc
```

### Via Copilot Chat

```
You: "@copilot How do we handle user authentication?"

Copilot: 
[Automatically searches KB]
"Based on your team's decision (decision-012) and 
pattern library (pattern-045), here's the recommended approach:

✓ Use OAuth2 with JWT tokens (decision-012)
✓ Implement token refresh mechanism (pattern-045)
✓ Store tokens securely (pattern-089)

Code example follows..."
```

---

## 📊 KB Management Commands

```bash
# Initialize (creates structure)
python3 kb-generator.py init

# Update index (after adding entries)
python3 kb-generator.py update-index

# Validate (check for issues)
python3 kb-generator.py validate

# Show stats
python3 kb-generator.py stats

# Search
python3 kb-generator.py search "query"
```

---

## 🔗 Integration with Other Skills

KWF works with (and enhances) your other skills:

### TDD Workflow Skill
```
Developer: "Write tests for login"
Copilot: [References KWF patterns for test structure]
Output: Tests follow team's proven patterns
```

### Playwright Testing Skill
```
Developer: "Create E2E test"
Copilot: [Checks decision-001 "Playwright vs Cypress"]
         [Applies pattern-010 "Playwright Best Practices"]
Output: Test code includes team standards
```

### AgentOps Integration
```
AgentOps logs which KB items were referenced
Dashboard shows: "Pattern-45 saved 3 hours this sprint"
Feedback → KB metrics updated → Continuous improvement
```

### LLMOps Validation Skill
```
Validator: "Check if code follows team patterns"
Check: Compare generated code to pattern library
Result: "✅ Follows 8/8 patterns (Security: 9/10)"
```

---

## 📈 Expected Timeline to Value

| Period | What Happens |
|--------|-------------|
| **Week 1** | Team adds current knowledge to KB |
| **Week 2-3** | Patterns/decisions align with current practices |
| **Week 4** | New team members have playbook; fewer "how do we do X?" questions |
| **Month 2** | First decision prevents a mistake; productivity +5-10% |
| **Month 3** | Incident prevention checklist saves debugging time |
| **Quarter 2** | Onboarding 30-40% faster |
| **Quarter 3** | Design quality notably improves |

---

## ✅ Best Practices

### For Recording Decisions

✅ **DO**:
- Record BEFORE implementation (not after)
- Explain the context clearly
- Include alternatives considered
- Set a review date (quarterly minimum)
- Link to related patterns/decisions

❌ **DON'T**:
- Record trivial decisions (variable naming)
- Forget to explain context
- Leave decisions PENDING forever
- Skip alternatives
- Ignore team consensus

### For Recording Patterns

✅ **DO**:
- Include working code examples (at least 2)
- Explain WHEN to use and WHEN NOT to use
- Reference related patterns
- Keep examples concise and clear
- Update when team learns something new

❌ **DON'T**:
- Document only abstract concepts
- Create patterns for one-off solutions
- Forget edge cases
- Use outdated libraries
- Leave incomplete implementations

### For Recording Lessons

✅ **DO**:
- Do thorough root cause analysis
- Create actionable prevention checklist
- Reference related patterns to update
- Share blameless post-mortems
- Update patterns afterward

❌ **DON'T**:
- Blame individuals (focus on systems)
- Leave incomplete lessons
- Duplicate incident records
- Ignore follow-ups
- Forget to prevent repeats

---

## 🛠️ Troubleshooting

### Issue: "Python script not found"
```bash
# Make sure you're in the right directory
cd .github/skills/knowledge-workflow-framework/

# Check Python is installed
python3 --version

# Run with full path
python3 ./kb-generator.py init
```

### Issue: "Index not updating"
```bash
# Manually regenerate
python3 kb-generator.py update-index

# Check if it worked
ls -la knowledge-base/knowledge-index.json

# View index
cat knowledge-base/knowledge-index.json | head -20
```

### Issue: "Copilot doesn't reference KB"
```
1. Make sure skill is in .github/skills/ directory
2. Commit changes to git
3. Reload VS Code
4. Use @-mention: "@copilot how should we..."
5. Check that knowledge-index.json exists and has content
```

### Issue: "Search returns no results"
```bash
# Verify entries exist
find knowledge-base -name "*.md" | grep -v example

# Regenerate index
python3 kb-generator.py update-index

# Try search again
python3 kb-generator.py search "query"
```

---

## 📚 File Reference

### Core Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Complete skill documentation |
| `kb-generator.py` | Knowledge base tool (init, index, search, validate) |
| `KWF-CONFIG.yaml` | Team configuration (categories, integrations, etc.) |

### Templates

| File | Purpose |
|------|---------|
| `decision-template.md` | Copy this when recording decisions |
| `pattern-template.md` | Copy this when documenting patterns |
| `lesson-template.md` | Copy this when recording incidents/lessons |

---

## 🔧 Customization

### Change Categories

Edit `KWF-CONFIG.yaml`:

```yaml
decision_categories:
  your_category_1:
    description: "Description"
  your_category_2:
    description: "Description"
```

Then regenerate index:
```bash
python3 kb-generator.py update-index
```

### Add Custom Fields

Edit `KWF-CONFIG.yaml`:

```yaml
custom_fields:
  decision:
    - name: "business_impact"
      type: "text"
      required: false
```

### Enable Slack Notifications

Edit `KWF-CONFIG.yaml`:

```yaml
integrations:
  slack:
    enabled: true
    webhook_url: "https://hooks.slack.com/..."
    notify_on_new_decision: true
```

---

## 📞 Getting Help

1. **Check SKILL.md** for detailed documentation
2. **Check templates** for examples of how to structure entries
3. **Search KB** for similar issues (once populated)
4. **Check GitHub Issues** in your repo
5. **Ask Copilot**: "@copilot how do I add a pattern?"

---

## 🚀 Next Steps

1. ✅ Copy skill to your repo
2. ✅ Run `kb-generator.py init`
3. ✅ Customize `KWF-CONFIG.yaml`
4. ✅ Add first decision/pattern/lesson
5. ✅ Commit to repository
6. ✅ Use in Copilot Chat
7. 📅 Monthly: Review and update KB entries
8. 📅 Quarterly: Full KB review and metrics

---

## 💡 Pro Tips

### Tip 1: Start with Existing Knowledge
Don't wait for perfect. Capture what your team already knows.

### Tip 2: Iterate on Templates
Templates are starting points, not iron rules. Adapt for your team.

### Tip 3: Link Everything
Cross-reference decisions, patterns, and lessons. The network is valuable.

### Tip 4: Make It Searchable
Use consistent tags. They make discovery easy.

### Tip 5: Review Quarterly
Set calendar reminders to review and refresh KB entries.

---

## 📊 Metrics to Track

After 3 months, measure:

- **KB size**: # of decisions, patterns, lessons
- **Usage**: How many times did Copilot reference KB?
- **Impact**: Time saved, bugs prevented
- **Adoption**: % of team using KB features
- **Quality**: Team satisfaction with KB content

---

## 🔄 Maintenance Checklist

### Weekly
- [ ] Review new entries for consistency
- [ ] Fix broken links
- [ ] Answer KB-related questions in Slack

### Monthly
- [ ] Regenerate index: `python3 kb-generator.py update-index`
- [ ] Validate: `python3 kb-generator.py validate`
- [ ] Archive outdated lessons
- [ ] Update pattern metrics

### Quarterly
- [ ] Full KB health check
- [ ] Review decision effectiveness
- [ ] Team retrospective on KB
- [ ] Update metrics dashboard

### Yearly
- [ ] Major reorganization if needed
- [ ] Consolidate similar entries
- [ ] Plan next year's improvements

---

## 📖 Further Reading

- **SKILL.md** - Complete technical documentation
- **decision-template.md** - How to record architecture decisions
- **pattern-template.md** - How to document reusable solutions
- **KWF-CONFIG.yaml** - Detailed configuration reference

---

## 📝 Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-01 | Initial release |
| 0.9 | 2026-02-15 | Beta testing |
| 0.1 | 2026-01-20 | Concept development |

---

## 📄 License & Contribution

This framework is part of your team's knowledge base. 

- **Ownership**: Your team / organization
- **Access**: GitHub Copilot integration
- **Contribution**: All team members encouraged to add entries

---

## 🎓 Training

### For New Team Members

Have them:
1. Read this README.md (5 min)
2. Browse existing decisions/patterns (10 min)
3. Search for answers before asking (5 min)
4. Add their first pattern after 1 week (15 min)

### For Experienced Team Members

Share:
1. How to structure decisions/patterns
2. Team categories and conventions
3. How to search effectively
4. How to contribute new entries

---

## 🌟 Success Criteria

Your KWF is working well when:

- ✅ New team members find answers without asking
- ✅ Decisions are made with team consensus and rationale
- ✅ Patterns are reused across projects
- ✅ Incidents don't repeat
- ✅ Code quality improves
- ✅ Team feels more aligned

---

**Ready to go!** 🚀

Start with Step 1 from Quick Start above.

Questions? Check SKILL.md or search your growing knowledge base!
