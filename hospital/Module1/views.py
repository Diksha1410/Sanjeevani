from django.shortcuts import render,HttpResponseRedirect,redirect,HttpResponse
from django.contrib.auth.models import User,auth
from.models import profilee
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required

#=======================================================================
@login_required
def index(request):
    return render(request,'index-1.html')
#========================================================================
@login_required
def doctor(request):
    return render(request,'doctors.html')

def pat(request):
    return render(request,'patients.html')

def about(request):
    return render(request,'about.html')
    
#=========================================Doctor Have All The Following Functionality==========================================
def docregister(request):
    return render(request,'doctor-register.html')

@login_required
def doctordashboard(request):
    return render(request,'doctor-dashboard.html')

def appointments(request):
    return render(request,'appointments.html')

def schedule(request):
    return render(request,'schedule-timings.html')

def reviews(request):
    return render(request,'reviews.html')

#==========================================================================================================================

#========================================Patient Have All The Following Functionality==============================================
@login_required
def patientdashboard(request):
    return render(request,'patient-dashboard.html')

@login_required
def patients(request):
    return render(request,'patients-list.html')

def search(request):
    return render(request,'search.html')


def bookingsuccess(request):
    return render(request,'booking-success.html')


#=====================================================REGISTRATION================================================================
def register(request):
    if request.method == "POST":
        username1=request.POST['username1']
        first_name1=request.POST['first_name1']
        last_name1=request.POST['last_name1']
        email1=request.POST['email1']
        password=request.POST['password11']
        password11=request.POST['password21']
        user_type=request.POST['value']
        if password==password11:
            if User.objects.filter(username=username1).exists():
                print("************ Username already taken **********")
                return redirect('register')
            elif User.objects.filter(email=email1).exists():
                print("********** Email already used *********")
                return redirect('register')
            else:
                if user_type=='doctor':
                    user=User.objects.create_user(first_name=first_name1,last_name=last_name1,username=username1,email=email1,password=password11,is_staff=True,is_active=False)
                    user.save()
                    print("*********** Doctor Registration Successful **********")
                    return redirect('/')  
                else:
                    user=User.objects.create_user(first_name=first_name1,last_name=last_name1,username=username1,email=email1,password=password11)   
                    user.save()
                    print("*********** Patient Registration Successful **********")
                    return redirect('/') 
        else:
            print("****************Password doesn't match*********************")
            return redirect('register')
    else:
        return render(request,'register.html')

#=========================================================LOGIN PAGE================================================================
def login(request):
    if request.method == 'POST':
        username1 = request.POST['username1']
        password11 = request.POST['password11']

        user = auth.authenticate(username=username1,password=password11)
         
        if user is not None:
            auth.login(request, user)
            if user.is_staff:
                print("Docto log in")
                return HttpResponseRedirect('/index-1')
            else:
                print("Patient log in")
                return HttpResponseRedirect('/index-1')
        
        else:
            print("*********Username or Password is Incorrect*********")
            return redirect('/')
           
    else:
        return render(request,'login.html')

#================================================Doctor Change Password========================================================

@login_required
def docchangepass(request):                                                        
    if request.method=="POST":
        fm= PasswordChangeForm(user=request.user,data=request.POST)
        print("in method")
        if fm.is_valid():
            fm.save()
            print("****** Password Changed Successfully ******")
        return HttpResponseRedirect('/')
    else:
        fm= PasswordChangeForm(user=request.user)
    return render(request,"doctor-change-password.html",{'form':fm})

#=============================================Patient Change Password======================================================

@login_required
def patchangepass(request):
    if request.method == "POST":
        fm= PasswordChangeForm(user=request.user,data=request.POST)
        print("in method")
        if fm.is_valid():
            print("in valid")
            fm.save()
            print("****** Password Changed Successfully ******")
        return HttpResponseRedirect('/')
    else:
        fm= PasswordChangeForm(user=request.user)
    return render(request,"patient-change-password.html",{'form':fm})

#=========================================================================================================================

#====================================================LOGOUT==============================================================================
@login_required
def logout(request):                                                                          
    auth.logout(request)
    print("*********LOGOUT***********")
    return redirect('/')
#======================================================================================================================

#=========================================== "PATIENT PROFILE SETTINGS" =========================================================
@login_required
def patprosettings(request):                                                                
    obj = User.objects.get(username=request.user)
    if request.method == 'POST':
            profile_image=request.FILES['profile_image']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            date_of_birth = request.POST['date_of_birth']
            blood_group = request.POST['blood_group']
            email_id = request.POST['email_id']
            mobile_number = request.POST['mobile_number']
            gender = request.POST['gender']
            age = request.POST['age']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            #country = request.POST['country']            Commented Bcoz country is default and disabled
            zip_code = request.POST['zip_code']
            var=profilee(profile_image=profile_image,first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,blood_group=blood_group,email_id=email_id,mobile_number=mobile_number,gender=gender,age=age,address=address,city=city,state=state,zip_code=zip_code,pro_id=obj.id)
            var.save()
            return redirect('patient-profile')
    else:
        return render(request,'patient-profile-settings.html')

#=================================================PATIENT PROFILE==========================================================
@login_required
def patientpro(request):                                                                 
    obj = User.objects.get(username=request.user)
    obj2 = profilee.objects.filter(pro_id=obj.id)
    print(obj2)
    for i in obj2:
        obj1 = profilee.objects.get(pro_id=obj.id)
        print(obj1.first_name)
        return render(request,'patient-profile.html',{'object':obj,'object1':obj1})
    else:
        return render(request,'patient-profile.html',{'object':obj})

#================================================Patient-Update-Profile=========================================================

