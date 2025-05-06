# 🗃️ Inventory Manager 

A command-line inventory management tool built in Python, designed for small-scale stock tracking with built-in validation, logging, and CSV persistence.

---

## ✨ Features

- 📦 Add new products with price and quantity
- 🔍 Search for products
- 📝 Update existing product information
- ❌ Delete products from inventory
- 📄 View the full inventory
- 🚫 Input validation using a banned word list
- 🕒 Logs every operation to a CSV file

---

## 📁 File Structure

















inventory/
├── inventory.csv # Stores the current inventory data
├── logs.csv # Logs all user operations
├── invalid.txt # List of banned product names
├── inventory.py # Main application logic
























🧠 Validation & Logging
Products are checked against invalid.txt — any match will raise a custom RiskError.

Actions (add, update, delete, etc.) are logged with timestamps in logs.csv.

🛠️ Requirements
No external dependencies — pure Python. Works out of the box with:

Python 3.6+

CSV file support

















$ python inventory.py
select a following option
1 add products
2 show complete
3 update
4 delete
5 search
6 quit
>>>: 1
please enter the name of your product: apples
please enter the price: 0.99
please enter the quantity: 100
product successfully added!














👨‍💻 Author
Developed by Hitham Hauter










