class Appointment:
    def __init__(self, title, date, time, description, email):
        self.title = title
        self.date = date
        self.time = time
        self.description = description
        self.email = email

    def to_dict(self):
        return {
            "title": self.title,
            "date": self.date,
            "time": self.time,
            "description": self.description,
            "email": self.email,
        }
