
from django.http import Http404
from django.shortcuts import render
import json
import subprocess
import sys
import tempfile
import shutil
import urllib.request
import urllib.error
from pathlib import Path
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ChallengeSerializer, ChallengeSerializerGet, UserCompletedChallengeSerializer, UserCompletedChallengeSerializerGet
from .models import Challenge, UserCompletedChallenge
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import status,authentication, permissions
from rest_framework import viewsets, filters, generics
from django.db.models import Q



# Create your views here.

class ChallengesView(APIView):
    def get(self, request, format=None):
        challenges= Challenge.objects.all()
        category_slug = request.query_params.get("category")
        if category_slug:
            challenges = challenges.filter(Category__slug=category_slug)
        serializer= ChallengeSerializerGet(challenges,many=True)
        return Response(serializer.data)

class ChallengeDetailsView(APIView):
    def get_object(self,category_slug,product_slug):
        try:
             return Challenge.objects.filter(Category__slug=category_slug,).get(slug=product_slug)
        except Challenge.DoesNotExist:
            raise Http404
    def get(self, request,category_slug,product_slug, format=None):
        challenge= self.get_object(category_slug,product_slug)
        serializer= ChallengeSerializerGet(challenge)
        return Response(serializer.data)

class ChallengeById(APIView):
    def get(self, request,id, format=None):
        challenge= Challenge.objects.get(id=id)
        serializer= ChallengeSerializer(challenge)

        return Response(serializer.data)




class CompletedChallengesView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request ,format = None):
        comch = UserCompletedChallenge.objects.filter(user=request.user)
        serializer = UserCompletedChallengeSerializerGet(comch , many=True)
        return Response(serializer.data)
        


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CompletedChallenge(request):
    serializer = UserCompletedChallengeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)    
            
class UserCreatedChallenges(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request ,format = None):
        crch= Challenge.objects.filter(Created_by=request.user)
        serializer= ChallengeSerializerGet(crch, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def CreateChallenge(request):
    print(request)
    serializer = ChallengeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(Created_by=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def search(request):
    query= request.data.get('query', '')

    if query:
        products= Challenge.objects.filter(Q(Title__icontains=query))
        serializer= ChallengeSerializerGet(products,many=True)
        return Response(serializer.data)
    else:
        return Response({"challenges": []})


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def run_code(request):
    code = request.data.get('code', '')
    language = request.data.get('language', 'python')

    if not code.strip():
        return Response(
            {"success": False, "output": "", "error": "No code was provided."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    if language == 'cpp':
        return run_cpp_code(code)

    if language != 'python':
        return Response(
            {"success": False, "output": "", "error": f"Unsupported language: {language}"},
            status=status.HTTP_400_BAD_REQUEST,
        )

    with tempfile.TemporaryDirectory() as temp_dir:
        code_path = Path(temp_dir) / "submission.py"
        code_path.write_text(code, encoding="utf-8")

        try:
            completed = subprocess.run(
                [sys.executable, str(code_path)],
                capture_output=True,
                text=True,
                timeout=5,
            )
        except subprocess.TimeoutExpired:
            return Response(
                {"success": False, "output": "", "error": "Code timed out after 5 seconds."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    output = (completed.stdout or "") + (completed.stderr or "")
    return Response(
        {
            "success": completed.returncode == 0,
            "output": output,
            "error": "" if completed.returncode == 0 else output,
        }
    )


def run_cpp_code(code):
    compiler = shutil.which("g++")
    if not compiler:
        return run_cpp_code_with_piston(code)

    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        source_path = temp_path / "submission.cpp"
        binary_path = temp_path / "submission"
        source_path.write_text(code, encoding="utf-8")

        compile_result = subprocess.run(
            [compiler, "-std=c++17", str(source_path), "-o", str(binary_path)],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if compile_result.returncode != 0:
            output = (compile_result.stdout or "") + (compile_result.stderr or "")
            return Response({"success": False, "output": output, "error": output})

        try:
            run_result = subprocess.run(
                [str(binary_path)],
                capture_output=True,
                text=True,
                timeout=5,
            )
        except subprocess.TimeoutExpired:
            return Response(
                {"success": False, "output": "", "error": "Code timed out after 5 seconds."},
                status=status.HTTP_400_BAD_REQUEST,
            )

    output = (run_result.stdout or "") + (run_result.stderr or "")
    return Response(
        {
            "success": run_result.returncode == 0,
            "output": output,
            "error": "" if run_result.returncode == 0 else output,
        }
    )


def run_cpp_code_with_piston(code):
    payload = json.dumps(
        {
            "language": "c++",
            "version": "10.2.0",
            "files": [{"name": "submission.cpp", "content": code}],
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        "https://emkc.org/api/v2/piston/execute",
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            data = json.loads(response.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as error:
        return Response(
            {
                "success": False,
                "output": "",
                "error": f"C++ runner is unavailable right now: {error}",
            },
            status=status.HTTP_502_BAD_GATEWAY,
        )

    run_result = data.get("run") or {}
    output = (run_result.get("stdout") or "") + (run_result.get("stderr") or "")
    return Response(
        {
            "success": run_result.get("code") == 0,
            "output": output,
            "error": "" if run_result.get("code") == 0 else output,
        }
    )













