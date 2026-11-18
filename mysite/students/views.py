from django.shortcuts import render

STUDENTS = {
    'Arun':  {'maths': 85, 'science': 90, 'english': 78},
    'Priya': {'maths': 92, 'science': 88, 'english': 95},
    'Kiran': {'maths': 70, 'science': 65, 'english': 80},
    'Meena': {'maths': 99, 'science': 94, 'english': 91},
}

def home(request):
    return render(request, 'home.html', {'students': STUDENTS.keys()})

def result(request, name):
    marks = STUDENTS.get(name)          # None if the name doesn't exist
    total = sum(marks.values()) if marks else 0
    return render(request, 'result.html', {
        'name': name,
        'marks': marks,
        'total': total,
    })