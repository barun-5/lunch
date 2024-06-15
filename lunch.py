from datetime import datetime, timedelta

def convert_to_24h(time_str):
    return datetime.strptime(time_str, '%I:%M %p')

def calculate_work_hours(start_time, end_time):
    start = convert_to_24h(start_time)
    end = convert_to_24h(end_time)
    if end < start:
        end += timedelta(days=1)  
    return (end - start).total_seconds() / 3600  

def calculate_lunch_break(work_hours):
    if work_hours < 4:
        return (0, 0)
    elif 4 <= work_hours <= 5:
        return (10, 0) 
    elif 5 < work_hours <= 7.6:
        return (10, 30)  
    elif work_hours > 7.6:
        return (2 * 10, 30)  

def adjust_work_hours(work_hours, paid_break, unpaid_break):
    total_break_minutes = paid_break + unpaid_break
    total_break_hours = total_break_minutes / 60
    return work_hours - total_break_hours

def lunch_break_app():
    start_time = input("Enter the start time (e.g., 9:00 AM): ")
    end_time = input("Enter the end time (e.g., 5:00 PM): ")

    work_hours = calculate_work_hours(start_time, end_time)
    paid_break, unpaid_break = calculate_lunch_break(work_hours)
    
    adjusted_work_hours = adjust_work_hours(work_hours, paid_break, unpaid_break)
    
   
    final_paid_break, final_unpaid_break = calculate_lunch_break(adjusted_work_hours)
    
    print(f"Total work hours before break: {work_hours:.2f}")
    print(f"Total work hours after break: {adjusted_work_hours:.2f}")
    print(f"Paid lunch break: {final_paid_break} minutes")
    print(f"Unpaid lunch break: {final_unpaid_break} minutes")
    print(f"Total break: {final_paid_break + final_unpaid_break} minutes")

    input("Press Enter to exit...")

if __name__ == "__main__":
    lunch_break_app()
