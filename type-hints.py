def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

def greeting(name: str) -> str:
    return 'Hello ' + name

print(get_full_name("john", "doe"))

print(greeting('Mike'))