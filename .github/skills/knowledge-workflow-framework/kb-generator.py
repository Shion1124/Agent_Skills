#!/usr/bin/env python3
"""
Knowledge Base Generator & Manager for Knowledge Workflow Framework
Automates knowledge indexing, validation, and lifecycle management
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
import re
from typing import Dict, List, Any
import hashlib

class KnowledgeBaseManager:
    def __init__(self, kb_path: str = "."):
        self.kb_path = Path(kb_path)
        self.config_path = self.kb_path / "KWF-CONFIG.yaml"
        self.index_path = self.kb_path / "knowledge-index.json"
        self.decisions_dir = self.kb_path / "knowledge-base" / "decisions"
        self.patterns_dir = self.kb_path / "knowledge-base" / "patterns"
        self.lessons_dir = self.kb_path / "knowledge-base" / "lessons"
        
    def init(self):
        """Initialize knowledge base structure"""
        print("📚 Initializing Knowledge Base...")
        
        # Create directories
        dirs = [
            self.kb_path / "knowledge-base" / "decisions",
            self.kb_path / "knowledge-base" / "patterns",
            self.kb_path / "knowledge-base" / "lessons" / "2025",
            self.kb_path / "knowledge-base" / "lessons" / "2026",
        ]
        
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
            print(f"  ✓ Created {dir_path}")
        
        # Create sample decision
        self._create_sample_decision()
        
        # Create sample pattern
        self._create_sample_pattern()
        
        # Generate index
        self.update_index()
        
        print("\n✅ Knowledge Base initialized!")
        print(f"   Location: {self.kb_path / 'knowledge-base'}")
        print("   Next: Add your team's decisions, patterns, and lessons")
        
    def _create_sample_decision(self):
        """Create a sample decision for reference"""
        sample = """---
name: decision-example
description: Example decision structure (delete after reading)
---

# Decision: Tool Selection for E2E Testing

**Date**: 2026-02-15  
**Status**: ACCEPTED  
**Decision Makers**: @team-lead  

## Context
Team needs to choose E2E testing framework. Options: Playwright, Cypress, Selenium.

## Decision
Use Playwright for:
1. Multi-browser support (Chrome, Firefox, Safari)
2. Better performance (~3x faster)
3. Active maintenance and modern tooling

## Consequences
- Team learning curve (~2 days)
- CI/CD adds browser dependencies
- Better long-term maintainability

## Alternatives Considered
- Cypress: Good DX but limited to Chrome
- Selenium: Too verbose for modern web

## Related Patterns
- pattern-010: Playwright Best Practices

## Follow-up
- [ ] Train team on Playwright (Week 1)
- [ ] Review after 2 sprints (2026-04-15)

---

