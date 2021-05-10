from django.shortcuts import render
from django.http import HttpResponse
from coursedetails.models import Coursedetails, Enrollment
from student.models import Studentdetails
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages

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


def saveenrollment(request):
    if 'stuname' and 'cname' in request.GET:
        stuname = request.GET.get('stuname')
        coursename = request.GET.get('cname')
        dataobj = Enrollment(studentname=stuname, coursename=coursename)
        cursorobj = connection.cursor()
        cursorobj.execute("select count(*) from (select coursename from django_443.coursedetails_enrollment where studentname='" + stuname + "') as table1;")
        number = dictfetchall(cursorobj)
        cursorobj2 = connection.cursor()
        cursorobj2.execute("select coursename from django_443.coursedetails_enrollment where studentname='" + stuname + "'")
        repeat = dictfetchall(cursorobj2)
        if number[0]['count(*)'] < 3:
            if again(coursename, repeat):
                dataobj.save()
                return HttpResponse("Success")
            else:
                print('You have already enrolled this course. Do not enroll again')
                return HttpResponse("Fail")
        else:
            print('You can only enroll 3 courses.')
            return HttpResponse("Fail")


def dictfetchall(cursor):
    column = [col[0] for col in cursor.description]
    return [
        dict(zip(column, row))
        for row in cursor.fetchall()
    ]


def again(coursename,repeat):
    course = []
    for i in repeat:
        course.append(i['coursename'])
    if coursename in course:
        return False
    return True