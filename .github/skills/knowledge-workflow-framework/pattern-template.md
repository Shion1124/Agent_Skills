---
name: pattern-TEMPLATE
description: "Pattern title and brief summary"
category: api-design  # api-design, testing, database, security, performance, frontend, backend, devops
complexity: beginner  # beginner, intermediate, advanced
author: your-name
date: 2026-03-01
last_updated: 2026-03-01
tags: []  # e.g., [testing, error-handling, async]
status: stable  # experimental, stable, proven, deprecated
maintenance_effort: low  # low, medium, high
maturity_level: proven  # experimental, stable, proven
---

# Pattern: [Pattern Name]

**Category**: [api-design|testing|database|security|performance|frontend|backend|devops]  
**Complexity**: [beginner|intermediate|advanced]  
**Author**: @your-name  
**Last Updated**: 2026-03-01  
**Status**: [experimental|stable|proven|deprecated]

---

## 🎯 Problem Statement

**The Challenge**
Describe the problem this pattern solves. Be specific and concrete.

**Example**:
> When handling async/await code in TypeScript, it's easy to accidentally leak resources 
> (database connections, file handles, network sockets) if an error occurs during execution. 
> Without proper cleanup, an application can exhaust available resources, causing cascading failures.

**Context Where This Arises**
- Situation 1: When...
- Situation 2: When...
- Situation 3: When...

**Example**:
- Any code that acquires a resource and then performs async operations
- Long-running applications with many concurrent requests
- Legacy code migrating from callbacks to async/await

**Common Pain Points**
- Pain point 1
- Pain point 2
- Pain point 3

---

## 💡 Solution

### Core Concept
Explain the pattern in 1-2 sentences before code examples.

**Example**:
> Use TypeScript/Python context managers (with/async with statements) to guarantee 
> that resources are released, even if an error occurs during processing.

### Implementation

#### Version 1: Basic Pattern

**Language**: [Language]

```typescript
// Example for TypeScript/JavaScript
// ❌ ANTI-PATTERN - Resource may leak on error
async function fetchUserData(userId: string) {
  const connection = await database.getConnection();
  
  try {
    const user = await connection.query(
      'SELECT * FROM users WHERE id = ?', 
      [userId]
    );
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    return null;
    // Connection is never released! ⚠️
  }
}
```

```typescript
// ✅ GOOD PATTERN - Resource cleanup with finally
async function fetchUserData(userId: string) {
  const connection = await database.getConnection();
  
  try {
    const user = await connection.query(
      'SELECT * FROM users WHERE id = ?', 
      [userId]
    );
    return user;
  } catch (error) {
    console.error('Error fetching user:', error);
    return null;
  } finally {
    await connection.release();  // Always executed
  }
}
```

#### Version 2: Advanced Pattern

```typescript
// ✅ BEST PATTERN - Context manager pattern
// This is a helper wrapper for automatic resource cleanup

class ManagedConnection {
  private connection: DatabaseConnection;
  
  constructor(connection: DatabaseConnection) {
    this.connection = connection;
  }
  
  async execute<T>(
    query: string, 
    params: any[] = []
  ): Promise<T> {
    try {
      return await this.connection.query(query, params);
    } finally {
      // Resource automatically released
      await this.connection.release();
    }
  }
  
  async transaction<T>(
    callback: (conn: DatabaseConnection) => Promise<T>
  ): Promise<T> {
    try {
      await this.connection.query('BEGIN TRANSACTION');
      const result = await callback(this.connection);
      await this.connection.query('COMMIT');
      return result;
    } catch (error) {
      await this.connection.query('ROLLBACK');
      throw error;
    } finally {
      await this.connection.release();
    }
  }
}

// Usage
async function fetchUserData(userId: string) {
  const managedConn = new ManagedConnection(
    await database.getConnection()
  );
  return managedConn.execute(
    'SELECT * FROM users WHERE id = ?',
    [userId]
  );  // Connection auto-released
}
```

#### Version 3: Using Finally Block (Python)

