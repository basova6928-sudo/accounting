from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    
    current_date = datetime.now()
    
    print(f"Текущая дата и время: {current_date}")
  
    
    print("-------------------")
    calculate_salary()
    print("-------------------")
    get_employees()
    print("-------------------")

