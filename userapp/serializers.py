from .models import User


from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id','username', 'name', 'password','email','phoneNumber', 'address', 'soft_delete')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            phoneNumber=validated_data['phoneNumber'],
            address=validated_data['address']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

