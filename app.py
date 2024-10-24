##---------------問題1------------------#
from flask import Flask, render_template, request
from getrecipe import GetRecipeURL

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

#--------------------------------------#


#---------------問題3------------------#
@app.route("/calc",methods=['GET','POST'])
def calculation():
    if request.method == "GET":
        return render_template('calculation.html')
    # elif request.method == "POST":
    #     name = request.form['name']
    #     genre = request.form['genre']
    #     scene = request.form['scene']
    #     # 台形の計算
    #     answer = trapezoid_area(top, bottom, height)

        # return render_template('calculation.html')


        
@app.route("/resultrecipe",methods=['GET','POST'])
def resultrecipe():
    if request.method == "GET":
        return render_template('resultrecipe.html')
    elif request.method == "POST":
        name = request.form['name']
        genre = request.form['genre']
        scene = request.form['scene']
        #食材と条件の入力情報を受け取っている

        # list1 = recipe_name_list
        # list2 = recipe_img_list
        # list3 = url_list
        # list4 = time_list
        # 台形の計算
        url_list, recipe_name_list, recipe_img_list, time_list = GetRecipeURL(name, genre, scene)
        # return url_list, recipe_name_list, recipe_img_list, time_list
        #代入するとgetrecipe.pyで４つのlist1,2,3,4が返ってくる。その結果が上記のurl_list, recipe_name_list, recipe_img_list, time_listに代入される。
        return render_template('resultrecipe.html', list1 = recipe_name_list, list2 = recipe_img_list, list3 = url_list, list4 = time_list)       

if __name__ == "__main__":
    app.run(debug=True)

#--------------------------------------#

#   return url_list, recipe_name_list, recipe_img_list, time_list
#   time.sleep(1)

# # def GetRecipeURL(top, genre, scene):
# list1 = recipe_name_list
# list2 = recipe_img_list
# list3 = url_list
# list4 = time_list
# print(list1)
# print(list2)
# print(list3)
# print(list4)
