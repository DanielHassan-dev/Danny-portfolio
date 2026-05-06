from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings


def index(request):
    context = {
        # ── Skills ──────────────────────────────────────
        "backend_skills": [
            {"name": "Django / DRF",   "level": 95},
            {"name": "Python",          "level": 93},
            {"name": "PostgreSQL",      "level": 88},
            {"name": "REST API Design", "level": 90},
            {"name": "Redis / Celery",  "level": 78},
        ],
        "frontend_skills": [
            {"name": "HTMX",           "level": 90},
            {"name": "Alpine.js",       "level": 88},
            {"name": "Tailwind CSS",    "level": 95},
            {"name": "HTML / CSS",      "level": 98},
            {"name": "JavaScript (ES6+)","level": 82},
        ],
        "tools": [
            "Git", "Docker", "Nginx", "Gunicorn",
            "GitHub Actions", "Linux", "VS Code",
            "Figma", "Postman", "AWS S3",
        ],
        "learning": [
            "Deno", "Astro", "Edge Functions", "WebSockets",
        ],

        # ── Projects ────────────────────────────────────
        "project_filters": [
            {"label": "All",      "value": "all"},
            {"label": "Web App",  "value": "webapp"},
            {"label": "API",      "value": "api"},
            {"label": "Tool",     "value": "tool"},
        ],
        "projects": [
            {
                "title":       "SaaSKit Pro",
                "emoji":       "🚀",
                "type":        "SaaS Boilerplate",
                "category":    "webapp",
                "description": "Production-ready Django SaaS boilerplate with Stripe billing, multi-tenancy, team management, and a full HTMX-powered dashboard.",
                "stack":       ["Django", "HTMX", "Alpine.js", "Stripe", "Postgres"],
                "github":      "https://github.com",
                "live":        "https://example.com",
            },
            {
                "title":       "Realtime Chat API",
                "emoji":       "💬",
                "type":        "WebSocket API",
                "category":    "api",
                "description": "Django Channels-powered real-time messaging API with JWT auth, rooms, read receipts, and presence indicators.",
                "stack":       ["Django Channels", "Redis", "JWT", "REST"],
                "github":      "https://github.com",
                "live":        None,
            },
            {
                "title":       "DevFlow CMS",
                "emoji":       "📝",
                "type":        "Content Platform",
                "category":    "webapp",
                "description": "A minimal, developer-first CMS built with Django and HTMX. Live preview, markdown support, and a clean Alpine.js editor UI.",
                "stack":       ["Django", "HTMX", "Alpine.js", "Tailwind"],
                "github":      "https://github.com",
                "live":        "https://example.com",
            },
            {
                "title":       "CLI Deploy Tool",
                "emoji":       "⚡",
                "type":        "Developer Tool",
                "category":    "tool",
                "description": "A Python CLI that automates Django deployments to any VPS — configures Nginx, Gunicorn, SSL, and environment variables in one command.",
                "stack":       ["Python", "Click", "Nginx", "Gunicorn"],
                "github":      "https://github.com",
                "live":        None,
            },
            {
                "title":       "Inventory Manager",
                "emoji":       "📦",
                "type":        "Web Application",
                "category":    "webapp",
                "description": "Full-featured inventory and order management system for SMEs, featuring HTMX-powered live search, barcode scanning, and PDF reports.",
                "stack":       ["Django", "HTMX", "Postgres", "WeasyPrint"],
                "github":      "https://github.com",
                "live":        "https://example.com",
            },
            {
                "title":       "Open Finance API",
                "emoji":       "💰",
                "type":        "Public REST API",
                "category":    "api",
                "description": "RESTful API delivering currency rates, stock summaries, and crypto tickers — with caching, rate limiting, and a developer docs portal.",
                "stack":       ["DRF", "Redis", "Celery", "Swagger"],
                "github":      "https://github.com",
                "live":        None,
            },
        ],

        # ── Experience ──────────────────────────────────
        "experience": [
            {
                "title":       "Senior Full-Stack Engineer",
                "company":     "Acme Tech Ltd.",
                "period":      "2022 – Present",
                "description": "Lead backend architecture for a multi-tenant SaaS platform serving 80k+ users. Migrated monolith to service-oriented Django apps, reducing API response times by 60%.",
                "stack":       ["Django", "DRF", "Redis", "PostgreSQL", "Docker"],
            },
            {
                "title":       "Full-Stack Developer",
                "company":     "CreativeStudio Agency",
                "period":      "2019 – 2022",
                "description": "Built 20+ client web applications from scratch. Championed the HTMX + Alpine.js workflow, eliminating the need for heavy JS frameworks on most projects.",
                "stack":       ["Django", "HTMX", "Alpine.js", "Tailwind", "AWS"],
            },
            {
                "title":       "Backend Developer",
                "company":     "FinTech Startup",
                "period":      "2017 – 2019",
                "description": "Developed RESTful APIs for mobile banking features, integrated third-party payment gateways, and built robust Celery task pipelines for async processing.",
                "stack":       ["Django", "DRF", "Celery", "PostgreSQL", "Stripe"],
            },
            {
                "title":       "Junior Web Developer",
                "company":     "Digital Solutions Co.",
                "period":      "2015 – 2017",
                "description": "Started my professional career building Django MVT applications and learning the craft of clean, maintainable Python code.",
                "stack":       ["Django", "Python", "jQuery", "MySQL"],
            },
        ],
    }
    return render(request, "portfolio/index.html", context)


@require_POST
def contact(request):
    """HTMX contact form handler."""
    name    = request.POST.get("name", "").strip()
    email   = request.POST.get("email", "").strip()
    subject = request.POST.get("subject", "Portfolio Contact").strip()
    message = request.POST.get("message", "").strip()

    if name and email and message:
        try:
            send_mail(
                subject=f"[Portfolio] {subject} — from {name}",
                message=f"From: {name} <{email}>\n\n{message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.CONTACT_EMAIL],
                fail_silently=False,
            )
            return HttpResponse(status=204)  # HTMX: no content, JS handles the UI
        except Exception:
            return HttpResponse("Something went wrong. Please try again.", status=500)

    return HttpResponse("Please fill in all required fields.", status=400)
