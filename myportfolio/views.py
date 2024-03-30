from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def projects(request):
    return render(request,'projects.html')

def resume(request):
    return render(request,'resume.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}',
                'your_email@example.com',
                ['your_email@example.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

