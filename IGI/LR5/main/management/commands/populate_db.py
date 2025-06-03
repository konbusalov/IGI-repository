from django.utils import timezone
from datetime import timedelta
import random
from main.models import *
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import random
from datetime import datetime
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        # Your database population logic goes here
        try:
            self.stdout.write(self.style.SUCCESS('Starting to populate database...'))

            products = [
                {"article": "ENG-1001", "name": "Timing Belt Kit", "price": 85.99, "category": "Engine Components", "quantity": 15},
                {"article": "ENG-1002", "name": "Water Pump", "price": 64.50, "category": "Engine Components", "quantity": 22},
                {"article": "ENG-1003", "name": "Oil Filter", "price": 12.99, "category": "Engine Components", "quantity": 100},
                {"article": "ENG-1004", "name": "Piston Ring Set", "price": 45.75, "category": "Engine Components", "quantity": 30},
                {"article": "ENG-1005", "name": "Cylinder Head Gasket", "price": 38.20, "category": "Engine Components", "quantity": 40},
                {"article": "ENG-1006", "name": "Fuel Injector", "price": 89.99, "category": "Engine Components", "quantity": 18},
                {"article": "ENG-1007", "name": "Turbocharger", "price": 320.00, "category": "Engine Components", "quantity": 8},
                {"article": "ENG-1008", "name": "Engine Mount", "price": 55.40, "category": "Engine Components", "quantity": 25},
                {"article": "ENG-1009", "name": "Valve Cover Gasket", "price": 22.90, "category": "Engine Components", "quantity": 60},
                {"article": "ENG-1010", "name": "Thermostat", "price": 28.75, "category": "Engine Components", "quantity": 35},
                {"article": "TRN-2001", "name": "Clutch Kit", "price": 145.99, "category": "Transmission", "quantity": 12},
                {"article": "TRN-2002", "name": "Automatic Transmission Filter", "price": 32.50, "category": "Transmission", "quantity": 28},
                {"article": "TRN-2003", "name": "CV Joint Axle", "price": 78.40, "category": "Transmission", "quantity": 16},
                {"article": "TRN-2004", "name": "Transmission Mount", "price": 42.30, "category": "Transmission", "quantity": 20},
                {"article": "TRN-2005", "name": "Shift Cable", "price": 65.80, "category": "Transmission", "quantity": 15},
                {"article": "TRN-2006", "name": "Differential Gear Set", "price": 210.00, "category": "Transmission", "quantity": 6},
                {"article": "TRN-2007", "name": "Transfer Case Seal", "price": 18.95, "category": "Transmission", "quantity": 45},
                {"article": "TRN-2008", "name": "Manual Transmission Rebuild Kit", "price": 175.60, "category": "Transmission", "quantity": 9},
                {"article": "TRN-2009", "name": "Torque Converter", "price": 195.00, "category": "Transmission", "quantity": 7},
                {"article": "TRN-2010", "name": "Shift Solenoid", "price": 48.75, "category": "Transmission", "quantity": 18},
                {"article": "SUS-3001", "name": "Shock Absorber", "price": 68.90, "category": "Suspension", "quantity": 24},
                {"article": "SUS-3002", "name": "Strut Assembly", "price": 95.50, "category": "Suspension", "quantity": 18},
                {"article": "SUS-3003", "name": "Control Arm", "price": 87.25, "category": "Suspension", "quantity": 15},
                {"article": "SUS-3004", "name": "Ball Joint", "price": 32.99, "category": "Suspension", "quantity": 40},
                {"article": "SUS-3005", "name": "Sway Bar Link", "price": 22.75, "category": "Suspension", "quantity": 50},
                {"article": "SUS-3006", "name": "Coil Spring", "price": 55.40, "category": "Suspension", "quantity": 20},
                {"article": "SUS-3007", "name": "Strut Mount", "price": 28.90, "category": "Suspension", "quantity": 35},
                {"article": "SUS-3008", "name": "Tie Rod End", "price": 26.50, "category": "Suspension", "quantity": 42},
                {"article": "SUS-3009", "name": "Bushing Kit", "price": 45.20, "category": "Suspension", "quantity": 30},
                {"article": "SUS-3010", "name": "Wheel Hub Assembly", "price": 72.30, "category": "Suspension", "quantity": 16},
                {"article": "BRK-4001", "name": "Brake Pad Set", "price": 42.99, "category": "Braking System", "quantity": 38},
                {"article": "BRK-4002", "name": "Brake Rotor", "price": 58.75, "category": "Braking System", "quantity": 25},
                {"article": "BRK-4003", "name": "Brake Caliper", "price": 89.50, "category": "Braking System", "quantity": 14},
                {"article": "BRK-4004", "name": "Brake Drum", "price": 47.80, "category": "Braking System", "quantity": 18},
                {"article": "BRK-4005", "name": "Brake Hose", "price": 19.95, "category": "Braking System", "quantity": 60},
                {"article": "BRK-4006", "name": "Master Cylinder", "price": 65.30, "category": "Braking System", "quantity": 12},
                {"article": "BRK-4007", "name": "ABS Sensor", "price": 38.40, "category": "Braking System", "quantity": 30},
                {"article": "BRK-4008", "name": "Brake Booster", "price": 112.00, "category": "Braking System", "quantity": 8},
                {"article": "BRK-4009", "name": "Parking Brake Cable", "price": 24.75, "category": "Braking System", "quantity": 45},
                {"article": "BRK-4010", "name": "Brake Fluid (1L)", "price": 9.99, "category": "Braking System", "quantity": 80},
                {"article": "ELE-5001", "name": "Car Battery 60Ah", "price": 110.00, "category": "Electrical", "quantity": 20},
                {"article": "ELE-5002", "name": "Alternator", "price": 145.75, "category": "Electrical", "quantity": 12},
                {"article": "ELE-5003", "name": "Starter Motor", "price": 98.50, "category": "Electrical", "quantity": 15},
                {"article": "ELE-5004", "name": "Headlight Bulb (H7)", "price": 14.99, "category": "Electrical", "quantity": 100},
                {"article": "ELE-5005", "name": "Fuse Box", "price": 32.40, "category": "Electrical", "quantity": 25},
                {"article": "ELE-5006", "name": "Spark Plug (Iridium)", "price": 8.50, "category": "Electrical", "quantity": 150},
                {"article": "ELE-5007", "name": "Ignition Coil", "price": 42.80, "category": "Electrical", "quantity": 30},
                {"article": "ELE-5008", "name": "Window Regulator", "price": 67.90, "category": "Electrical", "quantity": 18},
                {"article": "ELE-5009", "name": "Blower Motor", "price": 55.25, "category": "Electrical", "quantity": 22},
                {"article": "ELE-5010", "name": "Wiring Harness", "price": 89.99, "category": "Electrical", "quantity": 10},
            ]

            def create_products():
                for product in products:
                    Product.objects.create(
                        article=product["article"],
                        name=product["name"],
                        price=product["price"],
                        category=Category.objects.get(name=product['category']),
                        quantity=product["quantity"]
                    )
            
            def create_users_employees_customers():
                # Create 10 Employees
                employees = [
                    {
                        "username": "ivanov",
                        "first_name": "Ivan",
                        "last_name": "Ivanov",
                        "email": "ivanov@autoparts.by",
                        "position": "Sales Manager",
                        "phone": "+375 (29) 123-45-67",
                        "age": 35,
                        "responsibilities": "Handle wholesale accounts"
                    },
                    {
                        "username": "petrova",
                        "first_name": "Anna",
                        "last_name": "Petrova",
                        "email": "petrova@autoparts.by",
                        "position": "Warehouse Supervisor",
                        "phone": "+375 (33) 234-56-78",
                        "age": 42,
                        "responsibilities": "Inventory management"
                    },
                    {
                        "username": "sidorov",
                        "first_name": "Alexei",
                        "last_name": "Sidorov",
                        "email": "sidorov@autoparts.by",
                        "position": "Technical Specialist",
                        "phone": "+375 (25) 345-67-89",
                        "age": 28,
                        "responsibilities": "Part identification"
                    },
                    {
                        "username": "smirnov",
                        "first_name": "Dmitri",
                        "last_name": "Smirnov",
                        "email": "smirnov@autoparts.by",
                        "position": "Delivery Coordinator",
                        "phone": "+375 (29) 456-78-90",
                        "age": 31,
                        "responsibilities": "Shipping logistics"
                    },
                    {
                        "username": "kozlov",
                        "first_name": "Sergei",
                        "last_name": "Kozlov",
                        "email": "kozlov@autoparts.by",
                        "position": "Customer Service",
                        "phone": "+375 (44) 567-89-01",
                        "age": 26,
                        "responsibilities": "Order processing"
                    },
                    {
                        "username": "morozova",
                        "first_name": "Olga",
                        "last_name": "Morozova",
                        "email": "morozova@autoparts.by",
                        "position": "Accountant",
                        "phone": "+375 (33) 678-90-12",
                        "age": 38,
                        "responsibilities": "Financial records"
                    },
                    {
                        "username": "volkov",
                        "first_name": "Andrei",
                        "last_name": "Volkov",
                        "email": "volkov@autoparts.by",
                        "position": "IT Specialist",
                        "phone": "+375 (29) 789-01-23",
                        "age": 29,
                        "responsibilities": "System maintenance"
                    },
                    {
                        "username": "fedorova",
                        "first_name": "Elena",
                        "last_name": "Fedorova",
                        "email": "fedorova@autoparts.by",
                        "position": "Marketing Manager",
                        "phone": "+375 (25) 890-12-34",
                        "age": 33,
                        "responsibilities": "Promotions"
                    },
                    {
                        "username": "nikolaev",
                        "first_name": "Pavel",
                        "last_name": "Nikolaev",
                        "email": "nikolaev@autoparts.by",
                        "position": "Quality Control",
                        "phone": "+375 (44) 901-23-45",
                        "age": 45,
                        "responsibilities": "Part inspections"
                    },
                    {
                        "username": "pavlova",
                        "first_name": "Maria",
                        "last_name": "Pavlova",
                        "email": "pavlova@autoparts.by",
                        "position": "HR Manager",
                        "phone": "+375 (33) 012-34-56",
                        "age": 40,
                        "responsibilities": "Staff management"
                    }
                ]

                for emp in employees:
                    user = User.objects.create_user(
                        username=emp["username"],
                        password='autoparts2023',
                        first_name=emp["first_name"],
                        last_name=emp["last_name"],
                        email=emp["email"]
                    )
                    Employee.objects.create(
                        user=user,
                        position=emp["position"],
                        phone=emp["phone"],
                        age=emp["age"],
                        responsibilities=emp["responsibilities"]
                    )

                # Create 10 Customers
                customers = [
                    {
                        "username": "auto_shop1",
                        "first_name": "Viktor",
                        "last_name": "Baranov",
                        "email": "baranov@autoshop.by",
                        "phone": "+375 (29) 111-22-33",
                        "age": 44
                    },
                    {
                        "username": "car_center",
                        "first_name": "Yuri",
                        "last_name": "Gusev",
                        "email": "gusev@carcenter.by",
                        "phone": "+375 (33) 222-33-44",
                        "age": 39
                    },
                    {
                        "username": "minsk_motors",
                        "first_name": "Anatoly",
                        "last_name": "Kuzmin",
                        "email": "kuzmin@minsk-motors.by",
                        "phone": "+375 (25) 333-44-55",
                        "age": 51
                    },
                    {
                        "username": "bel_auto",
                        "first_name": "Natalia",
                        "last_name": "Vorobeva",
                        "email": "vorobeva@belauto.by",
                        "phone": "+375 (44) 444-55-66",
                        "age": 36
                    },
                    {
                        "username": "speed_service",
                        "first_name": "Oleg",
                        "last_name": "Tarasov",
                        "email": "tarasov@speedservice.by",
                        "phone": "+375 (29) 555-66-77",
                        "age": 48
                    },
                    {
                        "username": "grodno_garage",
                        "first_name": "Igor",
                        "last_name": "Medvedev",
                        "email": "medvedev@grodnogarage.by",
                        "phone": "+375 (33) 666-77-88",
                        "age": 42
                    },
                    {
                        "username": "vitebsk_auto",
                        "first_name": "Tatiana",
                        "last_name": "Sokolova",
                        "email": "sokolova@vitebskauto.by",
                        "phone": "+375 (25) 777-88-99",
                        "age": 37
                    },
                    {
                        "username": "brest_parts",
                        "first_name": "Roman",
                        "last_name": "Orlov",
                        "email": "orlov@brestparts.by",
                        "phone": "+375 (44) 888-99-00",
                        "age": 45
                    },
                    {
                        "username": "gomel_motors",
                        "first_name": "Darya",
                        "last_name": "Lebedeva",
                        "email": "lebedeva@gomelmotors.by",
                        "phone": "+375 (29) 999-00-11",
                        "age": 33
                    },
                    {
                        "username": "mogilev_auto",
                        "first_name": "Artem",
                        "last_name": "Vinogradov",
                        "email": "vinogradov@mogilevauto.by",
                        "phone": "+375 (33) 000-11-22",
                        "age": 41
                    }
                ]

                for cust in customers:
                    user = User.objects.create_user(
                        username=cust["username"],
                        password='customer2023',
                        first_name=cust["first_name"],
                        last_name=cust["last_name"],
                        email=cust["email"]
                    )
                    Customer.objects.create(
                        user=user,
                        phone=cust["phone"],
                        age=cust["age"]
                    )

            def create_categories():
                categories = [
                    {"name": "Engine Components", "description": "Parts related to engine systems"},
                    {"name": "Transmission", "description": "Gearboxes and related components"},
                    {"name": "Suspension", "description": "Shocks, struts, and suspension parts"},
                    {"name": "Braking System", "description": "Brake pads, rotors, calipers"},
                    {"name": "Electrical", "description": "Batteries, alternators, wiring"},
                    {"name": "Exhaust", "description": "Mufflers, pipes, catalytic converters"},
                    {"name": "Cooling System", "description": "Radiators, water pumps, hoses"},
                    {"name": "Interior", "description": "Seats, dash components, trim"},
                    {"name": "Exterior", "description": "Body panels, mirrors, lights"},
                    {"name": "Accessories", "description": "Aftermarket car accessories"},
                ]
                for cat in categories:
                    Category.objects.create(**cat)

            def create_suppliers():
                suppliers = [
                    {"name": "AutoParts Belarus", "address": "Minsk, Pobediteley Ave 100", "phone": "+375 (29) 111-22-33"},
                    {"name": "BelAvtoKomplekt", "address": "Gomel, Sovetskaya 50", "phone": "+375 (23) 222-33-44"},
                    {"name": "CarTech GmbH", "address": "Berlin, Germany", "phone": "+49 30 12345678"},
                    {"name": "Eastern Auto Supplies", "address": "Moscow, Russia", "phone": "+7 495 9998877"},
                    {"name": "Baltic Car Parts", "address": "Vilnius, Lithuania", "phone": "+370 5 2111111"},
                    {"name": "DieselPro", "address": "Brest, Moskovskaya 300", "phone": "+375 (16) 333-44-55"},
                    {"name": "TurboTech", "address": "Grodno, Ozheshko 25", "phone": "+375 (15) 444-55-66"},
                    {"name": "ElectroAuto", "address": "Vitebsk, Lenina 10", "phone": "+375 (21) 555-66-77"},
                    {"name": "Suspension Specialists", "address": "Mogilev, Pervomayskaya 75", "phone": "+375 (22) 666-77-88"},
                    {"name": "Brake Masters", "address": "Borisov, Gagarina 15", "phone": "+375 (17) 777-88-99"},
                ]
                for sup in suppliers:
                    Supplier.objects.create(**sup)

            def create_articles():
                articles = [
                    {"title": "Maintaining Your Engine in Winter", "summary": "Tips for cold weather engine care", "content": "Full content..."},
                    {"title": "Signs of Transmission Problems", "summary": "How to spot transmission issues early", "content": "Full content..."},
                    {"title": "Upgrading Your Suspension", "summary": "Guide to performance suspension parts", "content": "Full content..."},
                    {"title": "Brake Safety Checklist", "summary": "Essential brake maintenance steps", "content": "Full content..."},
                    {"title": "Car Electrical System Basics", "summary": "Understanding your vehicle's electronics", "content": "Full content..."},
                    {"title": "Exhaust System Upgrades", "summary": "Performance exhaust options explained", "content": "Full content..."},
                    {"title": "Cooling System Maintenance", "summary": "Keeping your engine at optimal temperature", "content": "Full content..."},
                    {"title": "Interior Restoration Tips", "summary": "Bringing old car interiors back to life", "content": "Full content..."},
                    {"title": "Exterior Detailing Guide", "summary": "Professional detailing techniques", "content": "Full content..."},
                    {"title": "Must-Have Car Accessories", "summary": "Useful accessories for every driver", "content": "Full content..."},
                ]
                for art in articles:
                    Article.objects.create(**art)

            def create_faqs():
                faqs = [
                    {"question": "How often should I change engine oil?", "answer": "Every 5,000-10,000 km depending on usage"},
                    {"question": "What are signs of bad shock absorbers?", "answer": "Excessive bouncing, uneven tire wear"},
                    {"question": "When should brake pads be replaced?", "answer": "When thickness is below 3mm or warning light appears"},
                    {"question": "How long do car batteries typically last?", "answer": "3-5 years depending on climate and usage"},
                    {"question": "What causes exhaust smoke?", "answer": "Different colors indicate different engine issues"},
                    {"question": "How often should coolant be replaced?", "answer": "Every 2-5 years depending on the type"},
                    {"question": "Can I install car parts myself?", "answer": "Some simple parts yes, but complex systems need professionals"},
                    {"question": "What's the difference between OEM and aftermarket parts?", "answer": "OEM are original manufacturer parts, aftermarket are alternatives"},
                    {"question": "How do I choose the right engine oil?", "answer": "Consult your owner's manual for specifications"},
                    {"question": "What maintenance does a turbocharger need?", "answer": "Regular oil changes and proper warm-up/cool-down"},
                ]
                for faq in faqs:
                    FAQ.objects.create(**faq)

            def create_job_openings():
                jobs = [
                    {"title": "Auto Parts Sales Specialist", "description": "Sell car parts to customers", "requirements": "Product knowledge, sales experience", "salary": "BYN 2500"},
                    {"title": "Warehouse Manager", "description": "Manage inventory and logistics", "requirements": "Logistics experience, organizational skills", "salary": "BYN 3000"},
                    {"title": "Mechanical Engineer", "description": "Design and test car components", "requirements": "Engineering degree, CAD skills", "salary": "BYN 4000"},
                    {"title": "Quality Control Inspector", "description": "Ensure part quality standards", "requirements": "Attention to detail, technical knowledge", "salary": "BYN 2800"},
                    {"title": "Customer Service Representative", "description": "Handle customer inquiries", "requirements": "Communication skills, patience", "salary": "BYN 2200"},
                    {"title": "Delivery Driver", "description": "Transport parts to customers", "requirements": "Driving license, clean record", "salary": "BYN 2000"},
                    {"title": "Marketing Specialist", "description": "Promote auto parts business", "requirements": "Marketing degree, creativity", "salary": "BYN 3500"},
                    {"title": "IT Support Technician", "description": "Maintain company IT systems", "requirements": "Technical skills, problem-solving", "salary": "BYN 3200"},
                    {"title": "Accountant", "description": "Handle financial records", "requirements": "Accounting degree, attention to detail", "salary": "BYN 3800"},
                    {"title": "HR Manager", "description": "Manage personnel matters", "requirements": "HR experience, people skills", "salary": "BYN 3700"},
                ]
                for job in jobs:
                    JobOpening.objects.create(**job)

            def create_promocodes():
                for i in range(10):
                    PromoCode.objects.create(
                        code=f"PROMO{i}",
                        discount=random.randint(5, 50),
                        valid_until=timezone.now() + timedelta(days=30)
                    )

            def run():
                print("Creating car parts database sample data...")
                
                # create_categories()
                # create_suppliers()
                # create_articles()
                # create_faqs()
                # create_job_openings()
                # print("Creating users, employees and customers...")
                # create_users_employees_customers()
                # print("Successfully created 10 employees and 10 customers!")
                # create_products()  
                create_promocodes()              

                print("Successfully created promocodes!")

            run()
            
            self.stdout.write(self.style.SUCCESS('Successfully populated the database'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error occurred: {str(e)}'))

