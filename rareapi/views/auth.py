from rareapi.models import RareUser
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def check_user(request):
    '''Checks to see if User has Associated Gamer

    Method arguments:
      request -- The full HTTP request object
    '''
    # Check if 'uid' is provided in the request data
    uid = request.data.get('uid')
    if not uid:
        return Response({'error': 'UID is required'}, status=400)

    # Query the user by uid
    rareUser = RareUser.objects.filter(uid=uid).first()

    # If the user is found, return the user info
    if rareUser:
        data = {
            'id': rareUser.id,
            'uid': rareUser.uid,
            'first_name': rareUser.first_name,
            'last_name': rareUser.last_name,
            'email': rareUser.email,
        }
        return Response(data)
    else:
        # If user doesn't exist, respond with an error
        return Response({'valid': False}, status=404)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Ensure UID is provided
    uid = request.data.get('uid')
    if not uid:
        return Response({'error': 'UID is required'}, status=400)

    # Create the user
    rareUser = RareUser.objects.create(
        uid=uid,
        first_name=request.data.get('first_name', ''),
        last_name=request.data.get('last_name', ''),
        bio=request.data.get('bio', ''),
        profile_image_url=request.data.get('profile_image_url', ''),
        email=request.data.get('email', ''),
        created_on=request.data.get('created_on', '2024-01-01'),  # Default date
        active=request.data.get('active', True),  # Default active
        is_staff=request.data.get('is_staff', False)  # Default not staff
    )

    # Return the gamer info to the client
    data = {
        'id': rareUser.id,
        'uid': rareUser.uid,
    }
    return Response(data)
