def new_appointment_template(title, date, time, description):
    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto;">
        <h2 style="color: #4a4a4a;">New Appointment Booked</h2>
        <p>Your new appointment has been successfully scheduled.</p>
        <table style="width: 100%; border-collapse: collapse;">
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Title:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{title}</td>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Date:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{date}</td>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Time:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{time}</td>
            </tr>
            <tr>
                <td style="padding: 10px;"><strong>Description:</strong></td>
                <td style="padding: 10px;">{description}</td>
            </tr>
        </table>
    </body>
    </html>
    """


def update_appointment_template(
    old_title, old_date, old_time, new_title, new_date, new_time, new_description
):
    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto;">
        <h2 style="color: #4a4a4a;">Appointment Updated</h2>
        <p>Your appointment has been updated. Here are the details:</p>
        <table style="width: 100%; border-collapse: collapse;">
            <tr>
                <th style="padding: 10px; border-bottom: 2px solid #eee; text-align: left;">Detail</th>
                <th style="padding: 10px; border-bottom: 2px solid #eee; text-align: left;">Old</th>
                <th style="padding: 10px; border-bottom: 2px solid #eee; text-align: left;">New</th>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Title</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{old_title}</td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{new_title}</td>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Date</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{old_date}</td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{new_date}</td>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Time</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{old_time}</td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{new_time}</td>
            </tr>
        </table>
        <p><strong>New Description:</strong> {new_description}</p>
    </body>
    </html>
    """


def cancel_appointment_template(title, date, time):
    return f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 600px; margin: 0 auto;">
        <h2 style="color: #4a4a4a;">Appointment Cancelled</h2>
        <p>The following appointment has been cancelled:</p>
        <table style="width: 100%; border-collapse: collapse; margin-top: 20px;">
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Title:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{title}</td>
            </tr>
            <tr>
                <td style="padding: 10px; border-bottom: 1px solid #eee;"><strong>Date:</strong></td>
                <td style="padding: 10px; border-bottom: 1px solid #eee;">{date}</td>
            </tr>
            <tr>
                <td style="padding: 10px;"><strong>Time:</strong></td>
                <td style="padding: 10px;">{time}</td>
            </tr>
        </table>
        <p style="margin-top: 20px;">If you have any questions, please contact us.</p>
    </body>
    </html>
    """
