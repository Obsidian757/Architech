# Claude Code Prompt Library 📚
**Your Complete Reference Guide**

---

## **Quick Start: The 5 Keys to Great Prompts**

1. **Be Specific** - Name files, functions, features
2. **Give Context** - Explain the "why" and background
3. **Set Expectations** - Say if you want planning or immediate action
4. **Mention Constraints** - Code style, frameworks, limitations
5. **Request Verification** - Ask for tests and explanations

---

## **Prompt Formula Template**

```
[Action] + [Target] + [Context] + [Constraints] + [Verification]

Example:
"Add unit tests [Action] to src/services/payment.ts [Target]
focusing on edge cases like invalid cards [Context].
Use Jest and follow our existing test patterns [Constraints].
Aim for 90%+ coverage [Verification]."
```

---

## **Category 1: Code Exploration & Understanding** 🔍

### **General Codebase Understanding**
```
Explain how the user authentication flow works in this codebase.
Show me the key files involved and how they interact.
```

```
I'm new to this project. Give me an overview of the codebase structure,
main technologies used, and where the critical business logic lives.
```

```
Create a visual diagram of the architecture showing how the frontend,
backend, and database interact.
```

### **Finding Specific Code**
```
Find all the places where we interact with the database.
Show me which files handle user data and payment data separately.
```

```
Show me all API endpoints in this project, grouped by resource type
(users, products, orders, etc).
```

```
Trace the execution path when a user clicks the 'Submit Order' button.
Show me every file and function that gets called.
```

### **Understanding Patterns**
```
What design patterns are used in this codebase?
Show me examples of each pattern and explain why they're used.
```

```
How is error handling implemented across the project?
Show me the different approaches and suggest standardization if needed.
```

```
Analyze our state management approach.
Is it consistent? Are there any anti-patterns?
```

---

## **Category 2: Bug Fixing** 🐛

### **Investigation**
```
Users are getting a '500 Internal Server Error' when uploading files larger than 5MB.
Find the issue in the upload handler and fix it with proper error messages.
```

```
The shopping cart total sometimes shows the wrong price.
Debug the calculation logic in src/cart/calculator.ts and fix any
rounding or currency issues.
```

```
The app crashes when users enter special characters in the search box.
Find the validation issue and add proper input sanitization.
```

### **Performance Bugs**
```
Memory usage keeps growing in our Node.js app.
Search for potential memory leaks, especially around event listeners
and database connections.
```

```
The dashboard page loads slowly after the recent update.
Profile the changes and identify what's causing the performance regression.
```

### **Race Conditions & Timing**
```
Users report that clicking 'Submit' quickly multiple times creates duplicate orders.
Add proper request deduplication and loading states.
```

```
The websocket connection sometimes drops and doesn't reconnect.
Debug the reconnection logic and add exponential backoff.
```

---

## **Category 3: Feature Implementation** ⚡

### **Authentication & Authorization**
```
Add a 'Remember Me' checkbox to the login form that keeps users logged in for 30 days.
Use JWT tokens and follow our existing auth patterns in src/auth/.
```

```
Implement role-based access control (RBAC) with three roles: admin, editor, viewer.
Add middleware to protect routes based on roles.
```

```
Create a password reset flow:
1. User requests reset via email
2. System sends token-based reset link
3. User sets new password
4. Old sessions are invalidated
Follow our existing email service patterns.
```

### **CRUD Operations**
```
Add full CRUD endpoints for a 'categories' resource:
- GET /api/categories (list with pagination)
- GET /api/categories/:id (single item)
- POST /api/categories (create)
- PUT /api/categories/:id (update)
- DELETE /api/categories/:id (soft delete)
Include validation, error handling, and tests.
```

### **UI Features**
```
Implement a search bar with autocomplete:
- Debounce input (300ms)
- Call /api/search endpoint
- Show results dropdown
- Highlight matching text
- Handle keyboard navigation (arrow keys, enter, escape)
```

```
Add pagination to the products listing page.
Support query parameters like ?page=2&limit=20 and return
total count and page metadata in the API response.
```

```
Create a dark mode toggle:
- Add theme context
- Update all components to respect theme
- Persist preference in localStorage
- Smooth transition between themes
```

