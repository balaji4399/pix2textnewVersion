from functions import processImage , extractImage , readImages
from flask import Flask,request,send_file , render_template
import warnings
warnings.filterwarnings('ignore')
import zipfile
import shutil
from flask_cors import CORS
import glob
import os
from pptx import Presentation
import pandas as pd
app = Flask(__name__)
cors = CORS(app)
app.config["SECRET_KEY"] ="formextraction"
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
@app.after_request
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, PATCH, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    return response
# 6b36c9778a480db4c96fc7d96e7d1d71bdf2a7f3dfac58705daa0e83aca7c6c0
# 6b36c9778a48
@app.route("/",methods = ['GET'])
def home():
  return "hi guys!"

@app.route("/formExt",methods=['GET','POST'])                          
def tableExtracter():
    try:
      data = request.files['image']  
      
      extractedTxtFile ="output_text/test.txt"
      extractedTxtFile = processImage(data,data.filename)
      return send_file(extractedTxtFile ,as_attachment=True, mimetype="text/csv")
    except Exception as e:
       print(e.args)

# @app.route('/pptFileFormExt',methods=['POST'])                                               
# def pptFileExtractionFunc():
#   success = False
#   resultDict={"success":success,"message":"imageExtraction Failed"}
#   imageList=[]
#   try:
#       data = request.files['image']
#       prs = Presentation(data)
#       ppt_filename = data.filename
#       zipFile = "images.zip"
#       extractImage(imageList, prs, ppt_filename)
#       with zipfile.ZipFile(zipFile, 'w') as f:
#             [f.write(file )for file in imageList]
#       [os.remove(file) for file in imageList]
#       result = readImages(zipFile)
#       if result:
#          zippedFile = "data.zip"
#          with zipfile.ZipFile(zippedFile, 'w') as f:
#             [f.write(file) for file in glob.glob('output_text1/*.txt')]
#          shutil.copytree("output_text1", "output_text" ,  dirs_exist_ok=True)
#          shutil.rmtree("output_text1")
#          return send_file(zippedFile,as_attachment=True,mimetype='application/zip')             
#   except Exception as e:
#     print(e.args)
#     return resultDict

# @app.route('/zipImgFormExt', methods=['POST'])
# def allTableExtraction():
#   resultDict ={"success":False ,"messages": " "}
#   try:
#     imageFile = request.files['image']
#     if imageFile.filename.split('.')[1] == "zip":
#        result = readImages(imageFile)
#        if result:
#           zipFile = "data.zip"
#           with zipfile.ZipFile(zipFile, 'w') as f:
#              [f.write(file) for file in glob.glob('output_text1/*.txt')]
#           shutil.copytree("output_text1", "output_text" ,  dirs_exist_ok=True)
#           shutil.rmtree("output_text1")

#           return send_file(zipFile,as_attachment=True,mimetype='application/zip')
#     else:
#        resultDict["messages"] = "please give valid File type"
#        return resultDict
#   except Exception as e:
#      print(e.args)


if __name__=="__main__":
  app.run(host='0.0.0.0',port=3004)
  