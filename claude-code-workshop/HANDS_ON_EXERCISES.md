# Claude Code Workshop: Hands-On Exercises 🎯

**Duration:** 45-60 minutes total
**Difficulty:** Progressive (Easy → Medium → Advanced)

---

## **Setup Instructions**

Before starting, ensure:
- ✅ Claude Code is installed (`cc --version`)
- ✅ You've cloned the workshop repository
- ✅ You're in the project directory
- ✅ You have your API key configured

**Start Claude Code:**
```bash
cd workshop-sample-app
cc
```

---

## **Exercise 1: Code Exploration** 🔍
**Duration:** 15 minutes
**Difficulty:** ⭐ Easy
**Goal:** Get comfortable exploring an unfamiliar codebase

### **Scenario**
You've just joined a team and need to understand their e-commerce application. The codebase has no documentation, and you need to get up to speed quickly.

### **Tasks**

#### **Task 1.1: High-Level Overview (5 min)**
**Your Prompt:**
```
I'm new to this project. Give me an overview of:
1. The codebase structure (folders and their purposes)
2. Main technologies and frameworks used
3. Where the critical business logic lives
4. The architecture pattern being used
```

**Expected Outcome:**
- Understand the project structure
- Know what frameworks are used
- Identify key directories

**Success Check:**
- ✅ Can you explain the project to someone else?
- ✅ Do you know where to find user-related code?
- ✅ Do you understand the tech stack?

---

#### **Task 1.2: Authentication Flow (5 min)**
**Your Prompt:**
```
Explain how user authentication works in this codebase.
Show me:
- The login flow from frontend to backend
- Where passwords are validated
- How sessions/tokens are managed
- Which middleware protects routes
List all relevant files.
```

**Expected Outcome:**
- Understanding of the complete auth flow
- List of files involved in authentication
- Knowledge of security measures in place

**Success Check:**
- ✅ Can you draw the authentication flow?
- ✅ Do you know which files handle login?
- ✅ Can you explain how sessions work?

---

#### **Task 1.3: API Endpoints Inventory (5 min)**
**Your Prompt:**
```
List all API endpoints in this project, organized by:
- Resource type (users, products, orders, etc.)
- HTTP method (GET, POST, PUT, DELETE)
- Authentication requirement (public vs protected)
Show me which file defines each endpoint.
```

**Expected Outcome:**
- Complete API inventory
- Understanding of route structure
- Knowledge of public vs protected endpoints

**Success Check:**
- ✅ Can you find the products API routes?
- ✅ Do you know which endpoints require authentication?
- ✅ Can you identify CRUD operations for each resource?

---

### **Exercise 1: Reflection Questions**

1. How long would this exploration take manually?
2. What surprised you about the codebase?
3. What would you explore next?

**Share with the group:** One interesting thing you discovered!

---

## **Exercise 2: Bug Fix & Testing** 🐛
**Duration:** 15 minutes
**Difficulty:** ⭐⭐ Medium
**Goal:** Debug a real issue, fix it, and add tests

### **Scenario**
Users are complaining that the shopping cart sometimes shows incorrect totals. The product manager has reported: "When a user applies a discount code to items already in the cart, sometimes the total is wrong."

### **Tasks**

#### **Task 2.1: Investigation (5 min)**
**Your Prompt:**
```
Users report that shopping cart totals are incorrect when discount codes
are applied. Investigate:
1. Find the cart total calculation logic
2. Find the discount code application logic
3. Identify the bug causing incorrect totals
4. Explain what's going wrong

Focus on src/cart/ and src/services/ directories.
```

**Expected Outcome:**
- Location of the buggy code
- Understanding of what's causing the issue
- Clear explanation of the problem

**Success Check:**
- ✅ Did you find the calculation logic?
- ✅ Can you explain the bug?
- ✅ Do you understand why it happens?

---

#### **Task 2.2: Fix the Bug (5 min)**
**Your Prompt:**
```
Fix the cart total calculation bug we just identified.

Requirements:
- Fix the calculation logic to handle discounts correctly
- Ensure discounts are applied before tax calculation
- Add proper rounding (2 decimal places for currency)
- Add clear code comments explaining the fix
- Don't break existing functionality

Test your fix with these scenarios:
1. Cart with discount code
2. Cart without discount
3. Cart with multiple items and discount
```

**Expected Outcome:**
- Bug is fixed
- Code is well-commented
- Edge cases are handled

**Success Check:**
- ✅ Does the cart total calculate correctly?
- ✅ Are edge cases handled?
- ✅ Is the code easy to understand?

---

