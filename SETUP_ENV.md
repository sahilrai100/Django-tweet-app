# Environment Setup Guide

## 🔐 Security Setup

### 1. Create .env File
Copy the `env_template.txt` file and rename it to `.env`:

```bash
cp env_template.txt .env
```

### 2. Update .env File
Edit the `.env` file with your actual credentials:

```env
# Django Settings
SECRET_KEY=your-secret-key-here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

# Admin Credentials
ADMIN_USERNAME=your-admin-username
ADMIN_EMAIL=your-admin-email@example.com
ADMIN_PASSWORD=your-secure-password

# Test User Credentials
TEST_USER_USERNAME=testuser
TEST_USER_PASSWORD=testpass123

# Sinchan User Credentials
SINCHAN_USERNAME=sinchan_fan
SINCHAN_PASSWORD=password123
```

### 3. Important Security Notes

#### ✅ DO:
- Keep `.env` file private and never commit it to version control
- Use strong, unique passwords for admin accounts
- Change default credentials in production
- Regularly update your secret key
- Use environment-specific .env files (.env.development, .env.production)

#### ❌ DON'T:
- Never commit `.env` files to Git
- Don't use default passwords in production
- Don't share your secret key
- Don't use the same credentials across different environments

### 4. Environment Variables Used

| Variable | Description | Default |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | django-insecure-... |
| `DEBUG` | Debug mode | True |
| `ALLOWED_HOSTS` | Allowed hosts | localhost,127.0.0.1 |
| `ADMIN_USERNAME` | Admin username | admin |
| `ADMIN_EMAIL` | Admin email | admin@tweetbar.com |
| `ADMIN_PASSWORD` | Admin password | admin123 |
| `TEST_USER_USERNAME` | Test user username | testuser |
| `TEST_USER_PASSWORD` | Test user password | testpass123 |
| `SINCHAN_USERNAME` | Sinchan user username | sinchan_fan |
| `SINCHAN_PASSWORD` | Sinchan user password | password123 |

### 5. Production Deployment

For production, create a separate `.env.production` file:

```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
ADMIN_PASSWORD=very-secure-production-password
```

### 6. Database Security

The current setup uses SQLite for development. For production:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

### 7. Email Configuration

For email functionality, update these in your .env:

```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### 8. API Keys (Future Use)

When adding external services, add API keys to .env:

```env
GOOGLE_API_KEY=your-google-api-key
AWS_ACCESS_KEY_ID=your-aws-access-key
AWS_SECRET_ACCESS_KEY=your-aws-secret-key
```

## 🚀 Quick Start

1. **Copy environment template:**
   ```bash
   cp env_template.txt .env
   ```

2. **Edit .env with your credentials**

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python chaiheadq/manage.py migrate
   ```

5. **Create superuser:**
   ```bash
   python chaiheadq/create_superuser.py
   ```

6. **Start server:**
   ```bash
   python chaiheadq/manage.py runserver 8001
   ```

## 🔒 Security Checklist

- [ ] `.env` file created and configured
- [ ] `.env` added to `.gitignore`
- [ ] Default passwords changed
- [ ] Secret key updated
- [ ] Debug mode disabled in production
- [ ] Allowed hosts configured
- [ ] CSRF settings configured
- [ ] Database credentials secured
- [ ] Email credentials configured (if needed)
- [ ] API keys secured (if using external services)

## 📝 Notes

- The `.env` file is automatically loaded by Django settings
- All sensitive information is now stored in environment variables
- The application will work with default values if `.env` is not found
- Always use different credentials for development and production 