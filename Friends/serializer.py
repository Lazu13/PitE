# friends/
class FriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = '__all__'


class MyFriendsSerilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')