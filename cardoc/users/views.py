import json, jwt, bcrypt
from json.decoder    import JSONDecodeError

from django.http     import JsonResponse
from django.views    import View

from cardoc.settings import SECRET_KEY, ALGORITHM
from users.models    import User

class SignUpView(View):
    def post(self, request):
        try:  
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']

            if User.objects.filter(account=account).exists():
                return JsonResponse({'message': 'ERROR_ACCOUNT_ALREADY_EXIST'}, status=409)
            
            User.objects.create(
                account  = account,
                password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            )

            return JsonResponse({'message': 'SUCCESS'}, status=201)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERORR'}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'})
    
class LoginView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            account  = data['account']
            password = data['password']

            if not User.objects.filter(account=account).exists():
                return JsonResponse({'message': 'INVALID_USER_ID'}, status=401)
            
            user = User.objects.get(account=account)

            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                token = jwt.encode({'id': user.id}, SECRET_KEY, algorithm=ALGORITHM)
                return JsonResponse({'token':token}, status=200)
            
            return JsonResponse({'message': 'INVALID_USER_PASSWORD'}, status=401)
        
        except KeyError:
            return JsonResponse({'message': 'KEY_ERORR'}, status=400)
            
        except JSONDecodeError:
            return JsonResponse({'message': 'JSON_DECODE_ERROR'})
