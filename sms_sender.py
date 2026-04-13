from twilio.rest import Client

import os
# Replace these placeholders with your real Twilio credentials.
# Instead of: account_sid = 'your_twilio_sid_here'
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('AUTH_TOKEN')

# Replace these placeholders with valid phone numbers in E.164 format.
FROM_PHONE_NUMBER = "+16416706313"
TO_PHONE_NUMBER = "+9779811874247"


def main() -> None:
    # Create the Twilio client using your account SID and auth token.
    client = Client(account_sid, auth_token)

    # Send the SMS message and print the returned message SID.
    message = client.messages.create(
        body="Hello, Sanjeet u doing great keep it up",
        from_=FROM_PHONE_NUMBER,
        to=TO_PHONE_NUMBER,
        status_callback="https://thud-pacifist-gatherer.ngrok-free.dev/sms-status"

    )

    print(f"Message sent. SID: {message.sid}")
    print(f"SID: {message.sid}")
    print(f"Status: {message.status}")

if __name__ == "__main__":
    main()
