from django.shortcuts import render, redirect
from .forms import PatientRegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Patient
from django.contrib.auth import login
from .firebase_repo import db, create_user_without_sign_in
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def patient_view(request, key):
    print(key)

    pat = db.child("Patients").order_by_child("name").equal_to(key)
    print(pat.get())

    return render(request, 'accounts/patient.html', {'key': key})

@login_required(login_url="login")
def search_patients_view(request):
    patients_from_db = db.child("Patients").get()

    patient_list = []

    for pat in patients_from_db.each():

        patient_details = pat.val().get("patient_details")
        print(patient_details)

        email = "-"
        date = "-"

        if patient_details is not None:
            # date_of_birth = patient_details["date_of_birth"]
            # date = datetime.strptime(str(date_of_birth), "%d%m%y").date()

            email = patient_details["email"]

        new_patient = {
            "name": pat.val().get("name"),
            "date_of_birth": date,
            "email": email,
            "key": pat.key()
        }
        patient_list.append(new_patient)

    return render(request, 'accounts/patients/search_patients.html', {'patients': patient_list})


@login_required(login_url="login")
def add_patients(response):
    if response.method == "POST":
        patient_form = PatientRegisterForm(response.POST)
        if patient_form.is_valid():
            first_name = patient_form.cleaned_data["first_name"]
            last_name = patient_form.cleaned_data["last_name"]
            email = patient_form.cleaned_data["email"]
            password = patient_form.cleaned_data["password"]
            phone_number = patient_form.cleaned_data["phone_number"]

            # new_patient = auth_fb.create_user_with_email_and_password(email=email, password=password)

            new_patient = create_user_without_sign_in(email, password)

            patient_details = {
                'email': email,
                'phone_number': phone_number,
            }

            db.child("Patients").child(new_patient.uid).set(
                {'name': first_name + " " + last_name})
            db.child("Patients").child(new_patient.uid).child(
                "patient_details").set(patient_details)

            messages.success(response, "Successfully created " +
                             first_name + " " + last_name)

        else:
            messages.warning(response, "bad credentails")

        patient_form = PatientRegisterForm()
        return render(response, "accounts/patients/search_patients.html", {'form': patient_form})

    else:
        patient_form = PatientRegisterForm()
        return render(response, "accounts/patients/add_patients.html", {'form': patient_form})


@login_required(login_url="login")
def register_doctor_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm

    return render(request, 'accounts/doctors/register_doctor.html', {'form': form})

