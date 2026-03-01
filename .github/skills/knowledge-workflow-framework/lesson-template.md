---
name: lesson-TEMPLATE
description: "Incident or lesson title"
date: 2026-03-01
incident_type: incident  # incident, retrospective, post-mortem, learning
severity: medium  # critical, high, medium, low
category: operations  # operations, performance, security, development, infrastructure
tags: []  # e.g., [database, connection-pool, resource-management]
status: resolved  # ongoing, resolved, prevention-complete
assignee: your-name
---

# Lesson Learned: [Incident or Learning Title]

**Date Discovered**: 2026-03-01  
**Type**: [incident|retrospective|post-mortem|learning]  
**Severity**: [critical|high|medium|low]  
**Category**: [operations|performance|security|development|infrastructure]  
**Status**: [ongoing|resolved|prevention-complete]  
**Owner**: @your-name

---

## 📋 Summary

**What Happened (TL;DR)**
Write 1-2 sentences summarizing the issue.

**Example**:
> Production database stopped accepting connections for ~30 minutes, causing complete 
> service outage. Root cause: connection pool exhaustion due to unclosed connections in 
> error handling code.

**Impact**
- Duration: X minutes/hours
- Users affected: X thousand
- Revenue impact: $X
- Reputational impact: [Low|Medium|High]

---

## 🕐 Timeline

| Time | Event |
|------|-------|
| 14:35 | Alerts fire: Database connection errors |
| 14:40 | On-call engineer confirms outage |
| 14:45 | Escalation to database team |
| 14:50 | Root cause identified |
| 15:05 | Fix deployed |
| 15:15 | Service fully recovered |
| 15:30 | Incident marked RESOLVED |

**Total Duration**: 40 minutes  
**Detection Time**: 5 minutes  
**Resolution Time**: 35 minutes

---

## 🔍 Incident Details

### Initial Symptoms
- What did users/monitoring see?
- What alerts fired?
- What was the first sign something was wrong?

**Example**:
- Alert: "Database connection pool usage > 95%"
- Error logs: "ECONNREFUSED on database queries"
- Customers: "Can't log in" (via support tickets)

### How It Started
- Root action or event that triggered this
- What conditions had to be in place?
- Was this a one-off or a known risk?

**Example**:
- Deployment of new user authentication feature
- Feature included retry logic with aggressive polling
- When authentication service was slow, retries queued up
- Retries didn't close connections properly on timeout

### Propagation
- How did the problem spread/escalate?
- Why wasn't it contained?

**Example**:
- First request timeout → connection left open
- Second request timeout → another connection left open
- Within 2-3 minutes, pool exhausted
- New requests couldn't get connections
- Cascading failures across all services using that DB
- Load balancer kept routing to failing service

---

## 🎯 Root Cause Analysis

### Direct Cause
What immediately caused the issue?

**Example**:
```python
# ❌ BAD - connection not released on error
async def authenticate_user(user_id):
    conn = await db.getConnection()
    try:
        result = await conn.query("SELECT * FROM users WHERE id = ?", [user_id])
        return result
    except TimeoutError:
        return None
        # Connection is NEVER released! 
```

### Root Cause(s)
Why did the direct cause exist?

**Example**:
1. **Code Review Missed It**: The retry logic was added hastily, code review didn't catch unclosed connection
2. **Testing Gap**: No load testing with slow database responses
3. **Knowledge Gap**: Developer new to async/await patterns wasn't familiar with resource cleanup
4. **Monitoring Gap**: No alerting on connection pool usage > 80%

### Contributing Factors

What circumstances made this worse?

**Example**:
- Authentication service was experiencing high latency (not at fault, but triggered the bug)
- Connection pool size was set to default (50) - could have caught earlier at higher limit
- No connection timeout configured - retries could wait forever
- No circuit breaker - should have failed fast

---

## 🔧 Resolution

### Immediate Fix
What was done to stop the incident?

**Example**:
1. Drained affected service instances
2. Deployed hotfix: Properly close connections in error handler
3. Increased connection pool size temporarily (100)
4. Cleared connection pool
5. Service recovered, traffic re-routed

### Permanent Fix
Code changes and improvements made:

```python
# ✅ FIXED - Connection always released
async def authenticate_user(user_id):
    conn = await db.getConnection()
    try:
        result = await conn.query(
            "SELECT * FROM users WHERE id = ?", 
            [user_id],
            timeout=5000  # Add timeout
        )
        return result
    except TimeoutError:
        return None
    finally:
        await conn.release()  # ALWAYS release
```

### Tests Added
What tests prevent regression?

