from rest_framework.views import APIView
from rest_framework.response import Response

class HelloAPIView(APIView):
    """Test API View"""
    def get(self, request, format = None):
        """Returns a list of APIView features"""
        an_apiview = [
        'Uses HTTP methos such as get,post...',
        'Is similar to tradinationl Django view',
        'Gives you the most control',
        'Is mapped manually to URLs'
        ]

        return Response({'message': 'Hello!',
                        'an_apiview': an_apiview})
