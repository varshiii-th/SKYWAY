
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
from .models import Flights,Booking
import json
from django.contrib.auth.decorators import login_required



@login_required
def book_seat(request):
    if request.method == 'POST':
        flight_id = request.POST['flight_id']
        seat_number = request.POST['seat_number']
        user_name = request.POST['user_name']
        meal_choice=request.POST['meal_choice']

        try:
            flight = Flights.objects.get(id=flight_id)
        except Flights.DoesNotExist:
            messages.error(request, "Flight not found.")
            return redirect('search_flights')

        # Check if seat already booked
        if Booking.objects.filter(flight=flight, seat_number=seat_number).exists():
            messages.error(request, f"Seat {seat_number} is already booked.")
            return redirect('search_flights')

        # Create the booking
        Booking.objects.create(
            flight=flight,
            seat_number=seat_number,
            user_name=user_name,
            user=request.user,
            meal_choice=meal_choice
        )

        # Remove seat from flight's available list (if using seats_available JSONField)
        if seat_number in flight.seats_available:
            flight.seats_available.remove(seat_number)
            flight.save()

        messages.success(request, f"Successfully booked seat {seat_number} on flight from {flight.origin} to {flight.destination}.")
        return redirect('ticket',flight_id=flight.id,seat_number=seat_number)
    
    else:
        return redirect('search_flights')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('search_flights')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
    
        return render(request,'login.html')
    
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password1=request.POST['password1']
        password2=request.POST['password2']
        email=request.POST['email']
        if(password1==password2):
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('register')

            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('user created')
                return redirect('login')
        else:
            messages.info(request,'passwords are not matching')
            return redirect('register')

    else:
        return render (request,'register.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def users(request):
    return render(request,'users.html')

def ticket(request, flight_id, seat_number):
    flight = get_object_or_404(Flights, id=flight_id)
    booking = get_object_or_404(Booking, flight=flight, seat_number=seat_number)

    context = {
        'flight': flight,
        'booking': booking,
    }
    return render(request, 'ticket.html', context)




def ticket(request, flight_id, seat_number):
    flight = get_object_or_404(Flights, id=flight_id)
    booking = get_object_or_404(Booking, flight=flight, seat_number=seat_number)


    
  
    

    context = {
        'flight': flight,
        'booking': booking,
        
    }
    return render(request, 'ticket.html', context)



def search_flights(request):
    if request.method=='POST':
        origin = request.POST.get('origin')
        destination = request.POST.get('destination')
        departure_date = request.POST.get('departure_date')

        flights = Flights.objects.filter(
            origin__iexact=origin,
            destination__iexact=destination,
            departure_date=departure_date
        )
        for flight in flights:
            all_seats = flight.generate_seats() 
            booked = Booking.objects.filter(flight=flight).values_list('seat_number', flat=True)
            seat_map = [{'name': s, 'booked': s in booked} for s in all_seats]
            flight.seat_map_json = json.dumps(seat_map) 
        
        return render(request, 'flight_form.html', {'flights': flights})
    else:
        flights = Flights.objects.all()

        for flight in flights:
            all_seats = flight.generate_seats()  
            booked = Booking.objects.filter(flight=flight).values_list('seat_number', flat=True)
            seat_map = [{'name': s, 'booked': s in booked} for s in all_seats]
            flight.seat_map_json = json.dumps(seat_map) 

        return render(request, 'flight_form.html', {'flights': flights})
