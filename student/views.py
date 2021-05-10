from django.shortcuts import render
from django.http import HttpResponse
from student.models import Studentdetails
from coursedetails.models import Coursedetails
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'student/login.html')

@login_required
def home(request):
    return render(request, 'student/home.html')

@login_required
def studentdetails(request):
    student_data = Studentdetails.objects.all()
    paginator = Paginator(student_data, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data': minidata}
    return render(request, 'student/studentdetails.html', context)

@login_required
def coursedetails(request):
    course_data = Coursedetails.objects.all()
    paginator = Paginator(course_data, 10)
    page = request.GET.get('page')
    minidata = paginator.get_page(page)
    context = {'data': minidata}
    return render(request, 'course/coursedetails.html', context)

@login_required
def enrollment(request):
    return render(request, 'student/courseenrollment.html')

@login_required
def enrollment(request):
    student_data = Studentdetails.objects.all()
    course_data = Coursedetails.objects.all()
    context = {'student': student_data, 'course': course_data}
    return render(request, 'student/courseenrollment.html', context)

#def dictfetchall(cursor):
#    column = [col[0] for col in cursor.description]
#   return [
#        dict(zip(columns, row))
#       for row in cursor.fetchall()
#    ]

#def studentlist(request):
#    cursorobj = connection.cursor()
#    cursorobj.execute("select concat(id,firstname) from student_studentdetails")
#    studentdata = dictfetchall(cursorobj)
#    context = {'data': studentdata}
#    return render(request, 'student/courseenrollment.html', context)


