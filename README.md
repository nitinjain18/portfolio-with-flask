# Flask Portfolio Website

## Overview
This is a personal portfolio website built with **Flask**, HTML, and CSS. 
It includes a homepage, contact form, and an admin panel to view messages.

## Features
- Homepage with personal info
- Contact form for visitors to send messages
- Messages stored in CSV (`messages.csv`)
- Admin login (username: `admin`, password: `password123`)
- Admin panel to view all submitted messages
- Logout option for admin

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/portfolio-flask.git
cd portfolio-flask
```

### 2. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

Activate it:
- **Windows (PowerShell):**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python app.py
```

### 5. Open in Browser
- Homepage: `http://127.0.0.1:5000/`
- Contact form: `http://127.0.0.1:5000/contact`
- Admin login: `http://127.0.0.1:5000/login`
- View messages after login: `http://127.0.0.1:5000/admin/messages`

## Notes
- You can update admin credentials in `app.py` under the login route.
- Messages are stored in `messages.csv`.
- You can enhance the project with CSS styling or deploy online (Heroku, Render, PythonAnywhere).