### **Integrations**
```
Integrate Stripe payment API into our checkout:
- Add payment intent creation
- Implement webhook handler for payment confirmation
- Handle errors gracefully with retry logic
- Add proper logging
Follow PCI compliance best practices.
```

```
Add Google Analytics tracking:
- Page views
- Custom events (signup, purchase, etc)
- User properties
Use our existing analytics wrapper pattern.
```

---

## **Category 4: Refactoring & Code Quality** 🔧

### **Code Organization**
```
The UserController.ts file is 800 lines long.
Refactor it into smaller, focused controllers following
single responsibility principle.
```

```
Extract the duplicated validation logic from src/controllers/
into reusable validator functions. Create a src/validators/
directory with proper TypeScript types.
```

```
This function has cyclomatic complexity of 15.
Simplify it by extracting helper functions and reducing nested conditionals.
```

### **Modern Patterns**
```
Convert the class components in src/components/legacy/ to
functional components with hooks. Start with the UserProfile component.
```

```
Replace callback-based async code with async/await throughout
src/services/. Improve error handling.
```

```
Convert CommonJS (require/module.exports) to ES6 modules (import/export)
in the backend code.
```

### **Type Safety**
```
Add TypeScript types to src/utils/helpers.js.
Infer types from usage and add proper JSDoc or convert to .ts
```

```
Fix all TypeScript 'any' types in the project.
Replace with proper types or use generics where appropriate.
```

---

## **Category 5: Testing** ✅

### **Unit Tests**
```
Add unit tests for src/services/pricing.ts.
Cover happy paths, edge cases (zero prices, negative discounts),
and error scenarios. Use Jest and aim for 90%+ coverage.
```

```
Write tests for the date formatting utilities in src/utils/date.ts.
Test different locales, timezones, and edge cases like leap years.
```

### **Integration Tests**
```
Create integration tests for the /api/orders endpoint:
- Test successful order creation
- Invalid input handling
- Authentication requirements
- Database transaction rollback on errors
```

### **E2E Tests**
```
Add E2E tests for the checkout flow using Playwright:
1. Add item to cart
2. Proceed to checkout
3. Fill shipping info
4. Enter payment details
5. Confirm order
6. Verify confirmation page
```

### **Test Fixes**
```
The tests in tests/auth.test.ts are failing after my recent changes.
Debug the tests, fix them, and ensure they properly validate the new behavior.
```

```
Our test suite is flaky - tests sometimes pass, sometimes fail.
Identify and fix race conditions, timing issues, and improper cleanup.
```

---

## **Category 6: Documentation** 📚

### **API Documentation**
```
Generate API documentation for all routes in src/routes/api/.
Create an OpenAPI/Swagger spec with:
- Request/response schemas
- Authentication requirements
- Example requests
- Error codes
```

### **Code Documentation**
```
Add JSDoc comments to all exported functions in src/utils/.
Include:
- Parameter descriptions and types
- Return type and description
- Usage examples
- Throws documentation for errors
```

### **Project Documentation**
```
Create a CONTRIBUTING.md file explaining:
- Git workflow (branch naming, commit messages)
- Code style guidelines
- Testing requirements
- PR process and review checklist
```

```
Update the README.md with current setup instructions:
- Prerequisites and versions
- Environment variables needed
- Database setup steps
- How to run locally
- How to run tests
- Deployment process
```

---

## **Category 7: Database & Migrations** 🗄️

### **Migrations**
```
Create a migration to add an 'email_verified' column to the users table.
Include:
- Up migration (add column with default false)
- Down migration (remove column)
- Update User model/schema
- Add index for performance
```

```
Create a migration to split the 'name' field into 'first_name' and 'last_name'.
Handle data migration for existing records.
```

### **Query Optimization**
```
Optimize the slow query in src/repositories/orders.ts.
The query joins 4 tables and takes 3+ seconds.
Add appropriate indexes and rewrite to avoid N+1 problems.
```

```
Add database query logging to identify slow queries.
Log any query taking over 100ms with the query text and execution time.
```

### **ORM Changes**
```
Convert our Mongoose schemas to Prisma.
Start with the User and Product models, maintaining all
existing fields, relationships, and validation rules.
```

---

