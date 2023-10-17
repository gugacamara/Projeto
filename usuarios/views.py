from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from usuarios.models import RegistroCliente

# Create
def some_view(request):
    # Crie seu gráfico aqui
    objects = RegistroCliente.objects.all()
    object1 = RegistroCliente.objects.filter(recebimento=True).values_list('valor', flat=True)
    object2 = RegistroCliente.objects.filter(recebimento=False).values_list('valor', flat=True)
    object3 = RegistroCliente.objects.filter(recebimento=None).values_list('valor', flat=True)
    object1 = sum(object1)
    object2 = sum(object2)
    object3 = sum(object3)
    plt.pie([object1, object2, object3], labels=['Pagamentos', 'Recebimentos', 'Desconhecido'])
    
    # Salvar a imagem em um buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Codifique a imagem em base64 e decodifique para string
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')
    
    # Passe o gráfico codificado para o template
    return render(request, 'usuarios/index.html', {'graphic': graphic})
