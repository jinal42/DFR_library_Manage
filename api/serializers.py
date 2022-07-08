from .models import Book, User,Issued_Book
from rest_framework import serializers



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id', 'email','password','user_name','user_type']
        extra_kwargs = {
                         'user_type':{'required': True}
                       }

    def create(self, validated_data):

        print("🚀 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``validated_data", validated_data)
       
        user = User.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        # User.objects.create(password=validated_data['password'])
        return user


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','book_title', 'book_author']
        
   

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=128)
    password = serializers.CharField(max_length=128)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['email','password']

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['id','email','user_name','user_type']


class Issued_BookSerializer(serializers.ModelSerializer):
    # issue_date = serializers.DateTimeField(format="%Y-%m-%d")
    class Meta:
        model = Issued_Book
        # fields = '__all__'
        fields = ['id','book_id','user_id','issue_date','return_date','actual_return_date']
        # read_only_fields = ('issue_date','return_date')


