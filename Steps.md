# 🚀 Civic Sense Project - Complete Setup Guide

## 📋 Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Setup](#project-setup)
3. [Database Configuration](#database-configuration)
4. [Running the Application](#running-the-application)
5. [Testing the Application](#testing-the-application)
6. [Troubleshooting](#troubleshooting)
7. [Customization](#customization)
8. [Deployment](#deployment)

---

## 🎯 Prerequisites

### **Required Software**
- **PHP 8.0+** (Recommended: PHP 8.3.0)
- **Web Browser** (Chrome, Firefox, Safari, Edge)
- **Text Editor** (VS Code, Sublime Text, Notepad++)

### **Optional Software**
- **XAMPP** (Alternative to standalone PHP)
- **MySQL Server** (If you prefer MySQL over SQLite)
- **Git** (For version control)

---

## 🛠️ Project Setup

### **Step 1: Download/Clone the Project**
```bash
# Option 1: Download ZIP from GitHub
# - Go to your GitHub repository
# - Click "Code" → "Download ZIP"
# - Extract to your desired location

# Option 2: Clone with Git
git clone https://github.com/yourusername/civic-sense-project.git
cd civic-sense-project
```

### **Step 2: Verify Project Structure**
Ensure your project has this structure:
```
Civic_Sense_Project/
├── assets/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
├── config/
│   ├── database.php (MySQL version)
│   └── database_sqlite.php (SQLite version)
├── database/ (will be created automatically)
├── includes/
│   ├── functions.php
│   ├── header.php
│   └── footer.php
├── pages/
│   ├── home.php
│   ├── problems.php
│   ├── solutions.php
│   ├── forum.php
│   ├── resources.php
│   ├── contact.php
│   ├── login.php
│   └── register.php
├── index.php
├── README.md
└── Steps.md
```

---

## 🗄️ Database Configuration

### **Option 1: SQLite (Recommended for Quick Start)**

#### **Step 1: Enable SQLite Extensions**
1. **Locate PHP Installation**:
   ```bash
   # Find your PHP installation
   where php
   # or
   Get-Command php | Select-Object Source
   ```

2. **Edit php.ini File**:
   - Navigate to your PHP directory (e.g., `C:\php-8.3.0\`)
   - Copy `php.ini-development` to `php.ini`
   - Edit `php.ini` and make these changes:

   ```ini
   ; Set extension directory
   extension_dir = "C:\php-8.3.0\ext"
   
   ; Enable required extensions
   extension=pdo_sqlite
   extension=sqlite3
   ```

3. **Verify Extensions**:
   ```bash
   php -m | findstr sqlite
   ```

#### **Step 2: Configure SQLite Database**
1. **Update index.php**:
   ```php
   // Change this line in index.php
   require_once 'config/database_sqlite.php';
   ```

2. **Database Directory**:
   - The `database/` folder will be created automatically
   - SQLite database file: `database/civic_sense.db`

### **Option 2: MySQL (Alternative)**

#### **Step 1: Install XAMPP**
1. Download XAMPP from: https://www.apachefriends.org/download.html
2. Install with default settings
3. Start Apache and MySQL services

#### **Step 2: Create Database**
1. Open: http://localhost/phpmyadmin
2. Create new database: `civic_sense_db`
3. Login: `root` / `` (empty password)

#### **Step 3: Configure MySQL**
1. **Edit index.php**:
   ```php
   // Change this line in index.php
   require_once 'config/database.php';
   ```

2. **Update config/database.php**:
   ```php
   define('DB_HOST', 'localhost');
   define('DB_NAME', 'civic_sense_db');
   define('DB_USER', 'root');
   define('DB_PASS', '');
   ```

---

## 🚀 Running the Application

### **Method 1: PHP Built-in Server (Recommended)**

#### **Step 1: Open Command Prompt**
```bash
# Windows
Win + R → cmd → Enter

# Or PowerShell
Win + X → Windows PowerShell
```

#### **Step 2: Navigate to Project**
```bash
cd "C:\Users\yourusername\Desktop\Civic_Sense_Project"
# or your actual project path
```

#### **Step 3: Start Server**
```bash
php -S localhost:8000
```

#### **Step 4: Access Application**
- Open browser: http://localhost:8000
- Server will show: "PHP 8.3.0 Development Server started"

### **Method 2: XAMPP (Alternative)**

#### **Step 1: Move Project to XAMPP**
```bash
# Copy project to XAMPP htdocs
copy "Civic_Sense_Project" "C:\xampp\htdocs\civic_sense"
```

#### **Step 2: Start XAMPP Services**
- Open XAMPP Control Panel
- Start Apache and MySQL
- Ensure both show green status

#### **Step 3: Access Application**
- Open browser: http://localhost/civic_sense/

---

## 🧪 Testing the Application

### **Step 1: Verify Home Page**
- URL: http://localhost:8000/
- Should display: "Civic Sense: Urgent Need of Society"
- Check all navigation links work

### **Step 2: Test Database Connection**
```bash
# Test SQLite connection
php test_sqlite.php

# Expected output:
# ✓ PDO SQLite extension is loaded
# ✓ SQLite database connection successful!
# ✓ Test query successful: 1
# ✓ Tables found: 0 (will be created on first access)
```

### **Step 3: Test All Pages**
Navigate through each section:
- **Home**: `/?page=home`
- **Problems**: `/?page=problems`
- **Solutions**: `/?page=solutions`
- **Forum**: `/?page=forum`
- **Resources**: `/?page=resources`
- **Contact**: `/?page=contact`
- **Login**: `/?page=login`
- **Register**: `/?page=register`

### **Step 4: Test User Registration**
1. Go to: `/?page=register`
2. Fill registration form
3. Verify account creation
4. Test login functionality

### **Step 5: Test Core Features**
- Report a civic problem
- Add a solution
- Create forum post
- Submit contact form

---

## 🔧 Troubleshooting

### **Common Issues & Solutions**

#### **Issue 1: "Connection failed: could not find driver"**
**Cause**: PDO extensions not enabled
**Solution**:
```bash
# Check if extensions are loaded
php -m | findstr pdo

# Enable extensions in php.ini
extension=pdo_sqlite
extension=sqlite3
```

#### **Issue 2: "Unable to load dynamic library"**
**Cause**: Wrong extension directory path
**Solution**:
```ini
# In php.ini, set correct path
extension_dir = "C:\php-8.3.0\ext"
```

#### **Issue 3: "No such column: p.user_id"**
**Cause**: Database tables not created
**Solution**:
- Access application in browser
- Tables are auto-created on first access
- Check `database/civic_sense.db` exists

#### **Issue 4: "Port 8000 already in use"**
**Cause**: Another service using port 8000
**Solution**:
```bash
# Kill existing PHP processes
taskkill /f /im php.exe

# Or use different port
php -S localhost:8080
```

#### **Issue 5: "Page not found"**
**Cause**: File paths or routing issues
**Solution**:
- Verify all files exist in correct locations
- Check file permissions
- Ensure `.php` extensions are correct

### **Debug Mode**
Enable error reporting in `index.php`:
```php
<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);
session_start();
// ... rest of code
```

---

## 🎨 Customization

### **Modifying Content**
1. **Text Content**: Edit files in `pages/` directory
2. **Styling**: Modify `assets/css/style.css`
3. **Functionality**: Update `assets/js/main.js`
4. **Database**: Edit `config/database_sqlite.php`

### **Adding New Features**
1. **New Page**: Create file in `pages/` directory
2. **Add Route**: Update routing in `index.php`
3. **Database Table**: Add to `createTables()` function
4. **Functions**: Extend `includes/functions.php`

### **Theme Customization**
```css
/* In assets/css/style.css */
:root {
    --primary-color: #007bff;
    --secondary-color: #6c757d;
    --success-color: #28a745;
    --danger-color: #dc3545;
    --warning-color: #ffc107;
    --info-color: #17a2b8;
}
```

---

## 🚀 Deployment

### **Local Development**
- Use PHP built-in server: `php -S localhost:8000`
- Database: SQLite (file-based)
- No external dependencies

### **Production Server**
1. **Upload Files**: Transfer to web server
2. **Database**: Use MySQL or PostgreSQL
3. **Web Server**: Apache/Nginx with PHP
4. **Security**: HTTPS, proper file permissions

### **Docker Deployment**
```dockerfile
FROM php:8.3-apache
RUN docker-php-ext-install pdo pdo_sqlite
COPY . /var/www/html/
EXPOSE 80
```

---

## 📱 Application Features

### **Core Functionality**
- ✅ User Authentication (Register/Login)
- ✅ Civic Problem Reporting
- ✅ Solution Management
- ✅ Community Forum
- ✅ Educational Resources
- ✅ Contact & Issue Reporting
- ✅ Responsive Design
- ✅ Search & Filter
- ✅ Like/Comment System

### **Technical Features**
- ✅ PDO Database Abstraction
- ✅ Session Management
- ✅ Input Sanitization
- ✅ AJAX Interactions
- ✅ Bootstrap 5.3.0 UI
- ✅ Font Awesome Icons
- ✅ Google Fonts
- ✅ Mobile-First Design

---

## 🔒 Security Considerations

### **Input Validation**
- All user inputs are sanitized
- SQL injection protection via PDO
- XSS prevention with `htmlspecialchars()`

### **Authentication**
- Password hashing with `password_hash()`
- Session-based authentication
- CSRF protection recommended

### **File Permissions**
- Database directory: Read/Write for web server
- Config files: Read-only for web server
- Uploads: Restricted directory access

---

## 📚 Additional Resources

### **Documentation**
- [PHP Documentation](https://www.php.net/docs.php)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [Bootstrap Documentation](https://getbootstrap.com/docs/)
- [PDO Documentation](https://www.php.net/manual/en/book.pdo.php)

### **Support**
- **GitHub Issues**: Report bugs in your repository
- **Community Forums**: Stack Overflow, Reddit
- **Documentation**: Check README.md for project details

---

## 🎯 Quick Start Checklist

- [ ] Download/Clone project
- [ ] Install PHP 8.0+
- [ ] Enable PDO SQLite extensions
- [ ] Configure database settings
- [ ] Start PHP server
- [ ] Access application
- [ ] Test all features
- [ ] Create user account
- [ ] Report test problem
- [ ] Verify database tables

---

## 🏆 Success Indicators

Your Civic Sense application is successfully running when:
- ✅ Home page loads without errors
- ✅ All navigation links work
- ✅ User registration succeeds
- ✅ Database tables are created
- ✅ No PHP errors in browser
- ✅ Responsive design works on mobile
- ✅ All CRUD operations function

---

## 📞 Need Help?

If you encounter issues:
1. Check this troubleshooting section
2. Verify all prerequisites are met
3. Check PHP error logs
4. Ensure file permissions are correct
5. Test database connection separately
6. Create GitHub issue with error details

---

**🎉 Congratulations! You've successfully set up the Civic Sense project!**

The application is now ready to help raise awareness about civic sense and provide a platform for community engagement and problem-solving.
