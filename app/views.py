import asyncio

import aiohttp
import pandas as pd
from django.http import JsonResponse
from django.shortcuts import render, redirect
from pydantic import BaseModel, ValidationError

from .forms import FileForm, ArticleForm
from config import config


SHORT_URL = config.URL_WILDCARD.get_secret_value()


class Item(BaseModel):
    article: int
    brand: str
    title: str


async def get_data_wildberries(url: str, article: int):
    """
    Функция асинхронного взаимодействия с HTTP запросом для получения данных о товаре по артикулу
    return: PyDantic method dictionary or Mistake or message String
    """
    async with aiohttp.ClientSession().get(url) as session:
        data = await session.json(content_type=None, encoding='utf-8')

    if data['data']['products']:
        art = data['data']['products'][0]['id']
        brand = data['data']['products'][0]['brand']
        title = data['data']['products'][0]['name']
    else:
        return f'Article |{article}| was not found'

    try:
        item = Item(article=art, brand=brand, title=title)
        return item.dict()
    except ValidationError as e:
        e.json()
        return 'Invalid data'


async def home_view(request):
    """
    Стартовая вьюшка
    """
    form_file = FileForm()
    form_article = ArticleForm()
    return render(
        request,
        'app/home_page.html',
        {
            'form_file': form_file,
            'form_art': form_article
        }
    )


async def article_view(request):
    """
        Вьюшка обработки одного артикул
        return: if form==True JsonResponse else render to page input data
    """
    if request.method == "POST":
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.cleaned_data.get('article')
            url = f'{SHORT_URL}{article}'

            loop = asyncio.get_event_loop()
            result = await loop.create_task(get_data_wildberries(url=url, article=article))

            return JsonResponse(result, safe=False, json_dumps_params={'ensure_ascii': False})

    return redirect(home_view)


async def file_view(request):
    """
    Вьюшка обработки  файл формата xlsx с артикулами
    return: if form==True JsonResponse else redirect to home page
    """
    if request.method == "POST":
        file_form = FileForm(request.POST, request.FILES)
        if file_form.is_valid():
            excel_file = file_form.cleaned_data.get('file')
            df = pd.read_excel(excel_file.read(), engine='openpyxl', names=['index'])

            results = await asyncio.gather(
                *(get_data_wildberries(
                    url=f'{SHORT_URL}{param}',
                    article=param
                ) for param in df['index'])
            )

            return JsonResponse(
                results,
                safe=False,
                json_dumps_params={'ensure_ascii': False}
            )

    return redirect(home_view)
