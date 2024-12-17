from rest_framework.response import Response
from rest_framework.decorators import api_view
from rareapi.models import RareUser

@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

   
    rareUser = RareUser.objects.filter(uid=uid).first()

    
    if rareUser is not None:
        data = {
            'id': rareUser.id,
            'uid': rareUser.uid,
            'bio': rareUser.bio,
            'first_name': rareUser.first_name,
            'last_name': rareUser.last_name,
            'profile_image_url': rareUser.profile_image_url,
            'email': rareUser.email,
            'created_on': rareUser.created_on,
            'active': rareUser.active,
            'is_staff': rareUser.is_staff
        }
        return Response(data)
    else:
    
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

   
    rareUser = RareUser.objects.create(
        uid=request.data['uid'],
        bio=request.data['bio'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        profile_image_url=request.data['profile_image_url'],
        email=request.data['email'],
        created_on=request.data['created_on'], 
        active=request.data.get('active', True),
        is_staff=request.data.get('is_staff', False)  
    )


    # Return the gamer info to the client
    data = {
        'id': rareUser.id,
        'uid': rareUser.uid,
        'bio': rareUser.bio,
        'first_name': rareUser.first_name,
        'last_name': rareUser.last_name,
        'profile_image_url': rareUser.profile_image_url,
        'email': rareUser.email,
        'created_on': rareUser.created_on,
        'active': rareUser.active,
        'is_staff': rareUser.is_staff
    }
    return Response(data)