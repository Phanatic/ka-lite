from django.conf.urls import include, patterns, url

from .api_resources import FacilityResource, FacilityGroupResource, FacilityUserResource, AttemptLogResource, ExerciseLogResource, DeviceLogResource

urlpatterns = patterns(__package__ + '.api_views',
    url(r'^', include(FacilityResource().urls)),
    url(r'^', include(FacilityGroupResource().urls)),
    url(r'^', include(FacilityUserResource().urls)),
    url(r'^', include(AttemptLogResource().urls)),
    url(r'^', include(ExerciseLogResource().urls)),
    url(r'^', include(DeviceLogResource().urls)),
)