```typescript
it('should release connection even on timeout', async () => {
  const mockConn = {
    query: jest.fn().mockImplementation(
      () => new Promise((_, reject) => 
        setTimeout(() => reject(new Error('Timeout')), 100)
      )
    ),
    release: jest.fn()
  };
  
  // Should not throw, connection should be released
  await authenticateUser('user1');
  
  // CRITICAL: Verify connection was released
  expect(mockConn.release).toHaveBeenCalled();
});
```

---

## ✅ Prevention Checklist

To prevent this issue from happening again:

### Immediate Actions (done within 24h)
- [ ] Deploy hotfix (connection cleanup)
- [ ] Update monitoring (pool usage alerts)
- [ ] Notify team in incident postmortem
- [ ] Update runbooks with connection pool recovery steps

### Short-term Actions (done within 1 sprint)
- [ ] Add automated tests for error path resource cleanup
- [ ] Add code review checklist item: "All resource cleanup"
- [ ] Document [pattern-089] "Resource Cleanup in Async Code"
- [ ] Training session on async/await best practices
- [ ] Add async code to critical path review requirements

### Long-term Actions (done within 1 quarter)
- [ ] Implement circuit breaker in auth client
- [ ] Add connection pool metrics to observability dashboard
- [ ] Audit all async code for resource leaks
- [ ] Add linting rule to detect unclosed connections
- [ ] Establish "async safety" code review standard

### Monitoring Improvements
- [ ] Alert if connection pool > 80% usage
- [ ] Alert if connection acquire latency > 100ms
- [ ] Dashboard: Real-time connection pool visualization
- [ ] Log all connection timeouts with stack trace

### Process Improvements
- [ ] Add connection pool review to deployment checklist
- [ ] Add "stress test with slow DB" to load testing plan
- [ ] Add "test error paths thoroughly" to definition of done
- [ ] Schedule quarterly async code audit

---

## 📚 Related Knowledge Base Items

### Related Decisions
- [decision-008] "Use connection pooling for database efficiency"
- [decision-015] "Async/await as standard for I/O operations"

### Related Patterns
- [pattern-089] "Resource Cleanup in Async Code" ← **Created from this incident**
- [pattern-012] "Error Handling in Async Code"
- [pattern-045] "Timeout Strategies"

### Similar Incidents
- [incident-005] (2025-11-20) "File handle exhaustion"
  - Same root cause, different resource type
  - Both fixed by [pattern-089]
  
- [incident-023] (2026-01-10) "Memory leak in request handler"
  - Similar "forgot to cleanup" pattern

---

## 📊 Impact Analysis

### Business Impact
- **Revenue Lost**: ~$50k (estimated)
- **Customers Affected**: ~10k (unable to login 40 min)
- **SLA Breach**: Yes (99.95% SLA, was 99.8%)
- **Reputation**: Moderate (mentioned in tech forums)

### Operational Impact
- **Investigation Time**: 3 hours
- **Resolution Time**: 40 minutes
- **Team Fatigue**: 2 engineers pulled from sprint work
- **On-call Stress**: High (weekend incident)

### Learning Gained
- **Knowledge Asset**: [pattern-089] + training
- **Process Improvement**: Better code review + monitoring
- **Cultural**: Increased focus on resource cleanup
- **Technical**: Whole team now understands async patterns better

---

## 🎓 Team Learnings

### What We Learned

**From Engineering**:
> "Always close resources in finally blocks, not catch blocks. Obvious in hindsight, 
> but wasn't common knowledge on our team." - @engineer-1

**From Ops**:
> "We need better visibility into resource pool usage. This could have been 
> prevented with an alert at 80% pool usage." - @ops-lead

**From Product**:
> "A brief service disruption is okay, but communication during incident was slow. 
> We should have posted status page update at 14:40." - @pm

### Skills Improved
- Async/await resource cleanup understanding: Team level 5→8 (1-10 scale)
- Connection pool management: Team level 4→7
- Incident response speed: 45 min → 35 min (for similar issues)

### Cultural Impact
- Increased blameless incident culture
- Better psychological safety in code review
- Shared responsibility for quality

---

## 🔄 Post-Mortem Notes

**Postmortem Held**: 2026-03-02, 10:00 AM  
**Attendees**: Engineering lead, database expert, on-call engineer, product manager

### Key Takeaways
1. Simple mistakes (missing finally) can have big impact
2. Need better tooling/visibility into resource usage
3. Error paths need same test coverage as happy paths
4. New team members need async safety training

### Appreciation
- 👏 @on-call-engineer for quick detection
- 👏 @db-expert for fast root cause analysis
- 👏 @junior-dev for admitting code was theirs (blameless culture!)

### Action Items
- [ ] Create async safety training (Owner: @tech-lead, Due: 2026-03-15)
- [ ] Add pool monitoring (Owner: @ops, Due: 2026-03-10)
- [ ] Code review guidelines update (Owner: @architect, Due: 2026-03-12)

