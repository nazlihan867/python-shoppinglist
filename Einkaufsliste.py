import sqlite3

# Verbindung zu sqlite-DB (falls nicht vorhanden ist, dann wird die erstellt.)
conn = sqlite3.connect('shoppinglist.db')

# Erstellung von Cursor um sql-Befehl durchzuführen. 
cursor = conn.cursor()

# Erstellung von Tabellen in shoppinglist.db
cursor.execute('''
CREATE TABLE IF NOT EXISTS shoppinglist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    price REAL NOT NULL, 
    amount INTEGER NOT NULL
    );
''')
# Erste Funktion hinzufügen (CREATE)
def add_shoppinglist(name, price, amount):
    cursor.execute(f'''
    INSERT INTO shoppinglist (name, price, amount) VALUES ("{name}", {price}, {amount})
    ''')
    conn.commit()
    print(f"{name} wurde hinzugefügt")

    # Erstellung von READ funktion
def show_shoppinglist():
    cursor.execute('SELECT * FROM shoppinglist')
    shoppinglist = cursor.fetchall()
    for name in shoppinglist:
        print(name)

# Update function to update shoppinglist data
def update_shoppinglist(id, name, price, amount):
    cursor.execute(f'''
    UPDATE shoppinglist SET name = "{name}", price = {price}, amount = {amount}
    WHERE id = {id}             
    ''')
    conn.commit()
    print(f"updated shoppinglist with id {id}")

# Adding a delete function to delete a shoppinglist

def delete_shoppinglist(id):
    cursor.execute(f'''
    DELETE FROM shoppinglist WHERE id = {id}                
    ''')
    conn.commit()
    print(f"shoppinglist has been deleted with id {id}")

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n----- shoppinglist -----")
        print("1. name, price, amount hinzufügen")
        print("2. shoppinglist anzeigen")
        print("3. shoppinglist aktualisieren")
        print("4. shoppinglist löschen")       
        print("5. Programm beenden")

        choice = input("Bitte wähle eine Option (1,2,3,4 oder 5): ")

        if choice == "1":
            print("Bitte gib die Daten des neuen produkt ein: ")
            name = input("name: ")
            price = input("price: ")
            amount = input("amount: ")
            add_shoppinglist(name, price, amount)
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Bitte gib die aktualisierten Daten mit id ein: ")
            id = input("id: ")
            name = input("name: ")
            price = input("price: ")
            amount = input("amount: ")
            update_shoppinglist(id, name, price, amount)
        elif choice == "4":
            print("Bitte gib die ID des zu löschenden Studentenshoppinglist ein: ")
            id = input("id: ")
            delete_shoppinglist(id)
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe! Bitte wähle 1,2,3,4 oder 5")

if __name__ == "__main__":
    main()