from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from .models import Student
from django.utils import timezone
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
import os


# class StudentList(ListView):
#     model = Student
#     template_name = 'crud/student_list.html'
#     context_object_name = 'student'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["students"] = Student.objects.all()
#         return context
    
# class StudentCreate(CreateView):
#     model = Student
#     template_name = 'crud/student_create.html'
#     fields = '__all__'
#     context_object_name = 'student'
#     success_url = reverse_lazy('student_list')
    
# class StudentUpdate(UpdateView):
#     model = Student
#     template_name = 'crud/student_update.html'
#     fields = '__all__'
#     context_object_name = 'student'
#     success_url = reverse_lazy('student_list')
    
# class StudentDelete(DeleteView):
#     model = Student
#     template_name = 'crud/student_delete.html'
#     context_object_name = 'student'
#     success_url = reverse_lazy('student_list')
    
    

def student_list(request):
    students = Student.objects.all()
    return render(request, 'crud/student_list.html', {'students': students})

def student_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        
        if not image:
            image = 'default.jpg'
            
        Student.objects.create(
            name = name,
            email = email,
            address = address,
            image = image,
            created = timezone.now()
        )
        
        return redirect('student_list')
    
    return render(request,'crud/student_create.html')

def student_delete(request,pk):
    student = get_object_or_404(Student, pk = pk )
    
    if request.method == 'POST':
        
        if student.image.name != 'default.jpg':
            if os.path.isfile(student.image.path):
                os.remove(student.image.path)
        student.delete()
        
        return redirect('student_list')
    
    return render(request,'crud/student_delete.html',{'student' : student})

def student_update(request,pk):
    student = get_object_or_404(Student , pk = pk)
    
    if request.method == 'POST':
        
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.address = request.POST.get('address')
        
        if 'image' in request.FILES:
            if student.image.name != 'default.jpg':
                if os.path.isfile(student.image.path):
                    os.remove(student.image.path)
            student.image = request.FILES['image']
        student.save()
        return redirect('student_list')
        
    return render(request,'crud/student_update.html',{'student' : student})

