# views.py
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views import View
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.decorators import user_passes_test
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

class HomeView(APIView):
    def get(self, request):
        data = {
            "carousel": [
                {"img": "/media/image/imagem1.jpg", "title": "Guerreiros no Tatame", "description": "Prof. Alexandre Salgado"},
                {"img": "/media/image/imagem2.jpg", "title": "Guerreiras no Tatame", "description": "Profa. Anna Carolina"},
                {"img": "/media/image/imagem3.jpg", "title": "Criançada no Tatame", "description": "Prof. Alexandre Salgado e Anna Carolina"}
            ],
            "gallery": [
                "/media/image/pessoal1.jpg",
                "/media/image/pessoal2.jpg",
                "/media/image/pessoal3.jpg",
                "/media/image/pessoal4.jpg",
                "/media/image/pessoal5.jpg",
                "/media/image/pessoal6.jpg"
            ]
        }
        return Response(data)


class AboutView(APIView):
    def get(self, request):
        data = {
            "image": "/media/image/professores.jpeg",
            "description": (
                "Na nossa academia, estamos comprometidos em transformar vidas através do jiu-jítsu e do bem-estar. "
                "Com mais de 10 anos de experiência, nosso time de instrutores dedicados, liderado por Alexandre "
                "Salgado e sua esposa Anna Carolina, oferece um ambiente acolhedor e seguro para alunos de todas as "
                "idades e níveis de habilidade."
                "Além das aulas de jiu-jítsu, oferecemos sessões de yoga ministradas pela nossa instrutora Anna Carolina."
            ),
            "schedule": [
                {
                    "day": "Segunda",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Terça",
                    "times": [
                        {"time": "12:00 - 13:00", "class": "Iniciantes kimono"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Quarta",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Quinta",
                    "times": [
                        {"time": "12:00 - 13:00", "class": "Iniciantes kimono"},
                        {"time": "18:00 - 19:00", "class": "Jiu-Jitsu"},
                        {"time": "19:20 - 20:20", "class": "Jiu-Jitsu(Infantil)"},
                        {"time": "20:00 - 21:00", "class": "Todos os níveis"}
                    ]
                },
                {
                    "day": "Sexta",
                    "times": [
                        {"time": "7:00 - 8:00", "class": "Todos os níveis"},
                        {"time": "18:00 - 19:00", "class": "Open Match"},
                        {"time": "Open Match", "class": "Open Match"}
                    ]
                }
            ],
            "testimonials": [
                {"name": "João Pereira", "text": "O que eu mais gosto nas aulas..."},
                {"name": "Carla Mendes", "text": "O jiu-jitsu não só me ajudou..."},
                {"name": "Beatriz Lima", "text": "Comecei a treinar jiu-jitsu..."}
            ]
        }
        return Response(data)
    

class ServiceView(APIView):
    def get(self, request):
        data = {
            "services": [
                {
                    "name": "Jiu-Jitsu",
                    "benefits": [
                        "Melhora do Condicionamento Físico",
                        "Perda de Peso",
                        "Melhora da Resiliência Física",
                        "Redução do Estresse",
                        "Desenvolvimento do Autocontrole",
                        "Habilidades de Autodefesa"
                    ],
                    "cta": "/contato"
                },
                {
                    "name": "Defesa Pessoal",
                    "benefits": [
                        "Aumento da Confiança",
                        "Redução do Estresse e Ansiedade",
                        "Desenvolvimento do Autocontrole",
                        "Resiliência Mental",
                        "Empoderamento Pessoal",
                        "Independência"
                    ],
                    "cta": "/contato"
                },
                {
                    "name": "Yoga",
                    "benefits": [
                        "Aumento da Flexibilidade",
                        "Melhora da Postura",
                        "Melhora da Respiração",
                        "Redução do Estresse",
                        "Melhora do Sono",
                        "Sensação de Paz Interior"
                    ],
                    "cta": "/contato"
                }
            ],
            "faq": [
                {
                    "id": "collapseUm",
                    "question": "O que é jiu-jitsu?",
                    "answer": "O jiu-jítsu é uma arte marcial focada em técnicas de alavanca, imobilizações e submissões, permitindo que uma pessoa menor e mais fraca possa se defender de um oponente maior e mais forte."
                },
                {
                    "id": "collapseDois",
                    "question": "Preciso ter experiência para começar?",
                    "answer": "Não, nossa academia oferece aulas para todos os níveis, desde iniciantes até avançados. Todo mundo começa do zero, e estamos aqui para ajudar no seu progresso."
                },
                {
                    "id": "collapseTres",
                    "question": "Quais são os benefícios de praticar jiu-jítsu?",
                    "answer": "Os benefícios incluem melhora da forma física, autoconfiança, disciplina, aprendizado de autodefesa, além de ser uma excelente forma de aliviar o estresse."
                },
                {
                    "id": "collapseQuatro",
                    "question": "Quanto tempo leva para obter a faixa preta?",
                    "answer": "O tempo varia de pessoa para pessoa, dependendo da dedicação, frequência de treino e aprendizado. Geralmente, leva de 8 a 12 anos para obter a faixa preta."
                },
                {
                    "id": "collapseCinco",
                    "question": "Quais equipamentos são necessários?",
                    "answer": "Para iniciar, você precisará de um kimono (Gi). Oferecemos kimonos para venda na academia. Mais adiante, você pode adquirir outros equipamentos, como rashguards e protetores bucais."
                },
                {
                    "id": "collapseSeis",
                    "question": "Há um limite de idade para começar?",
                    "answer": "Não há limite de idade. Temos alunos de todas as idades, desde crianças até adultos mais velhos. O jiu-jitsu é uma arte marcial inclusiva para todas as idades."
                }
            ]
        }
        return Response(data)



class ContactView(APIView):
    def get(self, request):
        data = {
            "team": [
                {
                    "name": "Alexandre Salgado",
                    "role": "Professor",
                    "image": "/media/image/alexandre.jpg"
                },
                {
                    "name": "NoGi",
                    "role": "Alexandre Salgado",
                    "image": "/media/image/nogi.jpeg"
                },
                {
                    "name": "Anna Carolina",
                    "role": "Professora",
                    "image": "/media/image/ana.jpg"
                },
                {
                    "name": "Meninas",
                    "role": "Anna Carolina",
                    "image": "/media/image/meninas.jpeg"
                }
            ]
        }
        return Response(data)
    
 
class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        print(f"Recebido email: {email}, password: {password}")  # Adicione isso para depuração


        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"message": "Usuário com este email não existe"}, status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=user.username, password=password)

        if user is not None:
            login(request, user)
            role = 'admin' if user.is_staff else 'aluno'  # Verificando o papel do usuário

            # Retornando o sucesso do login e redirecionando para o mesmo dashboard
            return Response({
                "message": "Login bem-sucedido", 
                "role": role,  # Passando o papel do usuário
                "redirect_url": "/area-do-aluno"  # Ambos vão para o mesmo dashboard
            }, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Email ou senha incorretos"}, status=status.HTTP_401_UNAUTHORIZED)


 
class SignupView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        confirm_password = request.data.get('confirmPassword')

        if password != confirm_password:
            return Response({"message": "As senhas não coincidem"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"message": "Nome de usuário já existe"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"message": "Email já está em uso"}, status=status.HTTP_400_BAD_REQUEST)

        if not validate_password(password):
            return Response({"message": "A senha deve ter pelo menos 8 caracteres, incluindo um número, uma letra maiúscula e um caractere especial"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({"message": "Registro bem-sucedido"}, status=status.HTTP_201_CREATED)



 
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char in '!@#$%^&*()_+-=' for char in password):
        return False
    return True



class PasswordResetRequestView(View):
    def post(self, request):
        email = request.POST.get('email')
        if not email:
            return JsonResponse({'error': 'Email é obrigatório'}, status=400)

        user = User.objects.filter(email=email).first()
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f'http://yourfrontend.com/reset/{uid}/{token}/'
            
            send_mail(
                'Redefinição de Senha',
                f'Clique no link para redefinir sua senha: {reset_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )

        return JsonResponse({'message': 'Se o email estiver registrado, um link foi enviado.'})



class PasswordResetConfirmView(View):
    def post(self, request):
        uidb64 = request.POST.get('uid')
        token = request.POST.get('token')
        new_password = request.POST.get('new_password')

        if not uidb64 or not token or not new_password:
            return JsonResponse({'error': 'Dados incompletos'}, status=400)

        try:
            uid = urlsafe_base64_decode(uidb64).decode()
            user = User.objects.get(pk=uid)
        except (User.DoesNotExist, ValueError, TypeError):
            return JsonResponse({'error': 'Token inválido'}, status=400)

        if not default_token_generator.check_token(user, token):
            return JsonResponse({'error': 'Token inválido ou expirado'}, status=400)

        user.set_password(new_password)
        user.save()
        return JsonResponse({'message': 'Senha redefinida com sucesso'})


def is_admin(user):
    return user.is_staff  # Apenas administradores têm is_staff=True


@user_passes_test(is_admin)
def admin_area(request):
    return JsonResponse({"message": "Bem-vindo à área do administrador!"})

@login_required
def aluno_area(request):
    user = request.user
    return JsonResponse({"message": f"Bem-vindo à sua área de trabalho, {user.username}!"})


class StudentDataView(APIView):
    def get(self, request):
        if request.user.is_staff:
            alunos = User.objects.all()
            return Response({"students": [student.username for student in alunos]})
        else:
            return Response({"student": request.user.username})


