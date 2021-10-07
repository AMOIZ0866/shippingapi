from rest_framework import serializers

from api.models import User, Dispatches, Pickups, Deliveries


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class PickupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pickups
        fields = '__all__'


class DeliveriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deliveries
        fields = '__all__'


class DispatchSerializer(serializers.ModelSerializer):
    pickup = PickupSerializer(many=True)
    deliveries = DeliveriesSerializer(many=True)

    class Meta:
        model = Dispatches
        fields = ['dis_id', 'dis_rep', 'dis_wieght', 'dis_dimen', 'dis_packages', 'commodity', 'date_created',
                  'dis_status', 'pickup', 'deliveries']

    def create(self, validated_data):
        pickups_data = validated_data.pop('pickup')
        dis_id = Dispatches.objects.create(**validated_data)
        for pickups_data in pickups_data:
            Pickups.objects.create(dis_id=dis_id, **pickups_data)
        deliveries_data = validated_data.pop('deliveries')
        for deliveries_data in deliveries_data:
            Deliveries.objects.create(dis_id=dis_id, **deliveries_data)
        return dis_id


class SimpleDispatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispatches
        fields = ['dis_id', 'dis_rep', 'dis_packages', 'commodity', 'date_created',
                  'dis_status']



