import os
from flyai.dataset import Dataset

from model import Model

data = Dataset()
model = Model(data)
p = model.predict(image_path=os.path.join('images', 'mnist_t10k_186.png'))
print(p)