Banking System using Django






Table of Contents

Project Overview

Features

Technologies Used

Database Design

Functional Modules

Screenshots

Installation

Usage

Future Enhancements

Contributing

License

Project Overview

Banking System is a web-based application built using Django to simulate real-world banking operations. It allows users to:

Register, log in, and manage accounts

Deposit, withdraw, and transfer funds

Track transaction history

Admins can manage users, monitor transactions, and generate reports. Security, data integrity, and user-friendly design are core priorities.

Features
Feature Type	User Features	Admin Features
Account Management	Register/Login, View Balance, Update Profile	Manage Users (CRUD), Monitor Accounts
Transactions	Deposit, Withdraw, Transfer, Transaction History	View All Transactions, Generate Reports
Security	Password Hashing, Session-based Login	Role-Based Access, Activity Logs
Technologies Used
Category	Tools/Frameworks
Frontend	HTML5, CSS3, Bootstrap 5
Backend	Python 3.11, Django 5.2.8
Database	SQLite (Dev), PostgreSQL/MySQL (Optional)
Version Control	Git, GitHub
Database Design

Tables Overview:

Table Name	Purpose	Key Fields
User	Stores user credentials	id, username, email, password
BankAccount	Stores account info & balance	account_number, user_id, balance
Transaction	Records deposits, withdrawals, transfers	transaction_id, from_account, to_account, amount, date
UserActivity	Logs user actions	user_id, action, timestamp

ER Diagram:


Replace this placeholder with your actual ER diagram image.

Functional Modules
1. User Authentication

Purpose: Secure user access and profile management.

Key Actions: Register, Login, Logout, Profile Update

Action	Description
Register	Create a new account
Login	Authenticate user credentials
Logout	End user session
Update Info	Modify profile details

Flow Diagram:

2. Bank Account

Purpose: Maintain accounts and balances for users.

Features:

Unique account number

Balance tracking

Link to a user

Field	Description
Account Number	Unique account ID
User	Linked user
Balance	Current balance

Diagram:

3. Transactions

Purpose: Handle all banking operations.

Features: Deposit, Withdraw, Transfer, Track Transaction History

Field	Description
Transaction ID	Unique identifier
From Account	Sender (nullable for deposits)
To Account	Receiver (nullable for withdrawals)
Type	Deposit / Withdraw / Transfer
Amount	Transaction amount
Timestamp	Date and time of transaction

Flow Diagram:

4. Dashboard

Purpose: Central interface for users and admins.

Section	User View	Admin View
Account Summary	Own account balance	Overview of all accounts
Transactions	Personal transaction history	All transactions
Quick Actions	Deposit, Withdraw, Transfer	Admin actions (monitor, report)
Reports	N/A	Generate reports
Activity Logs	N/A	User activity monitoring

Dashboard Diagram:

5. Security & User Activity

Purpose: Protect the system and log actions.

Features:

Password hashing and secure login

Role-based access

Activity logging

Field	Description
User ID	Which user performed the action
Action	Login, Deposit, Withdraw, Transfer
Timestamp	When the action occurred
Status	Success / Failure

Diagram:

6. Reports & Analytics

Purpose: Generate insights for admins.

Reports:

User Report (All accounts and balances)

Transaction Report (Deposits, Withdrawals, Transfers)

Daily Summary (Total daily transactions)

Custom Report (Filter by date, user, account)

Diagram:

Screenshots
Page	Screenshot
Home Page	

User Dashboard	

Transactions Page	

Admin Dashboard	

Replace placeholders with actual screenshots from your project.

Installation

Clone the repo:

git clone https://github.com/yourusername/bank_system.git
cd bank_system

Create & activate virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create superuser:

python manage.py createsuperuser

Run server:

python manage.py runserver

Open browser: http://127.0.0.1:8000

Usage

Users: Register → Login → Perform Transactions → View History

Admins: Login → Manage Accounts → Monitor Transactions → Generate Reports

Future Enhancements

Real payment gateway integration

Email/SMS notifications for transactions

Two-factor authentication (2FA)

Advanced analytics dashboard

Fully mobile-responsive UI

Contributing

Fork the repository

Create branch: git checkout -b feature/YourFeature

Commit: git commit -m "Add feature"

Push: git push origin feature/YourFeature

Open Pull Request

License

This project is licensed under MIT License. See LICENSE
 for details.
