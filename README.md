# Django Bookstore Application

This project is a simple web application built with Django that demonstrates the Model-View-Template (MVT) design pattern, user authentication, an admin panel, and integration with a PostgreSQL database. It allows users to manage a collection of books with full CRUD (Create, Read, Update, Delete) functionality.

## Features

* **Book Management:**
    * Display a list of books with individual cards (including View, Update, Delete buttons).
    * View detailed information for a single book.
    * Create new book entries via a dedicated form.
    * Update existing book details through an editable form.
    * Delete books, removing them from the database.
* **User Authentication & Authorization:**
    * User registration (Sign Up) page.
    * User login and logout functionality, redirecting to appropriate pages.
    * Permission-based access: Only specific authorized users can create new books.
* **Admin Panel:** Utilizes Django's built-in administrative interface for easy data management of books and users.
* **Database Integration:** Connects to a PostgreSQL database using Django's ORM (Object-Relational Mapper).
* **Responsive Design:** Designed with basic responsiveness for various screen sizes.

## Technologies Used

* **Backend:** Python 3.8+, Django 5.x
* **Database:** PostgreSQL
* **Frontend:** HTML, CSS (with basic styling, potentially enhanced with a framework like Tailwind CSS if desired in future iterations)

## Screenshots

Here are some screenshots showcasing the application's functionality:

### Book List Page
![WhatsApp Image 2025-06-21 at 2 21 54 AM](https://github.com/user-attachments/assets/08fc00b7-65f2-4302-b55e-5796854e3ab9)


### Create New Book Form
![WhatsApp Image 2025-06-21 at 2 22 55 AM](https://github.com/user-attachments/assets/d31aa400-cc70-45ea-9644-eeafb3ffa096)


### Update Book Form
![WhatsApp Image 2025-06-21 at 2 22 34 AM](https://github.com/user-attachments/assets/1de3aad6-7c09-4cb5-859d-e6e0cac13d59)


### Login Page
![WhatsApp Image 2025-06-21 at 2 20 15 AM](https://github.com/user-attachments/assets/1a17e7ad-4c20-4204-80df-ae65e5bc5a67)

### Sign Up Page
![WhatsApp Image 2025-06-21 at 2 21 24 AM](https://github.com/user-attachments/assets/041cb936-7275-4242-9d47-ba1d2d262a81)


### Admin Panel
![WhatsApp Image 2025-06-21 at 2 28 04 AM](https://github.com/user-attachments/assets/5b9a3141-ea28-4e23-802f-a50a0e5e963b)





## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Prerequisites

* Python 3.8+
* pip (Python package installer)
* PostgreSQL installed and running

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone [https://github.com/kerolosNabil247/django-bookstore-app.git]
cd django-bookstore-app
```
### 2. Create a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies:

```bash
python -m venv venv
```
### 3. Activate the Virtual Environment

* On Windows:

```bash
.\venv\Scripts\activate
```
* On macOS/Linux:

```bash
source venv/bin/activate
```
### 4. Install Dependencies
* Install all required Python packages. These are listed in the requirements.txt file.

```bash
pip install -r requirements.txt
```
