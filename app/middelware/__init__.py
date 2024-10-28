from sqlalchemy import create_engine
from flask import request, g
from sqlalchemy.exc import OperationalError
from app.api.models.models import Base  # Ensure you import your Base here
from sqlalchemy.orm import sessionmaker


class TenantConnectionMiddleware:
    def __init__(self, app):
        self.app = app

    def __call__(self):
        tenant_id = request.headers.get("tenant-id")

        if not tenant_id:
            return "Please provide tenant-id", 400

        # Construct this url using environment var
        # Don't hardcode the db scerets here
        db_url = f"postgresql://postgres:password3@localhost/db_tenant_{tenant_id}"

        try:
            engine = create_engine(db_url)
            Base.metadata.bind = engine

            Base.metadata.create_all(engine)
            g.engine = engine
            Session = sessionmaker(bind=g.engine)
            g.ssession = Session()
            print(f"Connected to tenant database: {db_url}")
        except OperationalError as e:
            print("Database connection error:", e)
            return "Database does not exist or connection failed.", 500
        
        