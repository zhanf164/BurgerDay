from sqlalchemy import MetaData, Table, create_engine


engine = create_engine(f"postgresql://{user}:{password}@{host}/{DBname}")

metadata_obj = MetaData()

class DBModel:
    def __init__(self, metadata_obj, engine):
        self.User = Table("User", metadate_obj, autoload_with=engine)
        self.Preferences = Table("Preferences", metadata_obj, autoload_with=engine)