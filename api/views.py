


from enum import Enum
from django.http import request 
from django.shortcuts import render
from rest_framework import generics, serializers, status

from rest_framework.response import Response
from rest_framework import mixins
from .models import Appointments, Business, CustomUser,Feedback,TimeSlots
from .serialzers import AppointmentSerializer,BusinessSerializer, UserSerialzer,FeedBackSerialzer,TimeSlotSerialzier

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver




class UserApiView(generics.GenericAPIView,mixins.ListModelMixin):
    serializer_class=UserSerialzer
    queryset=CustomUser.objects.all()
    def get(self,request):
        query_set=self.get_queryset()
        serializer= UserSerialzer(query_set,many=True)
        return Response({"users":serializer.data})
    



class BusinessApiView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,
mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class=BusinessSerializer
    queryset=Business.objects.all()

    lookup_field="id"
    
    def get(self,request,id=None,user=None):
     
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
        # if p.is_authenticated():
        if id and user==None:
            return self.retrieve(request)
        elif user:
            queryset = Business.objects.filter(owner=self.request.user)
            serializer = BusinessSerializer(queryset,many=True)
            return Response({"business":serializer.data},status=status.HTTP_200_OK)
        else:
            queryset = Business.objects.all()
            serializer = BusinessSerializer(queryset,many=True)
            return Response({"business":serializer.data},status=status.HTTP_200_OK)
        # else:
        #    return Response({"error":"you are not authenticated"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION) 
    def post(self,request):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
        # if p.is_authenticated():
        return self.create(request)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def perform_create(self, serializer):
        serialz=self.request.data
        name=serialz.get('name','')
        queryset=Business.objects.filter(name=name)
        if queryset:
            raise serializers.ValidationError({"error":"business already exists"})
        return serializer.save(owner=self.request.user)
    
    def put(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
        # if p.is_authenticated():
        return self.update(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def delete(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
        # if p.is_authenticated():
        return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)

    #             ,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    # serializer_class=RoleSerializers
    # queryset=Role.objects.all()

    # lookup_field="id"

    # def post(self,request):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
    #     # if p.is_authenticated():
    #     return self.create(request)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    # def perform_create(self, serializer):
    #     serialz=self.request.data
    #     name=serialz.get('role_name','')
    #     queryset=Role.objects.filter(role_name=name)
    #     if queryset:
    #         raise serializers.ValidationError({"error":"role already exists"})
    #     return serializer.save(created_user=self.request.user)
    
    # def get(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
    #     # if p.is_authenticated():
    #     if id:
    #         return self.retrieve(request)
    #     else:
    #         queryset = self.get_queryset()
    #         serializer = RoleSerializers(queryset,many=True)
    #         return Response({"roles":serializer.data},status=status.HTTP_200_OK)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    # def put(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
    #     # if p.is_authenticated():
    #     return self.update(request,id)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    # def delete(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
    #     # if p.is_authenticated():
    #     return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#Role prmission class is to define sepcific permission for roles
# class RolePermisionApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
#             mixins.CreateModelMixin,mixins.UpdateModelMixin):
#     serializer_class=RolePermisionSerializer
#     queryset=RolePermissions.objects.all()

#     lookup_field="id"

#     def create(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)

#     def post(self,request):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
#         # if p.is_authenticated():
#         serialz=request.data
#         name=serialz.get('page_name','')
#         queryset=RolePermissions.objects.filter(page_name=name)
#         if queryset:
#             d=queryset[0]
#             print(d.id)
#             id=d.id
#             return self.update(request,id)
#         else:
#             return self.create(request)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     def perform_create(self, serializer):
#         serialz=self.request.data
#         name=serialz.get('page_name','')
#         queryset=RolePermissions.objects.filter(page_name=name)
#         if queryset:
#             raise serializers.ValidationError({"error":"role already exists"})
#         return serializer.save(created_user=self.request.user)
    
#     def get(self,requet,id=None,role=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
#         # if p.is_authenticated():
#         if id:
#             try:

#                 queryset = RolePermissions.objects.get(page_name=id,role=role)
#                 serializer = RolePermisionSerializer(queryset,many=False)
#                 return Response(serializer.data,status=status.HTTP_200_OK)
#             except :
#                 return Response({"error":"no data"},status=status.HTTP_200_OK)
#         else:
#             queryset = self.get_queryset()
#             serializer = RolePermisionSerializer(queryset,many=True)
#             return Response({"roles":serializer.data},status=status.HTTP_200_OK)

#     def get_object(self):
#         queryset = self.get_queryset()
#         serialz=self.request.data
#         name=serialz.get('page_name','')
#         obj = generics.get_object_or_404(queryset, page_name=name)
#         return obj


        
#         # else:
        
        
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
       
   
                
#     def put(self,request,id=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
#         # if p.is_authenticated():
#         return self.update(request,id)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     def delete(self,request,id=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
#         # if p.is_authenticated():
#         return self.destroy(request,id)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
# ##assigning created role and permission class to user
# class UserRoleApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
#             mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = UserRoleSerialzer
#     queryset = UserRoles.objects.all()

#     lookup_field="id"

   
    
#     def create(self, request, *args, **kwargs):
#         s= request.data
#         print(s)
#         try:

#             for d in s:
#                 print(d.get('role',''))
#                 role=Role.objects.get(id=d.get('role'))
#                 business=Business.objects.get(id=d.get('business'))
#                 user=self.request.user
#                 data=UserRoles.objects.filter(user=user).filter(business=business).filter(role=role)
         
#                 if data:
#                     print(data)
#                     print('ffg')
#                     return Response({"error":"already exits"},status=status.HTTP_208_ALREADY_REPORTED)
#                 # return serializer.save(created_user=self.request.user)
               
#                 elif role and business and user:
#                     UserRoles.objects.create(role=role,business=business,user=user,created_user=self.request.user)
#                 else:
#                     print("hgh")
#         except:
#             raise serializers.ValidationError({"error":"something went wrong"})   
            

#         return Response({"status":"success"},status=status.HTTP_201_CREATED)

#     def post(self,request):
#         return self.create(request)

#     def perform_create(self, serializer):
#         serialz=self.request.data
#         print(serialz)
#         for i in serialz:
#             print(i)
#             business=i.get('business','')
#             role=i.get('role','')
#             data=UserRoles.objects.filter(user=self.request.user).filter(business=business).filter(role=role)
#             if data:
#                 raise serializers.ValidationError({"error":"already exists"})
#             return serializer.save(created_user=self.request.user)
    
#     def get(self,request,id=None):
       
#         if id:
#             return self.retrieve(request)
#         else:
#             queryset = self.get_queryset()
#             serializer = UserRoleSerialzer(queryset,many=True)
#             return Response({"user roles":serializer.data},status=status.HTTP_200_OK)
      
#     def put(self,request,id=None):
       
#         return self.update(request,id)
       
#     def delete(self,request,id=None):
#         return self.destroy(request,id)
      
# class CategoryApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
#             mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = CategorySerialzer
#     queryset = Categories.objects.all()

#     lookup_field="id"

#     def post(self,request):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
#         # if p.is_authenticated():
#         return self.create(request)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     def perform_create(self, serializer):
#         return serializer.save(created_user=self.request.user)
    
#     def get(self,request,id=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
#         # if p.is_authenticated():
#         if id:
#             return self.retrieve(request)
#         else:
#             queryset = self.get_queryset()
#             serializer = CategorySerialzer(queryset,many=True)
#             return Response({"categories":serializer.data},status=status.HTTP_200_OK)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     def put(self,request,id=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
#         # if p.is_authenticated():
#         return self.update(request,id)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
#     def delete(self,request,id=None):
#         # business=request.data.pop('business')
#         # business_obj=Business.objects.filter(id=business)
#         # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
#         # if p.is_authenticated():
#         return self.destroy(request,id)
#         # else:
#         #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
# class SubCategoryApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
#             mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
#     serializer_class = SubCategorySerialzer
#     queryset = SubCategories.objects.all()

#     lookup_field="id"

#     def post(self,request):
#         return self.create(request)
    
#     def perform_create(self, serializer):
#         return serializer.save(created_user=self.request.user)
    
#     def get(self,request,id=None):
#         if id:

#             queryset = SubCategories.objects.filter(category=id)
#             serializer = SubCategorySerialzer(queryset,many=True)
#             return Response({"SubCategories":serializer.data},status=status.HTTP_200_OK)
    
#     def put(self,request,id=None):
#         return self.update(request,id)
    
#     def delete(self,request,id=None):
#         return self.destroy(request,id)
    
# class ProductsApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
    #         mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    # serializer_class = ProductSerialzer
    # queryset = Products.objects.all()

    # lookup_field="id"

    # def post(self,request):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
    #     # if p.is_authenticated():
    #     return self.create(request)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    # def perform_create(self, serializer):
    #     return serializer.save(created_user=self.request.user)
    
    # def get(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
    #     # if p.is_authenticated():
    #     if id:
    #         queryset = Products.objects.filter(subCategory=id)
    #         serializer = ProductSerialzer(queryset,many=True)
    #         return Response({"products":serializer.data},status=status.HTTP_200_OK)
    #     else:
    #         queryset = self.get_queryset()
    #         serializer = ProductSerialzer(queryset,many=True)
    #         return Response({"products":serializer.data},status=status.HTTP_200_OK)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION) 
    # def put(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
    #     # if p.is_authenticated():
    #     return self.update(request,id)
    #     # else:
    #     #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    # def delete(self,request,id=None):
    #     # business=request.data.pop('business')
    #     # business_obj=Business.objects.filter(id=business)
    #     # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
    #     # if p.is_authenticated():
    #     return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)   
class AppointmentApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = AppointmentSerializer
    queryset = Appointments.objects.all()

    lookup_field="id"

    def post(self,request):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
        # if p.is_authenticated():
        return self.create(request)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def perform_create(self, serializer):
        data=self.request.data
    
        slot=data.get('slot')
        date=data.get('created_date')
        bus=data.get('business')
        ap=Appointments.objects.filter(created_user=self.request.user).filter(business=bus).filter(slot=slot).filter(created_date=date)
        if ap:
            raise serializers.ValidationError({"error":"already booked for the day"})
        apw=Appointments.objects.filter(slot=slot).filter(created_date=date)
        if apw.count() > 5:
            raise serializers.ValidationError({"error":"maximum user's booked for the slot"})
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None,user=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
        # if p.is_authenticated():
        if id and user==None:
            ap= Appointments.objects.filter(created_user=self.request.user)
            serializer = AppointmentSerializer(ap,many=True)
            return Response({"appointments":serializer.data},status=status.HTTP_200_OK)
        elif user:
            ap= Appointments.objects.filter(customer=self.request.user)
            serializer = AppointmentSerializer(ap,many=True)
            return Response({"appointments":serializer.data},status=status.HTTP_200_OK)
        else:
            queryset = Appointments.objects.all()
            serializer = AppointmentSerializer(queryset,many=True)
            return Response({"appointments":serializer.data},status=status.HTTP_200_OK)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def put(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
        # if p.is_authenticated():
        return self.update(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def delete(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
        # if p.is_authenticated():
        return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
class UserApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = UserSerialzer
    queryset = CustomUser.objects.all()

    lookup_field="id"

    def post(self,request):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
        # if p.is_authenticated():
        data = request.data
        access_company=data.pop('access_company')
        print(access_company)
        return self.create(request)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def perform_create(self, serializer):
        print("wofffjfff")
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
        # if p.is_authenticated():
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = UserSerialzer(queryset,many=True)
            return Response({"users":serializer.data},status=status.HTTP_200_OK)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def put(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
        # if p.is_authenticated():
        return self.update(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def delete(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
        # if p.is_authenticated():
        
        return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    @receiver(pre_save, sender = CustomUser)
    def pre_save_article_receiver(sender, instance, raw, using, **kwargs):
        print(raw)


class FeedBackApiView(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = FeedBackSerialzer
    queryset = Feedback.objects.all()

    lookup_field="id"

    def post(self,request):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
        # if p.is_authenticated():
      
        return self.create(request)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def perform_create(self, serializer):
        print("wofffjfff")
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
        # if p.is_authenticated():
        if id:
            return self.retrieve(request)
        else:
            queryset = Feedback.objects.filter()
            serializer = UserSerialzer(queryset,many=True)
            return Response({"users":serializer.data},status=status.HTTP_200_OK)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def put(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
        # if p.is_authenticated():
        return self.update(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def delete(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
        # if p.is_authenticated():
        
        return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
  
class TimeSlotApi(generics.GenericAPIView,mixins.RetrieveModelMixin,
            mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    serializer_class = TimeSlotSerialzier
    queryset = TimeSlots.objects.all()

    lookup_field="id"

    def post(self,request):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.CREATE)
        # if p.is_authenticated():
      
        return self.create(request)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def perform_create(self, serializer):
        print("wofffjfff")
        return serializer.save(created_user=self.request.user)
    
    def get(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.READ)
        # if p.is_authenticated():
        if id:
            return self.retrieve(request)
        else:
            queryset = self.get_queryset()
            serializer = TimeSlotSerialzier(queryset,many=True)
            return Response({"timeslots":serializer.data},status=status.HTTP_200_OK)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def put(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.EDIT)
        # if p.is_authenticated():
        return self.update(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
    def delete(self,request,id=None):
        # business=request.data.pop('business')
        # business_obj=Business.objects.filter(id=business)
        # p=permissionAuthenticate(user=self.request.user,business=business_obj[0],operation=Operations.DELETE)
        # if p.is_authenticated():
        
        return self.destroy(request,id)
        # else:
        #     Response({"error":"you are not autherized"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
  