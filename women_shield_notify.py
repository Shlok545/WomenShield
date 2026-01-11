# women_shield_notify.py
# WomenShield demo using winotify (stable)

from winotify import Notification

def main():
    print("=== WomenShield AI Filter Demo ===")

    while True:
        msg = input("\nEnter your message (or type 'exit' to quit): ")
        if msg.lower() == "exit":
            print("Exiting WomenShield demo...")
            break

        # Safe message
        if "kill" not in msg.lower():
            toast = Notification(app_id="WomenShield",
                                 title="WomenShield",
                                 msg=f"Message: {msg}\nAbsurdness chance = 0",
                                 duration="short")
            toast.show()
            print(f"Message delivered: {msg}")

        # Suspicious message
        else:
            toast = Notification(app_id="WomenShield",
                                 title="WomenShield Alert",
                                 msg="Suspicious content detected!\nAbsurdness chance = 1",
                                 duration="short")
            toast.show()
            print("⚠️ Suspicious message detected.")
            choice = input("Do you want to reveal the message? (yes/no): ").strip().lower()

            if choice == "yes":
                toast = Notification(app_id="WomenShield",
                                     title="Message Revealed",
                                     msg=f"{msg}\nAbsurdness chance = 1",
                                     duration="short")
                toast.show()
                print(f"Message revealed: {msg}")
            else:
                toast = Notification(app_id="WomenShield",
                                     title="Message Blocked",
                                     msg="You chose not to see the message.",
                                     duration="short")
                toast.show()
                print("Message blocked.")

if __name__ == "__main__":
    main()
