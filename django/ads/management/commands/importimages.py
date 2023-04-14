from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from ads.models import *
import os
import sys
import re
from django.core.management.base import BaseCommand, CommandError
from metadata.models import *

class Command(BaseCommand):
	
	'''
	file format must be like:
	DSC05223.JPG.txt
	DSC05223.JPG
	and be in side-by-side folders named:
	'images'
	'transcriptions'
	'''
	
	def handle(self, *args, **options):
		target_directory='ads/management/commands/import'
		imagesdir=os.path.join(target_directory,'images')
		transcriptionsdir=os.path.join(target_directory,'transcriptions')
		imagefilenames=[i for i in os.listdir(imagesdir) if i.lower().endswith('jpg') or i.lower().endswith('png')]
		transcriptionfilenames=[i for i in os.listdir(transcriptionsdir) if i.lower().endswith('txt')]
		imgs=[i for i in imagefilenames]
		trns=[re.sub("\.txt$","",i) for i in transcriptionfilenames]
		images_with_no_transcriptions=list(set(imgs).difference(set(trns)))
		trns_with_no_images=list(set(trns).difference(set(imgs)))
		failure=False
		if len(images_with_no_transcriptions)>0:
			print("the following images have no corresponding transcription filenames")
			for i in images_with_no_transcriptions:
				print(i)
			failure=True
		if len(trns_with_no_images)>0:
			print("the following transcriptions have no corresponding image filenames")
			for i in trns_with_no_images:
				print(i)
			failure=True
		if failure:
			exit()
		for imagefilename in imagefilenames:
			imagefilepath=os.path.join(imagesdir,imagefilename)
			transcriptionfilename=imagefilename+'.txt'
			transcriptionfilepath=os.path.join(transcriptionsdir,transcriptionfilename)
			d=open(transcriptionfilepath,'r')
			transcription_text=d.read()
			
			tr=DcDescriptionFulltext.objects.create(
				text_original=transcription_text
			)
			tr.save()
			
			d.close()
			ad,ad_isnew=StagedAdvertisement.objects.get_or_create(
				tmp_name=imagefilename
			)
			ad.save()
			ad.dc_description_fulltexts.add(tr)
			ad.save()
			f=open(imagefilepath,'rb+')
			stagedphoto=StagedPhoto.objects.create(
				filename=imagefilename,
				parent_item=ad
			)
			stagedphoto.save()
			stagedphoto.staged_photo.save(imagefilename,ContentFile(f.read()))
			stagedphoto.save()
			print(ad)