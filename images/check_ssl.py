import ssl

try:
    print(ssl.get_default_verify_paths())
except Exception as e:
    print(f"Error: {e}")
