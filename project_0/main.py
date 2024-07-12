from utils.utils import JournalFuncs

def main():
    journal = JournalFuncs()
    while True:
        print("\nJournal App")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Edit Entry")
        print("4. Delete Entry")
        print("5. Exit")
        for _ in range(1):
            print()

        choice = input("Enter your choice: ")

        if choice == '1':
            print()
            journal.add_entry()
        elif choice == '2':
            print()
            journal.view_entries()
        elif choice == '3':
            print()
            journal.edit_entry()
        elif choice == '4':
            print()
            journal.delete_entry()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()