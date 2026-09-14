# 🏦 Banking System Using Django

<p align="center">
  <img src="https://img.shields.io/badge/Framework-Django%205.2.8-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20Bootstrap-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Database-SQLite-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Prototype-informational?style=for-the-badge">
</p>

<p align="center">
  A secure, full-stack banking web application built using Django.
</p>

---

## 📌 Project Overview

The **Banking System** is a web-based financial management system developed using **Django 5.2.8**.
It simulates real-world banking operations including account handling, transaction processing, and administrative monitoring.

This project demonstrates:

* Backend architecture using Django
* Secure authentication system
* Database relationship modeling
* Financial transaction workflow implementation
* Admin monitoring and reporting system

---

# 🚀 Key Features

## 👤 User Functionalities

* User Registration & Login
* Profile Management
* Balance Checking
* Deposit Money
* Withdraw Money
* Transfer Funds
* View Transaction History

## 🔐 Admin Functionalities

* User Management (Create, Update, Delete)
* Monitor All Transactions
* System Activity Log Tracking
* Generate Reports
* Dashboard Analytics

---

# 🛠️ Tech Stack

| Layer               | Technology                |
| ------------------- | ------------------------- |
| **Frontend**        | HTML5, CSS3, Bootstrap 5  |
| **Backend**         | Python 3.11, Django 5.2.8 |
| **Database**        | SQLite (Development)      |
| **Version Control** | Git & GitHub              |

---

# 🗄️ Database Structure

## 📊 Tables Overview

| Table Name       | Description                                       |
| ---------------- | ------------------------------------------------- |
| **User**         | Stores authentication credentials                 |
| **BankAccount**  | Stores account number and current balance         |
| **Transaction**  | Records deposit, withdrawal, and transfer details |
| **UserActivity** | Logs login, logout, and system activities         |

## 🔗 Relationships

```
User (1) ─── (1) BankAccount
User (1) ─── (M) Transaction
User (1) ─── (M) UserActivity
```

---

# 🔐 Security Implementation

* Password hashing (Django authentication system)
* CSRF protection
* Session-based login authentication
* Role-based access control
* Input validation and ORM-based database queries
* Activity logging for monitoring

---

# 📊 System Modules

## 1️⃣ Authentication Module

* Register
* Login
* Logout
* Profile Update

## 2️⃣ Banking Operations Module

* Deposit Funds
* Withdraw Funds
* Transfer Funds
* Balance Validation
* Transaction Recording

## 3️⃣ Reporting Module

* Transaction Summary
* User Reports
* Daily Activity Overview
* Admin Monitoring Dashboard

---

# 🖥️ Dashboard Views

| User Dashboard        | Admin Dashboard       |
| --------------------- | --------------------- |
| Balance Overview      | System Monitoring     |
| Personal Transactions | All User Transactions |
| Quick Banking Actions | User Management       |
| Profile Settings      | Reports & Logs        |

---

### 📊 System Design & Diagrams

This section presents the Use Case Diagram and ER Diagram of the Banking System.
# 🔷 Use Case Diagram
| User Use Cases           | Admin Use Cases            |
| ------------------------ | -------------------------- |
| Register                 | Create User                |
| Login                    | Update User                |
| Logout                   | Delete User                |
| Check Balance            | View All Transactions      |
| Deposit Money            | Generate Reports           |
| Withdraw Money           | Track Login/Logout History |
| Transfer Funds           |                            |
| View Transaction History |                            |
| Update Profile           |                            |


<p align="center"> <img src="images/usecase.png" width="850"> </p>

### 🔷 ER Diagram (Entity Relationship Diagram)

# 📌 Overview

The ER Diagram represents the database structure of the Banking System.
It defines entities, attributes, and relationships to ensure proper data organization.

# 🗂️ Entity Structure
| Entity Name      | Primary Key    | Description                                          |
| ---------------- | -------------- | ---------------------------------------------------- |
| **User**         | id             | Stores authentication and personal details           |
| **BankAccount**  | account_number | Stores account details and balance                   |
| **Transaction**  | transaction_id | Records deposit, withdrawal, and transfer operations |
| **UserActivity** | activity_id    | Logs login, logout, and system activities            |

# 🔗 Relationship Mapping
| Relationship        | Cardinality | Explanation                                |
| ------------------- | ----------- | ------------------------------------------ |
| User → BankAccount  | 1 : 1       | Each user owns exactly one bank account    |
| User → Transaction  | 1 : Many    | A user can perform multiple transactions   |
| User → UserActivity | 1 : Many    | A user can generate multiple activity logs |

# 🖼️ ER Diagram
<p align="center"> <img src="banking/images/mermaid-diagram.png" width="900"> </p>


# 📦 Installation Guide

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Niraj-Bhatta/bank_system.git
cd bank_system
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

---

## 5️⃣ Run Development Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```

---

# 📈 Future Enhancements

* Payment Gateway Integration
* Email & SMS Notifications
* Two-Factor Authentication (2FA)
* REST API Integration
* Cloud Deployment
* Advanced Analytics Dashboard

---

# 🤝 Contribution Guidelines

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Developer

| Field       | Details                                                            |
| ----------- | ------------------------------------------------------------------ |
| **Name**    | Niraj Bhatta                                                       |
| **Role**    | Engineering Student / Developer                                    |
| **College** | Nepal College of Information Technology                            |
| **GitHub**  | [https://github.com/Niraj-Bhatta](https://github.com/Niraj-Bhatta) |
| **Email**   | [bhattaniraj559@gmail.com](mailto:bhattaniraj559@gmail.com)        |

---

<p align="center">
⭐ If you find this project useful, consider giving it a star.
</p>
