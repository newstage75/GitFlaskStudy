#モデルの保存
import cv2
import os
import numpy as np
from PIL import image
import re
import os.path

#フォルダ内の画像を取得
def get_images_and_labels():

    print('モデル保存中...')

    #トレーニング画像
    train_path = './train_images'

    #Haar-like特徴分類器（Haar-likeとは画像の明暗差により特徴を捉える）
    cascadePath = './haarcascade_frontalface_alt.xml'
    faceCascade = cv2.CascadeClassofoer(cascadePath)
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    #画像を格納する配列
    images = []

    #ラベルを格納する配列
    labels = []
    for f in os.listdir(train_path):
        #画像のパス

        #白黒で読み込み

        #Numpyの配列に格納

        #Haar-like特徴分類器で顔を検知

        #検出した画像の処理