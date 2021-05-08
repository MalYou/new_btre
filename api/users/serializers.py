from rest_framework import serializers

from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    """ Serializer for user objects """

    password1 = serializers.CharField(write_only=True,required=True)
    password2 = serializers.CharField(write_only=True,required=True)

    class Meta:
        model = get_user_model()
        fields = [
            'id', 'email', 'first_name', 'last_name',
            'phone', 'password1', 'password2'
        ]
        read_only_fields = ['id']

    def validate(self, attrs):
        """ Validate user inputs """

        password1 = attrs.pop('password1')
        password2 = attrs.pop('password2')
    
        if password1 != password2 :
            raise serializers.ValidationError('The passwords don\'t match', code="Register")
    
        attrs['password'] = password1

        return attrs

    def create(self, validate_data):
        """ create a serialized user """
        validate_data['is_customer'] = True
        user = get_user_model().objects.create_user(**validate_data)
        user.is_customer = True
    
        return user

