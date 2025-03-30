## 💡 Inspiration

We were inspired by the daily struggles of splitting bills while living with roommates. Typing itemized bills into Excel or trying to split shared groceries manually often led to confusion and unfairness. We wanted a faster, fairer, and more intuitive way to divide expenses—no spreadsheets, no arguments.

## ⚙️ What It Does

**D-SplitBill** is a smart receipt-splitting app built for roommates and groups who frequently share expenses. Here's what it does:

- **Uploads a receipt image** from a recent purchase (groceries, food delivery, etc.)
- **Uses OCR (Optical Character Recognition)** to extract item names and prices automatically
- **Displays all the items with checkboxes** beside each roommate’s name
- Users simply **select the items they bought**, including shared items
- The app **calculates the split** based on selections and divides shared items evenly
- Finally, it **displays who owes how much to whom** in a clear and fair way

## 🏗️ How We Built It

We built **D-SplitBill** using the following technologies and workflow:

- **Backend:** Python with Flask, handling routes, sessions, and processing logic
- **Frontend:** HTML, CSS (with Jinja2 templating), designed for clarity and ease of use
- **OCR Integration:** Asprise OCR API to process uploaded receipt images and extract item-level data
- **Storage:** Temporary in-memory session storage to keep track of usernames and items
- **Data Handling:** Logic to assign costs based on user selections, handling shared items dynamically

### Basic Flow:

```python
1. User submits form with roommate names and receipt
2. Flask receives the image and sends it to OCR API
3. OCR returns JSON with items and prices
4. Flask renders items.html with checkboxes for each roommate
5. User selections are posted to /split
6. App calculates the split and renders the result
```

## 🚧 Challenges We Ran Into

- **Inconsistent Receipt Formats:** OCR had to work across a wide variety of receipt layouts. Some were blurry, some had missing data, and others used abbreviations or vague item names.
- **Handling Shared Items:** It wasn’t as simple as just assigning costs one-to-one. We had to design logic to split items evenly when multiple people selected them, and ensure rounding errors were minimized.
- **User Experience (UX):** We wanted it to be intuitive—even for people who aren't tech-savvy. Designing a clean, checkbox-driven interface with clear result output was essential, and we had to iterate to get it right.
- **Session Management:** Keeping track of user data and items between routes without a database was tricky, but we opted for session-based storage for simplicity.

## 🏆 Accomplishments That We're Proud Of

- **OCR Integration:** Successfully turning raw receipt images into structured, usable data.
- **Fair Cost Splitting:** Implementing a clean and logical system for evenly dividing shared items.
- **Fully Functional Flow:** A complete, working app from upload → item selection → split result, with no manual entry.
- **User-Centric Design:** Building something people actually *want* to use, especially for everyday roommate situations.

## 📚 What We Learned

- **Working with OCR APIs** and the limitations of machine-read data
- **Flask Session Handling** to maintain user state across routes
- **Designing for Simplicity**, especially when dealing with multiple users and shared data
- **Real-World Problem Solving** by thinking about how people actually behave when splitting costs
- **Balancing Automation & Control**—letting the app do the work but keeping users in charge of selections

## 🚀 What’s Next for D-SplitBill

We see a lot of potential to evolve **D-SplitBill** into a full-featured platform. Some upcoming ideas include:

- 🔐 **User Authentication** – Let users log in, track past receipts, and manage their history  
- 🧾 **Editable Items** – Allow users to correct OCR errors or adjust item names/prices manually  
- 🤝 **"Who Paid?" Feature** – Mark who paid the bill so others know who to reimburse  
- 📱 **Mobile Version or PWA** – Make it super convenient to use on the go  
- 📤 **Shareable Summary or PDF Export** – So users can download or share the split result  
- 🌓 **Dark Mode Toggle & Animations** – Improve visual experience and accessibility  

```
