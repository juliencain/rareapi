from rareapi.models import RareUser
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def check_user(request):
    try:
        # Check if 'uid' exists in request data
        uid = request.data['uid']
        rare_user = RareUser.objects.filter(uid=uid).first()

        if rare_user:
            data = {
                'firstName': rare_user.first_name,
                'lastName': rare_user.last_name,
                'bio': rare_user.bio,
                'profileImageUrl': rare_user.profile_image_url,
                'email': rare_user.email,
                'created_on': rare_user.created_on,
                'active': rare_user.active,
                'isStaff': rare_user.is_staff,
            }
            return Response(data)
        else:
            return Response({'valid': False}, status=404)
    except KeyError:
        return Response({'error': "'uid' key is missing in the request"}, status=400)
    except Exception as e:
        return Response({'error': str(e)}, status=500)


@api_view(['POST'])
def register_user(request):
    rareUser = RareUser.objects.create(
        profile_image_url=request.data['profile_image_url'],
        bio=request.data['bio'],
        uid=request.data['uid'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        email=request.data['email']
    )

    data = {
        'id': rareUser.id,
        'uid': rareUser.uid,
        'bio': rareUser.bio,
        'firstName': rareUser.first_name,
        'lastName': rareUser.last_name,
        'profileImageUrl': rareUser.profile_image_url
    }

    return Response(data)
