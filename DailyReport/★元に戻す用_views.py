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
import pandas as pd
import numpy as nm

# from django.core.paginator import Paginator
# from django.core.paginator import EmptyPage
# from django.core.paginator import PageNotAnInteger

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
    model = Item

    # django-filter用設定
    filterset_class = ItemFilter
    strict = False

    # デフォルトの並び順を新しい順とする
    #queryset = Item.objects.all().order_by('-created_at')
    # queryset = Item.objects.filter(created_at__icontains=today, tmp__icontains=0)

    def get_queryset(self):
        return Item.objects.filter(created_at__icontains=date.today(), tmp__icontains=0)

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
    response = HttpResponse(content_type='text/csv; charset=utf8')
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

@login_required
def totalup(request):

    tmpdate = request.POST.get('key-word2', "fail")
    if tmpdate != "fail":
        """
        csvのdownload実験用
        """
        response = HttpResponse(content_type='text/csv; charset=utf8')
        filename = urllib.parse.quote((u'日報_' + str(tmpdate) + '.csv').encode("utf8"))
        response['Content-Disposition'] = 'attachment; filename*=UTF-8\'\'{}'.format(filename)
        writer = csv.writer(response)

        writer.writerow(["氏名", "宅配検品", "その他検品", "入庫商品化", "仕入商品化", "クリーニング", "データイレース",
                         "仕入PC", "SIMロック解除", "ツタヤ関連", "宅配開梱", "搬出・ピッキング", "データ・画像登録",
                         "送金関連", "返送関連", "ランク査定", "備考", "登録日"])

        # for item in Item.objects.all():
        for item in Item.objects.filter(created_at__icontains=tmpdate).order_by('name'):
            if item.tmp == 0:
                memo = item.memo.replace('～', '-')  # ダメ文字の暫定処置
                writer.writerow([item.name, item.takuhaikenpin, item.sonotakenpin, item.nyuukosyouhinka,
                                 item.shiiresyouhinka, item.cleaning, item.dataerase, item.shiirePC,
                                 item.SIMlockkaijo, item.tsutaya, item.takuhaikaikon, item.picking,
                                 item.datanyuuryoku, item.soukin, item.hensou, item.lanksatei, memo,
                                 item.created_at])
        return response

    tasknum = request.POST.getlist('tasknum', "0")
    print(tasknum)

    tmp_num, reg_num = count_num()
    today = date.today()
    each_worker = 0
    total = 0
    l1total = []
    l = []
    if request.method == "POST":
        tmpdate = request.POST.get('key-word', today)
    else:
        tmpdate = str(today)

    for item in Item.objects.filter(created_at__icontains=tmpdate, tmp__icontains=0).order_by('name'):
        datalt = [item.name, item.takuhaikenpin, item.sonotakenpin, item.nyuukosyouhinka,
                  item.shiiresyouhinka, item.cleaning, item.dataerase, item.shiirePC,
                  item.SIMlockkaijo, item.tsutaya, item.takuhaikaikon, item.picking,
                  item.datanyuuryoku, item.soukin, item.hensou, item.lanksatei, item.memo,
                  ]

        # 宅配検品からランク査定までの数値を足し算
        l1 = datalt[1] * 400  # 宅配検品
        l2 = datalt[2] * 200  # その他検品
        l3 = datalt[3] * 200  # 入庫商品化
        l4 = datalt[4] * 100  # 仕入商品化
        l5 = datalt[5] * 50  # クリーニング
        l6 = datalt[6] * 50  # データイレース
        l7 = datalt[7] * 1000  # 仕入PC
        l8 = datalt[8] * 200  # SIMロック解除
        l9 = float(datalt[9] * 2500)  # TSUTAYA
        l10 = float(datalt[10]) * 2500  # 宅配開墾
        l11 = float(datalt[11]) * 2500  # 搬出・ピッキング・ゴミ分別
        l12 = float(datalt[12]) * 1650  # 画像・データ入力
        l13 = float(datalt[13]) * 2500  # 送金関連業務
        l14 = float(datalt[14]) * 2500  # 返送関連業務
        l15 = float(datalt[15]) * 2500  # ランク査定
        each_worker = l1+l2+l3+l4+l5+l6+l7+l8+l9+l10+l11+l12+l13+l14+l15
        datalt.append(each_worker)
        total += each_worker
        l.append(datalt)
        tmpdate = str(tmpdate)

    print(each_worker)
    print(datalt)
    print(total)
    print(l)
    print(tmpdate)

    return render(request, 'DailyReport/totalup.html', {"l": l,
                                                        "tmpdate": tmpdate,
                                                        "each_worker": each_worker,
                                                        "total": total,
                                                        'tmp_num': tmp_num,
                                                        'reg_num': reg_num})

# #ページネーション（保留中）
#     paginator = Paginator(l, 10)
#     page = request.GET.get('page', 1)
#     try:
#     	pages = paginator.page(page)
#     except PageNotAnInteger:
#     	pages = paginator.page(1)
#     except EmptyPage:
#     	pages = paginator.page(1)
#     context = {'pages': pages}
