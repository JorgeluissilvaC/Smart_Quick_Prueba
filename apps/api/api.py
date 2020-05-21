from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from apps.api.serializers import ClientSerializer, ProductSerializer, ProductBills
from apps.client.models import Clients
from apps.product.models import Products
from apps.bill.models import Bills
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
import csv
from django.http import HttpResponse

#API clientes

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_clients(request):
    clients = Clients.objects.all()
    serializer = ClientSerializer(clients, many=True)
    return JsonResponse({'clients': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_client(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        client = Clients.objects.create(
            document=payload["document"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
            email=payload["email"]
        )
        serializer = ClientSerializer(client)
        return JsonResponse({'client': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_client(request, client_id):
    payload = json.loads(request.body)
    try:
        client = Clients.objects.filter(id=client_id)
        # returns 1 or 0
        client.update(**payload)
        clientNew = Clients.objects.get(id=client_id)
        serializer = ClientSerializer(clientNew)
        return JsonResponse({'client': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_client(request, client_id):
    try:
        client = Clients.objects.get(id=client_id)
        client.delete()

        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'deleted'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#API productos.

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_products(request):
    products = Products.objects.all()
    serializer = ProductSerializer(products, many=True)
    return JsonResponse({'products': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_product(request):
    payload = json.loads(request.body)
    try:
        product = Products.objects.create(
            name = payload["name"],
            description = payload["description"],
            attribute1 = payload["attribute1"],
            attribute2 = payload["attribute2"],
            attribute3 = payload["attribute3"],
            attribute4 = payload["attribute4"]
        )
        serializer = ProductSerializer(product)
        return JsonResponse({'product': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_product(request, product_id):
    payload = json.loads(request.body)
    try:
        product = Products.objects.filter(id=product_id)
        # returns 1 or 0
        product.update(**payload)
        productNew = Products.objects.get(id=product_id)
        serializer = ProductSerializer(productNew)
        return JsonResponse({'product': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    try:
        client = Products.objects.get(id=product_id)
        client.delete()

        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'deleted'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#API Facturas.
#Bills
#ProductBills

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_bills(request):
    bills = Bills.objects.all()
    serializer = ProductBills(bills, many=True)
    return JsonResponse({'bills': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_bill(request):
    payload = json.loads(request.body)
    try:
        client = Clients.objects.get(id=payload["client_id"])
        bill = Bills.objects.create(
            name = payload["name"],
            client_id = client,
            company_name = payload["company_name"],
            nit = payload["nit"],
            code = payload["code"]
        )
        product = Products.objects.get(id=payload["product"])

        bill.product.add(product)

        serializer = ProductBills(bill)
        return JsonResponse({'bill': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong' + str(Exception)}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_bill(request, bill_id):
    payload = json.loads(request.body)
    try:
        bill = Bills.objects.filter(id=bill_id)
        # returns 1 or 0
        bill.update(**payload)
        billNew = Bills.objects.get(id=bill_id)
        serializer = ProductBills(billNew)
        return JsonResponse({'bill': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_bill(request, bill_id):
    try:
        bill = Bills.objects.get(id=bill_id)
        bill.delete()
        return Response(status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'bill': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'deleted'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_data_on_csv(request):
    try:
        clients = Clients.objects.all()
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="NumBillsPerCli.csv"'
        writer = csv.writer(response)
        for client in clients:
            bs = len (Bills.objects.filter(client_id = client))
            writer.writerow([client.document, client.first_name + ' ' + client.last_name, bs])

        return response
    except ObjectDoesNotExist as e:
        return JsonResponse({'bill': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'deleted'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
