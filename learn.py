def display_menu( ):
    print("\nPersonal Diary Application")
    print("1. Add a new diary entry")
    print("2. View all diary entries")
    print("3. Search for entries by keyword")
    print("4. Exit")

def add_entry(entries):
       date = input("Enter the date (DD-MM-YYYY): ")
       content = input("Enter your dream entry: ")
       entry = {"date": date, "content": content}
       entries.append(entry)
       print("Dream entry added.")

def view_all_entries(entries):
    if not entries:
        print("No entries found.")
    else:
       for i, entry in enumerate(entries, start=1):
           print(f"\nEntry {i}")
           print(f"Date: {entry['date']}")
           print(f"Content: {entry['content']}")
           found = True

def search_entries(entries):
    keyword = input("Enter keyword: ")
    found = False
    for i, entry in enumerate(entries, start=1):
        if keyword.lower() in entry['content'].lower():
            print(f"\nEntry {i}:")
            print(f"Date: {entry['date']}")
            print(f"Content: {entry['content']}")
            found = True
    if not found:
        print("No entries found with this keyword.")
def main():
    entries = []
    while True:
        display_menu()
        option = input("Choose an option: ")
        if option == '1':
             add_entry(entries)
        elif option == '2':
            view_all_entries(entries)
        elif option == '3':
            search_entries(entries)
        elif option == '4':
            print("Goodbye!")
            break
        else:
            print("invalid choice. Please try again.")

if __name__== "__main__":
    main()