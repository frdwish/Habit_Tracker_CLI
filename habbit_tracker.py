import time
import sys

class HabitTracker:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    @staticmethod
    def welcome_box(message):
        length = len(message)
        print("+" + "-" * (length + 4) + "+")
        print("|" + " " * (length + 4) + "|")
        print(f"|  {message}  |")
        print("|" + " " * (length + 4) + "|")
        print("+" + "-" * (length + 4) + "+")

    @staticmethod
    def animated_loading(message="Loading"):
        for _ in range(3):
            for dot in "...":
                sys.stdout.write(f"\r{message}{dot}")
                sys.stdout.flush()
                time.sleep(0.2)
        print("\r" + " " * (len(message) + 3), end="\r")  # Clear line

    def calculate_progress(self):
        if not self.tasks:
            return 0
        done_count = sum(1 for task in self.tasks if task["done"])
        return int((done_count / len(self.tasks)) * 100)

    def show_menu(self):
        self.welcome_box("Welcome to Habit Tracker App!")
        self.animated_loading("Setting up")
        time.sleep(0.5)

        while True:
            print("\n<--- SELECT OPTION -->")
            print("1. Add a Habit")
            print("2. Show Habits")
            print("3. Mark a Habit")
            print("4. Delete a Habit")
            print("5. Exit")

            choice = input("---> ")

            if choice == "1":
                try:
                    n = int(input("Enter how many habits you want to add: "))
                    for _ in range(n):
                        task = input("Enter the habit --> ")
                        self.tasks.append({"task": task, "done": False})
                        print(f"✅ {self.name} added '{task}' to Habit Tracker 🛒\n")
                        time.sleep(0.3)
                except ValueError:
                    print("❌ Please enter a valid number.")

            elif choice == "2":
                if not self.tasks:
                    print("📭 No habits added yet.")
                else:
                    print("\n📋 Your Habits:")
                    for index, task in enumerate(self.tasks):
                        status = "✅ Done" if task["done"] else "❌ Not Done"
                        print(f"{index + 1}. {task['task']} - {status}")
                    print(f"\n📈 Progress: {self.calculate_progress()}% complete")

            elif choice == "3":
                try:
                    task_index = int(input("Enter the habit number to mark as done: ")) - 1
                    if 0 <= task_index < len(self.tasks):
                        self.tasks[task_index]["done"] = True
                        print("✅ Habit marked as done.")
                        print(f"📈 Progress: {self.calculate_progress()}% complete")
                    else:
                        print("❌ Invalid habit number.")
                except ValueError:
                    print("❌ Please enter a valid number.")

            elif choice == "4":
                delete_name = input("Which habit do you want to remove? ")
                found = False
                for task in self.tasks:
                    if task["task"].lower() == delete_name.lower():
                        self.tasks.remove(task)
                        found = True
                        print(f"🗑️ '{delete_name}' removed from Habit Tracker.")
                        break
                if not found:
                    print("❌ Habit not found.")

            elif choice == "5":
                self.animated_loading("Exiting")
                print("👋 Thank you for using the Habit Tracker. Keep growing!")
                break
            else:
                print("⚠️ Invalid choice. Please try again.")

# Run the App
person1 = HabitTracker("Fardwish")
person1.show_menu()
