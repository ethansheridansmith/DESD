from django.http import HttpResponse

count= ["", "", "", "", "", "", "", "", "", ""]

with open("firstApp\grades.txt") as Grades:
    for line in Grades: 
        if line == range(0-10):
            count[0]+="*"
        elif line == range(11-20):
            count[1]+="*"
        elif line == range(21-30):
            count[2]+="*"
        elif line == range(31-40):
            count[3]+="*"
        elif line == range(41-50):
            count[4]+="*"
        elif line == range(51-60):
            count[5]+="*"
        elif line == range(61-70):
            count[6]+="*"
        elif line == range(71-80):
            count[7]+="*"
        elif line == range(81-90):
            count[8]+="*"
        elif line == range(91-100):
            count[9]+="*"

def home(request):    
    return HttpResponse(content_type = "text/plain")
