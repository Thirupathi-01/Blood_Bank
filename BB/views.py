from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Donor, Request, BloodInventory
from .forms import BloodInventoryForm, DonorForm, RequestForm
from django.core.mail import send_mail
from django.utils.timezone import now

def home(request):
    return render(request, 'home.html')

def add_donor(request):
    if request.method == 'POST':
        form = DonorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DonorForm()
    return render(request, 'add_donor.html', {'form': form})
# Helper function to get compatible donor blood groups
BLOOD_COMPATIBILITY = {
    'A+': ['A+', 'A-', 'O+', 'O-'],
    'A-': ['A-', 'O-'],
    'B+': ['B+', 'B-', 'O+', 'O-'],
    'B-': ['B-', 'O-'],
    'AB+': ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'],
    'AB-': ['A-', 'B-', 'AB-', 'O-'],
    'O+': ['O+', 'O-'],
    'O-': ['O-'],
}

def handle_request(request):
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            inventory = BloodInventory.objects.filter(
            blood_type=blood_request.blood_type
            ).first()
            
            if inventory and inventory.units >= blood_request.units:
                inventory.units -= blood_request.units
                inventory.save()
                blood_request.save()
                
                return redirect('home')
            else:
                compatible_groups = BLOOD_COMPATIBILITY.get(blood_request.blood_type, [blood_request.blood_type])
                
                eligible_donors = Donor.objects.filter(
                    blood_group__in=compatible_groups,
                    city=blood_request.city,
                )
                recipient_list = [donor.email for donor in eligible_donors if donor.email]
                if recipient_list:
                    subject = "Urgent Blood Donation Request"
                    message = f"""
                    Dear Donor,
                    A patient in {blood_request.city} urgently requires {blood_request.units} units of {blood_request.blood_type} blood. 
                    If you are eligible, please consider donating. Visit the nearest blood bank.
                    Thank you for your generosity!
                    """
                    send_mail(subject, message, "noreply@bloodbank.com", recipient_list)
                
                return render(request, 'error.html', {'message': 'Insufficient blood units. Emails have been sent to eligible donors.'})
    else:
        form = RequestForm()
    
    return render(request, 'handle_request.html', {'form': form})

def view_donors(request):
    donors = Donor.objects.all().order_by('-date')  # optional ordering by latest
    return render(request, 'view_donors.html', {'donors': donors})




