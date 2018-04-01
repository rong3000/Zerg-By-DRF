from rest_framework.viewsets import ReadOnlyModelViewSet

from api.models import Banner, Theme
from api.serializer import BannerSerializer, ThemeSerializer
from api.validators import IdsValidator


class BannerViewSet(ReadOnlyModelViewSet):
    """
     Banner
     ---
     list:
         parameters:
             - name: page_num
               description: 当前页
               required: false
               type: string
               paramType: query
             - name: page_size
               description: 分页大小
               required: false
               type: string
               paramType: query
     retrieve:
        omit_serializer: false
        parameters_strategy:
            query: replace

     """
    queryset = Banner.objects.all().prefetch_related('items__img', 'items')
    serializer_class = BannerSerializer

    def retrieve(self, request, *args, **kwargs):
        self.get_object()


class ThemeViewSet(ReadOnlyModelViewSet):
    """
    ---
    list:
         parameters:
             - name: ids
               description: example id1,id2,id3,id4
               required: false
               type: string
               paramType: query
    """

    serializer_class = ThemeSerializer

    def get_queryset(self):
        queryset = Theme.objects.all()
        ids = self.request.GET.get('ids')
        IdsValidator()(ids)
        if ids:
            queryset = queryset.filter(pk__in=ids.split(','))
        return queryset

