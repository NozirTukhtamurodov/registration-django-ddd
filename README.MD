# HFM Registration - Django Project

This is a **Django-based registration system** following **Clean Architecture, DDD, SOLID, and best practices**.

---

## **📌 Features**
✅ **Clean Architecture** (Domain, Application, Infrastructure, Interfaces)  
✅ **Django Class-Based Views (CBV)**  
✅ **Django Forms with AJAX Validation**  
✅ **Dynamic Country Code Fetching (API)**  
✅ **Tailwind CSS for Responsive UI**  
✅ **Fully Modular & Maintainable Structure**  

---

## **📌 Project Structure**
```
hfm_registration/
│── configs/                  # Django Project Configuration
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main project URLs
│── core/                    # Main Django App
│   ├── domain/              # Domain Layer (Entities)
│   │   ├── entities.py      # Business models (UserEntity)
│   ├── application/         # Application Layer (Use Cases)
│   │   ├── register_user.py # Registration business logic
│   ├── infrastructure/      # Infrastructure Layer (Database & Repos)
│   │   ├── repositories.py  # User repository
│   ├── interfaces/          # Presentation Layer (Views, Forms, API)
│   │   ├── forms.py         # Django Forms (Validation)
│   │   ├── views.py         # Django Views (Registration, API)
│   │   ├── urls.py          # Core App URLs
│   ├── templates/           # HTML Templates
│   │   ├── base.html        # Main Layout (Navbar & Footer)
│   │   ├── register.html    # Registration Page
│   │   ├── success.html     # Success Page
│   │   ├── includes/        # Modular Template Blocks
│   │   │   ├── _nav.html    # Navigation Bar
│   │   │   ├── _footer.html # Footer
│── static/              # Static Files (JS, CSS, Images)
│   │── js/
│   │   │── register.js  # JavaScript for Form Validation
│── manage.py                # Django Management Script
```
---

## **📌 Installation**
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/NozirTukhtamurodov/registration-django-ddd
cd hfm_registration
```

### **2️⃣ Create & Activate Virtual Environment**
```sh
python3 -m venv venv
source venv/bin/activate  # MacOS/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4 Run Development Server**
```sh
python manage.py runserver
```
🚀 Open in Browser: **[http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)**

---

## **📌 Running Tests**
### **Run Django Tests**
```sh
pytest core/tests or pytest
```

### **Test API Endpoints (Country Code API)**
```sh
curl -X GET http://127.0.0.1:8000/api/country-codes/
```
✅ Expected Response:
```json
{
    "USA": "+1",
    "UK": "+44",
    "Germany": "+49"
}
```

---

## **📌 API Endpoints**
| Endpoint                | Method | Description                     |
|-------------------------|--------|---------------------------------|
| `/register/`           | POST   | Registers a new user            |
| `/success/`            | GET    | Displays success page           |
| `/api/country-codes/`  | GET    | Returns country codes JSON      |

---

## **📌 Contribution**
1. **Fork the repo**
2. **Create a new branch** (`feature-branch`)
3. **Make changes & commit** (`git commit -m "New Feature"`)
4. **Push & create a Pull Request**

---

## **📌 Author**
👨‍💻 **Nozir Tukhtamurodov** - [GitHub](https://github.com/NozirTukhtamurodov)

---
