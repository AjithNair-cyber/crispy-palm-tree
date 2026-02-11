import json
import asyncio


# 1️⃣ Mutable default argument bug
def add_item(item, collection=[]):
    collection.append(item)
    return collection


# 2️⃣ Logical bug (wrong formula)
def calculate_discount(price, discount_percent):
    # Should reduce price, but incorrectly increases it
    return price + (price * discount_percent / 100)


# 3️⃣ Division without guard
def calculate_ratio(a, b):
    return a / b


# 4️⃣ Unsafe dictionary access
def get_user_email(user):
    return user["email"].lower()


# 5️⃣ Type issue (string + int)
def increment_counter(counter):
    return counter + "1"


# 6️⃣ Async misuse
async def fetch_data():
    await asyncio.sleep(1)
    return {"status": "success"}


def call_async_function():
    result = fetch_data()  # Missing await
    return result["status"]


# 7️⃣ Attribute error
def process_items(items):
    items.append(100)
    return items.upper()


# 8️⃣ Poor exception handling
def parse_json(data):
    try:
        return json.loads(data)
    except:
        return None


# 9️⃣ KeyError
def get_config_value(config):
    return config["database"]["host"]


# 🔟 NameError
def print_total():
    print(total_amount)


# Trigger block for demo
if __name__ == "__main__":
    print(add_item(1))
    print(add_item(2))

    print(calculate_discount(100, 10))
    print(calculate_ratio(10, 0))

    user = {"name": "Ajith"}
    print(get_user_email(user))

    print(increment_counter(5))
    print(call_async_function())

    print(process_items([1, 2, 3]))

    print(parse_json("{invalid_json"))

    config = {}
    print(get_config_value(config))

    print_total()
