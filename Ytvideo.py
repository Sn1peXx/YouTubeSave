#ALPHA 
from pytube import YouTube
import os
from moviepy.editor import *

fn = input('Пожалуйста вставьте ссылку: ')
audio = 'Аудио'
YouTube(fn) #Ссылка на видео
yt = YouTube(fn) # Присваимваем переменной ссылку 
#print(yt.streams.all()) #Показать всевозможные варианты для скачивания
title_video = yt.title
print(title_video)
quality = input(f'В каком качестве скачать видео "{yt.title}" ?\n1080, 720, 480, 360, Аудио\n')

if quality == '1080':
	try:
		stream = yt.streams.filter(res = '1080p', progressive = 'True') #Только 1080p 
		#print(stream.all())
		stream.first().download('D:\\Backup') #Скачиваем первое 
	except:
		print('К сожалению выбранный формат не поддерживается для данного видео')
if quality == '720':
	try:
		stream = yt.streams.filter(res = '720p', progressive = 'True') #Первый элемент 720р
		print(stream.all())
		stream.first().download('D:\\Backup')
	except:
		print('К сожалению выбранный формат не поддерживается для данного видео')
if quality == '480':
	try:
		stream = yt.streams.filter(res = '480p', progressive = 'True') #Только 480p 
		#print(stream.all()) Показываем все возможные варианты
		stream.first().download('D:\\Backup') #Скачиваем первое 
	except:
		print('К сожалению выбранный формат не поддерживается для данного видео')

if quality == '360':
	try:
		stream = yt.streams.filter(res = '360p', progressive = 'True') #Первый элемент 720р
		stream.first().download('D:\\Backup')
	except:
		print('К сожалению выбранный формат не поддерживается для данного видео')

if quality.lower() == audio.lower():
	try:
		stream = yt.streams.filter() #Первый элемент mp4 без видео
		freshDownload = stream.first().download("D:\\Backup")
		input('Когда видео скачалось, нажмите любую кнопку...')
		
	except:
		print('К сожалению выбранный формат не поддерживается для данного видео')

	basePath, extencion = os.path.splitext(freshDownload)
	clip = VideoFileClip(os.path.join(basePath + '.mp4'))
	clip.audio.write_audiofile(os.path.join(basePath + '.mp3'))