## **Category 8: DevOps & Configuration** ⚙️

### **CI/CD**
```
Set up GitHub Actions CI/CD pipeline:
- Run tests and linting on every PR
- Deploy to staging when merging to develop branch
- Deploy to production when merging to main branch
- Notify Slack on deployment status
```

```
Add pre-commit hooks using husky:
- Run ESLint on staged files
- Run Prettier for formatting
- Run type checking
- Prevent commits to main branch
```

### **Docker**
```
Create Docker configuration for local development:
- Dockerfile for the Node.js app
- docker-compose.yml with app, PostgreSQL, Redis
- Volume mounts for hot reload
- Environment variable configuration
```

### **Configuration Management**
```
Add environment variable validation using Zod.
Create a config.ts that:
- Validates all required env vars on startup
- Provides type-safe access to config
- Fails fast with clear error messages
```

```
Move hardcoded configuration to environment variables:
- API keys and secrets
- Database URLs
- Third-party service endpoints
- Feature flags
```

---

## **Category 9: Security** 🔒

### **Vulnerability Scanning**
```
Audit the codebase for SQL injection vulnerabilities.
Check all database queries and convert any string concatenation
to parameterized queries or prepared statements.
```

```
Search for potential XSS vulnerabilities.
Check all places where user input is rendered in HTML
and ensure proper escaping/sanitization.
```

```
Review file upload handling for security issues:
- File type validation
- File size limits
- Filename sanitization
- Storage location (outside web root)
```

### **Authentication & Authorization**
```
Review our authentication middleware for security issues:
- Proper JWT token validation
- Expiration checking
- Refresh token rotation
- Session invalidation on logout
```

```
Add rate limiting to API endpoints using express-rate-limit:
- Strict limits on auth endpoints (5 attempts per 15 min)
- Moderate limits on write operations (100 per hour)
- Lenient limits on read operations (1000 per hour)
```

### **Dependencies**
```
Audit dependencies for security vulnerabilities using npm audit.
Fix all high and critical issues. Document any that can't be
fixed immediately with mitigation plans.
```

---

## **Category 10: Performance Optimization** ⚡

### **Frontend Performance**
```
The homepage takes 3 seconds to load.
Analyze the bundle size, identify large dependencies,
and implement code splitting for routes.
```

```
Add lazy loading to our React app:
- Split bundle by route
- Lazy load components below the fold
- Add loading skeletons
- Preload critical routes
```

```
Optimize images in public/assets/:
- Convert to WebP format
- Generate multiple sizes for responsive images
- Add lazy loading with Intersection Observer
- Implement blur-up placeholder technique
```

### **Backend Performance**
```
Profile the /api/dashboard endpoint which takes 2+ seconds.
Identify slow database queries and add caching with Redis
for frequently accessed data (5 min TTL).
```

```
The API response payload is 2MB.
Add pagination, implement field filtering (?fields=id,name),
and use compression middleware.
```

### **Caching**
```
Implement a multi-layer caching strategy:
- Browser caching (Cache-Control headers)
- CDN caching for static assets
- Redis caching for database queries
- In-memory caching for config/constants
Document TTL for each layer.
```

---

## **Category 11: Dependency Management** 📦

### **Updates**
```
Update all npm packages to their latest compatible versions.
Run tests after updating and fix any breaking changes.
Generate a summary of what changed.
```

```
Upgrade React from v17 to v18:
- Update React and ReactDOM
- Migrate to new createRoot API
- Test for breaking changes
- Update concurrent features usage
```

### **Replacements**
```
We're using deprecated package 'request'.
Replace all instances with 'axios' following our existing
HTTP client patterns. Update error handling.
```

```
Replace moment.js with date-fns to reduce bundle size.
Update all date formatting and manipulation code.
Verify output matches existing behavior.
```

### **Cleanup**
```
Identify and remove unused dependencies from package.json.
Use depcheck to find packages that aren't imported anywhere.
```

---

## **Category 12: Git Operations** 🌿

### **Branching & Commits**
```
Create a feature branch called 'feature/add-wishlist',
implement a basic wishlist feature (add/remove items),
commit with clear messages, and push to origin.
```

```
Review the changes in the last 3 commits.
Check for:
- Code quality issues
- Potential bugs
- Security concerns
- Missing tests
Suggest improvements.
```

