<<<<<<< HEAD
# Danny-portfolio
Personal portfolio website showcasing my software development projects and technical expertise. Built with a focus on performance and clean UI.
=======
# 🚀 Danny Codes. — Portfolio

> A high-end, dark futuristic developer portfolio built with Django, Alpine.js, Tailwind CSS v4, and HTMX.

---

## ✨ Features

- **Custom cursor** with smooth lag-follow animation
- **Particle canvas** background with connecting lines
- **Typewriter** effect cycling through roles
- **Glassmorphism** cards with animated gradient borders on hover
- **Scroll reveal** animations for every section
- **Animated skill bars** triggered on viewport entry
- **HTMX contact form** — no page reload, smooth UX
- **Alpine.js project filter** — filter projects by category
- **Fully responsive** — mobile-first design
- **Neon glow** design system with CSS custom properties

---

## 📁 File Structure

```
danny_portfolio/
├── static/
│   ├── css/
│   │   ├── input.css        ← Tailwind v4 source (edit this)
│   │   └── output.css       ← Tailwind v4 compiled (generated)
│   └── js/
│       └── main.js          ← Alpine.js + vanilla JS
├── templates/
│   └── portfolio/
│       ├── base.html        ← Nav, footer, CDN links
│       └── index.html       ← All page sections
├── views.py                 ← Django views + context data
├── urls.py                  ← URL routing
├── settings_snippet.py      ← Settings to add to your project
└── README.md
```

---

## ⚡ Quick Setup

### 1. Install dependencies

```bash
pip install django
```

### 2. Create your Django project (if not already)

```bash
django-admin startproject mysite
cd mysite
python manage.py startapp portfolio
```

### 3. Copy files

- Copy `templates/` → `mysite/templates/`
- Copy `static/` → `mysite/static/`
- Copy `views.py` and `urls.py` → `mysite/portfolio/`

### 4. Update settings

Add the contents of `settings_snippet.py` to your `settings.py`.

### 5. Wire up URLs

In `mysite/urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    path("", include("portfolio.urls")),
]
```

### 6. Compile Tailwind CSS v4

Install the Tailwind CLI:

```bash
npm install -D tailwindcss @tailwindcss/cli
```

Compile:

```bash
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --watch
```

Or for production build:

```bash
npx @tailwindcss/cli -i ./static/css/input.css -o ./static/css/output.css --minify
```

### 7. Collect static + Run

```bash
python manage.py collectstatic
python manage.py runserver
```

---

## 🎨 Customisation

### Personal info
Edit `views.py` → update the `context` dict with your real:
- Skills and percentages
- Projects (title, description, links, stack)
- Work experience

### Colours
Edit `static/css/input.css` → `@theme {}` block to change the colour palette.

### Logo
The `<Danny/>` logo uses:
- `JetBrains Mono` font for the code look
- `c · o · d · e · s · · ·` dot ellipsis treatment for "codes"

### Contact email
Update `CONTACT_EMAIL` in settings to receive form submissions.

### Profile photo
In `index.html`, find the `<!-- Placeholder avatar -->` comment and replace with:

```html
<img src="{% static 'images/daniel.jpg' %}" alt="Daniel" class="w-full h-full object-cover rounded-2xl" />
```

---

## 🛠 Tech Stack

| Layer      | Technology                |
|------------|---------------------------|
| Backend    | Django 5.x                |
| Frontend   | Alpine.js 3.x             |
| Interactivity | HTMX 2.x              |
| Styling    | Tailwind CSS v4           |
| Fonts      | JetBrains Mono · Syne · DM Sans |
| Icons      | Inline SVG                |

---

## 📄 License

MIT — use it, customise it, make it yours.

---

*Built with ❤ by Danny Codes...*
>>>>>>> ea96ff3 (initial commit)
