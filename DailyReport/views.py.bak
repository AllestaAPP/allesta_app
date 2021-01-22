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
import numpy as np

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
    tmp_num, reg_num = count_num()
    today = date.today()

    # csvダウンロード用(totalup.htmlの"csvダウンロード"ボタンが押されたか判定する。)
    tasknum = request.POST.get('key-word3', "false")
    if request.POST.get('key-word2', "fail") != "fail" and request.POST.get('key-word3', "fail") != "fail":
        #################csvダウンロード用####################
        if request.POST.get('key-word3') != "false":
            # key-word3の余計な文字を削除してリストに変換
            tasknum = tasknum.replace('[', '').replace("'", '').replace(',', '').replace(']', '')
            tasknum = tasknum.split(" ")

        l = []
        l2 = []
        datalt = []
        if request.method == "POST":
            tmpdate = request.POST.get('key-word2', today)
        else:
            tmpdate = str(today)

        for item in Item.objects.filter(created_at__icontains=tmpdate, tmp__icontains=0).order_by('name'):
            datalt = [item.name, item.takuhaikenpin, item.sonotakenpin, item.nyuukosyouhinka,
                      item.shiiresyouhinka, item.cleaning, item.dataerase, item.shiirePC,
                      item.SIMlockkaijo, float(item.tsutaya), float(item.takuhaikaikon), float(item.picking),
                      float(item.datanyuuryoku), float(item.soukin), float(item.hensou), float(item.lanksatei),
                      item.memo]
            # 作業費計算用
            datalt2 = [item.takuhaikenpin * 400, item.sonotakenpin * 200, item.nyuukosyouhinka * 200,
                       item.shiiresyouhinka * 100, item.cleaning * 50, item.dataerase * 50, item.shiirePC * 1000,
                       item.SIMlockkaijo * 200, float(item.tsutaya) * 2500, float(item.takuhaikaikon) * 2500,
                       float(item.picking) * 2500, float(item.datanyuuryoku) * 1650, float(item.soukin) * 2500,
                       float(item.hensou) * 2500, float(item.lanksatei) * 2500]

            l.append(datalt)
            l2.append(datalt2)
            tmpdate = str(tmpdate)

        # totalup.htmlで表示するtd用データフレームを作成
        df = pd.DataFrame(l, columns=['作業者', '宅配検品', 'その他検品', '入庫商品化', '仕入商品化', 'クリーニング', 'データイレース',
                                      '仕入PC', 'SIMロック解除', 'TSUTAYA', '宅配開梱', '搬出・ピッキング・ゴミ分別',
                                      '画像・データ入力', '送金関連業務', '返送関連業務', 'ランク査定', '備考'])
        # 作業費計算用のデータフレームを作成
        df2 = pd.DataFrame(l2, columns=['宅配検品', 'その他検品', '入庫商品化', '仕入商品化', 'クリーニング', 'データイレース',
                                        '仕入PC', 'SIMロック解除', 'TSUTAYA', '宅配開梱', '搬出・ピッキング・ゴミ分別',
                                        '画像・データ入力', '送金関連業務', '返送関連業務', 'ランク査定'])
        # totalupからPOSTされた値(宅配検品-ランク査定)に応じてDataFrameから必要な列のみ抽出
        if tasknum != "false":
            df2 = df2.loc[:, tasknum]
            df3 = pd.DataFrame(df2.sum(axis=1), columns=['作業費小計'])
            tasknum.insert(0, '作業者')
            df = df.loc[:, tasknum]
            df4 = pd.concat([df, df3], axis=1)
        else:
            df3 = pd.DataFrame(df2.sum(axis=1), columns=['作業費小計'])
            df4 = pd.concat([df, df3], axis=1)

        total = df4['作業費小計'].sum()
        context = df4.to_html(index=False)

        file_name = 'xxxxxxxxxxxxxxxxxxxxx.csv'
        print(df4)
        df4_csv = df4.to_csv(index=False)
        response = HttpResponse(df4_csv, content_type='csv')
        response['Content-Disposition'] = 'attachment; filename=' + file_name

        return response
    else:
        pass
    #################csvダウンロード用####################

    tasknum = request.POST.getlist('tasknum', "false")
    l = []
    l2 = []
    datalt = []

    if request.method == "POST":
        tmpdate = request.POST.get('key-word', today)
    else:
        tmpdate = str(today)

    for item in Item.objects.filter(created_at__icontains=tmpdate, tmp__icontains=0).order_by('name'):
        datalt = [item.name, item.takuhaikenpin, item.sonotakenpin, item.nyuukosyouhinka,
                  item.shiiresyouhinka, item.cleaning, item.dataerase, item.shiirePC,
                  item.SIMlockkaijo, float(item.tsutaya), float(item.takuhaikaikon), float(item.picking),
                  float(item.datanyuuryoku), float(item.soukin), float(item.hensou), float(item.lanksatei),
                  item.memo]
        # 作業費計算用
        datalt2 = [item.takuhaikenpin * 400, item.sonotakenpin * 200, item.nyuukosyouhinka * 200,
                   item.shiiresyouhinka * 100, item.cleaning * 50, item.dataerase * 50, item.shiirePC * 1000,
                   item.SIMlockkaijo * 200, float(item.tsutaya) * 2500, float(item.takuhaikaikon) * 2500,
                   float(item.picking) * 2500, float(item.datanyuuryoku) * 1650, float(item.soukin) * 2500,
                   float(item.hensou) * 2500, float(item.lanksatei) * 2500]

        l.append(datalt)
        l2.append(datalt2)
        tmpdate = str(tmpdate)

    # totalup.htmlで表示するtd用データフレームを作成
    df = pd.DataFrame(l, columns=['作業者', '宅配検品', 'その他検品', '入庫商品化', '仕入商品化', 'クリーニング', 'データイレース',
                                  '仕入PC', 'SIMロック解除', 'TSUTAYA', '宅配開梱', '搬出・ピッキング・ゴミ分別',
                                  '画像・データ入力', '送金関連業務', '返送関連業務', 'ランク査定', '備考'])
    # 作業費計算用のデータフレームを作成
    df2 = pd.DataFrame(l2, columns=['宅配検品', 'その他検品', '入庫商品化', '仕入商品化', 'クリーニング', 'データイレース',
                                    '仕入PC', 'SIMロック解除', 'TSUTAYA', '宅配開梱', '搬出・ピッキング・ゴミ分別',
                                    '画像・データ入力', '送金関連業務', '返送関連業務', 'ランク査定'])
    # totalupからPOSTされた値(宅配検品-ランク査定)に応じてDataFrameから必要な列のみ抽出
    if tasknum != "false":
        df2 = df2.loc[:, tasknum]
        df3 = pd.DataFrame(df2.sum(axis=1), columns=['作業費小計'])
        tasknum.insert(0, '作業者')
        df = df.loc[:, tasknum]
        df4 = pd.concat([df, df3], axis=1)
    else:
        df3 = pd.DataFrame(df2.sum(axis=1), columns=['作業費小計'])
        df4 = pd.concat([df, df3], axis=1)

    total = df4['作業費小計'].sum()
    context = df4.to_html(index=False)

    return render(request, 'DailyReport/totalup.html', {"tmpdate": tmpdate,
                                                        'tmp_num': tmp_num,
                                                        'reg_num': reg_num,
                                                        'tasknum': tasknum,
                                                        'total': total,
                                                        'context': context})
