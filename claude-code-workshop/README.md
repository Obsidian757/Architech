# Claude Code Workshop - Setup Guide 🎓

**Workshop Duration:** 2-3 hours
**Target Audience:** Software Development Teams
**Instructor Guide & Participant Setup Instructions**

---

## **📦 What's Included**

This workshop package contains everything you need to run a successful Claude Code training session:

```
claude-code-workshop/
├── README.md                    # This file - setup instructions
├── WORKSHOP_AGENDA.md           # Complete workshop timeline
├── PROMPT_LIBRARY.md            # 50+ ready-to-use prompts
├── HANDS_ON_EXERCISES.md        # 3 progressive exercises
├── QUICK_REFERENCE.md           # One-page cheat sheet
├── RESOURCES.md                 # Post-workshop materials
└── sample-app/                  # Practice codebase (see below)
```

---

## **🎯 Workshop Objectives**

By the end of this workshop, participants will:

1. ✅ Understand what Claude Code is and what it can do
2. ✅ Know how to write effective prompts
3. ✅ Have hands-on experience with real-world tasks
4. ✅ Feel confident using Claude Code in daily work
5. ✅ Have a library of prompts for common tasks

---

## **👥 For Instructors: Pre-Workshop Checklist**

### **2 Weeks Before**

- [ ] **Schedule the workshop**
  - Book conference room with projector/screen
  - Send calendar invites
  - Confirm participant count

- [ ] **Prepare sample codebase**
  - Option A: Use the provided sample-app
  - Option B: Prepare a sanitized version of team's actual code
  - Ensure it has some intentional "bugs" for exercises

- [ ] **Arrange API access**
  - Option A: Request workshop API keys from Anthropic
  - Option B: Have participants bring their own API keys
  - Prepare backup keys in case of issues

- [ ] **Review materials**
  - Customize exercises for team's tech stack
  - Add team-specific use cases to examples
  - Update contact info in all documents

### **1 Week Before**

- [ ] **Send pre-workshop email to participants** (see template below)
- [ ] **Test the sample app**
  - Clone and run locally
  - Verify all exercises work
  - Test on different OS (Mac, Windows, Linux)

- [ ] **Prepare environment**
  - Test Claude Code installation
  - Verify all demos work
  - Prepare screen recording software (backup plan)

### **2 Days Before**

- [ ] **Send reminder email** with setup verification steps
- [ ] **Print materials** (optional, can be digital)
  - Prompt Library (1 per participant)
  - Quick Reference Cheat Sheet (1 per participant)
  - Exercise Guide (1 per participant)

### **Day Of**

- [ ] **Arrive 30 min early**
- [ ] **Test equipment**
  - Projector/screen sharing
  - Audio (if virtual)
  - Internet connection
  - Have mobile hotspot as backup

- [ ] **Prepare demonstration**
  - Open terminal with Claude Code ready
  - Have sample prompts ready to copy-paste
  - Open browser tabs with resources

---

## **📧 Pre-Workshop Email Template**

**Subject:** Claude Code Workshop - Setup Instructions (Action Required)

**Body:**

> Hi team!
>
> Looking forward to our Claude Code workshop on [DATE] at [TIME] in [LOCATION/VIDEO LINK].
>
> **Please complete these setup steps BEFORE the workshop** (takes ~15 minutes):
>
> ### Required Setup
>
> 1. **Install Node.js 18 or higher**
>    - Download: https://nodejs.org/
>    - Verify: Open terminal and run `node --version`
>    - Should show v18.0.0 or higher
>
> 2. **Install Git**
>    - Download: https://git-scm.com/downloads
>    - Verify: Run `git --version`
>
> 3. **Install Claude Code**
>    ```bash
>    npm install -g @anthropic-ai/claude-code
>    ```
>    - Verify: Run `cc --version`
>
> 4. **Clone the workshop repository**
>    ```bash
>    git clone [WORKSHOP_REPO_URL]
>    cd claude-code-workshop/sample-app
>    npm install
>    ```
>
> 5. **API Key Setup**
>    - Option A: I'll provide API keys at the workshop
>    - Option B: Get your own key at https://console.anthropic.com/
>    - You'll enter this during the workshop
>
> 6. **Verify Everything Works**
>    ```bash
>    cd claude-code-workshop/sample-app
>    cc
>    ```
>    - If prompted for API key, enter it
>    - Type: "What is this project?"
>    - You should get a response about the e-commerce sample app
>    - Type `/exit` to quit
>
> ### Recommended
>
> - Install VS Code (or your preferred editor)
> - Have a second screen if possible (one for code, one for Claude)
>
> ### Troubleshooting
>
> If you run into any issues, please:
> 1. Check the troubleshooting section in the repo README
> 2. Reach out to me: [YOUR_CONTACT]
> 3. We'll have 15 min at the start for setup help
>
> ### What to Bring
>
> - Laptop with terminal access
> - Curiosity and questions!
>
> See you at the workshop!
>
> [YOUR_NAME]

