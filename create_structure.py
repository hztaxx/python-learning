# -*- coding: utf-8 -*- 
import os 
 
def create_weeks(weeks=4, days_per_week=5, files_per_day=3): 
    for week in range(1, weeks + 1): 
        for day in range(1, days_per_week + 1): 
            dir_path = f"basics/w{week}/d{day}" 
            os.makedirs(dir_path, exist_ok=True) 
            for file_num in range(1, files_per_day + 1): 
                file_name = f"{dir_path}/w{week}d{day}-{file_num}.py" 
                with open(file_name, 'w', encoding="utf-8") as f: 
                    f.write(f"# w{week}d{day}-{file_num}.py\n") 
                print(f"? {file_name}") 
 
create_weeks(weeks=4, days_per_week=5, files_per_day=3) 
