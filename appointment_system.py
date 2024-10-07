from dotenv import load_dotenv
import os
import json
import re
from datetime import timedelta
from appointment import Appointment
from helpers import verify_date_time, str_to_datetime
from email_sender.main import email_sender
from email_sender.templates import (
    new_appointment_template,
    update_appointment_template,
    cancel_appointment_template,
)

load_dotenv()


class AppointmentSystem:
    def __init__(self, filename="appointments.json"):
        self.filename = filename
        self.appointments = []
        self.load_appointments()

    @staticmethod
    def is_valid_email(email):
        """Validate email address using regex."""
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None

    def is_conflicting(self, new_start, new_end, exclude_index=None):
        for i, appointment in enumerate(self.appointments):
            if i == exclude_index:
                continue
            existing_start = str_to_datetime(appointment.date, appointment.time)
            existing_end = existing_start + timedelta(hours=1)

            if new_start < existing_end and new_end > existing_start:
                return True
        return False

    def load_appointments(self):
        try:
            with open(self.filename, "r") as file:
                data = json.load(file)
                self.appointments = []
                for appointment_data in data:
                    if "email" not in appointment_data:
                        appointment_data["email"] = os.getenv("DEFAULT_EMAIL")
                    self.appointments.append(Appointment(**appointment_data))
        except FileNotFoundError:
            self.appointments = []

    def save_appointments(self):
        with open(self.filename, "w") as file:
            json.dump(
                [appointment.to_dict() for appointment in self.appointments],
                file,
                indent=2,
            )

    def add_appointment(self, title, date, time, description, email):
        if not verify_date_time(date, time):
            print("Error: The appointment date and time cannot be in the past.")
            return

        new_start = str_to_datetime(date, time)
        new_end = new_start + timedelta(hours=1)

        if self.is_conflicting(new_start, new_end):
            print("Error: This appointment conflicts with an existing appointment.")
            return
        if email and not self.is_valid_email(email):
            print("Error: Invalid email address provided.")
            return
        new_appointment = Appointment(title, date, time, description, email)
        self.appointments.append(new_appointment)
        self.save_appointments()
        print("Appointment added successfully.")

        if email:
            subject = "New Appointment Booked"
            body = new_appointment_template(title, date, time, description)
            try:
                email_sender(email, subject, body)
                print("Confirmation email sent.")
            except Exception as e:
                print(f"Failed to send confirmation email: {str(e)}")
        else:
            print("No email provided. Skipping confirmation email.")

    def update_appointment(self, index, title, date, time, description, email):
        if 0 <= index < len(self.appointments):
            if email and not self.is_valid_email(email):
                print("Error: Invalid email address provided.")
                return
            if self.appointments[index].email == email or email is None:
                old_appointment = self.appointments[index]

                new_start = str_to_datetime(date, time)
                new_end = new_start + timedelta(hours=1)

                if self.is_conflicting(new_start, new_end, exclude_index=index):
                    print(
                        "Error: This appointment conflicts with an existing appointment."
                    )
                    return

                self.appointments[index] = Appointment(
                    title, date, time, description, email
                )
                self.save_appointments()
                print("Appointment updated successfully.")

                recipient_email = email or old_appointment.email
                if recipient_email:
                    subject = "Appointment Updated"
                    body = update_appointment_template(
                        old_appointment.title,
                        old_appointment.date,
                        old_appointment.time,
                        title,
                        date,
                        time,
                        description,
                    )
                    try:
                        email_sender(recipient_email, subject, body)
                        print("Update confirmation email sent.")
                    except Exception as e:
                        print(f"Failed to send update confirmation email: {str(e)}")
                else:
                    print("No email provided. Skipping update confirmation email.")
            else:
                print("You don't have permission to update this appointment.")
        else:
            print("Invalid appointment index.")

    def delete_appointment(self, index, email):
        if 0 <= index < len(self.appointments):
            if email and not self.is_valid_email(email):
                print("Error: Invalid email address provided.")
                return
            if self.appointments[index].email == email or email is None:
                deleted_appointment = self.appointments.pop(index)
                self.save_appointments()
                print("Appointment deleted successfully.")

                if deleted_appointment.email:
                    subject = "Appointment Cancelled"
                    body = cancel_appointment_template(
                        deleted_appointment.title,
                        deleted_appointment.date,
                        deleted_appointment.time,
                    )
                    try:
                        email_sender(deleted_appointment.email, subject, body)
                        print("Cancellation email sent.")
                    except Exception as e:
                        print(f"Failed to send cancellation email: {str(e)}")
                else:
                    print(
                        "No email associated with the appointment. Skipping cancellation email."
                    )
            else:
                print("You don't have permission to delete this appointment.")
        else:
            print("Invalid appointment index.")

    def view_appointments(self, email=None):
        if email:
            user_appointments = [apt for apt in self.appointments if apt.email == email]
            appointments_to_show = user_appointments
        else:
            appointments_to_show = self.appointments

        if not appointments_to_show:
            print("No appointments found.")
        else:
            for i, appointment in enumerate(appointments_to_show, 1):
                print(
                    f"{i}. {appointment.title} - {appointment.date} {appointment.time}"
                )
                print(f"   Description: {appointment.description}")
                print(f"   Email: {appointment.email}")
                print()
