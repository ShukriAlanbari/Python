from logistics_system import AdminMenu
import os


class Main():
    def main_menu(self):

        MAINMENU = \
            '''
     > Logistics System <

    1. Admin Menu
    2. User Menu
    3. > Unknown <
    4. > Unknown <
    5. Exit
            '''
        print(MAINMENU)

    def run(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice (1-5): ")
            os.system("cls")  # Clear the screen (you can use os.system("clear") on Linux)

            if choice == "1":
                admin_menu = AdminMenu()  # Create an instance of AdminMenu
                admin_menu.run()  # Run the AdminMenu
                
            elif choice == "2":
                # Implement User Menu
                print("User Menu is not implemented yet.")
            
            elif choice == "3":
                # Handle the "< Unknown >" option
                print("Option 3 is not implemented yet.")
            
            elif choice == "4":
                # Handle the "< Unknown >" option
                print("Option 4 is not implemented yet.")
            
            elif choice == "5":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main = Main()
    main.run()



run= Main()
run.run()