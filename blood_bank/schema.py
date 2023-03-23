import graphene
from graphene_django import DjangoObjectType
from accounts.models import CustomUser
from .models import Blood_doner, Blood_bank, Division, District, Upazila

class UserType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = ('id', 'email')

class DivisionType(DjangoObjectType):
    class Meta:
        model = Division
        fields = ('id', 'name')

class DonerType(DjangoObjectType):
    class Meta:
        model = Blood_doner
        fields = ('id', 'user', 'first_name', 'last_name', 'blood_group', 'contact_no', 'address_line_1', 'division', 'district', 'upazila', 'country', 'data_of_birth', 'gender', 'is_active' )

class Query(graphene.ObjectType):
    all_doners = graphene.List(DonerType)
    category_by_blood_type = graphene.List(DonerType, blood_group=graphene.String(required=True)) 

    def resolve_all_doners(root, info):
        # We can easily optimize query count in the resolve method
        return Blood_doner.objects.all()

    def resolve_category_by_blood_type(root, info, blood_group):
        try:
            return Blood_doner.objects.filter(blood_group=blood_group)
        except Blood_doner.DoesNotExist:
            return None

schema = graphene.Schema(query=Query)