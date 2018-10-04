from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.messages.views import SuccessMessageMixin
from .models import Car
from .models import Booking
from .forms import BookingForm
from .forms import CustomUserCreationForm
from .models import CustomUser

#from django.views.generic import DetailView

class SignUp(SuccessMessageMixin,generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    success_message = "You have successfully signed up!"

def Account(request):
    Bookings = Booking.objects.filter(customer=request.user).order_by('-book_start_date')
    context = { 'Bookings': Bookings }
    return render(request, 'account.html', context)

def CreateBooking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            bform = form.save(commit=False)
            bform.customer = request.user
            bform.save()
            messages.success(request, 'Your booking has been saved!')
            return redirect('account')
    else:
        form = BookingForm(request.POST)
    return render(request, 'book.html', {'form': form})

#class CarView(DetailView):
    #template_name = 'car_details.html'
    #model = Car

    #def get_context_data(self, **kwargs):
        #context = super(CarView, self).get_context_data(**kwargs)
        #context['booking_success'] = 'booking-success' in self.request.GET
        #return context