#### **Task 2.3: Add Tests (5 min)**
**Your Prompt:**
```
Add unit tests for the cart total calculation we just fixed.

Test cases:
1. Cart with single item, no discount
2. Cart with multiple items, no discount
3. Cart with 10% discount code
4. Cart with $5 off discount code
5. Cart with items that have different tax rates
6. Empty cart

Use Jest. Place tests in tests/cart.test.ts.
Follow existing test patterns in tests/ directory.
Aim for 100% coverage of the calculation function.
```

**Expected Outcome:**
- Comprehensive test suite
- All edge cases covered
- Tests pass

**Success Check:**
- ✅ Do all tests pass?
- ✅ Are edge cases tested?
- ✅ Would these tests catch the bug we just fixed?

---

### **Exercise 2: Reflection Questions**

1. How confident are you that the bug is fixed?
2. What other edge cases might exist?
3. How would you prevent this type of bug in the future?

**Share with the group:** What was the root cause of the bug?

---

## **Exercise 3: Feature Implementation** 🚀
**Duration:** 20-30 minutes
**Difficulty:** ⭐⭐⭐ Advanced
**Goal:** Build a complete feature from scratch with tests and documentation

### **Scenario**
Your product team wants to add a "Wishlist" feature. Users should be able to:
- Add products to their wishlist
- View their wishlist
- Remove items from wishlist
- Move items from wishlist to cart

This requires both backend API and frontend UI.

### **Tasks**

#### **Task 3.1: Planning (5 min)**
**Your Prompt:**
```
I need to implement a wishlist feature. Here's what's needed:

Backend:
- POST /api/wishlist (add item)
- GET /api/wishlist (get user's wishlist)
- DELETE /api/wishlist/:itemId (remove item)
- POST /api/wishlist/:itemId/move-to-cart (move to cart)

Frontend:
- Add "Add to Wishlist" button on product pages
- Create wishlist page showing all items
- Add "Move to Cart" and "Remove" buttons

Requirements:
- Users must be authenticated
- Prevent duplicate items
- Handle errors gracefully
- Add tests

Please create a detailed implementation plan:
1. List all files that need to be created/modified
2. Describe the database changes needed
3. Outline the implementation steps
4. Identify potential challenges

Don't implement yet - just plan.
```

**Expected Outcome:**
- Detailed implementation plan
- List of files to modify
- Clear step-by-step approach
- Identified potential issues

**Success Check:**
- ✅ Does the plan cover backend and frontend?
- ✅ Are database changes identified?
- ✅ Are edge cases considered?

---

#### **Task 3.2: Backend Implementation (10 min)**
**Your Prompt:**
```
Implement the wishlist backend API based on our plan:

1. Create database model/schema for wishlist items
   - Fields: userId, productId, addedAt
   - Unique constraint on (userId, productId)

2. Create wishlist routes in src/routes/wishlist.ts
   - POST /api/wishlist - Add item (requires auth)
   - GET /api/wishlist - Get items (requires auth)
   - DELETE /api/wishlist/:itemId - Remove item (requires auth)
   - POST /api/wishlist/:itemId/move-to-cart - Move to cart (requires auth)

3. Create controller in src/controllers/wishlist.ts
   - Validate product exists before adding
   - Prevent duplicates
   - Include product details when fetching wishlist
   - Handle errors with appropriate status codes

4. Add validation middleware
   - Validate productId is valid UUID/ObjectId
   - Check product exists

Follow existing patterns in src/routes/products.ts and src/controllers/products.ts.
Use the same auth middleware we use for other routes.
```

**Expected Outcome:**
- Working API endpoints
- Proper validation
- Error handling
- Follows existing code patterns

**Success Check:**
- ✅ Can you add an item to wishlist?
- ✅ Can you retrieve the wishlist?
- ✅ Does it prevent duplicates?
- ✅ Are errors handled properly?

---

#### **Task 3.3: Add Backend Tests (5 min)**
**Your Prompt:**
```
Add integration tests for the wishlist API in tests/wishlist.test.ts.

Test cases:
1. Adding item to wishlist (authenticated user)
2. Getting wishlist items (authenticated user)
3. Preventing duplicate items
4. Removing item from wishlist
5. Moving item to cart
6. Unauthorized access attempts (no auth token)
7. Adding non-existent product
8. Removing non-existent item

Use the test patterns from tests/products.test.ts.
Mock the database and auth middleware.
Ensure tests can run independently.
```

**Expected Outcome:**
- Comprehensive test coverage
- All scenarios tested
- Tests pass

**Success Check:**
- ✅ Do all tests pass?
- ✅ Are success and failure cases covered?
- ✅ Can tests run independently?

---

