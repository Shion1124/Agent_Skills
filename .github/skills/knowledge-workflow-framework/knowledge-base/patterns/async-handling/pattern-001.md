---
name: pattern-001
description: Error handling in async operations
complexity: Intermediate
tags: async, error-handling, promises, typescript
category: async-handling
---

# Pattern: Error Handling in Async Operations

**Category**: Async Handling  
**Complexity**: Intermediate  
**Author**: Team  
**Date**: 2026-02-25  

## Problem
Async code can silently fail if errors are not properly handled, leading to:
- Unhandled promise rejections
- Resource leaks
- Silent data loss

## Solution

### ✅ GOOD - Using try-catch with async-await

```typescript
async function fetchUserData(userId: string) {
  try {
    const response = await fetch(`/api/users/${userId}`);
    if (!response.ok) {
      throw new Error(`HTTP ${response.status}: ${response.statusText}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch user data:', error);
    throw error;
  }
}
```

### ✅ GOOD - Using Promise.catch() for cleanup

```typescript
function loadData(url: string) {
  return fetch(url)
    .then(r => r.json())
    .then(data => processData(data))
    .catch(error => {
      console.error('Error loading data:', error);
      return null;
    });
}
```

## When to Use
- Any async operation (fetch, database calls, file I/O)
- Long chains of promises
- Resource acquisition and cleanup

## When NOT to Use
- Synchronous code (use regular try-catch)
- Single operations without cleanup needs

## Related Patterns
- pattern-015: Resource Cleanup
- pattern-020: Promise Composition
