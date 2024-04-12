from sqlmodel import SQLModel, create_engine


filepath = "/assets/database.sqlite"
url = f"sqlite://{filepath}"


engine = create_engine(url, echo=True)
SQLModel.metadata.create_all(engine)
