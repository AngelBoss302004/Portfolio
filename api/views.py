from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.
class aboutview(View):
    def get(self,request):
        data= {
            "id":"2345678",
            "full_name":"angel boss",
            "professional title":" software tester",
            "bio":"software tester",
            "email":"angelboss200430@gmail.com",
            "contact":"456789",
            "dob":"20/3/2044",
            "github":" github.com/github",
            "linkedin":"linledin.com/linkedin "
        }
        return JsonResponse(data)
class educationview(View):
    def get(self,request):
        result={
            "id":"2",
            "institution":"kites",
            "degreee course":"btech",
            "university":"ktu",
            "startyear":"2022",
            "end year":"2026",
            "grade":"B+",
            "description":"completed B.Tech in computer science and enginnering"

        }
        return JsonResponse(result)
class projectview(View):
    def get(self,request):
        results=[
            {
                "id": 1,
                "title": "Online Book Store",
                "short_description": "A web application for browsing and purchasing books online.",
                "long_description": "Online Book Store is a web-based application where users can browse books, search for books, view book details, add books to a cart, and place orders. Admins can manage books, users, and orders.",
                "technologies_used": [
                "Python",
                "Django",
                "MySQL",
                "HTML",
                "CSS",
                "JavaScript"
                ],
                "live_url": "https://example.com/online-book-store",
                "github_url": "https://github.com/username/online-book-store",
                "image_url": "https://example.com/images/book-store.jpg",
                "featured": True
            },
            {
                "id": 2,
                "title": "Student Management System",
                "short_description": "A system for managing student information and academic records.",
                "long_description": "Student Management System is a Django-based application that allows administrators to add, update, delete, and view student information. It provides an organized way to manage student records using a database.",
                "technologies_used": [
                "Python",
                "Django",
                "MySQL",
                "HTML",
                "CSS",
                "Bootstrap"
                ],
                "live_url": "https://example.com/student-management",
                "github_url": "https://github.com/username/student-management",
                "image_url": "https://example.com/images/student-management.jpg",
                "featured": True
            },
            {
                "id": 3,
                "title": "Weather Application",
                "short_description": "A web application that displays current weather information for different locations.",
                "long_description": "Weather Application allows users to search for a city and view its current weather conditions, temperature, humidity, and wind speed. The application uses a weather API to retrieve real-time weather data.",
                "technologies_used": [
                "Python",
                "Django",
                "REST API",
                "HTML",
                "CSS",
                "JavaScript"
                ],
                "live_url": "https://example.com/weather-app",
                "github_url": "https://github.com/username/weather-app",
                "image_url": "https://example.com/images/weather-app.jpg",
                "featured": False
            }
        ]
        return JsonResponse(results,safe=False)
class skillsview(View):
    def get(self,request):
        datas=[


  {
    "id": 1,
    "skill_name": "Python",
    "category": "Programming Language",
    "proficiency_level": "Advanced",
    "years_of_experience": 2
  },
  {
    "id": 2,
    "skill_name": "Django",
    "category": "Web Framework",
    "proficiency_level": "Intermediate",
    "years_of_experience": 1
  },
  {
    "id": 3,
    "skill_name": "MySQL",
    "category": "Database",
    "proficiency_level": "Intermediate",
    "years_of_experience": 1
  }


 
        ]
        return JsonResponse(datas,safe=False)
class experianceview(View):
    def get(self,request):
        result=[

  {
    "id": 1,
    "job_title": "Python Developer",
    "company_name": "Tech Solutions Pvt Ltd",
    "location": "Kochi, Kerala",
    "employee_type": "Full-time",
    "start_date": "2024-06-01",
    "end_date": "2025-05-31",
    "currently_working": False,
    "description": "Developed and maintained web applications using Python and Django. Worked with MySQL databases and implemented REST APIs."
  },
  {
    "id": 2,
    "job_title": "Django Developer Intern",
    "company_name": "WebWorks Technologies",
    "location": "Bangalore, Karnataka",
    "employee_type": "Internship",
    "start_date": "2025-06-01",
    "end_date": "2025-09-30",
    "currently_working": False,
    "description": "Worked on Django web applications, database integration, API development, debugging, and basic frontend development."
  },
  {
    "id": 3,
    "job_title": "Junior Software Developer",
    "company_name": "Innovate Digital Solutions",
    "location": "Kochi, Kerala",
    "employee_type": "Full-time",
    "start_date": "2025-10-01",
    "end_date": "2025-11-09",
    "currently_working": True,
    "description": "Currently developing web applications using Python and Django. Responsible for API development, database management, testing, and application maintenance."
  }  
        ]
        return JsonResponse(result,safe=False)
class certificationview(View):
    def get(self,request):
        data=[
        
  {
    "id": 1,
    "certification_name": "Python Programming Certification",
    "organization_name": "Coursera",
    "issued_year": 2025
  },
  {
    "id": 2,
    "certification_name": "Django Web Development Certification",
    "organization_name": "Udemy",
    "issued_year": 2025
  },
  {
    "id": 3,
    "certification_name": "MySQL Database Certification",
    "organization_name": "Great Learning",
    "issued_year": 2026
  }
  ]
        return JsonResponse(data,safe=False)  
class serviceview(View):
    def get(self,request):
        datas=[
            
  {
    "id": 1,
    "service_name": "Web Development",
    "description": "I develop responsive and user-friendly websites and web applications according to client requirements.",
    "technologies": [
      "HTML",
      "CSS",
      "JavaScript",
      "Python",
      "Django"
    ],
    "contact_information": {
      "email": "developer@example.com",
      "phone": "+91 9876543210"
    }
  },
  {
    "id": 2,
    "service_name": "Backend Development",
    "description": "I build secure and scalable backend applications, APIs, database systems, and server-side functionality.",
    "technologies": [
      "Python",
      "Django",
      "Django REST Framework",
      "MySQL",
      "REST API"
    ],
    "contact_information": {
      "email": "backend@example.com",
      "phone": "+91 9876543211"
    }
  },
  {
    "id": 3,
    "service_name": "Database Management",
    "description": "I design and manage databases for storing, retrieving, updating, and organizing application data efficiently.",
    "technologies": [
      "MySQL",
      "SQL",
      "Django ORM"
    ],
    "contact_information": {
      "email": "database@example.com",
      "phone": "+91 9876543212"
    }
  }


  
            

        ]  
           

