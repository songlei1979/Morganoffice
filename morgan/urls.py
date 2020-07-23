from rest_framework import routers
from .api import DepartmentViewSet, EmployeeViewSet, ProjectViewSet, AssignmentViewSet

router = routers.DefaultRouter()
router.register('api/departments', DepartmentViewSet,'Departments')
router.register('api/branches', EmployeeViewSet,'Employees')
router.register('api/verifies', ProjectViewSet,'Projects')
router.register('api/assignments', AssignmentViewSet,'Assignments')


urlpatterns = router.urls