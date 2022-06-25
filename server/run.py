from app import app, db

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    db.create_all()
    app.run(host='0.0.0.0', port=port, debub=True)
