from rest_framework.throttling import AnonRateThrottle

class MatriculaAnonRateThroattle(AnonRateThrottle):
    rate = '5/day'
