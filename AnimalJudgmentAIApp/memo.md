# 仮想環境の作成
python -m venv AnimalJudgmentAIApp
# 仮想環境の起動
AnimalJudgmentAIApp\Scripts\activate

# 画像収集
python download.py monkey
python download.py horse
python download.py boar
python download.py dog
python download.py cat
python download.py tiger
python download.py bear
python download.py capybara
python download.py penguin
python download.py rabbit
python download.py elephant
python download.py panda
python download.py giraffe
python download.py dolphin
python download.py gorilla

# インストール内容
python -m pip install --upgrade pip
pip install flickrapi
pip install numpy
pip install pillow
pip install sklearn
pip install tensorflow
pip install Flask
pip install keras

# 精度
batch_size: 16  
epochs: 5  
loss: 0.2430  
accuracy: 0.9323  
test loss: 0.24303343892097473  
test acc: 0.9322671890258789  

テストデータの実施結果  
正解率：0.866667 (11/15)

# プログラム実行方法
## 画像データをnumpyに変換
python generate_data.py
## モデルの作成
python make_model.py

## Flaskのアプリケーション指定
set FLASK_APP=predictfile.py
## Flaskの実行
flask run

## テスト
python predict.py ./test_data/test_bear_1.jpg


# インストール内容の確認
pip freeze

absl-py==0.11.0
astunparse==1.6.3
cachetools==4.2.0
certifi==2020.12.5
chardet==4.0.0
click==7.1.2
Flask==1.1.2
flatbuffers==1.12
flickrapi==2.4.0
gast==0.3.3
google-auth==1.24.0
google-auth-oauthlib==0.4.2
google-pasta==0.2.0
grpcio==1.32.0
h5py==2.10.0
idna==2.10
importlib-metadata==3.3.0
itsdangerous==1.1.0
Jinja2==2.11.2
joblib==1.0.0
Keras==2.4.3
Keras-Preprocessing==1.1.2
Markdown==3.3.3
MarkupSafe==1.1.1
numpy==1.19.5
oauthlib==3.1.0
opt-einsum==3.3.0
Pillow==8.1.0
protobuf==3.14.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
PyYAML==5.3.1
requests==2.25.1
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rsa==4.7
scikit-learn==0.24.0
scipy==1.6.0
six==1.15.0
sklearn==0.0
tensorboard==2.4.0
tensorboard-plugin-wit==1.7.0
tensorflow==2.4.0
tensorflow-estimator==2.4.0
termcolor==1.1.0
threadpoolctl==2.1.0
typing-extensions==3.7.4.3
urllib3==1.26.2
Werkzeug==1.0.1
wrapt==1.12.1
zipp==3.4.0

# TODO gitに上げるときはAPIキー等を変更する。
# TODO アップロードしたファイルの削除機能が欲しい
# TODO test_dataは上げない
# TODO APIキーは上げない
# TODO 画像データの精査