```python
# Python version with context manager
import contextlib

@contextlib.asynccontextmanager
async def database_connection():
    """Context manager for database connections"""
    connection = await db.get_connection()
    try:
        yield connection
    finally:
        await connection.release()

# Usage
async def fetch_user_data(user_id: str):
    async with database_connection() as conn:
        # Connection auto-released when exiting block
        return await conn.query(
            "SELECT * FROM users WHERE id = ?",
            [user_id]
        )
```

---

### Key Points

**Critical Details**
1. Point 1: Explanation
2. Point 2: Explanation
3. Point 3: Explanation

**Example**:
1. **Always use finally**: Guarantees execution even on error
2. **Test error paths**: Verify resource release on exceptions
3. **Monitor resource pools**: Detect leaks before they cause outages

---

## ✅ When to Use This Pattern

### Perfect Use Cases
- Use case 1: [Description] ✅
- Use case 2: [Description] ✅
- Use case 3: [Description] ✅

**Example**:
- Any database query operation ✅
- File I/O operations with async code ✅
- Network requests requiring connection pooling ✅
- Temporary locks/mutexes in concurrent code ✅

### Situations Where This Shines
- Situation 1: When...
- Situation 2: When...

---

## ❌ When NOT to Use This Pattern

### Anti-Use Cases
- Don't use for: Simple synchronous operations
- Don't use for: Stateless utility functions
- Don't use for: In-memory only operations

**Example**:
- Simple array operations (no resource needed)
- Pure functions that don't need cleanup
- Cached data that doesn't require release

### When Simpler Approaches Work
- If the operation is synchronous, use regular `try/finally`
- If there's no resource to manage, skip cleanup code
- If using higher-level libraries (ORMs), use their patterns

---

## 🔗 Related Patterns

### Complementary Patterns
- [pattern-012] Error Handling in Async Code - Often used together
- [pattern-045] Logging Best Practices - Log resource lifecycle
- [pattern-089] Connection Pooling - Pairs with this pattern

### Similar Patterns (Choose One)
- [pattern-050] Generator Functions - Alternative for resource management
- [pattern-060] Async Generators - Modern TypeScript approach

### When You've Mastered This
- [pattern-101] Advanced: Custom Resource Managers
- [pattern-102] Advanced: Reactive Resource Cleanup

---

## 📊 Complexity & Prerequisites

**Difficulty Level**: Intermediate  
**Time to Learn**: 30-60 minutes  
**Time to Master**: 1-2 weeks  

### Prerequisites
- Understanding of async/await
- Familiarity with try/catch/finally
- Basic knowledge of resource management

### Skills Gained
- Resource safety in async code
- Error handling patterns
- Memory efficiency

---

## 🧪 Testing This Pattern

### Unit Test Example

```typescript
describe('Resource Cleanup', () => {
  it('should release connection on success', async () => {
    const mockConn = { 
      query: jest.fn().mockResolvedValue({ id: 1 }),
      release: jest.fn()
    };
    
    await fetchUserData(1);
    
    expect(mockConn.release).toHaveBeenCalled();
  });

  it('should release connection even on error', async () => {
    const mockConn = { 
      query: jest.fn().mockRejectedValue(new Error('DB Error')),
      release: jest.fn()
    };
    
    try {
      await fetchUserData(1);
    } catch (e) {
      // Expected to throw
    }
    
    // Critical assertion - connection must be released!
    expect(mockConn.release).toHaveBeenCalled();
  });
});
```

### Integration Test Example

```typescript
it('should not exhaust connection pool under load', async () => {
  const pool = database.getPoolStats();
  const initialConnections = pool.activeConnections;
  
  // Simulate 100 concurrent requests
  const promises = Array.from({ length: 100 }, (_, i) =>
    fetchUserData(i).catch(() => null)  // Ignore some errors
  );
  
  await Promise.all(promises);
  
  const finalConnections = pool.activeConnections;
  
  // No connection leak!
  expect(finalConnections).toBe(initialConnections);
});
```

---

## 📈 Performance Considerations

**Memory Impact**
- Minimal: Pattern forces resource cleanup

**Speed Impact**
- Negligible: Cleanup usually < 1ms

**Scalability**
- Excellent: Prevents resource exhaustion as traffic grows

### Benchmark Example

```
Without cleanup: 500 requests → pool exhausted (30 sec)
With cleanup:    500 requests → sustained performance
```