@login_required
def patupdateprofile(request):
    obj = User.objects.get(username=request.user)
    obj2 = profilee.objects.filter(pro_id=obj.id)
    print(obj2)
    for i in obj2:
        obj1 = profilee.objects.get(pro_id=obj.id)
        if request.method == 'POST':
            profile_image=request.FILES['profile_image']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            date_of_birth = request.POST['date_of_birth']
            blood_group = request.POST['blood_group']
            email_id = request.POST['email_id']
            mobile_number = request.POST['mobile_number']
            gender = request.POST['gender']
            age = request.POST['age']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            #country = request.POST['country']           Commented bcoz country is default and disabled
            zip_code = request.POST['zip_code']
            var=profilee(id=obj1.id,profile_image=profile_image,first_name=first_name,last_name=last_name,date_of_birth=date_of_birth,blood_group=blood_group,email_id=email_id,mobile_number=mobile_number,gender=gender,age=age,address=address,city=city,state=state,zip_code=zip_code,pro_id=obj.id)
            var.save()
            return redirect('patient-profile')
        else:
            return render(request,'patient-update-profile.html',{'object':obj,'object1':obj1})
    else:
        return render(request,'patient-update-profile.html')

#================================================ "DOCTOR PROFILE SETTINGS" ===================================================)
@login_required
def docprofilesettings(request):
    obj = User.objects.get(username=request.user)
    if request.method == 'POST':
            profile_image=request.FILES['profile_image']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email_id = request.POST['email_id']
            mobile_number = request.POST['mobile_number']
            age = request.POST['age']
            gender = request.POST['gender']
            #city = request.POST['city']
            clinic_name = request.POST['clinic_name']
            clinic_contact_number= request.POST['clinic_contact_number']
            clinic_address = request.POST['clinic_address']
            clinic_start_time = request.POST['clinic_start_time']
            clinic_end_time = request.POST['clinic_end_time']
            first_time_consultFees = request.POST['first_time_consultFees']
            second_time_consultFees = request.POST['second_time_consultFees']
            clinic_city_name = request.POST['clinic_city_name']
            state = request.POST['state']
            #country = request.POST['country']                     Commented bcoz country is default and disabled
            zip_code = request.POST['zip_code']
            specialization = request.POST['specialization']
            education = request.POST['education']
            experience = request.POST['experience']
            var=profilee(profile_image=profile_image,first_name=first_name,last_name=last_name,email_id=email_id,mobile_number=mobile_number,age=age,gender=gender,clinic_name=clinic_name,clinic_contact_number=clinic_contact_number,clinic_address=clinic_address,clinic_start_time=clinic_start_time,clinic_end_time=clinic_end_time,first_time_consultFees=first_time_consultFees,second_time_consultFees=second_time_consultFees,clinic_city_name=clinic_city_name,state=state,zip_code=zip_code,specialization=specialization,education=education,experience=experience,pro_id=obj.id)
            var.save()
            return redirect('doctor-profile')
    else:
        return render(request,'doctor-profile-settings.html')  

#(=========================================== "DOCTOR PROFILE" =========================================================)
@login_required
def doctorprofile(request):
    obj = User.objects.get(username=request.user)
    obj2 = profilee.objects.filter(pro_id=obj.id)
    print(obj2)
    for i in obj2:
        obj1 = profilee.objects.get(pro_id=obj.id)
        print(obj1.first_name)
        return render(request,'doctor-profile.html',{'object':obj,'object1':obj1})
    else:
        return render(request,'doctor-profile.html',{'object':obj})

#==================================================== "DOCTOR UPDATE PROFILE" =========================================================)
@login_required
def doctorupdateprofile(request):
    obj = User.objects.get(username=request.user)
    obj2 = profilee.objects.filter(pro_id=obj.id)
    print(obj2)
    for i in obj2:
        obj1 = profilee.objects.get(pro_id=obj.id)
        if request.method == 'POST':
            profile_image=request.FILES['profile_image']
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email_id = request.POST['email_id']
            mobile_number = request.POST['mobile_number']
            age = request.POST['age']
            gender = request.POST['gender']
            #city = request.POST['city']
            clinic_name = request.POST['clinic_name']
            clinic_contact_number= request.POST['clinic_contact_number']
            clinic_address = request.POST['clinic_address']
            clinic_start_time = request.POST['clinic_start_time']
            clinic_end_time = request.POST['clinic_end_time']
            first_time_consultFees = request.POST['first_time_consultFees']
            second_time_consultFees = request.POST['second_time_consultFees']
            clinic_city_name = request.POST['clinic_city_name']
            state = request.POST['state']
            #country = request.POST['country']                        Commented bcoz country is default and disabled  
            zip_code = request.POST['zip_code']
            specialization = request.POST['specialization']
            education = request.POST['education']
            experience = request.POST['experience']
            var=profilee(id=obj1.id,profile_image=profile_image,first_name=first_name,last_name=last_name,email_id=email_id,mobile_number=mobile_number,age=age,gender=gender,clinic_name=clinic_name,clinic_contact_number=clinic_contact_number,clinic_address=clinic_address,clinic_start_time=clinic_start_time,clinic_end_time=clinic_end_time,first_time_consultFees=first_time_consultFees,second_time_consultFees=second_time_consultFees,clinic_city_name=clinic_city_name,state=state,zip_code=zip_code,specialization=specialization,education=education,experience=experience,pro_id=obj.id)
            var.save()
            return redirect('doctor-profile')
        else:
            return render(request,'doctor-update-profile.html',{'object':obj,'object1':obj1})
    else:
        return render(request,'doctor-update-profile.html')
    

#========================================FORGOT PASSWORD===================================

def forgotpass(request):
    return render(request,'forgot-password.html')

#==========================================ADMIN PAGE===================================
def admin(request):
    return render(request,'admin.html')



# Create your views here.
