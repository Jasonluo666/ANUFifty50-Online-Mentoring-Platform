from django.shortcuts import render
from mentee.forms import User_menteeform
from mentee.models import User_mentee

#the function executes with the signup url to take the inputs
def signup(request):

    if request.method == 'POST':  # if the form has been filled

        form = User_mentee(request.POST)

        gender = request.POST.get('gender', '')
        # creating an user object containing all the data
        user_obj = User_mentee(gender=gender)
        # saving all the data in the current object into the database
        user_obj.save()

        return render(request, 'mentee/tee_signup.html', {'user_obj': user_obj}) # Redirect after POST

    else:
        form = User_menteeform()  # an unboundform

        return render(request, 'mentee/tee_signup.html', {'form': form})