#### **Task 3.4: Frontend Implementation (5-10 min)**
**Your Prompt:**
```
Implement the wishlist frontend:

1. Create wishlist service in src/services/wishlist.ts
   - addToWishlist(productId)
   - getWishlist()
   - removeFromWishlist(itemId)
   - moveToCart(itemId)
   - Handle API errors and return user-friendly messages

2. Add "Add to Wishlist" button to ProductCard component
   - Heart icon that fills when clicked
   - Show loading state while adding
   - Show success message
   - Handle errors

3. Create WishlistPage component at src/pages/Wishlist.tsx
   - Display all wishlist items in a grid
   - Show product image, name, price
   - "Move to Cart" button
   - "Remove" button with confirmation
   - Empty state when wishlist is empty
   - Loading state while fetching

4. Add wishlist route to router
   - /wishlist path
   - Requires authentication

Follow the patterns in src/pages/Products.tsx and src/components/ProductCard.tsx.
Use our existing UI components from src/components/ui/.
```

**Expected Outcome:**
- Working UI components
- Proper loading and error states
- Good user experience

**Success Check:**
- ✅ Can you add items to wishlist from product page?
- ✅ Does the wishlist page display items correctly?
- ✅ Can you move items to cart?
- ✅ Are loading states shown?

---

#### **Task 3.5: Documentation (3 min)**
**Your Prompt:**
```
Document the wishlist feature:

1. Update API documentation (docs/api.md)
   - Add wishlist endpoints
   - Include request/response examples
   - Document error codes

2. Add code comments to wishlist controller
   - Explain business logic
   - Document validation rules

3. Update user-facing docs (docs/features.md)
   - How to use wishlist feature
   - Include screenshots if possible
```

**Expected Outcome:**
- Complete API documentation
- Clear code comments
- User-friendly feature documentation

**Success Check:**
- ✅ Can a new developer understand the API?
- ✅ Are business rules documented?
- ✅ Can users learn how to use the feature?

---

#### **Task 3.6: Create Pull Request (2 min)**
**Your Prompt:**
```
Create a feature branch and pull request for the wishlist feature:

1. Create branch: feature/wishlist
2. Commit all changes with clear commit message
3. Push to origin
4. Create PR with description including:
   - What was implemented
   - Testing done
   - Screenshots of UI
   - Breaking changes (if any)

Don't merge yet - just create the PR for review.
```

**Expected Outcome:**
- Clean git history
- Well-described PR
- Ready for team review

**Success Check:**
- ✅ Is the branch properly named?
- ✅ Is the commit message clear?
- ✅ Does the PR description explain the changes?

---

### **Exercise 3: Reflection Questions**

1. How long would this feature take without Claude Code?
2. What challenges did you encounter?
3. What would you improve about this implementation?
4. How confident are you deploying this to production?

**Share with the group:** Demo your working wishlist feature!

---

## **Bonus Challenges** 🎖️

If you finish early, try these:

### **Bonus 1: Performance Optimization**
```
Profile the wishlist page load time.
If it takes more than 200ms, optimize it by:
- Adding database indexes
- Implementing caching
- Lazy loading images
- Reducing API payload size
```

### **Bonus 2: Security Review**
```
Review the wishlist implementation for security issues:
- Check for authorization vulnerabilities
- Verify input validation
- Look for potential injection attacks
- Ensure rate limiting is applied
Implement fixes for any issues found.
```

### **Bonus 3: Analytics Integration**
```
Add analytics tracking for:
- When users add items to wishlist
- When users move items to cart
- Wishlist page views
- Most wishlisted products
Use our existing analytics service.
```

---

## **Workshop Wrap-Up** 🎉

### **What You've Accomplished**

✅ Explored an unfamiliar codebase quickly
✅ Debugged and fixed a real bug
✅ Added comprehensive tests
✅ Built a complete feature from scratch
✅ Created documentation
✅ Made proper git commits

### **Key Takeaways**

1. **Specificity Matters** - Detailed prompts get better results
2. **Context is King** - Reference existing patterns and files
3. **Iterate and Refine** - Don't expect perfection on first try
4. **Always Review** - AI is a tool, you're the expert
5. **Test Everything** - Don't trust code you haven't tested

### **Next Steps**

1. **Use it Daily** - Start with small tasks
2. **Build a Prompt Library** - Save your best prompts
3. **Share Learnings** - Teach your team what works
4. **Give Feedback** - Help improve the tool
5. **Stay Updated** - Features are constantly improving

---

## **Feedback Form** 📝

Help us improve this workshop!

**What worked well?**
_____________________________________________________________________

**What was confusing?**
_____________________________________________________________________

**What would you like to learn more about?**
_____________________________________________________________________

**How likely are you to use Claude Code in your daily work? (1-10)**
_____________________________________________________________________

**Additional comments:**
_____________________________________________________________________
_____________________________________________________________________

---

**Congratulations!** 🎊

You're now equipped to use Claude Code as your AI pair programmer.

**Questions?** Ask your instructor or check the resources document!

---

**Workshop Version:** 1.0
**Last Updated:** January 2026
**Instructor:** [Your contact info]
