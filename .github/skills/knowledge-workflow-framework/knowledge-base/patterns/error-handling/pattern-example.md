---
name: pattern-example
description: Example pattern structure (delete after reading)
---

# Pattern: Error Handling in Async Code

**Category**: Error Handling  
**Complexity**: Beginner  
**Author**: Team  
**Date**: 2026-02-20  

## Problem
Async code can leave resources unclosed if errors occur.

## Solution

```python
# ❌ BAD - Resource might leak on error
async def fetch_user(id):
    conn = await db.getConnection()
    user = await conn.query("SELECT * FROM users WHERE id = ?", [id])
    return user
```

```python
# ✅ GOOD - Resource always released
async def fetch_user(id):
    async with db.getConnection() as conn:
        user = await conn.query("SELECT * FROM users WHERE id = ?", [id])
        return user
```

## When to Use
- Any resource acquisition (DB, file, network)
- Async/await patterns
- Context manager available

## When NOT to Use
- Simple operations without resources
- Synchronous code (use regular with statement)

## Related Patterns
- pattern-089: Resource Cleanup

---

This is a template. Create your own patterns based on team learnings.
