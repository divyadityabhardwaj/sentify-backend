from app import app as application  # Rename app to application for Gunicorn

if __name__ == "__main__":
    application.run()
