# Appointment System

## Description

This Appointment System is a command-line application built in Python. It allows users to manage appointments, including adding, viewing, updating, and deleting appointments. The system also includes email notifications for appointment actions.

## Features

-   Add new appointments
-   View existing appointments
-   Update appointments
-   Delete appointments
-   Email notifications for appointment actions
-   Conflict checking to prevent overlapping appointments
-   Email validation

## Requirements

-   Python 3.6+
-   `dotenv` library
-   SMTP access (Gmail account recommended)

## Installation

1. Clone this repository:

```
   git clone https://github.com/yourusername/appointment-system.git
   cd appointment-system
```

2. Install required packages:

```
    pip install python-dotenv
```

3. Create a `.private.env` file in the project root directory with the following content:

```
   EMAIL=your_email@gmail.com
   PASSWORD=your_app_password
```

Replace `your_email@gmail.com` with your Gmail address and `your_app_password` with an app password generated for your Gmail account.

## Usage

Run the main script:

```
    python main.py
```

Follow the on-screen prompts to manage appointments.

## File Structure

-   `main.py`: The main script to run the appointment system
-   `appointment_system.py`: Contains the `AppointmentSystem` class with core functionality
-   `appointment.py`: Contains the `Appointment` class
-   `helpers.py`: Contains helper functions for date/time operations
-   `email_sender/main.py`: Contains the email sending functionality
-   `.private.env`: Contains email configuration (not tracked by git)

## Email Configuration

To use the email functionality:

1. Use a Gmail account
2. Enable "Less secure app access" or use an "App Password"
3. Add your Gmail address and password/app password to the `.private.env` file

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
