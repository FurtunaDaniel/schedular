from django.shortcuts import redirect


def home(request):
    if request.user.is_authenticated():
        user = request.user
        if user.is_student:
            return redirect('users:student_details')
        if user.is_teacher:
            return redirect('users:students')
    return redirect('users:login')
