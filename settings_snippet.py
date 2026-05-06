# ═══════════════════════════════════════════════════════════
#  Danny Codes. — Portfolio
#  Django / Alpine.js / Tailwind CSS 4 / HTMX
# ═══════════════════════════════════════════════════════════

# ── Add to INSTALLED_APPS ────────────────────────────────
INSTALLED_APPS = [
    # ...
    "portfolio",   # <- your app
]

# ── Templates ────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ── Static files ─────────────────────────────────────────
STATIC_URL  = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# ── Email (update with real credentials) ─────────────────
DEFAULT_FROM_EMAIL = "noreply@dannycodes.dev"
CONTACT_EMAIL      = "daniel@example.com"   # <- your email

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST     = "smtp.gmail.com"
EMAIL_PORT     = 587
EMAIL_USE_TLS  = True
EMAIL_HOST_USER     = ""   # set in .env
EMAIL_HOST_PASSWORD = ""   # set in .env
