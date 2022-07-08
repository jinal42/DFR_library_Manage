from cgi import print_arguments
from django.shortcuts import render
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework import status

from rest_framework.views import APIView
from .models import Issued_Book, User,Book

from .serializers import UserSerializer,LoginSerializer,BookSerializer,UserInfoSerializer,Issued_BookSerializer
from  rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.generics import ListAPIView

from rest_framework import filters,generics


class UserAPI(APIView):

    # permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    # def get_object(self):
    #     return self.request.user

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        # print("🚀 ~ file: views.py ~ line 299 ~ serializer>>>>>>>>>>>>>>>>>>", serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None, format=None):
        if id:
            customer_type = User.objects.get(id=id)
            serializer =  UserSerializer(customer_type)
            return Response(serializer.data)

        customer_type = User.objects.all()
        serializer = UserSerializer(customer_type,many=True)
        return Response(serializer.data)


    def delete(self, request, id=None):
        customer_type = get_object_or_404(User, id=id)
        customer_type.delete()
        return Response({"status": "success", "data": "User Deleted"})


    def put(self, request, id, format=None):
            # permission_classes=[IsAuthenticated]

            customer_type = get_object_or_404(User, id=id)

            serializer = UserSerializer(customer_type, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"status": "success", "data": "User Data Updated"})

    def put(self, request, id, format=None):
            customer_type = get_object_or_404(User, id=id)

            serializer = UserSerializer(customer_type, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPI(APIView):
    serializer_class = LoginSerializer
    # permission_classes = (AllowAny,)

    def post(self,request):

        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')

            user=authenticate(email=email,password=password)
            print("------------------------------------------------",user)
            # serializer.save()

            if user is  not None:
                token = RefreshToken.for_user(user)
                # user_serializer = UserSerializer1(user)  # get all user info from 
                # user_serializer = UserInfoSerializer(user)

                data = {
                    'refresh': str(token),
                    "access": str(token.access_token),
                    # 'user_serializer': user_serializer.data,
                    "msg" : "Login Successfully"
                }
                return Response(data)

            else:
                return Response({"msg" : "Invalid Email or Password"})            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








class BookAPI(APIView):

    # permission_classes = (IsAuthenticated,)
    serializer_class = BookSerializer

    # def get_object(self):
    #     return self.request.user

    def post(self, request, format=None):
        serializer = BookSerializer(data=request.data)
        # print("🚀 ~ file: views.py ~ line 299 ~ serializer>>>>>>>>>>>>>>>>>>", serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None, format=None):
        if id:
            book = Book.objects.get(id=id)
            serializer =  BookSerializer(book)
            return Response(serializer.data)

        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)


    def delete(self, request, id=None):
        customer_type = get_object_or_404(Book, id=id)
        customer_type.delete()
        return Response({"status": "success", "data": "Book Deleted"})


    def put(self, request, id, format=None):
            # permission_classes=[IsAuthenticated]

            book = get_object_or_404(Book, id=id)

            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"status": "success", "data": "Book Data Updated"})

    def put(self, request, id, format=None):
            book = get_object_or_404(Book, id=id)

            serializer = BookSerializer(book, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






class Search_Book(ListAPIView):
   queryset=Book.objects.all()
   serializer_class = BookSerializer

   filter_backends = [SearchFilter]
   search_fields = ['book_title', 'book_author']
   search_fields = ['=book_title', '=book_author']
   search_fields = ['^book_title','^book_author']
   search_fields = ['@book_title']





class Searchh(generics.ListAPIView):
    search_fields = ['book_title']
    filter_backends = (filters.SearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class User_info(APIView):
  
    def get(self, request, id=None, format=None):
        if id:
            book = Book.objects.get(id=id)
            serializer =  BookSerializer(book)
            return Response(serializer.data)

        book = Book.objects.all()
        serializer = BookSerializer(book,many=True)
        return Response(serializer.data)








class UserDetail(APIView):
    serializer_class = UserInfoSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, format= None):
        all_user = User.objects.filter(id=request.user.id).first()
        serializer = self.serializer_class(all_user)
        data= serializer.data
        return Response(data)





class Issued_BookAPI(APIView):

    # permission_classes = (IsAuthenticated,)
    serializer_class = Issued_BookSerializer

    # def get_object(self):
    #     return self.request.user

    def post(self, request, format=None):
        serializer = Issued_BookSerializer(data=request.data)
        # print("🚀 ~ file: views.py ~ line 299 ~ serializer>>>>>>>>>>>>>>>>>>", serializer)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request, id=None, format=None):
        if id:
            book = Issued_Book.objects.get(id=id)
            serializer = Issued_BookSerializer(book)
            return Response(serializer.data)

        book = Issued_Book.objects.all()
        serializer = Issued_BookSerializer(book,many=True)
        return Response(serializer.data)


    def delete(self, request, id=None):
        customer_type = get_object_or_404(Issued_Book, id=id)
        customer_type.delete()
        return Response({"status": "success", "data": "Data Deleted"})


    def put(self, request,id, format=None):
            # permission_classes=[IsAuthenticated]

            book = get_object_or_404(Issued_Book,id=id)

            serializer = Issued_BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response({"status": "success", "data": " Data Updated"})

    def put(self, request, id, format=None):
            book = get_object_or_404(Issued_Book, id=id)

            serializer = Issued_BookSerializer(book,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get_fine(self,request,id):

        get_id = Issued_Book.objects.get(id=id)
        print("🚀 ~ file: views.py ~ line 85 ~ i", get_id)
        serializer = Issued_BookSerializer(get_id,many=True)
        return Response(serializer.data)

        # qs = self.get_queryset().filter(Total_Quantity=i)
        # print("🚀 ~ file: views.py ~ line 62 ~ qs", qs)

# ^^^^^^^^^^^^^^^^^^^^^^^
class FineAPI(APIView):
    serializer_class = Issued_BookSerializer

    def get(self, request, id=None, format=None):
        if id:
            book = Issued_Book.objects.get(id=id)
            # print("🚀 ~````````````````````` file: views.py ~ line 332 ~ book", book)

            # issdate= Issued_Book.object.filter(issue_date=book)
            # print_arguments("🚀 ~ file: views.py ~ line 335 ~ issdate", issdate)

            serializer = Issued_BookSerializer(book)
            return Response(serializer.data)

        book = Issued_Book.objects.all()
        serializer = Issued_BookSerializer(book,many=True)
        return Response(serializer.data)

    """   
    def put(self,request,id):
        i = Issued_Book.objects.get(id=id)
        # print("-------------------------------------", i.id)
        # print("-------------------------------------", i.issue_date)
        # print("-------------------------------------", i.return_date)
        # issue_date = i.issue_date

        
        actual_return_date = i.actual_return_date
        print("🚀 ~ file: views.py ~ line 355 ~ actual_return_date", actual_return_date)


        return_date = i.return_date
        days = actual_return_date-return_date
        # print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^", days)
        d=days.days
        print("***********************************************",d)
        fine1=d*10
        print("***********************************************",fine1)
        # getFine = Issued_Book.objects.filter(id=id).update(fine=10*days.days)
        # print("🚀 ~ file: views.py ~ line 366 ~ getFine", getFine)

        # cart = Add_Cart.objects.filter(id=id,quantity=filter_items.quantity).update(quantity=filter_items.quantity+1)

        return Response(status=status.HTTP_200_OK)

    """


    def put(self, request, id, format=None):
        obj = get_object_or_404(Issued_Book, id=id)
        # print("🚀 ~ file: views.py ~ line 377 ~ obj", obj)

        extra_days = obj.actual_return_date-obj.return_date
        if obj.actual_return_date > obj.return_date:
            extra_days = obj.actual_return_date-obj.return_date
            charges = extra_days* 10
            print("--------------------------------------- : ", charges.days)

        serializer = Issued_BookSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# ------------

