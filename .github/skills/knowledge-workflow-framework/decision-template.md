---
name: decision-TEMPLATE
description: "Decision title here"
date: 2026-03-01
status: PENDING  # Options: PENDING, ACCEPTED, REJECTED, SUPERSEDED, ARCHIVED
decision_makers: []  # @username list of who made this decision
category: architecture  # architecture, tools, database, security, process, performance
tags: []  # e.g., [frontend, testing, api-design]
review_date: 2026-06-01
---

# Decision: [Your Decision Title]

**Date**: 2026-03-01  
**Status**: PENDING  
**Decision Makers**: @your-name, @colleague-name  
**Category**: [architecture|tools|database|security|process|performance]

## 📋 Context

**The Situation**
- Describe the situation that prompted this decision
- What problem are we trying to solve?
- What constraints do we have?

**Example**: 
> Our current testing framework (Cypress) is showing performance issues in CI/CD. Tests 
> that pass locally fail intermittently in our GitHub Actions pipeline. We need a more 
> reliable solution that supports our multi-browser requirements.

**Stakeholders Involved**
- QA Team
- DevOps Team  
- Frontend Team

---

## 🎯 The Decision

**Decision Statement**
Clearly state the decision in 1-2 sentences.

**Example**:
> We will adopt Playwright as our primary E2E testing framework, replacing Cypress.

**Why This Decision?**

### Reasons
1. **Reason 1**: Explanation
2. **Reason 2**: Explanation  
3. **Reason 3**: Explanation

**Example**:
1. **Multi-browser support**: Native support for Chrome, Firefox, Safari, and WebKit
2. **Performance**: 3x faster test execution compared to Cypress
3. **Reliability**: Zero flakiness in our test runs (based on community feedback)
4. **Modern tooling**: Better TypeScript support and active maintenance

### Key Metrics / Success Criteria
- Metric 1: X should improve by Y%
- Metric 2: Z should be resolved

**Example**:
- Test suite completion time should drop from 15 mins to 5 mins
- Zero intermittent test failures in CI/CD (vs. current 5-10 per run)
- Team able to write tests with proficiency within 1 week

---

## ⚖️ Consequences

### Positive Consequences (✅)
- Benefit 1: Details
- Benefit 2: Details
- Benefit 3: Details

**Example**:
- Faster feedback loop for developers (5 min vs 15 min)
- Better user experience testing (mobile emulation included)
- Reduced time spent debugging flaky tests

### Negative Consequences / Tradeoffs (⚠️)
- Tradeoff 1: Details and mitigation
- Tradeoff 2: Details and mitigation

**Example**:
- Team learning curve: ~2-3 days of training
  - *Mitigation*: Schedule internal workshop, pair programming
  
- CI/CD pipeline size increase: +200MB for browser binaries
  - *Mitigation*: Cache Docker layer, use browser package optimization

### Resource Impact
- **Time to implement**: X days/weeks
- **Training required**: X days
- **Ongoing maintenance**: X hours per month

**Example**:
- **Time to implement**: 1 week (setup + migration)
- **Training required**: 2-3 days (workshop + practice)
- **Ongoing maintenance**: 1-2 hours/month (dependency updates)

---

## 🔄 Alternatives Considered

### Alternative 1: [Name]
**Pros**:
- Pro 1
- Pro 2

**Cons**:
- Con 1
- Con 2

**Why not chosen**: Brief explanation

---

### Alternative 2: [Name]
**Pros**:
- Pro 1
- Pro 2

**Cons**:
- Con 1
- Con 2

**Why not chosen**: Brief explanation

---

## 📊 Impact Analysis

### Team Impact
- Skill impact: Required skills are [...]
- Workload impact: Estimated [X hours] to adopt
- Hiring impact: Do we need to hire specialists?

### Technical Debt
- Will this reduce: [Yes/No] - explain
- Will this increase: [Yes/No] - explain

### Dependency Impact
- New dependencies: [List]
- Removed dependencies: [List]
- License implications: [Summary]

### Cost Impact
- One-time costs: [List with amounts]
- Recurring costs: [List with monthly/yearly amounts]

---

## 🔗 Related Items

### Related Decisions
- [decision-001] - Previous related decision
- [decision-015] - Complementary decision

### Related Patterns
- [pattern-010] - Playwright Best Practices
- [pattern-089] - Testing Best Practices

### Related Lessons
- [incident-002] - Similar issue that prompted this decision

---

## ✅ Follow-up Actions

**Implementation Tasks**
- [ ] Task 1: Description (Owner: @name, Due: Date)
- [ ] Task 2: Description (Owner: @name, Due: Date)
- [ ] Task 3: Description (Owner: @name, Due: Date)

**Learning & Documentation**
- [ ] Create internal documentation
- [ ] Record decision-making rationale
- [ ] Document any gotchas discovered

**Training & Rollout**
- [ ] Plan training session
- [ ] Conduct workshop
- [ ] Pair program first implementations

**Metrics & Monitoring**
- [ ] Set up metrics collection
- [ ] Create monitoring dashboard
- [ ] Schedule review points

---

## 📅 Review & Approval

### Initial Review
- **Proposed by**: @name (Date)
- **Technical review**: @reviewer (Date) - ✅ Approved / ⏳ Pending
- **Team review**: @team-lead (Date) - ✅ Approved / ⏳ Pending
- **Stakeholder feedback**: [Document any feedback]

### Status Changes
- [ ] Proposed (2026-03-01)
- [ ] Under Review (2026-03-05)
- [ ] Accepted (2026-03-08)
- [ ] Implemented (2026-03-15)
- [ ] Next Review: 2026-06-01

---

## 📝 Notes

**Discussion Summary**
- Summary of key discussion points
- Consensus reached
- Any dissent and why

**Assumptions**
- Assumption 1: [State clearly]
- Assumption 2: [State clearly]

**Open Questions**
- Question 1: [State and note answer when found]
- Question 2: [State and note answer when found]

---

## 📚 References & Resources

- [Reference 1 - URL](https://example.com)
- [Reference 2 - URL](https://example.com)
- [Internal Doc - Path](.github/docs/testing-guidelines.md)

---

## 🔄 Next Review

**Review Date**: 2026-06-01  
**Review Criteria**:
- Criterion 1: [metric/evidence]
- Criterion 2: [metric/evidence]
- Criterion 3: [metric/evidence]

**Possible Outcomes**:
- ✅ **Continue**: Evidence shows success
- 🔄 **Revise**: Some adjustments needed
- ❌ **Revert**: Decision wasn't effective, switch to alternative

---

**Document Version**: 1.0  
**Last Updated**: 2026-03-01  
**Template Version**: 1.0

---

## 💡 Tips for Writing Good Decisions

✅ **DO**:
- Document BEFORE implementation
- Explain context clearly (not obvious to new team members)
- Include alternatives (shows due diligence)
- Be specific about consequences and timelines
- Set a review date
- Update decision if context changes

❌ **DON'T**:
- Record trivial decisions (variable naming, code style)
- Forget to explain WHY (not just what)
- Leave decisions in PENDING forever
- Ignore dissenting opinions
- Skip metrics/success criteria
