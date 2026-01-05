# Claude Code Quick Reference Cheat Sheet 📋
**Print this and keep it at your desk!**

---

## **Getting Started**

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Start in your project
cd /path/to/project
cc

# Start with a task
cc "Explain how authentication works"

# Check version
cc --version

# Get help
cc --help
```

---

## **The 5 Keys to Great Prompts**

| Key | Example |
|-----|---------|
| 1. **Be Specific** | ✅ "Add tests to src/services/auth.ts" <br> ❌ "Add tests" |
| 2. **Give Context** | ✅ "Users report login fails on mobile" <br> ❌ "Fix login" |
| 3. **Set Expectations** | ✅ "Plan first, then implement" <br> ❌ [no guidance] |
| 4. **Mention Constraints** | ✅ "Use Jest, follow patterns in tests/" <br> ❌ [no constraints] |
| 5. **Request Verification** | ✅ "Add tests and explain changes" <br> ❌ [no verification] |

---

## **Prompt Formula**

```
[ACTION] + [TARGET] + [CONTEXT] + [CONSTRAINTS] + [VERIFICATION]

Example:
"Add unit tests [ACTION] to src/services/payment.ts [TARGET]
for edge cases like invalid cards [CONTEXT].
Use Jest and follow existing test patterns [CONSTRAINTS].
Aim for 90%+ coverage and explain your approach [VERIFICATION]."
```

---

## **Quick Prompts by Task Type**

### **Code Exploration**
```
"Explain how [feature] works. Show key files and interactions."
"Trace the flow when a user [does action]."
"Find all files related to [domain/feature]."
```

### **Bug Fixing**
```
"Users report [symptom]. Debug [file] and fix it."
"Find and fix [issue type] in [area of code]."
```

### **Feature Implementation**
```
"Add [feature] to [location]. Use [tech]. Follow [pattern file]."
"Implement [requirement] with tests and documentation."
```

### **Refactoring**
```
"Refactor [file] to [improvement]. Add tests."
"Extract [pattern] from [files] into reusable [utility]."
```

### **Testing**
```
"Add [test type] for [file]. Cover [scenarios]. Use [framework]."
"Fix failing tests in [test file] after my changes."
```

### **Documentation**
```
"Generate API docs for routes in [directory]."
"Add JSDoc comments to [file] with examples."
```

---

## **Common Tasks - Ready to Use**

| Task | Prompt |
|------|--------|
| **Understand codebase** | "I'm new here. Overview of structure, tech stack, and key areas." |
| **Find API endpoints** | "List all API endpoints, grouped by resource." |
| **Debug error** | "Users get [error]. Find cause in [area] and fix." |
| **Add validation** | "Add input validation to [endpoint/form]. Validate [fields]." |
| **Write tests** | "Add unit tests to [file]. Cover happy path and edge cases." |
| **Add feature** | "Add [feature] to [component/file]. Follow [reference pattern]." |
| **Optimize query** | "Optimize slow query in [file]. Add indexes if needed." |
| **Update docs** | "Update README with current setup instructions." |
| **Security audit** | "Check for [vulnerability type] in [area]." |
| **Create PR** | "Create PR for current branch with clear description." |

---

## **Do's and Don'ts**

### **✅ DO:**
- Reference specific files and functions
- Mention your tech stack and versions
- Ask for explanations of changes
- Request tests for new code
- Specify code style preferences
- Review all generated code
- Start with small tasks to learn

### **❌ DON'T:**
- Use vague prompts like "make it better"
- Assume Claude knows your context
- Skip specifying constraints
- Forget to test generated code
- Trust code blindly without review
- Batch multiple unrelated tasks
- Use for learning basic syntax

---

## **Workflow Tips**

### **Starting a Task**
1. Read existing code first
2. Write a clear, specific prompt
3. Review Claude's plan (if given)
4. Watch the implementation
5. Test the results
6. Review and refine

### **Working with Files**
```
✅ "Read src/utils/auth.ts and add error handling"
❌ "Add error handling" (which file?)
```

### **Iterating**
```
If first result isn't perfect:
"Adjust the previous code to [specific change]"
"The [part] doesn't work with our [setup]. Please fix."
```

### **Git Workflow**
```
"Create feature branch, implement [feature], commit, push"
"Create PR with description of [changes]"
```

---

## **Troubleshooting**

| Problem | Solution |
|---------|----------|
| **Vague responses** | Add more context and specificity |
| **Wrong approach** | Specify constraints and patterns to follow |
| **Code doesn't work** | Mention your framework versions and setup |
| **Missed requirements** | List all requirements explicitly |
| **Not following style** | Reference a file that shows your style |

---

## **Advanced Techniques**

### **Multi-Step Tasks**
```
"I need [complex feature]. Requirements:
1. [Requirement 1]
2. [Requirement 2]
3. [Requirement 3]

Plan this first, then implement step by step."
```

### **Comparing Approaches**
```
"We need [feature]. Suggest 2-3 approaches with pros/cons
based on our current architecture."
```

### **Maintaining Context**
```
"Based on the auth code we just reviewed, implement
password reset following the same patterns."
```

---

## **Quality Checklist**

After Claude generates code, always check:

- [ ] Code follows project conventions
- [ ] No hardcoded secrets or credentials
- [ ] Error handling is appropriate
- [ ] Edge cases are handled
- [ ] Tests are included (when appropriate)
- [ ] No security vulnerabilities introduced
- [ ] Performance is acceptable
- [ ] Documentation is updated
- [ ] No console.logs left in production code

---

## **Performance Tips**

### **Fast Tasks** ⚡ (< 1 min)
- Reading and explaining code
- Finding specific functions/files
- Suggesting approaches
- Reviewing small changes

### **Medium Tasks** 🏃 (1-5 min)
- Bug fixes with tests
- Small feature additions
- Refactoring single files
- Writing documentation

### **Slower Tasks** 🚶 (5-15 min)
- Large feature implementations
- Multi-file refactoring
- Complex migrations
- Comprehensive test suites

---

## **Remember:**

> **Claude Code is a tool, you're the expert.**
>
> Always review, test, and understand the code it generates.
>
> Start small, build confidence, then tackle bigger tasks.

---

## **Quick Examples**

### **Example 1: Bug Fix**
```
❌ "Fix the cart bug"

✅ "Users report cart totals are wrong when applying discount codes.
   Debug src/cart/calculator.ts and fix the calculation.
   Add tests to prevent regression."
```

### **Example 2: Feature**
```
❌ "Add dark mode"

✅ "Implement dark mode toggle:
   - Add theme context in src/context/
   - Update components to use theme
   - Persist in localStorage
   - Follow the pattern in src/components/Settings.tsx"
```

### **Example 3: Refactor**
```
❌ "Clean up the code"

✅ "Refactor UserController.ts (800 lines) into smaller controllers.
   Follow single responsibility principle.
   Keep existing functionality. Add tests."
```

---

## **Resources**

- **Documentation:** docs.anthropic.com
- **Workshop Materials:** [Workshop repo]
- **Community:** [Slack/Discord link]
- **Instructor:** [Contact info]

---

**Pro Tip:** Keep a "prompt journal" - save prompts that work well for your team's common tasks!

---

**Version 1.0** | Claude Code Workshop | Print & Keep Handy! 📌