---

## 🚀 Advanced Variations

### Variation 1: Timeout Handling

```typescript
async function fetchUserDataWithTimeout(
  userId: string, 
  timeoutMs: number = 5000
) {
  const connection = await database.getConnection();
  
  try {
    return await Promise.race([
      connection.query('SELECT * FROM users WHERE id = ?', [userId]),
      new Promise((_, reject) =>
        setTimeout(() => reject(new Error('Timeout')), timeoutMs)
      )
    ]);
  } finally {
    await connection.release();
  }
}
```

### Variation 2: Retry with Cleanup

```typescript
async function fetchUserDataWithRetry(
  userId: string,
  maxRetries: number = 3
) {
  let lastError;
  
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    const connection = await database.getConnection();
    
    try {
      return await connection.query(
        'SELECT * FROM users WHERE id = ?',
        [userId]
      );
    } catch (error) {
      lastError = error;
      console.log(`Attempt ${attempt} failed, retrying...`);
    } finally {
      await connection.release();  // Clean up even if retrying
    }
  }
  
  throw lastError;
}
```

---

## ⚠️ Common Pitfalls

**Pitfall 1: Forgetting the finally block**
```typescript
// ❌ WRONG
try {
  return await connection.query(...);
} catch (e) {
  logger.error(e);
}
// Resource leaked!
```

**Pitfall 2: Releasing in catch only**
```typescript
// ❌ WRONG
try {
  return await connection.query(...);
} catch (e) {
  await connection.release();  // Bypassed if success!
  throw e;
}
// Not released on success!
```

**Pitfall 3: Not handling nested resources**
```typescript
// ❌ WRONG - If outer fails, inner not released
const conn1 = await getConnection();
const conn2 = await getConnection();
// If conn2 fails, conn1 not released

// ✅ RIGHT - Nested try/finally
const conn1 = await getConnection();
try {
  const conn2 = await getConnection();
  try {
    // Use both
  } finally {
    await conn2.release();
  }
} finally {
  await conn1.release();
}
```

---

## 💼 Real-World Examples

### Example 1: Database Query Wrapper

See [pattern-089-database-query-wrapper.md](.github/skills/knowledge-workflow-framework/knowledge-base/patterns/database/pattern-089.md)

### Example 2: File Upload Handler

See [incident-047-file-descriptor-leak.md](.github/skills/knowledge-workflow-framework/knowledge-base/lessons/2026/incident-047.md)

### Example 3: HTTP Client with Retry

See code repository: `src/lib/http-client.ts`

---

## 📚 References & Learning Resources

- [MDN: Promise.prototype.finally()](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise/finally)
- [Node.js: Error handling](https://nodejs.org/en/docs/guides/nodejs-error-handling/)
- [PEP 343 – The "with" Statement (Python)](https://www.python.org/dev/peps/pep-0343/)
- [Resource Management in Rust (ownership)](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html)

---

## 🔄 Review & Feedback

**Effectiveness Score**: 9/10  
**Times Applied**: 45+  
**Issues Found**: 0  
**Last Reviewed**: 2026-02-28

### Feedback from Team
- "Saved us from a critical production incident" - @dave
- "Makes code much safer and easier to reason about" - @alice
- "Learning curve was short but impact is huge" - @bob

---

## 📅 Maintenance

**Last Updated**: 2026-03-01  
**Next Review**: 2026-09-01  
**Author**: @your-name  
**Maintainers**: [@reviewer1, @reviewer2]

**Change Log**:
- v1.0 (2026-03-01): Initial pattern documentation
- v0.9 (2026-02-15): Review feedback incorporated
- v0.1 (2026-01-20): Pattern draft

---

## 💡 Quick Reference Card

| Aspect | Details |
|--------|---------|
| **Use for** | Async resource management |
| **Key technique** | try/finally (or async context manager) |
| **Critical rule** | Always cleanup in finally block |
| **Test focus** | Error path scenarios |
| **Performance** | No degradation; prevents resource exhaustion |
| **Learning time** | 30-60 minutes to understand, 1-2 weeks to master |

---

**Pattern Version**: 1.0  
**Template Version**: 1.0  
**Last Updated**: 2026-03-01
