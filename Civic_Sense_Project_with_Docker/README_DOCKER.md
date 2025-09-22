# 🐳 Civic Sense Project - Docker Deployment

This guide will help you deploy the Civic Sense project using Docker on any Windows computer.

## 📋 Prerequisites

- **Docker Desktop** for Windows
- **Docker Compose** (included with Docker Desktop)
- **Git** (optional, for cloning the repository)

### Installation Links
- **Docker Desktop**: https://www.docker.com/products/docker-desktop/
- **Git**: https://git-scm.com/download/win

## 🚀 Quick Start

### Step 1: Download/Clone the Project
```bash
# If you have Git installed
git clone <repository-url>
cd Civic_Sense_Project

# Or simply copy the project folder to your new computer
```

### Step 2: Run with Docker Compose
```bash
# Start all services (PHP, MySQL, phpMyAdmin)
docker-compose up -d

# Or build and start
docker-compose up --build -d
```

### Step 3: Access the Application
- **Main Application**: http://localhost:8080
- **phpMyAdmin**: http://localhost:8081
- **MySQL Database**: localhost:3306

## 🛠️ Docker Services

### 1. Web Application (PHP + Apache)
- **Container**: `civic_sense_web`
- **Port**: 8080
- **Technology**: PHP 8.3 + Apache
- **Features**: URL rewriting, security headers

### 2. MySQL Database
- **Container**: `civic_sense_mysql`
- **Port**: 3306
- **Version**: MySQL 8.0
- **Database**: `civic_sense_db`
- **Credentials**:
  - Username: `civic_user`
  - Password: `civic_password`
  - Root Password: `root_password`

### 3. phpMyAdmin (Optional)
- **Container**: `civic_sense_phpmyadmin`
- **Port**: 8081
- **Purpose**: Database management interface

## 📁 Project Structure

```
Civic_Sense_Project/
├── docker/
│   ├── apache-config.conf    # Apache configuration
│   └── mysql-init/
│       └── 01-init.sql       # Database initialization
├── config/
│   ├── database_docker.php   # Docker database config
│   ├── database_sqlite.php   # Local SQLite config
│   └── database.php          # Original MySQL config
├── Dockerfile                # PHP application container
├── docker-compose.yml        # Multi-container setup
├── .dockerignore            # Files to exclude from Docker
└── README_DOCKER.md         # This file
```

## 🔧 Configuration

### Environment Variables
The application automatically detects Docker environment and uses these variables:

```env
DB_HOST=mysql
DB_NAME=civic_sense_db
DB_USER=civic_user
DB_PASS=civic_password
```

### Database Connection
- **Local Development**: Uses SQLite (`database_sqlite.php`)
- **Docker Environment**: Uses MySQL (`database_docker.php`)

## 📊 Database Management

### Access phpMyAdmin
1. Open http://localhost:8081
2. Login with:
   - Server: `mysql`
   - Username: `civic_user`
   - Password: `civic_password`

### Direct MySQL Access
```bash
# Connect to MySQL container
docker exec -it civic_sense_mysql mysql -u civic_user -p civic_sense_db

# Or using root
docker exec -it civic_sense_mysql mysql -u root -p
```

## 🚀 Common Commands

### Start Services
```bash
# Start all services
docker-compose up -d

# Start with logs
docker-compose up

# Rebuild and start
docker-compose up --build -d
```

### Stop Services
```bash
# Stop all services
docker-compose down

# Stop and remove volumes (WARNING: This deletes database data)
docker-compose down -v
```

### View Logs
```bash
# View all logs
docker-compose logs

# View specific service logs
docker-compose logs web
docker-compose logs mysql
```

### Access Container Shell
```bash
# Access web container
docker exec -it civic_sense_web bash

# Access MySQL container
docker exec -it civic_sense_mysql bash
```

## 🔄 Development Workflow

### Making Changes
1. Edit files in your local project directory
2. Changes are automatically reflected in the container (volume mount)
3. Refresh browser to see changes

### Database Changes
1. Make changes to `docker/mysql-init/01-init.sql`
2. Recreate containers: `docker-compose down && docker-compose up --build -d`

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Check what's using the port
netstat -an | findstr :8080
netstat -an | findstr :3306

# Stop conflicting services or change ports in docker-compose.yml
```

### Database Connection Issues
```bash
# Check if MySQL is running
docker-compose logs mysql

# Restart MySQL
docker-compose restart mysql
```

### Permission Issues
```bash
# Fix file permissions
docker-compose exec web chown -R www-data:www-data /var/www/html
```

### Container Won't Start
```bash
# Check logs
docker-compose logs web

# Rebuild container
docker-compose build --no-cache web
```

## 📦 Backup & Restore

### Backup Database
```bash
# Create backup
docker exec civic_sense_mysql mysqldump -u civic_user -pcivic_password civic_sense_db > backup.sql
```

### Restore Database
```bash
# Restore from backup
docker exec -i civic_sense_mysql mysql -u civic_user -pcivic_password civic_sense_db < backup.sql
```

## 🌐 Production Deployment

### Environment Variables
Create a `.env` file for production:
```env
DB_HOST=your_mysql_host
DB_NAME=your_database_name
DB_USER=your_username
DB_PASS=your_secure_password
```

### Security Considerations
1. Change default passwords
2. Use environment variables for sensitive data
3. Enable SSL/TLS in production
4. Regular security updates

## 📱 Application Features

- ✅ **Responsive Design** - Works on all devices
- ✅ **User Authentication** - Login/Register system
- ✅ **Problem Reporting** - Report civic issues
- ✅ **Solution Sharing** - Share and find solutions
- ✅ **Community Forum** - Discussion platform
- ✅ **Admin Panel** - Manage content and users
- ✅ **Database Management** - Full CRUD operations

## 🎯 Default Access

### Application URLs
- **Home**: http://localhost:8080
- **Problems**: http://localhost:8080/?page=problems
- **Solutions**: http://localhost:8080/?page=solutions
- **Forum**: http://localhost:8080/?page=forum
- **Resources**: http://localhost:8080/?page=resources
- **Contact**: http://localhost:8080/?page=contact
- **Login**: http://localhost:8080/?page=login
- **Register**: http://localhost:8080/?page=register

### Default Admin Account
- **Username**: admin
- **Email**: admin@civicsense.org
- **Password**: password (change in production!)

## 🎉 Success!

Your Civic Sense project is now running in Docker! The application is fully containerized and can be easily deployed on any Windows computer with Docker installed.

## 📞 Support

If you encounter any issues:
1. Check the logs: `docker-compose logs`
2. Verify all services are running: `docker-compose ps`
3. Check port availability
4. Ensure Docker Desktop is running
