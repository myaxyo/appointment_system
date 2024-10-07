from appointment_system import AppointmentSystem
from helpers import get_user_input, get_date_input, get_time_input


def book():
    appointment_system = AppointmentSystem()

    while True:
        print("\n--- Appointment System ---")
        print("1. Add Appointment")
        print("2. View Appointments")
        print("3. Update Appointment")
        print("4. Delete Appointment")
        print("5. Exit")

        choice = get_user_input("Enter your choice (1-5): ")

        if choice == "1":
            title = get_user_input("Enter appointment title: ")
            date = get_date_input()
            time = get_time_input()
            description = get_user_input("Enter appointment description: ")
            email = get_user_input("Enter your email address: ")
            appointment_system.add_appointment(title, date, time, description, email)

        elif choice == "2":
            appointment_system.view_appointments()

        elif choice == "3":
            appointment_system.view_appointments()
            try:
                index = (
                    int(
                        get_user_input("Enter the index of the appointment to update: ")
                    )
                    - 1
                )
                if index < 0 or index >= len(appointment_system.appointments):
                    raise ValueError

                title = get_user_input("Enter new title: ")
                date = get_date_input()
                time = get_time_input()
                description = get_user_input("Enter new description: ")
                email = get_user_input("Enter your email address: ")
                appointment_system.update_appointment(
                    index, title, date, time, description, email
                )
            except ValueError:
                print("Invalid input. Please enter a valid appointment number.")

        elif choice == "4":
            appointment_system.view_appointments()
            try:
                index = (
                    int(
                        get_user_input("Enter the index of the appointment to delete: ")
                    )
                    - 1
                )
                if index < 0 or index >= len(appointment_system.appointments):
                    raise ValueError
                email = get_user_input("Enter your email address: ")
                appointment_system.delete_appointment(index, email)
            except ValueError:
                print("Invalid input. Please enter a valid appointment number.")

        elif choice == "5":
            print("Thank you for using the Appointment System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
