def transactional(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print("Transaction committed")
            return result
        except Exception as e:
            print("Transaction rolled back")
            raise e
    return wrapper

@transactional
def update_database(record):
    # Simulate database update
    if record == "bad":
        raise ValueError("Simulated error")
    print(f"Updated record: {record}")

update_database("good")
update_database("bad")
