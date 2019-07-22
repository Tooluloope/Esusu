from rest_framework import serializers
from.models import Groups


class GroupListSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Groups
        fields = ['id','name', 'group_id','no_of_members','savings_amount','begin_date','created_by','members']
        
class GroupDetailSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Groups
        fields = ['name', 'group_id','description','no_of_members','savings_amount','begin_date','created_by','members','searchable']
  
class GroupCreateSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Groups
        fields = ['name', 'group_id','no_of_members','savings_amount','begin_date','members','searchable']
  