### **Pull Requests**
```
Create a PR for the current branch:
- Write a clear title summarizing the changes
- Add a description with:
  * What changed and why
  * Testing instructions
  * Screenshots (if UI changes)
  * Breaking changes (if any)
- Link related issues
```

### **Conflict Resolution**
```
Merge the 'develop' branch into current feature branch
and resolve any conflicts. Prefer changes from develop
for shared utilities, keep feature code for new files.
```

---

## **Advanced Multi-Step Prompts** 🎯

### **Complete Feature with Everything**
```
I need to add user profile editing. Here's what I need:

1. Backend:
   - PUT /api/users/:id endpoint
   - Validation for email, phone, bio fields
   - Authorization (users can only edit their own profile)
   - Unit tests

2. Frontend:
   - Profile edit form with validation
   - Real-time validation feedback
   - Success/error notifications
   - Integration tests

3. Other:
   - Update API documentation
   - Add database migration if needed

Please plan this out first showing all the files you'll change,
then implement it step by step.
```

### **Refactoring Project**
```
Refactor our authentication system to be more maintainable:

Current issues:
- Auth logic is scattered across 5+ files
- Inconsistent error handling
- No refresh token support
- Hard to test

Goals:
- Centralize auth logic in src/auth/
- Add proper TypeScript types
- Implement refresh tokens
- Add comprehensive tests
- Update documentation

Create a plan showing the new structure, then implement it.
```

---

## **Troubleshooting Prompts** 🔧

### **When Things Don't Work**
```
I tried to implement [feature] but got this error: [paste error].
Help me debug and fix it.
```

```
The code you generated doesn't work with our setup.
We use [framework/library version]. Please adjust the code to be compatible.
```

### **When You Need Options**
```
We need to add real-time notifications.
Research our codebase and suggest 2-3 approaches
(WebSockets, SSE, polling) with pros/cons for each
based on our current architecture.
```

---

## **Tips for Even Better Results** 💡

### **DO:**
✅ Reference specific files: `src/services/auth.ts`
✅ Mention your tech stack: "We use Express with TypeScript"
✅ Specify code style: "Follow our existing patterns in src/utils/"
✅ Request tests: "Add unit tests using Jest"
✅ Ask for explanation: "Explain why you made these choices"

### **DON'T:**
❌ Be vague: "Fix the bug" (which bug? where?)
❌ Assume context: "Use that pattern we discussed" (be explicit)
❌ Skip constraints: "Add caching" (which layer? what tool?)
❌ Forget verification: Always ask for tests
❌ Batch unrelated tasks: One focused task at a time

---

## **Quick Reference: Prompt Templates**

| Task Type | Template |
|-----------|----------|
| **Exploration** | "Explain how [feature] works in this codebase. Show key files and their interactions." |
| **Bug Fix** | "Users report [symptom]. Debug [file/area] and fix the issue with proper error handling." |
| **Feature** | "Add [feature] to [location]. Use [technology]. Follow patterns in [reference file]." |
| **Refactor** | "Refactor [file] to [improvement]. Maintain functionality and add tests." |
| **Test** | "Add [test type] for [file]. Cover [scenarios]. Use [framework]. Aim for [coverage]%." |
| **Docs** | "Document [code] with [format]. Include [details]." |
| **Performance** | "Optimize [slow part]. Profile and fix bottlenecks. Target [metric]." |

---

**Version:** 1.0
**Workshop:** Claude Code for Development Teams
**Keep this handy!** Refer to it whenever you use Claude Code.

---

## **Your Turn! ✍️**

**Practice Space - Write Your Own Prompts:**

**My Current Task:**
_____________________________________________________________________

**My Prompt Using the 5 Keys:**

[Action]: _______________________________________________________________

[Target]: _______________________________________________________________

[Context]: ______________________________________________________________

[Constraints]: __________________________________________________________

[Verification]: _________________________________________________________

**Complete Prompt:**
_____________________________________________________________________
_____________________________________________________________________
_____________________________________________________________________

---

**Questions or Need Help?**
- Workshop instructor: [Contact info]
- Claude Code docs: docs.anthropic.com
- Community: [Slack/Discord link]
