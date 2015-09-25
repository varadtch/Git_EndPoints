from django.shortcuts import render_to_response
from models import Userdatabase


def listallusers(request):
    Users = []
    try:
        list_of_users = Userdatabase.objects.all()

        Available_Combinations_professions = []
        Available_Combinations_city = []
        Available_Combinations_state = []

        for available_lists in list_of_users:
            if available_lists.profession not in Available_Combinations_professions:
                Available_Combinations_professions.append(available_lists.profession)
            if available_lists.city not in Available_Combinations_city:
                Available_Combinations_city.append(available_lists.city)
            if available_lists.state not in Available_Combinations_state:
                Available_Combinations_state.append(available_lists.state)

        for users in list_of_users:
            Users.append({
                'id':users.id,
                'username':users.username,
                'email':users.email,
                'profession':users.profession,
                'city':users.city,
                'state':users.state
            })
        return render_to_response('query_page.html',locals())
    except:
        error_message = "Failed to get the user list"
        return render_to_response('query_page.html',locals())


def searchuserbyprofession(request, filter_factor, filter_criteria, group_criteria):
    Users = []
    try:
        Available_Combinations_professions = []
        Available_Combinations_city = []
        Available_Combinations_state = []

        list_of_combinations = Userdatabase.objects.all()
        for available_lists in list_of_combinations:
            if available_lists.profession not in Available_Combinations_professions:
                Available_Combinations_professions.append(available_lists.profession)
            if available_lists.city not in Available_Combinations_city:
                Available_Combinations_city.append(available_lists.city)
            if available_lists.state not in Available_Combinations_state:
                Available_Combinations_state.append(available_lists.state)

        if filter_factor.lower() in ['profession', 'city', 'state']:
            if group_criteria.lower() in ['profession', 'city', 'state']:
                if filter_factor.lower() == 'profession':
                    list_of_users = Userdatabase.objects.filter(
                        profession="%s"%filter_criteria.strip()
                    ).order_by('%s'%group_criteria.lower())
                elif filter_factor.lower() == 'city':
                    list_of_users = Userdatabase.objects.filter(
                        city="%s"%filter_criteria.strip()
                    ).order_by('%s'%group_criteria.lower())
                elif filter_factor.lower() == 'state':
                    list_of_users = Userdatabase.objects.filter(
                        state="%s"%filter_criteria.strip()
                    ).order_by('%s'%group_criteria.lower())
            for users in list_of_users:
                Users.append({
                    'id':users.id,
                    'username':users.username,
                    'email':users.email,
                    'profession':users.profession,
                    'city':users.city,
                    'state':users.state
                })
            else:
                error_message = "Invalid grouping criteria"
            return render_to_response('query_page.html',locals())
        else:
            error_message = "Invalid search criteria"
            return render_to_response('query_page.html',locals())
    except:
        error_message = "Failed while fetching specific data"
        return render_to_response('query_page.html',locals())