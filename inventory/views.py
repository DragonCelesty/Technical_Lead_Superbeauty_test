from datetime import datetime, date

from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EquipmentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from .forms import UserRegisterForm
from .models import User_Equipment, Equipment


# Create your views here.
class Index(TemplateView):
    template_name = 'inventory/index.html'

class Dashboard(LoginRequiredMixin, View):
    def get(self,request):
        user_equipments = User_Equipment.objects.filter(user=request.user.id).order_by('id')
        for user_equipment in user_equipments:
            if user_equipment.equipment.rental_end_date and user_equipment.equipment.rental_end_date < date.today():
                user_equipment.rental_expired = True
            else:
                user_equipment.rental_expired = False
        return render(request, 'inventory/dashboard.html',{'user_equipments': user_equipments})
class SingUpView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'inventory/singup.html', {'form': form})
    def post(self,request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('index')
        return render(request, 'inventory/singup.html', {'form': form})


class Equipment_APIView(APIView):
    permission_classes = [IsAuthenticated]  # policy attribute
    renderer_classes = [JSONRenderer]  # policy attribute

    def get(self, request, format=None, *args, **kwargs):
        equipments = Equipment.objects.all()
        serializer = EquipmentSerializer(equipments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)