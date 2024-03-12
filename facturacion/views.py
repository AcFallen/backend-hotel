from django.shortcuts import render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status , permissions
from gestion.permissions import *
from .serializer import *
from habitaciones.models import Habitacion
from os import environ
import requests
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from datetime import datetime

# Create your views here.

@swagger_auto_schema(method='post',request_body=GenerarBoletaSerializer)
@api_view(http_method_names=['POST'])
@permission_classes([permissions.IsAuthenticated])
def generarBoleta( request : Request ):
    
    serializador = GenerarBoletaSerializer ( data=request.data)
    serializador.is_valid(raise_exception=True)

    body = serializador.validated_data

    items = []

    total_general = 0

    total_igv = 0

    habitacion = body.get('habitacion_id')
    print(body)
    
    habitacion_encontrada = Habitacion.objects.filter(id = habitacion).first()

    if not habitacion_encontrada:
        return Response(data={
            'message': 'La reserva no existe'
        })
    base = habitacion_encontrada.precio / 1.18

    print((habitacion_encontrada.precio - base) * 1)

    item = {
        'unidad_de_medida':'NIU',
        'descripcion':habitacion_encontrada.descripcion,
        'cantidad': body.get('cantidad_dias'),
        'valor_unitario':base,
        'precio_unitario':habitacion_encontrada.precio,
        'subtotal':base*body.get('cantidad_dias'),
        'tipo_de_igv':1,
        'igv':(habitacion_encontrada.precio - base) * body.get('cantidad_dias'),
        'total':habitacion_encontrada.precio * body.get('cantidad_dias'),
        'anticipo_regularizacion':False,
    }

    total_general += habitacion_encontrada.precio * body.get('cantidad_dias')
    
    total_igv += (habitacion_encontrada.precio - base) * body.get('cantidad_dias')

    items.append(item)
    
    
    data = {
        "operacion": "generar_comprobante",
        "tipo_de_comprobante": 2,
        "serie": "BBB1",
        "numero": body.get('numero_factura'),
        "sunat_transaction": 1,
        "cliente_tipo_de_documento": 1,
        "cliente_numero_de_documento": body.get('documento_usuario'),
        "cliente_denominacion": body.get('nombre_usuario'),
        "fecha_de_emision": datetime.now().strftime('%d-%m-%Y'),
        "moneda": 1,
        'total_igv': total_igv,
        'total_gravada':total_general - total_igv,
        "porcentaje_de_igv": 18.00,
        "total": total_general,
        "items": items
    }

    peticion = requests.post(
        url=environ.get('NUBEFACT_URL'),
        headers={
            'Authorization': 'Bearer '+environ.get('NUBEFACT_TOKEN')
        },json=data
    )        
    print(peticion.json().get("errors"))
    print(peticion.status_code)

    if peticion.json().get("errors"):
        return Response(data={
            'message':peticion.json().get("errors"),
        },status=status.HTTP_400_BAD_REQUEST)

    return Response(data={
        'message':'Boleta Creada Exitosamente',
        'content': peticion.json().get('enlace_del_pdf')
    },status=status.HTTP_201_CREATED)
    
@api_view(http_method_names=['GET'])
@permission_classes([permissions.IsAuthenticated])
def consultarBoleta(request:Request , serie , numero):
    data = {
            'operacion': 'consultar_comprobante',
            'tipo_de_comprobante': 2,
            'serie': serie , 
            'numero': numero
        }

    peticion = requests.post(
        url=environ.get('NUBEFACT_URL'),
        headers={
            'Authorization': 'Bearer '+environ.get('NUBEFACT_TOKEN')
        },json=data
    )

    return Response(data={
        'message': peticion.json()
    })