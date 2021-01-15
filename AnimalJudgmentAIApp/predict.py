import numpy as np
from PIL import Image
import sys
from tensorflow.keras.models import load_model
from const import CLASSES, IMAGE_SIZE


# 引数から画像ファイルを参照して読み込む
image = Image.open(sys.argv[1])
image = image.convert('RGB')
image = image.resize((IMAGE_SIZE, IMAGE_SIZE))
data = np.asarray(image) / 255.0

X = []
X.append(data)
X = np.array(X)

# モデルのロード
model = load_model("./AnimalJudgmentModel.h5")

result = model.predict([X])[0]
predicted = result.argmax()
percentage = int(result[predicted] * 100)

print(CLASSES[predicted], str(percentage) + " %")
