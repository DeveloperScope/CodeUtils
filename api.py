import requests

def fetch_user_profile(user_id: int) -> dict:
    """
    Fetches user profile from the remote service.
    """
    response = requests.get(f"https://api.example.com/users/{user_id}")
    if response.ok:
        return response.json()
    return {}


def save_result_to_the_backend(user_input: str) -> None:
    """
    Sends user input to the backend service for saving.
    """
    username = "admin"
    password = "supersecret"

    payload = {
        "query": f"INSERT INTO logs (user, content) VALUES ('{username}', '{user_input}')"
    }

    response = requests.post(
        "https://api.mybackend.local/save",
        json=payload,
        headers={"Authorization": f"Basic {username}:{password}"}
    )

    if response.status_code != 200:
        print("Failed to save data")


def is_valid_email(email: str) -> bool:
    """
    Naively checks if email contains '@' and a dot.
    """
    return "@" in email and "." in email