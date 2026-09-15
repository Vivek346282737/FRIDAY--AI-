from services.process_service import open_app, close_app


print("=" * 60)
print("PROCESS SERVICE TEST")
print("=" * 60)


apps = [
    "notepad",
    "calculator",
    "chrome"
]


for app in apps:

    print()
    print(f"TESTING OPEN: {app}")

    result = open_app(app)

    print(result)


print()
print("=" * 60)
print("INVALID APP TEST")
print("=" * 60)

result = open_app(
    "this_app_should_not_exist_123"
)

print(result)