This is a template. Edit and customize for your decisions.
"""
        decision_path = self.decisions_dir / "architecture" / "decision-example.md"
        decision_path.parent.mkdir(parents=True, exist_ok=True)
        decision_path.write_text(sample)
        print("  ✓ Created sample decision")
    
    def _create_sample_pattern(self):
        """Create a sample pattern for reference"""
        sample = """---
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
"""
        pattern_path = self.patterns_dir / "error-handling" / "pattern-example.md"
        pattern_path.parent.mkdir(parents=True, exist_ok=True)
        pattern_path.write_text(sample)
        print("  ✓ Created sample pattern")
    
    def update_index(self):
        """Generate/update knowledge-index.json from all entries"""
        print("\n📑 Generating Knowledge Index...")
        
        index = {
            "knowledge_base_version": "1.0",
            "last_updated": datetime.now().isoformat(),
            "entries": [],
            "search_tags": set(),
            "stats": {
                "total_decisions": 0,
                "total_patterns": 0,
                "total_lessons": 0,
                "by_category": {}
            }
        }
        
        # Index decisions
        entries = self._index_directory(
            self.decisions_dir,
            "decision",
            ["status", "tags", "date"]
        )
        index["entries"].extend(entries)
        index["stats"]["total_decisions"] = len(entries)
        
        # Index patterns
        entries = self._index_directory(
            self.patterns_dir,
            "pattern",
            ["complexity", "tags", "category"]
        )
        index["entries"].extend(entries)
        index["stats"]["total_patterns"] = len(entries)
        
        # Index lessons
        entries = self._index_directory(
            self.lessons_dir,
            "lesson",
            ["severity", "tags", "category"]
        )
        index["entries"].extend(entries)
        index["stats"]["total_lessons"] = len(entries)
        
        # Calculate category stats
        for entry in index["entries"]:
            if "category" in entry:
                cat = entry["category"]
                index["stats"]["by_category"][cat] = \
                    index["stats"]["by_category"].get(cat, 0) + 1
            if "tags" in entry and isinstance(entry["tags"], list):
                index["search_tags"].update(entry["tags"])
        
        # Convert set to list for JSON
        index["search_tags"] = sorted(list(index["search_tags"]))
        
        # Save index
        with open(self.index_path, "w") as f:
            json.dump(index, f, indent=2, default=str)
        
        print(f"  ✓ Decisions: {index['stats']['total_decisions']}")
        print(f"  ✓ Patterns: {index['stats']['total_patterns']}")
        print(f"  ✓ Lessons: {index['stats']['total_lessons']}")
        print(f"  ✓ Tags: {len(index['search_tags'])}")
        print(f"\n✅ Index updated: {self.index_path}")
    
    def _index_directory(self, dir_path: Path, entry_type: str, 
                        metadata_fields: List[str]) -> List[Dict[str, Any]]:
        """Index all markdown files in directory"""
        entries = []
        
        if not dir_path.exists():
            return entries
        
        for md_file in dir_path.rglob("*.md"):
            if md_file.name == "*.md" or "example" in md_file.name:
                continue
            
            entry = self._parse_markdown(md_file, entry_type, metadata_fields)
            if entry:
                entries.append(entry)
        
        return entries
    
    def _parse_markdown(self, file_path: Path, entry_type: str,
                       metadata_fields: List[str]) -> Dict[str, Any]:
        """Parse markdown file and extract metadata"""
        content = file_path.read_text()
        
        # Extract YAML front matter
        match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
        frontmatter = {}
        body_text = content
        
        if match:
            yaml_text = match.group(1)
            for line in yaml_text.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    frontmatter[key.strip()] = value.strip()
            body_text = content[match.end():].strip()
        
        # Extract title
        title_match = re.search(r'^# (.+)$', body_text, re.MULTILINE)
        title = title_match.group(1) if title_match else file_path.stem
        
        # Create entry
        entry = {
            "id": frontmatter.get("name", file_path.stem),
            "type": entry_type,
            "title": title,
            "path": str(file_path.relative_to(self.kb_path)),
            "created": datetime.fromtimestamp(file_path.stat().st_ctime).isoformat(),
            "modified": datetime.fromtimestamp(file_path.stat().st_mtime).isoformat(),
        }
        
        # Add metadata fields
        for field in metadata_fields:
            if field in frontmatter:
                if field == "tags":
                    entry[field] = [t.strip() for t in 
                                   frontmatter[field].split(",")]
                else:
                    entry[field] = frontmatter[field]
        
        # Add search content (first 500 chars of body)
        search_content = re.sub(r'[#*`]', '', body_text)[:500]
        entry["search_preview"] = search_content
        
        return entry
    
    def validate(self):
        """Validate knowledge base structure and completeness"""
        print("\n🔍 Validating Knowledge Base...")
        
        issues = []
        
        # Check for orphaned files
        for md_file in self.kb_path.rglob("*.md"):
            if md_file.name.startswith("_"):
                continue
            
            # Check for front matter
            content = md_file.read_text()
            if not content.startswith("---"):
                issues.append(f"⚠️  Missing front matter: {md_file.relative_to(self.kb_path)}")
            
            # Check for title
            if not re.search(r'^# ', content, re.MULTILINE):
                issues.append(f"⚠️  Missing title: {md_file.relative_to(self.kb_path)}")
        
        # Check for broken references
        for md_file in self.kb_path.rglob("*.md"):
            content = md_file.read_text()
            # Find references like [decision-001], [pattern-010]
            refs = re.findall(r'\[(decision|pattern|lesson)-\d+\]', content)
            for ref in refs:
                # Check if referenced file exists
                ref_path = self._find_entry(ref)
                if not ref_path:
                    issues.append(f"❌ Broken reference {ref} in {md_file.relative_to(self.kb_path)}")
        
        # Report
        if issues:
            print("\n⚠️  Issues found:")
            for issue in issues:
                print(f"  {issue}")
            print(f"\nTotal issues: {len(issues)}")
        else:
            print("✅ Knowledge Base is healthy!")
        
        return len(issues) == 0
    
    def _find_entry(self, entry_id: str) -> Path:
        """Find entry file by ID"""
        for md_file in self.kb_path.rglob("*.md"):
            content = md_file.read_text()
            if f'name: {entry_id}' in content:
                return md_file
        return None
    
    def search(self, query: str, limit: int = 10):
        """Search knowledge base"""
        if not self.index_path.exists():
            print("❌ Index not found. Run 'update-index' first.")
            return
        
        print(f"\n🔎 Searching for: '{query}'")
        
        with open(self.index_path) as f:
            index = json.load(f)
        
        query_lower = query.lower()
        results = []
        
        for entry in index["entries"]:
            score = 0
            
            # Score by match location
            if query_lower in entry.get("title", "").lower():
                score += 10
            if any(query_lower in tag.lower() for tag in entry.get("tags", [])):
                score += 5
            if query_lower in entry.get("search_preview", "").lower():
                score += 1
            
            if score > 0:
                results.append((score, entry))
        
        # Sort by score
        results.sort(key=lambda x: x[0], reverse=True)
        
        if not results:
            print("  No results found")
            return
        
        print(f"\n  Found {len(results)} results:\n")
        for score, entry in results[:limit]:
            print(f"  [{entry['type'].upper()}] {entry['title']}")
            print(f"    Path: {entry['path']}")
            print(f"    Tags: {', '.join(entry.get('tags', []))}")
            print()
    
    def stats(self):
        """Show knowledge base statistics"""
        if not self.index_path.exists():
            print("❌ Index not found. Run 'update-index' first.")
            return
        
        with open(self.index_path) as f:
            index = json.load(f)
        
        print("\n📊 Knowledge Base Statistics")
        print("=" * 40)
        print(f"Decisions:  {index['stats']['total_decisions']}")
        print(f"Patterns:   {index['stats']['total_patterns']}")
        print(f"Lessons:    {index['stats']['total_lessons']}")
        print(f"Total:      {sum(index['stats'].get(k, 0) for k in ['total_decisions', 'total_patterns', 'total_lessons'])}")
        print(f"\nTags:       {len(index['search_tags'])}")
        
        print(f"\nBy Category:")
        for category, count in sorted(index['stats']['by_category'].items()):
            print(f"  {category:20} {count:3}")
        
        print(f"\nLast Updated: {index['last_updated']}")


def main():
    """CLI entry point"""
    manager = KnowledgeBaseManager()
    
    commands = {
        'init': manager.init,
        'update-index': manager.update_index,
        'validate': manager.validate,
        'stats': manager.stats,
    }
    
    if len(sys.argv) < 2:
        print("Knowledge Base Manager")
        print("\nUsage: python kb-generator.py <command>")
        print("\nCommands:")
        for cmd in commands.keys():
            print(f"  {cmd}")
        return
    
    command = sys.argv[1]
    
    if command == 'search' and len(sys.argv) > 2:
        manager.search(' '.join(sys.argv[2:]))
    elif command in commands:
        commands[command]()
    else:
        print(f"❌ Unknown command: {command}")
        print(f"Available: {', '.join(commands.keys())}")


if __name__ == "__main__":
    main()
