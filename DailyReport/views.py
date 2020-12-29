import csv
import urllib
from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django_filters.views import FilterView

from .filters import ItemFilter
from .forms import ItemForm
from .models import Item


# _base部分に表示する日報登録数。
def count_num():
    tmp_num = Item.objects.filter(tmp__icontains=1).count()
    reg_num = Item.objects.filter(created_at__icontains=date.today(), tmp__icontains=0).count()
    return tmp_num, reg_num

@login_required
def _base(request):
    tmp_num, reg_num = count_num()
    return render(request, 'DailyReport/_base.html', {'tmp_num': tmp_num, 'reg_num': reg_num})


# Create your views here.
# 検索一覧画面
class ItemFilterView(LoginRequiredMixin, FilterView):
    today = date.today()
    model = Item

    # django-filter用設定
    filterset_class = ItemFilter
    strict = False

    # デフォルトの並び順を新しい順とする
    #queryset = Item.objects.all().order_by('-created_at')
    queryset = Item.objects.filter(created_at__icontains=today, tmp__icontains=0)

    # 1ページあたりの表示件数
    paginate_by = 30

    # 検索条件をセッションに保存する
    # def get(self, request, **kwargs):
    #     if request.GET:
    #         request.session['query'] = request.GET
    #     else:
    #         request.GET = request.GET.copy()
    #         if 'query' in request.session.keys():
    #             for key in request.session['query'].keys():
    #                 request.GET[key] = request.session['query'][key]
    #
    #     # return super().get(request, **kwargs)
    #     super_g = super().get(request, **kwargs)
    #     return super_g

    # def get_context_data(self, **kwargs):
    #     tmp_num, reg_num = count_num()
    #     return {'tmp_num': tmp_num, 'reg_num': reg_num}




# 詳細画面
class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item

    # _base部分に表示する日報登録数。
    # def get_context_data(self, **kwargs):
    #     tmp_num, reg_num = count_num()
    #     return {'tmp_num': tmp_num, 'reg_num': reg_num}


# 登録画面
class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 更新画面
class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = ItemForm
    success_url = reverse_lazy('index')


# 削除画面
class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('index')

    # _base部分に表示する日報登録数。
    def get_context_data(self, **kwargs):
        tmp_num, reg_num = count_num()
        return {'tmp_num': tmp_num, 'reg_num': reg_num}

@login_required
def csvdownload(request):
    """
    csvのdownload実験用
    """
    response = HttpResponse(content_type='text/csv; charset=Shift-JIS')
    filename = urllib.parse.quote((u'日報_' + str(date.today()) + '.csv').encode("utf8"))
    response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
    writer = csv.writer(response)

    writer.writerow(["氏名", "宅配検品", "その他検品", "入庫商品化", "仕入商品化", "クリーニング", "データイレース",
                     "仕入PC", "SIMロック解除", "ツタヤ関連", "宅配開梱", "搬出・ピッキング", "データ・画像登録",
                     "送金関連", "返送関連", "ランク査定", "備考", "登録日"])

    # for item in Item.objects.all():
    for item in Item.objects.filter(created_at__icontains=date.today()):
        # yymmdd = str(item.created_at)
        # str_yymmdd = re.sub('\s\S.*', '', yymmdd)
        # print(str_yymmdd)
        if item.tmp == 0:
            writer.writerow([item.name, item.takuhaikenpin, item.sonotakenpin, item.nyuukosyouhinka,
                             item.shiiresyouhinka, item.cleaning, item.dataerase, item.shiirePC,
                             item.SIMlockkaijo, item.tsutaya, item.takuhaikaikon, item.picking,
                             item.datanyuuryoku, item.soukin, item.hensou, item.lanksatei, item.memo,
                             item.created_at])
    return response

@login_required
def tmpsave(request):
    params = {}
    tmp_num, reg_num = count_num()
    for item in Item.objects.filter(tmp__icontains=1):
        params[str(item.id)] = item.name
    return render(request, 'DailyReport/tmpsave.html', {'params': params, 'tmp_num': tmp_num, 'reg_num': reg_num})

@login_required
def default(request):
    tmp_num, reg_num = count_num()
    today = date.today()
    return render(request, 'DailyReport/default.html', {'tmp_num': tmp_num, 'reg_num': reg_num, 'today': today})



