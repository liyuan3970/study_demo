
import tensorflow as tf
import inception as inception



model = inception.Inception()
pred=model.classify(image_path='images/bannel.jpg')
model.print_scores(pred=pred,k=10,only_first_name=True)