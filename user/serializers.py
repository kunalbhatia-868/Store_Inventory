from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id','password','username']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self, **kwargs):
        username=self.validated_data['username']   
        password=self.validated_data['password']
                
        account=User(username=username)
        account.set_password(password)
        account.save()
        return account