from datetime import datetime

now = datetime.now()
date_str = now.strftime("%A, %d %B %Y")    # Example: Saturday, 02 August 2025
time_str = now.strftime("%I:%M %p")        # Example: 12:35 PM
