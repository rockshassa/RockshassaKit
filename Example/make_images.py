import os, sys, fnmatch, json, shutil
from PIL import Image

class XCAsset:
	def __init__(self,size,scale,idiom,filename):
		self.size = size
		self.scale = scale
		self.idiom = idiom
		self.filename = filename+'_'+str(self.size)+'_'+str(self.scale)+'x.png'

	def to_json(self):
		jsonDict = {}
		jsonDict['size'] = str(self.size)+'x'+str(self.size)
		jsonDict['idiom'] = self.idiom
		jsonDict['filename'] = self.filename
		jsonDict['scale'] = str(self.scale)+'x'
		# print jsonDict
		return jsonDict

def emptyDir(directory):
	for root, dirs, files in os.walk(directory):
		for f in files:
			os.unlink(os.path.join(root, f))
		for d in dirs:
			shutil.rmtree(os.path.join(root, d))

def findFiles(projectPath):
	
	pattern = 'AppIcon.appiconset'

	for root, dirnames, filenames in os.walk(projectPath):

		for directory in dirnames:
			if pattern in directory:
				print 'found file'
				fullPath = os.path.join(root, directory)
				print fullPath
				return fullPath

def makeImage(source_img,asset):
	try:
		pixels = asset.size*asset.scale
		size = (pixels,pixels)
		source_img.thumbnail(size)
		source_img.save(asset.filename, "PNG")
		successStr = 'created image for size ' + str(size)
		print successStr
	except IOError:
		errStr = 'cannot create image for size ' + str(size)
		print errStr
		return

def generate_assets(filename):
	iphone = 'iphone'
	scale2x = 2
	scale3x = 3
	assets = [
			XCAsset(60,scale3x,iphone,filename),
			XCAsset(60,scale2x,iphone,filename),

			XCAsset(40,scale3x,iphone,filename),
			XCAsset(40,scale2x,iphone,filename),
			
			XCAsset(29,scale3x,iphone,filename),
			XCAsset(29,scale2x,iphone,filename)
			]
	return assets

def writeContents(assets):

	jsonDict = {}

	jsonDict['info'] = {
					    'version' : 1,
					    'author' : 'xcode'
						}

	images = []
	for a in assets:
		images.append(a.to_json())

	jsonDict['images'] = images

	#pretty print
	print json.dumps(jsonDict,sort_keys=True,indent=4,separators=(',', ': '))

	with open('Contents.json', 'w') as outfile:
		json.dump(jsonDict, outfile)

def main():

	#intended invocation:
	#python make_images.py <imagename (relative to script location)> <project path>
	#python make_images.py DBAppIcon2.png /Users/niko/Documents/DuncansBurgers
	argsList = sys.argv

	if len(argsList) < 3:
		exit('not enough args')

	path = argsList.pop()
	imgName = argsList.pop()
	fileName = os.path.splitext(imgName)[0]

	source_img = Image.open(imgName)

	newDir = findFiles(path)
	emptyDir(newDir)
	assets = generate_assets(fileName)
	os.chdir(newDir)

	for a in assets:
		img = source_img.copy()
		makeImage(img,a)

	writeContents(assets)

if __name__ == '__main__':
	main()