---

## **👨‍💻 For Participants: Setup Instructions**

### **Prerequisites**

- Computer with macOS, Linux, or Windows
- Terminal/Command Prompt access
- Internet connection
- 15 minutes for setup

### **Step 1: Install Node.js**

**Check if already installed:**
```bash
node --version
```

If you see v18.0.0 or higher, skip to Step 2.

**Install Node.js:**
- Go to https://nodejs.org/
- Download the LTS version (18.x or higher)
- Run the installer
- Verify: `node --version`

### **Step 2: Install Git**

**Check if already installed:**
```bash
git --version
```

If you see a version number, skip to Step 3.

**Install Git:**
- Go to https://git-scm.com/downloads
- Download for your OS
- Run the installer
- Verify: `git --version`

### **Step 3: Install Claude Code**

```bash
npm install -g @anthropic-ai/claude-code
```

**Note:** On Mac/Linux, you might need `sudo`:
```bash
sudo npm install -g @anthropic-ai/claude-code
```

**Verify installation:**
```bash
cc --version
```

You should see a version number like `1.x.x`

### **Step 4: Get API Key**

**Option A: Use Workshop-Provided Key**
- Your instructor will provide this at the workshop

**Option B: Get Your Own Key**
1. Go to https://console.anthropic.com/
2. Sign up or log in
3. Navigate to API Keys section
4. Create a new key
5. Copy it somewhere safe (you won't see it again!)

### **Step 5: Clone Workshop Repository**

```bash
git clone [WORKSHOP_REPO_URL]
cd claude-code-workshop/sample-app
npm install
```

This might take a few minutes to download dependencies.

### **Step 6: Test Claude Code**

```bash
cd claude-code-workshop/sample-app
cc
```

**First time setup:**
- You'll be prompted to enter your API key
- Paste your key and press Enter
- It will be saved for future use

**Test it works:**
Type this prompt:
```
What is this project and what technologies does it use?
```

You should get a response explaining the sample e-commerce app.

**Exit Claude Code:**
```
/exit
```

### **✅ You're Ready!**

If all steps worked, you're ready for the workshop!

---

## **🔧 Troubleshooting**

### **Issue: "npm: command not found"**

**Cause:** Node.js not installed or not in PATH

**Solution:**
1. Reinstall Node.js from https://nodejs.org/
2. Restart your terminal
3. Try again

---

### **Issue: "Permission denied" when installing Claude Code**

**Cause:** No permission to install global npm packages

**Solution (Mac/Linux):**
```bash
sudo npm install -g @anthropic-ai/claude-code
```

**Solution (Windows):**
- Run Command Prompt as Administrator
- Run the install command again

---

### **Issue: "cc: command not found"**

**Cause:** Global npm bin folder not in PATH

**Solution (Mac/Linux):**
Add to your `~/.bashrc` or `~/.zshrc`:
```bash
export PATH="$PATH:$(npm config get prefix)/bin"
```
Then run: `source ~/.bashrc` (or `~/.zshrc`)

**Solution (Windows):**
1. Find npm global folder: `npm config get prefix`
2. Add that path to your System Environment Variables
3. Restart terminal

---

### **Issue: "API key invalid"**

**Cause:** Incorrect API key or expired key

**Solution:**
1. Verify you copied the entire key
2. Check there are no extra spaces
3. Try generating a new key
4. Contact instructor for workshop key

---

### **Issue: "Error: Cannot connect to API"**

**Cause:** Network/firewall issues

**Solution:**
1. Check your internet connection
2. Try on a different network
3. Check if company firewall blocks api.anthropic.com
4. Contact IT or instructor

---

### **Issue: Sample app won't install**

**Cause:** Dependency issues or wrong Node.js version

**Solution:**
```bash
# Ensure Node.js 18+
node --version

# Clear npm cache
npm cache clean --force

# Try installing again
cd claude-code-workshop/sample-app
rm -rf node_modules package-lock.json
npm install
```

---

### **Still Having Issues?**

**During workshop:** Flag the instructor for help
**Before workshop:** Contact [INSTRUCTOR_EMAIL]
**In general:** Check docs at https://docs.anthropic.com/

---

## **🏗️ Sample App Overview**

The workshop includes a sample e-commerce application with:

- **Backend:** Node.js + Express + PostgreSQL
- **Frontend:** React + TypeScript
- **Features:** Products, Cart, Checkout, Auth
- **Intentional bugs:** For the bug-fixing exercise
- **Missing features:** For the implementation exercise

**Structure:**
```
sample-app/
├── src/
│   ├── components/      # React components
│   ├── services/        # Business logic
│   ├── routes/          # API routes
│   ├── controllers/     # Request handlers
│   └── utils/           # Helper functions
├── tests/               # Test files
├── docs/                # Documentation
└── package.json
```

---

## **🎭 Workshop Delivery Tips**

### **For Instructors**

**Opening (First 5 min):**
- Introduce yourself
- Set expectations
- Quick icebreaker: "What's your biggest pain point in development?"

**During Demos:**
- Type prompts slowly and narrate what you're thinking
- Show both good and bad prompts
- Let Claude "fail" occasionally to show iteration
- Emphasize the review step

**During Exercises:**
- Circulate and help
- Note common questions for group discussion
- Encourage participants to help each other
- Have backup solutions ready

**Handling Questions:**
- "Great question! Let me demo that..."
- "What prompt would you use for that?"
- "Let's see what Claude suggests..."

**Energy Management:**
- Take breaks every 45-50 min
- Mix lecture with hands-on
- Encourage stretch and water breaks
- End on a high note (show something impressive)

---

## **📊 Workshop Success Metrics**

Track these to measure impact:

**Immediate:**
- % completing all exercises
- Average satisfaction score
- Number of engaged questions

**Week 1:**
- Number of participants using Claude Code
- Types of tasks being done
- Questions/issues encountered

**Week 4:**
- % of team regularly using it
- Time saved on common tasks
- Feature velocity improvement

---

## **🎁 Post-Workshop**

**Day 1:**
- [ ] Send recording (if recorded)
- [ ] Send feedback survey
- [ ] Share additional resources
- [ ] Offer 1-on-1 help sessions

**Week 1:**
- [ ] Follow up on adoption
- [ ] Collect success stories
- [ ] Address common questions
- [ ] Share team best practices

**Month 1:**
- [ ] Measure impact
- [ ] Plan advanced workshop
- [ ] Update materials based on feedback

---

## **📞 Support & Resources**

**Official Resources:**
- Documentation: https://docs.anthropic.com/
- API Console: https://console.anthropic.com/
- GitHub: https://github.com/anthropics/claude-code

**Workshop Materials:**
- Repository: [WORKSHOP_REPO_URL]
- Instructor: [YOUR_CONTACT]
- Team Channel: [SLACK/TEAMS_CHANNEL]

---

## **📝 Feedback & Improvements**

This is a living workshop! Please share feedback:

- What worked well?
- What was confusing?
- What exercises were most valuable?
- What should be added/removed?
- How can we improve?

Submit feedback: [FEEDBACK_FORM_URL] or [INSTRUCTOR_EMAIL]

---

## **📄 License & Usage**

This workshop material is provided for:
- Internal team training
- Customer workshops
- Educational purposes

Feel free to:
- Customize for your team
- Add your own examples
- Modify exercises
- Share with clients

Please:
- Keep attribution
- Share improvements back
- Report issues

---

## **🙏 Credits**

Created by: [YOUR_NAME]
Company: [YOUR_COMPANY]
Date: January 2026
Version: 1.0

Based on Claude Code by Anthropic

---

## **🚀 Ready to Run the Workshop?**

**Quick Pre-Workshop Checklist:**

- [ ] All participants completed setup
- [ ] Sample app tested and working
- [ ] API keys distributed
- [ ] Materials printed or shared digitally
- [ ] Demos prepared and tested
- [ ] Backup plan ready (offline materials)
- [ ] Energy drinks acquired ☕

**Let's teach some developers how to code faster!** 🎉

---

**Questions before the workshop?**
Contact: [YOUR_EMAIL] | [YOUR_PHONE] | [YOUR_SLACK]

**During workshop issues?**
Flag the instructor immediately - we're here to help!

**After workshop questions?**
Check RESOURCES.md or reach out anytime!
