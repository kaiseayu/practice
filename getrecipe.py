from bs4 import BeautifulSoup
import requests
import urllib
import urllib.parse
import time
#import predict 
def GetRecipeURL(name, genre, scene):

  name, genre, scene = name, genre, scene = str(name), str(genre), str(scene)
    #材料によって検索名を変える
    #最初に空の変数を定義すれば、条件分岐しても同じ変数を使える
    # global food_name
    # food_name = ''
    # if name == 'キャベツ':
    #   food_name = name + 'の芯'
    # elif name == 'ブロッコリー':
    #   food_name = name + 'の茎'
    # elif name == 'ピーマン':
    #   food_name = name + 'の種'
    # else:
    #   food_name = name + 'の皮'
    #料理名をURLに入れるための処理

    #検索でヒット件数を増やすための言い換え処理
    # global food_name
    # food name = ''
    # if name ==  '筋トレ':
    #   
  x = name + ' ' + genre + ' ' + scene
  name_quote = urllib.parse.quote(x)
    #URLを指定し、Webページを取得
  base_url = 'https://recipe.rakuten.co.jp/search/' + name_quote
  print(base_url)
  response = requests.get(base_url)
    #文字化けが起こらないようにする
  response.encoding = response.apparent_encoding
    #Webページを解析する
  bs = BeautifulSoup(response.text, 'html.parser')
    #<li class='recipe_ranking__item'></li>を取得する
  li_tag_list = bs.find_all('li', class_='recipe_ranking__item', limit=3) 
    #urlを格納するリスト
    #他のpyファイル(app.py)でも使用したい変数はglobal宣言する
  global url_list
  url_list = []
    #その中の<a href=''></a>を取得する
    #find_allはリストで返されるからfor文を使う
  for li_tag in li_tag_list:
      for a_tag in li_tag.find_all('a'):
        href = a_tag.attrs['href']
        #URLを結合し、url_listにappend
        url = 'https://recipe.rakuten.co.jp/' + href
        url_list.append(url)
    
  global recipe_name_list
  recipe_name_list = []
  for li_tag_name in li_tag_list:
      for span_tag in li_tag_name.find_all('span', class_='recipe_ranking__recipe_title omit_2line'):
        recipe_name_list.append(span_tag.get_text())
  global recipe_img_list
  recipe_img_list = []
  for li_tag_img in li_tag_list:
      for img_tag in li_tag_img.find_all('img'):
        img_url = img_tag.attrs['src']
        recipe_img_list.append(img_url)

  global time_list
  time_list = []
  for all_recipe in url_list:

   #URLを指定し、Webページを取得
      base_url =  all_recipe
      response = requests.get(base_url)
      #文字化けが起こらないようにする
      response.encoding = response.apparent_encoding
      #Webページを解析する
      bs = BeautifulSoup(response.text, 'html.parser')

      data_count = []
      recipe_data_set = []

      time = bs.find('li', class_= 'recipe_info_text__note_item recipe_info__time')
      #print(base_url + time.text)
      # 文字列.replace("置換元文字列","置換後文字列")
      time1 = time.text.replace('\n', '').replace(' ', '')
      time_list.append(time1)

  return url_list, recipe_name_list, recipe_img_list, time_list
  time.sleep(1)

# def GetRecipeURL(top, genre, scene):
# list1 = recipe_name_list
# list2 = recipe_img_list
# list3 = url_list
# list4 = time_list
# print(list1)
# print(list2)
# print(list3)
# print(list4)

# def trapezoid_area(top, genre, scene):
#     try:

#         top, genre, scene = top, genre, scene = float(top), float(genre), float(scene)

#         if top > 0 and genre > 0 and scene > 0: # 全ての長さが正の場合
#             area = (top + genre) * scene * 0.5
#             return area

#         else:
#             raise Exception # exceptに飛ばす
#     except:
#         return False

#--------------------------------------#