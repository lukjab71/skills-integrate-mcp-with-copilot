from src.models import Base, engine

# Tworzy tabele w bazie danych na podstawie modeli
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Baza danych i tabele zostały utworzone.")
