import pytest
from datetime import datetime, timedelta
from appointment_system import AppointmentSystem


@pytest.fixture
def appointment_system():
    return AppointmentSystem(filename="test_appointments.json")


@pytest.fixture
def future_date():
    return (datetime.now() + timedelta(days=7)).strftime("%Y-%m-%d")


@pytest.fixture(autouse=True)
def clear_appointments(appointment_system):
    appointment_system.appointments = []
    yield
    appointment_system.appointments = []


def test_add_appointment(appointment_system, future_date):
    appointment_system.add_appointment(
        "Test Appointment", future_date, "14:00", "Test description", "test@example.com"
    )
    assert len(appointment_system.appointments) == 1
    assert appointment_system.appointments[0].title == "Test Appointment"


def test_update_appointment(appointment_system, future_date):
    appointment_system.add_appointment(
        "Initial", future_date, "10:00", "Initial description", "initial@example.com"
    )
    appointment_system.update_appointment(
        0, "Updated", future_date, "11:00", "Updated description", "initial@example.com"
    )
    assert appointment_system.appointments[0].title == "Updated"


def test_delete_appointment(appointment_system, future_date):
    appointment_system.add_appointment(
        "To Delete", future_date, "12:00", "To be deleted", "delete@example.com"
    )
    appointment_system.delete_appointment(0, "delete@example.com")
    assert len(appointment_system.appointments) == 0


def test_view_appointments(appointment_system, future_date, capsys):
    appointment_system.add_appointment(
        "Appointment 1", future_date, "09:00", "Description 1", "user1@example.com"
    )
    appointment_system.add_appointment(
        "Appointment 2", future_date, "10:00", "Description 2", "user2@example.com"
    )
    appointment_system.view_appointments()
    captured = capsys.readouterr()
    assert "Appointment 1" in captured.out
    assert "Appointment 2" in captured.out


def test_is_conflicting(appointment_system, future_date):
    appointment_system.add_appointment(
        "Existing", future_date, "13:00", "Existing appointment", "existing@example.com"
    )
    conflicting_start = datetime.strptime(f"{future_date} 13:30", "%Y-%m-%d %H:%M")
    conflicting_end = conflicting_start + timedelta(hours=1)
    assert appointment_system.is_conflicting(conflicting_start, conflicting_end) == True


def test_invalid_email(appointment_system, future_date):
    appointment_system.add_appointment(
        "Invalid Email", future_date, "11:00", "Invalid email test", "invalid-email"
    )
    assert len(appointment_system.appointments) == 0
