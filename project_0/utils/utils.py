import json
import os

class JournalFuncs():
    def __init__(self):
        self.FILE_PATH = "entries.json"
        self.entries = self.load_entries()

    def load_entries(self):
        if os.path.exists(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as file:
                return json.load(file)
        return []

    def save_entries(self):
        with open(self.FILE_PATH, 'w') as file:
            json.dump(self.entries, file, indent=4)

    def add_entry(self):
        title = input("Enter the title of your journal entry: ")
        content = input("Enter the content of your journal entry: ")
        entry = {"title": title, "content": content}
        self.entries.append(entry)
        self.save_entries()
        print("Journal entry added!")

    def view_entries(self):
        if not self.entries:
            print("No entries found.")
            return
        for index, entry in enumerate(self.entries):
            print(f"{index + 1}. {entry['title']}")
            print(f"   {entry['content']}\n")

    def delete_entry(self):
        self.view_entries()
        if not self.entries:
            return
        index = int(input("Enter the number of the entry you want to delete: ")) - 1
        if 0 <= index < len(self.entries):
            self.entries.pop(index)
            self.save_entries()
            print("Journal entry deleted!")
        else:
            print("Invalid entry number.")      

    def edit_entry(self):
        self.view_entries()
        if not self.entries:
            return
        
        for _ in range(3):
            print()

        index = int(input("Enter the number of the entry you want to edit: ")) - 1
        if 0 <= index < len(self.entries):
            # Fetch the existing entry
            old_entry = self.entries[index]
            
            # Display the current entry
            print(f"Editing Entry: {old_entry['title']}")
            print(f"Current Content: {old_entry['content']}")
            
            # Prompt for action: append or replace
            action = input("Do you want to append new content (A) or replace entire content (R)? ").upper()
            
            # Process user choice
            if action == 'A':
                new_content = input("Enter new content to append: ")
                old_entry['content'] += " " + new_content  # Append new content
            elif action == 'R':
                new_content = input("Enter new content (this will replace existing): ")
                old_entry['content'] = new_content  # Replace entire content
            else:
                print("Invalid action. Keeping current content.")
            
            # Save updated entries
            self.save_entries()
            print("Entry updated successfully!")
        else:
            print("Invalid entry number.")
