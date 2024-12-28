                              #RABRI PROGRAM 
faculty_members = 12
admin_staff = 4
students = 100
absent_member = 12
rabri_per_person = 250 


total_members = faculty_members + admin_staff + students    
present_members = total_members - absent_member
print(f"Total Present Members: {present_members}")


rabri_g = present_members * rabri_per_person
print(f"Total Rabri In Grams: {rabri_g}g")


rabri_kg = rabri_g // 1000 
print(f"Total Rabri In Kilograms: {rabri_kg}kg")


rabri_price_per_kg = 1100 
total_rabri_price = rabri_kg * rabri_price_per_kg
print(f"Rabri 1 Kg Price: {rabri_price_per_kg} PKR")
print(f"Total Rabri Price: {total_rabri_price} PKR")