---

## 🛡️ Similar Issues To Watch For

Based on this incident, watch for:

1. **Any resource that needs cleanup**: Database connections, file handles, network sockets, locks
   - Pattern to apply: [pattern-089]
   - Code review focus: Verify finally block

2. **Cascading failures**: One service's exhaustion → impacts others
   - Pattern to apply: [pattern-045] Timeouts + Circuits
   - Monitoring: Add health checks

3. **Silent failures**: Error paths not tested → bugs hidden
   - Pattern to apply: Test both success AND error paths
   - Checklist: "Error path tested" in definition of done

---

## 📈 Metrics

### Before Fix
- Database connection errors: ~500/hour during incident
- Service availability: 99.8%
- Error rate spike: 40x normal

### After Fix
- Database connection errors: <1/hour (normal baseline)
- Service availability: 99.96%
- Error rate: Normal

### Prevention Metrics (3 months)
- [ ] Similar incidents: 0 (goal: prevent entirely)
- [ ] Team async code confidence: 8/10
- [ ] Code review catch rate for resource cleanup: 95%+
- [ ] New async code defects: 0

---

## 🎬 Action Items Summary

| Action | Owner | Due | Status |
|--------|-------|-----|--------|
| Deploy hotfix | @dev-lead | 2026-03-01 | ✅ Done |
| Update monitoring | @ops | 2026-03-10 | ⏳ In progress |
| Create training | @tech-lead | 2026-03-15 | ⏳ Planned |
| Audit all async code | @architect | 2026-03-31 | ⏳ Planned |
| Update code review | @tech-lead | 2026-03-12 | ⏳ Planned |

---

## 💡 Lessons for Future

### What Worked Well
- ✅ Clear alerting caught issue quickly
- ✅ Team communication was good
- ✅ Runbooks existed to resolve (even if they caught late)
- ✅ No data loss occurred

### What Could Be Better
- ⚠️ Monitoring should have caught pool exhaustion earlier
- ⚠️ Load testing didn't include slow database scenarios
- ⚠️ Error paths weren't tested as thoroughly
- ⚠️ New developers didn't get async patterns training

### This Time vs. Last Time
Compared to [incident-005] (file handle exhaustion):
- ✅ Same pattern, caught earlier
- ✅ Better root cause analysis
- ✅ Faster resolution
- ⚠️ Still not prevented (should have caught before production)

---

## 🔗 Knowledge Base Updates

**New entries created from this incident**:
- ✅ [pattern-089] "Resource Cleanup in Async Code"
- ✅ Added to code review checklist: "Resource cleanup verified"
- ✅ Training slides: "Async/await Safety Patterns"

**Updated entries**:
- 📝 [decision-015] "Async/await standards": Added resource cleanup requirement
- 📝 [pattern-012] "Error Handling": Added finally block example

---

## 📝 Notes & Follow-up

### Open Questions (resolved)
- Q: Could this happen with other resource types?  
  A: Yes, file handles and locks. Added to audit.

- Q: Why didn't tests catch this?  
  A: Error paths weren't tested. Now fixed.

- Q: How often should we audit for this?  
  A: Quarterly async code audit added to process.

### Ideas for Future
- Linter rule to detect missing finally on resources?
- Automatic timeout enforcement for all DB queries?
- Chaos engineering test for pool exhaustion scenarios?

---

## ✅ Resolution Sign-Off

**Incident Status**: 🟢 RESOLVED  
**Prevention Status**: 🟡 IN PROGRESS  
**Root Cause Fixed**: ✅ Yes  
**Tests Added**: ✅ Yes  
**Documentation Updated**: ✅ Yes  
**Runbook Updated**: ✅ Yes  
**Prevention In Place**: 🟡 Partial (monitoring done, audit pending)

**Resolved By**: @your-name  
**Date Closed**: 2026-03-02  
**Next Review**: 2026-06-01

---

## 📞 Questions?

- Need help with [pattern-089]? Check knowledge-base/patterns/error-handling/pattern-089.md
- Similar issue? Check knowledge-base/lessons/ for [incident-005]
- Want to add a related pattern? Copy pattern-template.md

---

**Version**: 1.0  
**Last Updated**: 2026-03-01  
**Status**: RESOLVED & DOCUMENTED  
**Learning Impact**: HIGH ⭐⭐⭐⭐⭐

---

## 💪 Remember

This incident taught us something valuable. The investment in [pattern-089], training, and 
monitoring will prevent future occurrences. Thank you to everyone who contributed to 
this learning opportunity!

**Next Similar Issue**: Prevented by applying this lesson 🎯
